define(['jquery', 'backbone.marionette', 'attachedmediaitems/collections', 'attachedmediaitems/models'], function(jQuery, Marionette, collections, models) {


    var AttachedMediaItemManagementView = Marionette.LayoutView.extend({

        addInlineView: function(model) {
            var index = this.getTotalForms();  // index is zero-based so no need to add 1
            var view = new NewAttachedMediaItemInlineView({index: index, model: model});
            view.render();
            this.updateTotalForms();
        },

        collectionEvents: {
            'add': 'addInlineView',
            'remove': 'updateTotalForms'
        },

        initialize: function(options) {
            this.bindUIElements();  // Bind UI elements to existing HTML

            // Attach inline views to regions
            _.each(this.regions, function(value, key) {
                region = this.getRegion(key);
                region.attachView(new ExistingAttachedMediaItemInlineView({'el': region.el}));
            }, this);

            // Reset collection
            this.resetCollection();
        },

        getInlineForms: function() {
            return this.$el.find('.inline-related:not(.empty-form)');
        },

        getTotalForms: function() {
            return parseInt(this.ui.totalForms.val(), 10);
        },

        resetCollection: function() {
            models = new Array();
            _.each(this.regions, function(value, key) {
                models.push(this.getRegion(key).currentView.model);
            }, this);
            this.options.collection.reset(models);
        },

        regions: function(options) {
            regions = {};
            $(options.el).find('.inline-related:not(.empty-form)').each(function(index) {
                regions[$(this).attr('id')] = '#' + $(this).attr('id');
            });
            return regions;
        },

        ui: {
            'initialForms': '[name$="-INITIAL_FORMS"]',
            'maxNumForms': '[name$="-MAX_NUM_FORMS"]',
            'totalForms': '[name$="-TOTAL_FORMS"]'
        },

        updateTotalForms: function() {
            this.ui.totalForms.val(this.getInlineForms().length);
        },

    });


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

        updateModel: function() {
            // Update the model attributes based on the field values
            this.model.set('order', this.ui.order.val());
            this.model.set('content_type', parseInt(this.ui.contenttype.val(), 10));
            this.model.set('object_id', this.ui.objectId.val());
            this.model.set('delete', this.ui.delete.prop('checked'));
        },

        updateFields: function() {
            // Update the field values based on the model attributes
            this.ui.order.val(this.model.get('order'));
            this.ui.contenttype.val(this.model.get('content_type'));
            this.ui.objectId.val(this.model.get('object_id'));

            if (this.ui.delete.length) {
                // An existing view, just mark the delete input.
                this.ui.delete.prop('checked', this.model.get('delete'));
            } else if (this.model.get('delete')) {
                // A new view, delete it.
                this.model.collection.remove(this.model);
                this.destroy();  // TODO
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
            this.$el.addClass('inline-related ' + prefix);

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


    return {
        'AttachedMediaItemManagementView': AttachedMediaItemManagementView
    };


});
