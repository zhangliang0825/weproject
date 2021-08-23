import base64
from Crypto.Cipher import AES
from Crypto import Random

#对密钥进行填充到指定格式

def add_to_16(text):
    while len(text) % 16 !=0:
        text += '\0'
    return str.encode(text)

def decode_base64(data):
    missing_padding = 4-len(data)%4
    if missing_padding:
        data += b'='*missing_padding
    return data


key = 'Fcniggersm'
key = add_to_16(key)
print(key)

message = 'gYknrv3zMWYXEpRLDL0n8q+6s68DKapAfRpBDhN1XGM='
encrypt_data = message
encrypt_data = decode_base64(encrypt_data)
print(encrypt_data)


