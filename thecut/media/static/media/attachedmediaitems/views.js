define(['log', 'jquery', 'jquery-ui', 'underscore', 'backbone.marionette', 'attachedmediaitems/models'], function (log, jQuery, jQueryUi, _, Marionette, models) {


    'use strict';


    var BaseAttachedMediaItemInlineView = Marionette.ItemView.extend({

        events: {
            'change': 'updateModel'
        },

        modelEvents: {
            'change': 'updateFields'
        },

        serializeFields: function () {
            var data = {};
            data.order = parseInt(this.ui.order.val(), 10);
            data.content_type = parseInt(this.ui.contenttype.val(), 10);
            data.object_id = parseInt(this.ui.objectId.val(), 10);
            if (this.ui.delete_.length) {
                data['delete'] = this.ui.delete_.prop('checked');
            }
            return data;
        },

        template: false,

        updateModel: function () {
            // Update the model attributes based on the field values
            this.model.set(this.serializeFields());
        },

        updateFields: function () {
            log(['Updating fields from model', this.model.toJSON()]);
            // Update the field values based on the model attributes
            this.ui.order.val(this.model.get('order'));
            this.ui.contenttype.val(this.model.get('content_type'));
            this.ui.objectId.val(this.model.get('object_id'));
            if (this.model.has('delete')) {
                // An existing model
                this.ui.delete_.prop('checked', this.model.get('delete'));
            }
        },

        ui: {
            'order': '[name$="-order"]',
            'contenttype': '[name$="-content_type"]',
            'objectId': '[name$="-object_id"]',
            'delete_': '[name$="-DELETE"]'
        }

    });


    var NewAttachedMediaItemInlineView = BaseAttachedMediaItemInlineView.extend({

        emptyInlineRelatedSelector: '#media-attachedmediaitem-parent_content_type-parent_object_id-empty',  // TODO

        initialize: function () {
            this.$emptyInlineForm = jQuery(this.emptyInlineRelatedSelector);
            this.template = this.$emptyInlineForm.prop('outerHTML');
        },

        onRender: function () {
            // Set inline id and class
            var prefix = this.$emptyInlineForm.closest('[data-form-prefix]').attr('data-form-prefix');  // TODO
            this.$el.attr('id', prefix + '-' + this.options.index);
            this.$el.addClass('inline-related ' + 'dynamic-' + prefix);

            // Replace other references and __prefix__ with index
            var pattern = new RegExp('(' + prefix + '-(\\d+|__prefix__))', 'g');
            var newHtml = this.$el.html().replace(pattern, prefix + '-' + this.options.index);
            this.$el.html(newHtml);

            // Insert and rebind UI / update fields with model data
            this.$emptyInlineForm.before(this.$el);
            this.bindUIElements();
            this.updateFields();
        },

        updateIndex: function (index) {
            this.options.index = index;
            this.render();
        }

    });


    var ExistingAttachedMediaItemInlineView = BaseAttachedMediaItemInlineView.extend({

        initialize: function () {
            NewAttachedMediaItemInlineView.__super__.initialize.call(this);
            this.bindUIElements();  // Bind UI elements to existing HTML
            this.model = new models.AttachedMediaItem(this.serializeFields());
        },

        updateIndex: function () {
            // noop - existing forms don't require their index updating.
        }

    });


    var AttachedMediaItemManagementView = Marionette.CollectionView.extend({

        childView: NewAttachedMediaItemInlineView,  // For *new* inline forms

        childViewOptions: function () {
            // For *new* inline forms
            // index is zero-based so no need to add 1
            return {index: this.getTotalForms()};
        },

        collectionEvents: {
            'add': 'setInitialOrder'
        },

        getInlineForms: function () {
            return this.$el.find('.inline-related:not(.empty-form)');
        },

        getTotalForms: function () {
            return parseInt(this.ui.totalForms.val(), 10);
        },

        initialize: function () {
            this.bindUIElements();  // Bind UI elements to existing HTML

            // Create views for *existing* inline forms and attach as children
            _.each(this.getInlineForms(), function (el, index) {
                var view = new ExistingAttachedMediaItemInlineView({'el': el, 'index': index});
                this.children.add(view);
            }, this);

            // Reset collection
            this.resetCollection();

            // Bind child add/remove so the form total is updated.
            this.on('add:child', this.updateTotalForms);
            this.on('remove:child', this.updateTotalForms);
        },

        resetCollection: function () {
            models = [];
            this.children.each(function (view) {
                models.push(view.model);
            });
            this.collection.reset(models);
        },

        setInitialOrder: function (model) {
            if (model.get('order') === 0) {
                model.set('order', this.getTotalForms());
            }
        },

        ui: {
            'initialForms': '[name$="-INITIAL_FORMS"]',
            'maxNumForms': '[name$="-MAX_NUM_FORMS"]',
            'totalForms': '[name$="-TOTAL_FORMS"]'
        },

        updateTotalForms: function () {
            this.ui.totalForms.val(this.getInlineForms().length);
            this.updateChildIndexes();
        },

        updateChildIndexes: function () {
            this.children.each(function (childView, index) {
                childView.updateIndex(index);
            });
        }

    });


    return {
        'AttachedMediaItemManagementView': AttachedMediaItemManagementView
    };


});
