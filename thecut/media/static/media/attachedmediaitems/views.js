define(['jquery', 'backbone.marionette', 'attachedmediaitems/collections', 'attachedmediaitems/models'], function(jQuery, Marionette, collections, models) {


    var AttachedMediaItemManagementView = Marionette.LayoutView.extend({

        initialize: function(options) {
            this.bindUIElements();  // Bind UI elements to existing HTML

            // Attach inline views to regions
            _.each(this.regions, function(value, key) {
                region = this.getRegion(key);
                region.attachView(new AttachedMediaItemInlineView({'el': region.el}));
            }, this);

            // Reset collection
            this.resetCollection();
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
        }

    });


    var AttachedMediaItemInlineView = Marionette.ItemView.extend({

        events: {
            'change': 'updateModel'
        },

        initialize: function(options) {
            this.model = new models.AttachedMediaItem();
            this.bindUIElements();  // Bind UI elements to existing HTML
            this.updateModel();
        },

        modelEvents: {
            'change': 'updateFields'
        },

        // TODO: We should find the template within the inline admin container
        //template: '#media-attachedmediaitem-parent_content_type-parent_object_id-empty',

        updateModel: function() {
            // Update the model attributes based on the field values
            this.model.set('order', this.ui.order.val());
            this.model.set('content_type', this.ui.contenttype.val());
            this.model.set('object_id', this.ui.objectId.val());
            this.model.set('delete', this.ui.delete.prop('checked'));
        },

        updateFields: function() {
            // Update the field values based on the model attributes
            this.ui.order.val(this.model.get('order'));
            this.ui.contenttype.val(this.model.get('content_type'));
            this.ui.objectId.val(this.model.get('object_id'));
            this.ui.delete.prop('checked', this.model.get('delete'));
        },

        ui: {
            'order': '[name$="-order"]',
            'contenttype': '[name$="-content_type"]',
            'objectId': '[name$="-object_id"]',
            'delete': '[name$="-DELETE"]'
        }

    });


    return {
        'AttachedMediaItemManagementView': AttachedMediaItemManagementView,
        'AttachedMediaItemInlineView': AttachedMediaItemInlineView
    };


});
