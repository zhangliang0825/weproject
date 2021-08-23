import execjs


with open('js_url_index.js') as f:
    js_code_text = f.read()
    js_code = execjs.compile(js_code_text).call("visit",'U3kwBQctIQAjMHYBUzJmSwApNlsQUVQZKBwbAyFcYxRWJ11R')
    print(js_code)