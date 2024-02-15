from flask import jsonify, make_response
import json


class HttpResponseUtil:

    @staticmethod
    def success(data=None):
        data = json.dumps({'errorCode': '0', "errorMsg": "success", "data": data},
                          default=lambda o: o.__dict__)
        response = make_response(data)
        response.headers['Content-Type'] = 'application/json'
        return response

    @staticmethod
    def fail(error_code=500, error_msg="fail"):
        return jsonify({'errorCode': error_code, "errorMsg": error_msg, "data": None})

    @staticmethod
    def param_error(error_msg):
        return jsonify({'errorCode': 400, "errorMsg": error_msg, "data": None})
