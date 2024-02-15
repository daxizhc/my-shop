let app = getApp()

Page({
    data: {
        addressList: [],
        selected_address: -1,
        type: null
    },
    onLoad: function (options) {
        if (options.selected_address) {
            this.setData({
                selected_address: Number(options.selected_address)
            })
        }
        this.setData({
            type: options.type
        })

    },
    onShow: function () {
        let that = this;
        wx.request({
            url: app.buildUrl("/api/address/list"),
            method: 'POST',
            header: app.getRequestHeader(),
            success: function (res) {
                let data = res.data.data
                that.setData({
                    addressList: data
                })
            }
        })
    },

    selectTap: function (e) {
        if (this.data.type === 'edit') {
            return
        }
        let address_id = e.currentTarget.dataset.id;
        this.setData({
            selected_address: address_id
        })
    },
    onConfirm: function (e) {
        let selected_address = null;
        for (let i in this.data.addressList) {
            if (this.data.addressList[i].id === this.data.selected_address) {
                selected_address = this.data.addressList[i];
                break
            }
        }

        const pages = getCurrentPages();
        const beforePage = pages[pages.length - 2]
        beforePage.setData({  //会直接更新A页面的数据，A页面不需要其他操作
            address: selected_address
        })
        wx.navigateBack()
    },
    onCreate: function () {
        wx.navigateTo({
            url: '/pages/address/set'
        })
    },
    onEdit: function (e) {
        let id = e.currentTarget.dataset.id;
        wx.navigateTo({
            url: '/pages/address/set?id=' + id
        })
    }


});