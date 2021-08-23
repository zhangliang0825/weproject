import execjs
from binascii import b2a_hex, a2b_hex
with open('demo_js.js','r',encoding='utf8') as f:
    js_code_text = f.read()


js_code = execjs.compile(js_code_text,cwd=r'C:\Users\39098\AppData\Roaming\npm').call("getPwd",'11235')
print(js_code)
print(111111111111111111111111111111111111111111111)
# import base64
# from Crypto.Cipher import AES
# def AES_encrypt(text, key, iv):
#     pad = 16 - len(text) % 16
#     text = text + pad * chr(pad)
#     text = text.encode("utf-8")
#     encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
#     encrypt_text = encryptor.encrypt(text)
#     encrypt_text = base64.b64encode(encrypt_text)
#     return b2a_hex(encrypt_text).decode("utf-8")
#
# password = AES_encrypt('11235',"20171109124536982017110912453698",b"2017110912453698")
# print(password)

import execjs
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


def js_aes(text):
    jscode = """
    function encryptByAES(pwd) {
        var cryptoJS = require("crypto-js");

        let i = cryptoJS.enc.Utf8.parse("12345678901234561234567890123456");
        let t = cryptoJS.enc.Utf8.parse(pwd);
        let o = cryptoJS.enc.Utf8.parse("1234567890123456");
        return cryptoJS.AES.encrypt(t, i, {
                    iv: o,
                    mode: cryptoJS.mode.CBC,
                    padding: cryptoJS.pad.Pkcs7
                }).ciphertext.toString()
    }
    """
    ctx = execjs.compile(jscode)
    encrypto = ctx.call("encryptByAES", text)

    return encrypto


def py_aes(text):
    key = b"20171109124536982017110912453698" # 长度必须为16
    text = text.encode("utf-8")

    cryptor = AES.new(key, AES.MODE_CBC, iv=b"2017110912453698")
    pad = 16 - len(text) % 16
    text = text + (chr(pad) * pad).encode("utf-8")  # 相当于JS里面的 padding: cryptoJS.pad.Pkcs7
    ciphertext = cryptor.encrypt(text)

    return b2a_hex(ciphertext).decode("utf-8").upper()


text = "11235"
# js_res = js_aes(text)
py_res = py_aes(text)
print(py_res)
#
# print(js_res == py_res)
# print(js_res)
# print(js_res)