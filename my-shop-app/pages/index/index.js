let app = getApp();

Page({
    data: {
        goods_list: [],
        goods_list_has_next: true,
        goods_search_key: '',
        category_list: [],
        category_id_selected: 0,
    },
    onLoad: function (options) {

    },
    onShow: function () {
        this.setBanners();
        this.setGoodsCategoryList();
        this.queryGoodsList();
    },
    setBanners: function (e) {
        let that = this;
        wx.request({
            url: app.buildUrl('/api/banners'),
            method: 'GET',
            header: app.getRequestHeader(),
            data: {},
            success: function (res) {
                that.setData({banners: res.data.data})
            }
        })
    },
    setGoodsCategoryList: function (e) {
        let that = this;
        wx.request({
            url: app.buildUrl('/api/category_list'),
            method: 'GET',
            header: app.getRequestHeader(),
            data: {},
            success: function (res) {
                let category_list = [{
                    "id": 0,
                    "category_name": "全部"
                }]
                that.setData({category_list: category_list.concat(res.data.data)})
            }
        })
    },
    onCategoryTap: function (e) {
        let category_id = Number(e.currentTarget.id);
        this.setData({
            category_id_selected: category_id,
            goods_list_has_next: true
        });
        this.queryGoodsList();
    },
    onGoodsItemTap: function (e) {
        wx.navigateTo({
            url: '/pages/goods/detail?id=' + e.currentTarget.dataset.id
        })
    },
    onReachBottom: function (e) {
        this.scrollGoodsList()
    },
    queryGoodsList: function () {
        let search_key = this.data.goods_search_key
        let category_id = this.data.category_id_selected
        let that = this;
        wx.request({
            url: app.buildUrl('/api/goods_list'),
            method: 'GET',
            header: app.getRequestHeader(),
            data: {
                start_index: 0,
                search_key: search_key,
                category_id: category_id
            },
            success: function (res) {
                that.setData({
                    goods_list: res.data.data.goods_list,
                    goods_list_has_next: res.data.data.has_next,
                    goods_search_key: search_key
                })
            }
        })
    },
    scrollGoodsList: function () {
        if (!this.data.goods_list_has_next) {
            return
        }

        let that = this;
        let start_index = this.data.goods_list.length
        let goods_search_key = this.data.goods_search_key
        wx.request({
            url: app.buildUrl('/api/goods_list'),
            method: 'GET',
            header: app.getRequestHeader(),
            data: {
                start_index: start_index,
                search_key: goods_search_key
            },
            success: function (res) {
                let current_list = that.data.goods_list;
                that.setData({
                    goods_list: current_list.concat(res.data.data.goods_list),
                    goods_list_has_next: res.data.data.has_next
                })
            }
        })
    },
    listenerSearchInput: function (e) {
        this.setData({
            goods_search_key: e.detail.value
        })
    }


});