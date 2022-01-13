from flask_old import abort
"""
返回错误自定义错误状态码,和错误信息
"""
# 406为返回的错误的状态码
# description为错误的信息
abort(406, description="身份证号为空")
# 可只返回错误状态码
abort(407)
