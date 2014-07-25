define(['backbone.paginator'], function(BasePageableCollection) {


    var PageableCollection = BasePageableCollection.extend({

        mode: 'infinite',

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
        'PageableCollection': PageableCollection
    };


});
