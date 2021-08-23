import execjs


with open('cailian.js','r') as f:
    js_code_text = f.read()

js_code = execjs.compile(js_code_text).call('getsign',"app=CailianpressWeb&category=&hasFirstVipArticle=1&lastTime=1624974075&os=web&rn=20&subscribedColumnIds=&sv=7.5.5")
print(js_code)



