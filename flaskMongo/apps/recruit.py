from flask import jsonify

from . import recruit_bp


@recruit_bp.route('/tencent')
def tencent():
    data = {
        'id': 1,
        'name': '腾讯网'
    }
    return jsonify(data=data)