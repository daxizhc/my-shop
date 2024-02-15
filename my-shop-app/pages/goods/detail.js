let app = getApp();
Page({
    data: {
        goods_detail: {
            id: null,
            goods_images: [],
            desc_images: [
                '/resources/goods_6.jpg',
                '/resources/goods_6.jpg',
                '/resources/goods_6.jpg'
            ],
            item_stock: 0,
            item_name: '',
            item_price: 0,
            main_image: ''
        },
        show_popup: false,
        add_cart_popup: false,
        buy_number: null,
        can_not_minus: false,
        can_not_plus: false
    },
    onLoad: function (options) {
        let id = options.id;
        let that = this;
        wx.request({
            url: app.buildUrl('/api/goods/detail/' + id),
            method: 'GET',
            header: app.getRequestHeader(),
            data: {},
            success: function (res) {
                that.setData({
                    goods_detail: res.data.data
                })
            }
        })
    },
    addCartTap: function () {
        this.setData({
            show_popup: true,
            add_cart_popup: true,
            buy_number: 1,
            can_not_minus: true,
            can_not_plus: false
        })
    },
    buyNowTap: function () {
        this.setData({
            show_popup: true,
            add_cart_popup: false,
            buy_number: 1,
            can_not_minus: true,
            can_not_plus: false
        })
    },
    popupCloseTap: function () {
        this.setData({
            show_popup: false
        })
    },
    numberMinusTap: function () {
        if (this.data.buy_number <= 1) {
            return
        }
        let buy_number = this.data.buy_number - 1;
        let can_not_minus = buy_number <= 1;
        let can_not_plus = buy_number >= this.data.goods_detail.item_stock;
        this.setData({
            buy_number: buy_number,
            can_not_minus: can_not_minus,
            can_not_plus: can_not_plus
        })
    },
    numberPlusTap: function () {
        if (this.data.buy_number >= this.data.goods_detail.item_stock) {
            return
        }
        let buy_number = this.data.buy_number + 1;
        let can_not_plus = buy_number >= this.data.goods_detail.item_stock
        let can_not_minus = buy_number <= 1;
        this.setData({
            buy_number: this.data.buy_number + 1,
            can_not_minus: can_not_minus,
            can_not_plus: can_not_plus
        })
    },
    onShareAppMessage: function () {
        return {
            title: this.data.goods_detail.item_name,
            path: '/pages/goods/detail?id=' + this.data.goods_detail.id,
            imageUrl: this.data.goods_detail.main_image
        }
    },
    buyConfirm: function () {
        let that = this;
        wx.redirectTo({
            url: '/pages/orders/create?id=' + that.data.goods_detail.id + '&number=' + that.data.buy_number
        })
    }
});