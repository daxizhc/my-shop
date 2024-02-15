const check_response = function (res) {
    if (res.statusCode !== 200) {
        wx.showToast({
            title: res.errMsg,
            icon: 'none',
            duration: 2000
        })
        return false
    }
    if (res.data.errorCode !== "0") {
        return false
    }

    return true
}

module.exports = {
    check_response
}
