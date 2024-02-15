let app = getApp();

const queryGoodsDetail = (id, callback) => {
    wx.request({
        url: app.buildUrl("/api/goods/detail/" + id),
        method: 'GET',
        header: app.getRequestHeader(),
        success: function (res) {
            callback(res.data)
        }
    })
}

module.exports = {
    queryGoodsDetail: queryGoodsDetail
}