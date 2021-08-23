# import base64
# import random
#
# from Crypto.Cipher import AES
#
# random_num = ''.join([random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(16)])
#
#
# params = '''{"rid":"R_SO_4_1854105063","threadId":"R_SO_4_1854105063","pageNo":"2","pageSize":"20","cursor":"1624518735310","offset":"40","orderType":"1","csrf_token":""}'''
# params1 = "010001"
# params2 = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
# params3 = "0CoJUm6Qyw8W8jud"
# vi = b"0102030405060708"
# def AES_encrypt(text, key, iv):
#     pad = 16 - len(text) % 16
#     text = text + pad * chr(pad)
#     text = text.encode("utf-8")
#     encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
#     encrypt_text = encryptor.encrypt(text)
#     encrypt_text = base64.b64encode(encrypt_text)
#     return encrypt_text.decode('utf-8')
#
#
# aes1 = AES_encrypt(params,params3,vi)
# aes2 = AES_encrypt(aes1,random_num,vi)
# print(aes2,)
# from Crypto.Cipher import PKCS1_OAEP
# from Crypto.PublicKey import RSA
#
#
#
# def RSAEncrypt(session_key):
#     modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b' \
#               '5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417' \
#               '629ec4ee341f56135fccf695280104e0312ecbda92557c93' \
#               '870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b' \
#               '424d813cfe4875d3e82047b97ddef52741d546b8e289dc69' \
#               '35b3ece0462db0a22b8e7'
#     public_key = '010001'
#     key = RSA.construct(rsa_components=(int(modulus, 16), int(public_key, 16)))
#     public_key = key.publickey()
#     rsa = PKCS1_OAEP.new(key=public_key)
#     cipher_text = rsa.encrypt(message=session_key).hex()
#     return cipher_text
#
# RSA_ = RSAEncrypt("ZPkkxmBqjEAxXcDR")
# print(RSA)

import execjs
import requests

params = {"rid":"R_SO_4_1854105063","threadId":"R_SO_4_1854105063","pageNo":"2","pageSize":"20","cursor":"1624518735310","offset":"40","orderType":"1","csrf_token":""}
params1 = "010001"
params2 = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
params3 = "0CoJUm6Qyw8W8jud"

with open('demo.js','r') as f:
    js_code_text = f.read()

js_for = ('d("{0}","{1}","{2}","{3}")').format(params,params1,params2,params3)
print(js_for)
js_code = execjs.compile(js_code_text,cwd=r'C:\Users\39098\AppData\Roaming\npm').call('d',f"{params}",f"{params1}",f"{params2}",f"{params3}")
params = js_code['encText']  # 获取encText
encSecKey = js_code['encSecKey']  #
index_url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
formdata = {'params': params, 'encSecKey': encSecKey}
response = requests.post(index_url,data=formdata )
print(response.text)
