import execjs


with open('js_demo.js','r',encoding='utf-8') as f:
    l ='{"body":{"loginMethod":"1","name":"15001836972","password":"1234512345"},"head":{"userCode":null,"channelCode":"101","transTime":1623314094664,"transToken":"","customerId":null,"transSerialNumber":""}}'
    jscode = f.read()
    js_reslut = execjs.compile(jscode).call('getpwd',l)
    print(js_reslut)
