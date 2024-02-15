let GoodsService = require('../../services/goods-service.js');
import {check_response} from "../../utils/response-util.js";

let app = getApp();

Page({
    data: {
        goods_list: [],
        total_price: 0,
        address: null
    },
    onLoad: function (options) {
        let id = options.id;
        let buy_number = options.number;
        let that = this;
        GoodsService.queryGoodsDetail(id, function (res) {
            let goods = res.data;
            goods['buy_number'] = buy_number;
            that.setData({
                goods_list: [goods],
                total_price: buy_number * goods.item_price
            })
        })

        wx.request({
            url: app.buildUrl("/api/address/default"),
            method: 'POST',
            header: app.getRequestHeader(),
            success: function (res) {
                let data = res.data.data
                that.setData({
                    address: data
                })
            }
        })
    },

    selectAddress: function () {
        let address = this.data.address;
        wx.navigateTo({
            url: '/pages/address/select?selected_address=' + address.id + '&type=select'
        })
    },

    createOrder: function (e) {
        let address_id = this.data.address.id;
        let item_id = this.data.goods_list[0].id;
        let item_count = this.data.goods_list[0].buy_number;

        wx.request({
            url: app.buildUrl("/api/order/create"),
            method: 'POST',
            header: app.getRequestHeader(),
            data: {
                address_id: address_id,
                item_id: item_id,
                item_count: item_count
            },
            success(res) {
                if (!check_response(res)) {
                    return
                }
                wx.redirectTo({
                    url: "/pages/orders/pay?id=" + res.data.data
                });
            }

        })

    }


});