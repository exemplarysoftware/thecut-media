define(['jquery', 'backbone.marionette', 'attachedmediaitems/collections', 'attachedmediaitems/models'], function(jQuery, Marionette, collections, models) {


    var BaseAttachedMediaItemInlineView = Marionette.ItemView.extend({

        emptyInlineRelatedSelector: '#media-attachedmediaitem-parent_content_type-parent_object_id-empty',  // TODO

        events: {
            'change': 'updateModel'
        },

        initialize: function(options) {
            this.$emptyInlineForm = $(this.emptyInlineRelatedSelector);
        },

        modelEvents: {
            'change': 'updateFields'
        },

        serializeFields: function() {
            var data = new Object();
            data['order'] = parseInt(this.ui.order.val(), 10);
            data['content_type'] = parseInt(this.ui.contenttype.val(), 10);
            data['object_id'] = parseInt(this.ui.objectId.val(), 10);
            if (this.ui.delete.length) {
                data['delete'] = this.ui.delete.prop('checked');
            }
            return data;
        },

        template: false,

        updateModel: function() {
            // Update the model attributes based on the field values
            this.model.set(this.serializeFields());
        },

        updateFields: function() {
            // Update the field values based on the model attributes
            this.ui.order.val(this.model.get('order'));
            this.ui.contenttype.val(this.model.get('content_type'));
            this.ui.objectId.val(this.model.get('object_id'));
            if (this.model.has('delete')) {
                // An existing model
                this.ui.delete.prop('checked', this.model.get('delete'));
            }
        },

        ui: {
            'order': '[name$="-order"]',
            'contenttype': '[name$="-content_type"]',
            'objectId': '[name$="-object_id"]',
            'delete': '[name$="-DELETE"]'
        }

    });


    var NewAttachedMediaItemInlineView = BaseAttachedMediaItemInlineView.extend({

        initialize: function(options) {
            NewAttachedMediaItemInlineView.__super__.initialize.call(this);
            this.template = this.$emptyInlineForm.prop('outerHTML');
        },

        onRender: function() {
            // Set inline id and class
            var prefix = this.$emptyInlineForm.closest('[data-form-prefix]').attr('data-form-prefix');  // TODO
            this.$el.attr('id', prefix + '-' + this.options.index);
            this.$el.addClass('inline-related ' + 'dynamic-' + prefix);

            // Replace __prefix__ with index
            var newHtml = this.$el.html().replace(new RegExp('__prefix__', 'g'), this.options.index);
            this.$el.html(newHtml);

            // Insert and rebind UI / update fields with model data
            this.$emptyInlineForm.before(this.$el);
            this.bindUIElements();
            this.updateFields();
        }

    });


    var ExistingAttachedMediaItemInlineView = BaseAttachedMediaItemInlineView.extend({

        initialize: function(options) {
            NewAttachedMediaItemInlineView.__super__.initialize.call(this);
            this.model = new models.AttachedMediaItem();
            this.bindUIElements();  // Bind UI elements to existing HTML
            this.updateModel();
        }

    });


    var AttachedMediaItemManagementView = Marionette.CollectionView.extend({

        childView: NewAttachedMediaItemInlineView,  // For *new* inline forms

        childViewOptions: function() {
            // For *new* inline forms
            return {index: this.getTotalForms()}  // index is zero-based so no need to add 1
        },

        collectionEvents: {
            'add': 'setInitialOrder'
        },

        getInlineForms: function() {
            return this.$el.find('.inline-related:not(.empty-form)');
        },

        getTotalForms: function() {
            return parseInt(this.ui.totalForms.val(), 10);
        },

        initialize: function(options) {
            this.bindUIElements();  // Bind UI elements to existing HTML

            // Create views for *existing* inline forms and attach as children
            _.each(this.getInlineForms(), function(el) {
                var view = new ExistingAttachedMediaItemInlineView({'el': el});
                this.children.add(view);
            }, this);

            // Reset collection
            this.resetCollection();

            // Bind child add/remove so the form total is updated.
            this.on('add:child', this.updateTotalForms);
            this.on('remove:child', this.updateTotalForms);
        },

        resetCollection: function() {
            models = new Array();
            this.children.each(function(view) {
                models.push(view.model);
            });
            this.collection.reset(models);
        },

        setInitialOrder: function(model) {
            if (model.get('order') == 0) {
                model.set('order', this.getTotalForms() + 1);
            }
        },

        ui: {
            'initialForms': '[name$="-INITIAL_FORMS"]',
            'maxNumForms': '[name$="-MAX_NUM_FORMS"]',
            'totalForms': '[name$="-TOTAL_FORMS"]'
        },

        updateTotalForms: function() {
            this.ui.totalForms.val(this.getInlineForms().length);
        }

    });


    return {
        'AttachedMediaItemManagementView': AttachedMediaItemManagementView
    };


});
