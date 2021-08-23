import execjs
with open('js_fangtianxia.js', 'r',encoding='utf-8') as f:
    js = f.read().strip()
    js_code = execjs.compile(js,).call('encryptedString','123456')
    print(js_code)