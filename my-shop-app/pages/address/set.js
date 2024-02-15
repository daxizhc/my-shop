//获取应用实例
let commonCityData = require('../../utils/city.js');
const {check_response} = require("../../utils/response-util");
let app = getApp();
Page({
    data: {
        provinces: [],
        citys: [],
        districts: [],
        selProvince: '请选择',
        selCity: '请选择',
        selDistrict: '请选择',
        selProvinceIndex: 0,
        selCityIndex: 0,
        selDistrictIndex: 0,
        id: null
    },
    onLoad: function (e) {
        this.setData({
            id: e.id
        })
        this.initCityData(1);
    },
    onShow: function () {
        if (!this.data.id) {
            return
        }
        this.getAddressInfo()
    },
    //初始化城市数据
    initCityData: function (level, obj) {
        if (level === 1) {
            let pinkArray = [];
            for (let i = 0; i < commonCityData.cityData.length; i++) {
                pinkArray.push(commonCityData.cityData[i].name);
            }
            this.setData({
                provinces: pinkArray
            });
        } else if (level === 2) {
            let pinkArray = [];
            let dataArray = obj.cityList
            for (let i = 0; i < dataArray.length; i++) {
                pinkArray.push(dataArray[i].name);
            }
            this.setData({
                citys: pinkArray
            });
        } else if (level === 3) {
            let pinkArray = [];
            let dataArray = obj.districtList
            for (let i = 0; i < dataArray.length; i++) {
                pinkArray.push(dataArray[i].name);
            }
            this.setData({
                districts: pinkArray
            });
        }
    },
    bindPickerProvinceChange: function (event) {
        let selIterm = commonCityData.cityData[event.detail.value];
        this.setData({
            selProvince: selIterm.name,
            selProvinceIndex: event.detail.value,
            selCity: '请选择',
            selCityIndex: 0,
            selDistrict: '请选择',
            selDistrictIndex: 0
        });
        this.initCityData(2, selIterm);
    },
    bindPickerCityChange: function (event) {
        let selIterm = commonCityData.cityData[this.data.selProvinceIndex].cityList[event.detail.value];
        this.setData({
            selCity: selIterm.name,
            selCityIndex: event.detail.value,
            selDistrict: '请选择',
            selDistrictIndex: 0
        });
        this.initCityData(3, selIterm);
    },
    bindPickerChange: function (event) {
        let selIterm = commonCityData.cityData[this.data.selProvinceIndex].cityList[this.data.selCityIndex].districtList[event.detail.value];
        if (selIterm && selIterm.name && event.detail.value) {
            this.setData({
                selDistrict: selIterm.name,
                selDistrictIndex: event.detail.value
            })
        }
    },
    bindCancel: function () {
        wx.navigateBack({});
    },
    bindSave: function (e) {
        let data = {
            'id': this.data.id,
            'nickname': e.detail.value.nickname,
            'mobile': e.detail.value.mobile,
            'address': e.detail.value.address,
            'province_str': this.data.selProvince,
            'city_str': this.data.selCity,
            'country_str': this.data.selDistrict
        }
        wx.request({
            url: app.buildUrl("/api/address/save_or_update"),
            header: app.getRequestHeader(),
            method: 'POST',
            data: data,
            success: function (res) {
                if (!check_response(res)) {
                    wx.showToast({
                        title: '保存失败',
                        icon: 'error',
                        duration: 1000
                    })
                    return
                }
                wx.navigateBack()
            }
        })

    },
    deleteAddress: function (e) {
        let that = this;
        wx.showModal({
            title: '警告',
            content: '确认删除地址？',
            success(res) {
                if (res.confirm) {
                    wx.request({
                        url: app.buildUrl("/api/address/delete"),
                        header: app.getRequestHeader(),
                        method: 'POST',
                        data: {
                            'id': that.data.id
                        },
                        success: function (res) {
                            if (!check_response(res)) {
                                wx.showToast({
                                    title: '删除失败',
                                    icon: 'error',
                                    duration: 1000
                                })
                                return
                            }
                            wx.navigateBack()
                        }
                    })
                }
            }
        })
    },

    getAddressInfo: function () {
        let that = this;
        wx.request({
            url: app.buildUrl("/api/address/info"),
            header: app.getRequestHeader(),
            method: 'POST',
            data: {'address_id': that.data.id},
            success: function (res) {
                that.setData({
                    nickname: res.data.data.nickname,
                    mobile: res.data.data.mobile,
                    address: res.data.data.address,
                    selProvince: res.data.data.province_str,
                    selCity: res.data.data.city_str,
                    selDistrict: res.data.data.country_str
                })
            }
        })
    }
});
