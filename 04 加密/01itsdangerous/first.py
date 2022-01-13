from itsdangerous import JSONWebSignatureSerializer, SignatureExpired, BadSignature, URLSafeSerializer, Signer, \
    TimestampSigner, URLSafeTimedSerializer
import itsdangerous
import time

# 自己的密钥
salt = "zhangmeng_salt"
"""
1.签名,
签名得到的字符串,前半部分为加密前的字符串,后半部分为加密后得到的秘文
"""

# salt 为自己使用的密钥
s1 = Signer(salt)
# 给定字符串的签名。
s1_1 = s1.sign("my string")
print(s1_1)
# "my string.WQeL_GbX5Eg66l4LDlz8nPiTWEA"
# 前半部分为加密前的字符串,后半部分为加密后得到的秘文
# 取消给定字符串的签名。
s1_2 = s1.unsign("my string.WQeL_GbX5Eg66l4LDlz8nPiTWEA")
print(s1_2)
try:
    # 如果修改前面的字符串会报错
    s1.unsign("my add string.WQeL_GbX5Eg66l4LDlz8nPiTWEA")
    # 报错如下
    # Traceback (most recent call last):
    #   ...
    # itsdangerous.exc.BadSignature: Signature b'WQeL_GbX5Eg66l4LDlz8nPiTWEA' does not match
except itsdangerous.exc.BadSignature as e:
    print(e)
# 签名验证
print(s1.validate("my string.WQeL_GbX5Eg66l4LDlz8nPiTWEA"))
# True
print(s1.validate("my add string.WQeL_GbX5Eg66l4LDlz8nPiTWEA"))
# False
# 获取给定值的签名
print(s1.get_signature("my string"))
# b'WQeL_GbX5Eg66l4LDlz8nPiTWEA'
# print(s1.derive_key())

title2 = """
2. 签名加入有效时间
"""
print(title2)

s = TimestampSigner(salt)
string = s.sign('foo')
print(string)
# time.sleep(6)
try:
    # 设置签名的最大时间为5秒,前面sleep(6)所以会报错
    s2a = s.unsign(string, max_age=5)
    # itsdangerous.exc.SignatureExpired: Signature age 6 > 5 seconds
except itsdangerous.exc.SignatureExpired as e:
    print(e)
print(s.validate(string, max_age=5))
# False
# 因为超时
print(s.get_timestamp())
# 1611138966   ;当前时间戳


title3 = """
3.url序列化
"""
# 包含_'、'-'、'.等特殊字符
# URLSafeTimedSerializer为加入时间限制
print(title3)
s = URLSafeSerializer(salt)
print(s.dumps([1, 2, 3, 4]))
'WzEsMiwzLDRd.VqrDxTjXYP3CnfKI77svokJ2Whc'
print(s.loads("WzEsMiwzLDRd.VqrDxTjXYP3CnfKI77svokJ2Whc"))
# [1, 2, 3, 4]


title4 = """
4. json 序列花签名
"""
print(title4)

from itsdangerous import JSONWebSignatureSerializer

s = JSONWebSignatureSerializer(salt)
print(s.dumps({"x": 42}))
print(s.loads(
    "eyJhbGciOiJIUzUxMiJ9.eyJ4Ijo0Mn0.xi3I9IMCJKUkciYxl1RCUe0TFdmplgDZGbmhDut55NVGhrpNTRaQPIq35pNWlf8Bi1R_4vDdcLWcONTAIZNguA"))
