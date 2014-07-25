define(['backbone.paginator', 'contenttypes/models'], function(PageableCollection, models) {


    var ContentTypeCollection = PageableCollection.extend({

        mode: 'server',
        model: models.ContentType,

        initialize: function(models, options) {
            this.url = options['url'];
        },

        queryParams: {
            currentPage: 'page',
            pageSize: 'limit',
            totalPages: null,
            totalRecords: null,
            sortKey: null,
            order: null
        },

        state: {
            pageSize: null
        },

        parseLinks: function (data) {
            return {next: data.next, prev: data.previous}
        },

        parseRecords: function (data) {
            return data.results;
        },

        parseState: function (data) {
            return {totalRecords: data.count}
        }

    });


    return {
        'ContentTypeCollection': ContentTypeCollection
    };


});
