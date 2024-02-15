import {check_response} from "../../utils/response-util";

let app = getApp();

Page({
    data: {
        statusType: ["待付款", "待发货", "待收货", "已完成"],
        status: ["0", "1", "2", "3"],
        currentType: 0,
        tabClass: ["", "", "", ""],
        orderList: []
    },
    onLoad: function (options) {
    },
    onShow: function () {
        this.showOrderList(this.data.status[this.data.currentType])
    },
    setStatusAndShow: function (status) {
        this.setData({
            currentType: status
        });
        this.showOrderList(this.data.status[this.data.currentType])
    },
    statusTap: function (e) {
        let curType = e.currentTarget.dataset.index;
        this.setData({
            currentType: curType
        });
        this.showOrderList(this.data.status[this.data.currentType])
    },
    showOrderList: function (status) {
        let that = this;
        wx.request({
            url: app.buildUrl("/api/order/query"),
            method: 'POST',
            header: app.getRequestHeader(),
            data: {
                status: status,
                page_size: 10,
                start_id: -1
            },
            success: function (res) {
                if (!check_response(res)) {
                    return
                }
                that.setData({
                    orderList: res.data.data.orders
                })
            }
        })
    },
    toPay: function (e) {
        wx.navigateTo({
            url: "/pages/orders/pay?id=" + e.currentTarget.dataset.id
        })
    },
    orderConfirm: function (e) {
        let that = this;
        wx.showModal({
            title: '提示',
            content: '确认已经收到商品？',
            success: function (res) {
                if (res.confirm) {
                    wx.request({
                        url: app.buildUrl("/api/order/operate"),
                        method: 'POST',
                        header: app.getRequestHeader(),
                        data: {
                            id: e.currentTarget.dataset.id,
                            operate: 3
                        },
                        success: function (res) {
                            if (!check_response(res)) {
                                return
                            }
                            that.setStatusAndShow(2)
                        }
                    })
                }
            }
        })


    }


});