class CommonException(Exception):

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def to_dict(self):
        return {
            'code': self.code,
            'msg': self.msg
        }


CATEGORY_NOT_EXIST = CommonException(1001, '分类不存在')

GOODS_NOT_EXIST = CommonException(2001, '商品不存在')
GOODS_IS_ON_SALE = CommonException(2002, '商品已经上架')
GOODS_STOCK_NOT_ENOUGH = CommonException(2003, '商品库存不足')

USER_NOT_LOGIN = CommonException(3001, '用户未登录')
USER_NOT_EXIST = CommonException(3002, '用户不存在')

ADDRESS_NOT_EXIST = CommonException(4001, '地址不存在')

ORDER_NOT_EXIST = CommonException(5001, '订单不存在')

ACCOUNT_NOT_EXIST = CommonException(6001, '账号不存在')
ACCOUNT_PASSWORD_ERROR = CommonException(6002, '账号密码错误')


THIRD_PARTY_ERROR = CommonException(9001, '第三方系统错误')

