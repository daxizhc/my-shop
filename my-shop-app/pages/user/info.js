import {check_response} from "../../utils/response-util";

let app = getApp();

Page({
    data: {
        user_info: null,
        edit_nickname: false,
        nickname: ''
    },
    onLoad: function (options) {

    },
    onShow: function () {
        let that = this;
        wx.request({
            url: app.buildUrl("/api/user/info"),
            method: 'POST',
            header: app.getRequestHeader(),
            success: function (res) {
                if (!check_response(res)) {
                    return
                }
                that.setData({
                    user_info: res.data.data
                })
            }
        })
    },
    onChooseAvatar(e) {
        const {avatarUrl} = e.detail
        let that = this;
        wx.request({
            url: app.buildUrl("/api/user/update"),
            method: 'POST',
            header: app.getRequestHeader(),
            data: {
                avatar: avatarUrl
            },
            success: function (res) {
                if (!check_response(res)) {
                    return
                }
                that.onShow()
            }
        })
    },
    nicknameSet(e) {
        this.setData({
            edit_nickname: true
        })
    },
    nicknameInput(e) {
        console.info(e)
        this.setData({
            nickname: e.detail.value
        })
    },
    finishEditNickname: function () {
        let that = this;
        wx.request({
            url: app.buildUrl("/api/user/update"),
            method: 'POST',
            header: app.getRequestHeader(),
            data: {
                nickname: that.data.nickname
            },
            success: function (res) {
                if (!check_response(res)) {
                    return
                }
                that.setData({
                    edit_nickname: false
                })
                that.onShow()
            }
        })
    },
    myOrder: function () {
        wx.switchTab({url: '/pages/orders/list'})
    }


});