# import execjs
#
#
#
# with open('demo_js.js', 'rb') as f:
#
#     code_js_text = f.read().decode('utf8').strip()
#     code = execjs.compile(code_js_text).call('getpwd','111')
#     print(code)
import os

sign = os.popen(r"D:\nodejs\node demo_js.js {}".format("123"))

sigin = sign.read().strip()

print(sigin,1111111111)