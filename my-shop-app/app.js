// app.js
App({
    onLaunch() {
        // 展示本地存储能力
        const logs = wx.getStorageSync('logs') || []
        logs.unshift(Date.now())
        wx.setStorageSync('logs', logs)

        let that = this;
        // 登录
        wx.login({
            success: res => {
                // 发送 res.code 到后台换取 openId, sessionKey, unionId
                wx.request({
                    url: that.buildUrl('/api/user/login'),
                    method: 'POST',
                    header: that.getRequestHeader(),
                    data: {
                        code: res.code
                    },
                    success: function (res) {
                        wx.setStorageSync('token', res.data.data)
                    }
                })

            }
        })
    },
    globalData: {
        userInfo: null,
        domain: 'http://127.0.0.1:5050'
    },
    getRequestHeader: function () {
        return {
            'content-type': 'application/json',
            'token': wx.getStorageSync('token')
        }
    },
    buildUrl: function (path, params) {
        let url = this.globalData.domain + path;
        let paramUrl = "";
        if (params) {
            paramUrl = Object.keys(params).map(function (k) {
                return [encodeURIComponent(k), encodeURIComponent(params[k])].join("=");
            }).join("&");
            paramUrl = "?" + paramUrl
        }
        return url + paramUrl
    }
})
