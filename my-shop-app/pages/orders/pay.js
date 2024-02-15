let app = getApp();
import {check_response} from "../../utils/response-util.js";

Page({
    data: {
        id: null
    },
    onLoad: function (options) {
        let id = options.id;
        this.setData({
            id: id
        })
    },
    cancelPay: function (e) {
        wx.switchTab({
            url: "/pages/orders/list",
            success: function (e) {
                let page = getCurrentPages().pop();
                if (page === undefined || page == null) {
                    return
                }
                page.setStatusAndShow(0);
            }
        });
    },
    finishPay: function (e) {
        let that = this;
        wx.request({
            url: app.buildUrl("/api/order/operate"),
            method: 'POST',
            header: app.getRequestHeader(),
            data: {
                id: that.data.id,
                operate: 1
            },
            success: function (res) {
                if (!check_response(res)) {
                    return
                }
                wx.switchTab({
                    url: "/pages/orders/list",
                    success: function (e) {
                        let page = getCurrentPages().pop();
                        if (page === undefined || page == null) {
                            return
                        }
                        page.setStatusAndShow(1);
                    }
                });
            }
        })


    }


});