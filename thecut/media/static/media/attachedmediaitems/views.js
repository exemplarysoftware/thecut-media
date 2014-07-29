define(['jquery', 'backbone.marionette', 'attachedmediaitems/models'], function(jQuery, Marionette, models) {


    var AttachedMediaItemManagementView = Marionette.View.extend({

        //media-attachedmediaitem-parent_content_type-parent_object_id-group

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
        },

        updateFields: function() {
            // Update the field values based on the model attributes
            this.ui.order.val(this.model.get('order'));
            this.ui.contenttype.val(this.model.get('content_type'));
            this.ui.objectId.val(this.model.get('object_id'));
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
