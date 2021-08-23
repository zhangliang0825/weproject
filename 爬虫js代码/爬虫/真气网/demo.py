# import os
#
# import requests
#
# sign = os.popen('node demo.js {keyword}'.format(keyword='昆明'))
# sign_ =sign.read().strip()
#
# index_url ='https://www.aqistudy.cn/apinew/aqistudyapi.php'
#
# headers = {
# 'Accept':'*/*',
# 'Accept-Encoding':'gzip, deflate, br',
#
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
# 'X-Requested-With':'XMLHttpRequest',
# }
#
# data = {'huZTSaQri':sign_}
# print(data)
# response = requests.post(index_url,data=data).text
#
# print(response)
#
#
# hAe9bX86b:
import re


def decode_packed_codes(code):
    def encode_base_n(num, n, table=None):
        FULL_TABLE = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if not table:
            table = FULL_TABLE[:n]

        if n > len(table):
            raise ValueError('base %d exceeds table length %d' % (n, len(table)))

        if num == 0:
            return table[0]

        ret = ''
        while num:
            ret = table[num % n] + ret
            num = num // n
        return ret

    pattern = r"}\('(.+)',(\d+),(\d+),'([^']+)'\.split\('\|'\)"
    mobj = re.search(pattern, code)
    obfucasted_code, base, count, symbols = mobj.groups()
    base = int(base)
    count = int(count)
    symbols = symbols.split('|')
    symbol_table = {}

    while count:
        count -= 1
        base_n_count = encode_base_n(count, base)
        symbol_table[base_n_count] = symbols[count] or base_n_count

    return re.sub(
        r'\b(\w+)\b', lambda mobj: symbol_table[mobj.group(0)],
        obfucasted_code)
import base64
import requests
from lxml import etree
headers = {

'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

}
response = requests.get("https://www.aqistudy.cn/html/city_realtime.php?v=2.3",headers=headers)
HTML = etree.HTML(response.text)
scripter_url = 'https://www.aqistudy.cn'+HTML.xpath("//script[2]/@src")[0].strip("..")
print(scripter_url)
js_code = requests.get(scripter_url,headers=headers).text
js_code_text =decode_packed_codes(js_code)

if 'dswejwehxt' in js_code_text:

    ds_ = js_code_text.count('dswejwehxt')
    if ds_ == 1:

        js_code_text = js_code_text.strip("eval(dswejwehxt(").strip(')').replace('\\','')

        js_code = base64.b64decode(js_code_text).decode("utf-8")

        js_text = js_code
    else:
        print("2222222222221")

        js_code_text = js_code_text.strip("eval(dswejwehxt(").strip(')').replace('\\', '')

        js_code = base64.b64decode(js_code_text).decode("utf-8").replace('\\', '')

        js_code = base64.b64decode(js_code).decode("utf-8").replace('\\', '')
        print(js_code, 222222222221312)

        if 'eval' in js_code:
            js_text = decode_packed_codes(js_code)
            js_code = base64.b64decode(js_code).decode("utf-8").replace('\\', '')
            js_text = decode_packed_codes(js_code)
            print(js_text,2222222222222221)
        else:
            js_text = js_code

else:



    js_text = decode_packed_codes(js_code)
    print(js_text,1111111111111)


js_text = js_text.replace("\\",'')

print(js_text)

code_clog = re.findall(r'\(!(.*?)\(',js_text)[0].split("=")[-1]

params = re.findall("data:{(.*?):",js_text)[0]



js_ = r'''
var  hex_md5 = require("md5-node");
var CryptoJS = require("crypto-js")

function Base64() {
    _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    this.encode = function(input) {
        var output = "";
        var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
        var i = 0;
        input = _utf8_encode(input);
        while (i < input.length) {
            chr1 = input.charCodeAt(i++);
            chr2 = input.charCodeAt(i++);
            chr3 = input.charCodeAt(i++);
            enc1 = chr1 >> 2;
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
            enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
            enc4 = chr3 & 63;
            if (isNaN(chr2)) {
                enc3 = enc4 = 64
            } else {
                if (isNaN(chr3)) {
                    enc4 = 64
                }
            }
            output = output + _keyStr.charAt(enc1) + _keyStr.charAt(enc2) + _keyStr.charAt(enc3) + _keyStr.charAt(enc4)
        }
        return output
    }
    ;
    this.decode = function(input) {
        var output = "";
        var chr1, chr2, chr3;
        var enc1, enc2, enc3, enc4;
        var i = 0;
        input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
        while (i < input.length) {
            enc1 = _keyStr.indexOf(input.charAt(i++));
            enc2 = _keyStr.indexOf(input.charAt(i++));
            enc3 = _keyStr.indexOf(input.charAt(i++));
            enc4 = _keyStr.indexOf(input.charAt(i++));
            chr1 = (enc1 << 2) | (enc2 >> 4);
            chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
            chr3 = ((enc3 & 3) << 6) | enc4;
            output = output + String.fromCharCode(chr1);
            if (enc3 != 64) {
                output = output + String.fromCharCode(chr2)
            }
            if (enc4 != 64) {
                output = output + String.fromCharCode(chr3)
            }
        }
        output = _utf8_decode(output);
        return output
    }
    ;
    _utf8_encode = function(string) {
        string = string.replace(/\r\n/g, "\n");
        var utftext = "";
        for (var n = 0; n < string.length; n++) {
            var c = string.charCodeAt(n);
            if (c < 128) {
                utftext += String.fromCharCode(c)
            } else {
                if ((c > 127) && (c < 2048)) {
                    utftext += String.fromCharCode((c >> 6) | 192);
                    utftext += String.fromCharCode((c & 63) | 128)
                } else {
                    utftext += String.fromCharCode((c >> 12) | 224);
                    utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                    utftext += String.fromCharCode((c & 63) | 128)
                }
            }
        }
        return utftext
    }
    ;
    _utf8_decode = function(utftext) {
        var string = "";
        var i = 0;
        var c = c1 = c2 = 0;
        while (i < utftext.length) {
            c = utftext.charCodeAt(i);
            if (c < 128) {
                string += String.fromCharCode(c);
                i++
            } else {
                if ((c > 191) && (c < 224)) {
                    c2 = utftext.charCodeAt(i + 1);
                    string += String.fromCharCode(((c & 31) << 6) | (c2 & 63));
                    i += 2
                } else {
                    c2 = utftext.charCodeAt(i + 1);
                    c3 = utftext.charCodeAt(i + 2);
                    string += String.fromCharCode(((c & 15) << 12) | ((c2 & 63) << 6) | (c3 & 63));
                    i += 3
                }
            }
        }
        return string
    }
}

%s
console.log(%s("GETDATA",{"city": "杭州"}))


'''%(js_text,code_clog)

print(js_)
print(params)
data = {
    'h9tYjWYHM':'eyJhcHBJZCI6IjcxZGQyZjZiZDY4YTdmZGI3OGQwMzBjZTE1YTcxZjhiIiwibWV0aG9kIjoiR0VUREFUQSIsInRpbWVzdGFtcCI6MTYyNjg3NjY0MDg1MSwiY2xpZW50dHlwZSI6IldFQiIsIm9iamVjdCI6eyJjaXR5Ijoi5p2t5beeIn0sInNlY3JldCI6Ijg4ZTFmZjFmM2Y3MzI1MjVjNGQ3OGY3NGI2ODRlZGNjIn0='
}
post_url = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'

response = requests.post(post_url, headers=headers,data=data).text
print(response)
"dr6h96mjsogupMhpC4G1Q39KI8FDBmq5Ybpub7uZnWntuQ7HeDzPf9DCUyxlGh1FQ7SJ6ZFrp45/HiGr4wJCgMzCsIutRh3sIbw4AyE1T5Nj5EIoP9W1hQRZTzpTgVjyH2kCpdsyawloeWydzXEMKYFODNr6OGq5S0cS7fJm8y2hIQAh+uctg537WvjFoxHqoB7kspU2zqScxRr8fVQ4uxSTUBW3sgldt0mFnwrLhsCAfTXjJiNCSA//dhyssj9ntMtlrRy4nYHsHqUwxz87pKZo9x7qQ8AMtqMPwatIz/OELo3Viq0RrwDpYpyglqlKn7pTSWqJrhtGHLs8qiOb9r4R2+2ZPU6GR2Gjdq5knHh7Qa/ptI2ZL1UZVQDke5Mj1z31FzwDyxlZQKEwXpyZYdnCuOxjDL4m+Q+Xffw+v7zZvC+asu5zE/6yB5SY5Z3yP2JQ5ZwpIRnUCQdRNOOJeCF98N/eOyYXdf3EkJvzlQx4JtFVzvA0PORsVKpFBimViV7noJQz0GBCD10A7qf+UspqBjOpFJSHecjsiL/n26utcSZSGo3IhlvNDUPSjUn9k1ujUJVPifEpeI4yQp/uDTkd0NA6DRImH32pbQwMFuOV4gJyI1JNF6on0b4IXaDgoZ5akADK40vNHIV7ufepuzv8BFO3nuI9jhqshSRVk07z4rwY+FeBTWXEmo3kJnuSIKwS848IKtVAhzYTIOdZCmvMegiO7VT9KC3RJohjvNGl2I+Z6VGSn0TU8tye+iQu8jSx84wrI0pgSLIOMQzpiFM+gUV2vUQjQHGh6kHkyctTDOmRU2OcEKTQE8AdELwHzdw0O9uq0yE81ao9DvYG5rlF/E9w8TBR/gblaT4akR4UiSyfEY2AqQeaILIB0NJcgQqxcoPwWbrzq/8ileO4FNqFIJ72FCUyVwYC08XhWZZwq3uc0J57gQaAkcD4tyir4AJOgi/7u5eS35DYwF0lrw/t/qlos+wEhGomt04GJiMalE/QX8cPcNV/WCuf3c7sIOnob3Rmhix8Gw7vEm7flnexXluiSZzqcSB8X2G8YG/FwF/VVXy0emvDenJNxRPZnQzar6Qc0SsLCp9skrJgVehomYN8hHkw56Ah/R2+Sa0OIw4cOx8v3p/OvhUfe4+QCJmMsU6WqprKhREA77/vL7cLk5ioo17lumkDCNHfY5EL3HI1aKJQgnfEb7ADXOpc/gL/XkSmGU0rDtXFSUHePrRVgy5ZfgSshOhebjmGmfYNUMBEIQPWY9JWCRPFGmSlic3Aq8iPQK3gCztELcM+nBw62JNsjMGrM1BtRlCkt60hnRd1nqS9ofnp0BFKUKUxxwwSrxqCdZkDpe4zgsc1M+YojjNq8xnOERslLeWSC2FABCP4nifUbvsndmzjuVoKgnxF92YPWc0QJgNkK6UgTkOYMMvbLSoP3SVTa5/v6z3kVcxc0FbMbbEaCsBoae1W80DhL+ubvVQyGanaSt+WQkezjEAeUlR5+hALAw4UunZ2uBU76vLeNtopAihLTxe7cj6gRnMcmwdTvdPdcw9YtyxbB3HSu53SjtFqWEih+c+JBV7ya2kWq9siocFTs1N4Bk/CUqVH16jsntQBqNUgXJDUOnpkTRBluh4SmQxvB4mZ6QBHmxiGtPAeX9H2uiBXS5G7PoPjohV9hfQsGQq/dMLxYNuGdJCZOAIfT4t9tgdjsGe7xjVYXFw5F0/tPLzr8a2XPJ/FlFo/Ll4zsbjVwyTkNgw80/smL2AeqQevMEivywHgOdPtO70C+PHjRztv4Hs0Xm0A855R1DsmAhFmkJcAsTdBd+QHM3KtopL/Q/1tGyMrEapQD6RyM8oE4wbA5e8EvIzY+vi61UyP0Hha/D4uom7OAmrkw7LfoT6Uy45utBB44ObYgUQNLr842XuWG6sJ1VU7ACx7xDBj3UeE4Jfh9qs1iR+wbXdG4wca8SXVaYRJJzp4gDMO7f3yDgk3lclq82uvA260X3ExXniwdiopjTwrSvB3mR30uhsb9o49TnKy8sznG+AiEhy9KLyXI6ia7LR22ZFKEEYEJrro6MCUsCn8J60fEIQZzkWrYibTcuFZu3w6eeuRCj4YGg06KNRfXpwqgtGUhWkVZUdAkrt25IPjUZGIoodQfc/SKd6FA0uQS4AghZjjevoVOBCk0K3+YNRS+SCyozhGfpUygehT0OW/CioLFLNFfXZmApBBVk1TMvuVwJv0zmxryIfNm0D7JmYml1ZuD1KUcHf5KXEmd/yN85UBhzT5M8lTIkjrif4/69vS9GH5l3qoarVNpqCSiyQDe7S+d2U3KJZCK+kk46Z43Ey+8jbZdQafqxaoR8lDwBWk6/jqFvLBGKLYR65DMvoDMdxMoK5lIXWnLo4p4V1kDQaY21sHMCzMLxaqMZxlTDsmVukJY8w0bh3cY6JWOzaaS3SOS5ctVWUjGSb0ibJnbhYrbnXJTnkqX/0xxtIopKMAYqnu/Ibqzw5eHEDgG3gHCAp8+L5XnI1RVncOB1caROlC+doYcpGs2gm5ZKbCrheHCy0869713mSmLfR5E5CBnpk16hF+WuvENm/uIvMkYW6GvvRMjDv/hlH4qvdreFffmddIKOMBoHyywKy0Cfdiu+uFvUObBL+zn1ZbWu/Hg+e95FPjCrmpX3uptAKzZSM0xYb3bVcEXSLcaEMw7HqmDY0k/IAeAgaAwDdJMbje1xA79Ssg+0hcfMlJZosgQz53qQnG9GjZ2Qu7NrbH1AGg8sho6VhX5kv7dCvvWFsA4oRsltgSp7mNkdieMX7igkvuUUq/WHmpsIg8H4JZhWl+iHzvNrQcRrAkp6p7U9NR1JlNHi4+wsgO5xSlggXI9S/jXnQGwPS3EwzXKFSTl9B/oOvgBL6qc52UzsSX1q4ITbLw2VnwRG7N27n+n0obw+k0NcEVxApjjw5l74LaSrkaGlPQEajEYpfxPNryOTtjhnz658rrSig7ctt0YbYFD2i6IvbRuD+qc9DjtF4WeA9a5/uzofDYVlTxyqqU51GGMJAarDZ9xEEB5ha9Ca4KQr3VhmzUcguBRkLgln0p14uhzq3Q5/yiRl+lDF1/movZNA/RpvIizSWihziWrcH5QAuaU7xUoCbX1m6HOoWjPY8d1tNCFQnTfHwmKFNMSab4oGJzbeCRYiu5o9Hidvmly5A1WX2g+EndE5aE/+ohHPwGAC5QFkiMMtwzE3KUT2CW4TpW23ygJaWAgHHfpVucpFSrY2gfFRnwozyqK4c2iYEu7HnqdmzTuZ3vdNz/GDxZG84Ns545btUnn8ODldCjteaYKKbhglc5LSe2gmQUXGW0wkEGNHd8pGbFxGu3aQ0W+IrrDqj1aKdaYVB01TtmKV08Vg9htrvRO2kKk6O7cSKXM1cijqVcA2Csizf1ftvu/jzM9ApXcx/dU1vaGcWP8x/kn5QQ5bJoZ0wUgevJ0u08QigzeHIiBC/qbtdpMxyWJNRwrn26gcZ+oZwA/8CX4lmlwVDbRceI6+ZfEAzgkCUGqZT/RtiFGKc+YAgvkir1qC5D+/eOqWH7ftuQOHolsD/L0gucgRmRHgbUCFoQZS2RHPjh2AY7zALL040l1jL4ic28SiCZn8WpG1AfpPVRfktPn/VTPZFLZj0sH7f8u/EcIA53gUuvHP46SNRpHem6nWGmlF2FHcE1BfGaPOwEt5L7hCt38pTr+uuZN8L+Nk2dIFfvxwXpLzko0zo4tYuc/N4obzWdy6EbJj8KoRDSolM7+6b+cbBBAWb7pUpBgI44KnLf+cwAFGz2RXEleM74NUDoFzcIKbVs5PDLn20mOKKoh2Ptw93f0V6m/H6lDIpCGCxmZFpiA7+b3Vq7UoFVEc30Yc0sNt859yqY/P4EgAIFEfxrwMYb2QYUWp5xFjCeqMheSHjCs4XDcWCr/5oXrAyNz+wJRU/5OEWa19BaZJ344G5zz2DuuydvVbf91dvUQL2oWW4oFSg355t634nnW45ktlmiRNgDqAGBH+mGWPSTFvCFUwsccgzJw21KSuNmL/5fHveqhMYfcNnrUhLCoWP8p/b65JUP4Qr/0+mgLX7GNCP/s4u2xHfX6NcCvCguwMY5yPbRy8FEoKXrbN3lELeLq7D+Bbr7/+Mj/i8mXOrg/ufpJvTbHB80i4XW+svt1X2S83nLY9LJIwupblEsUjM9QIghmh/jtkLOA+9nSWS8wL5QeYrAzYRw3o/l1fC1CgC+mtFn2MQrVVccRzmuKO5UuZ2hitzbLhI5TzJPv7qgbKTCfuGlvTKKEWBa3MsJEk9rp1SSEH4CkhOizXBp8sE78mK+Kfm8HzDDxzkQM+510eRMZmXKtSNIf/5OCvsL2iv0xGtIVUH1kOdDHQERVghqB+52ass92cNInY5GGGH7evwhSgzgfGFCxg/NWD6NWAol5DZSqjkI1P12X0Nz8+eL+0ai4OcMEYW9tUm8gA88tbze1omH67U1sPGg6I6s8jDrMidJdN0vOJuMcYF3wafWVQUDH9xdK9IJCPnW8JN3V0DVhNhC7Arcwz2Thvzl9H3NjczPe6CPfSG8DvxuAZXm7znNxstDfiOpyvo5E/yR08WVbQCrztAYk2xRNhZ6xVmxtujRIRjC9vpyLratnPTVKfGnTlbUJs+SliEWiKSj7eZkxj6ejMxTXZ5OOUH+zjBb6WKmu+g82+QWjzWvfQ3zGuNLYgVsyFRzttYSwtdZbwym99b5ir4uBls+tQtl26Lfy4TCJ5z54U8rGqIEp3P385ZPWFIjfRuuxa23hd9QE3QptWZG7jlsEVV8M2/F3k4sUh8KDWEj2KjrCrWEwLGPjP1BzbDicKXPVg+vVjqKOxYrVtxISWGJdar7vEazKQBtyZrCmGsqEt7uKQZhXDn+ZJtEOL7IXPku/gPDEabkr5oqM7ovqF2/3wlpI9XFEkgrALify2wvW7h9eslXARSTY2vC3iWHQzLfgfoibbf1Z6rJQ64W1JG+AY1YftxWJicf9qjhY/ScuX604WBfJo23safECa+94timYI6bPvodCa0WarlRIll2aW/zgH+eJCe28it/sqLe/XRQsGanawwJmPenXWHsCv8f58SZGI0jQu8Oj1HZ82EQLNGLcvENZDSy+NINSpIJdNl/dlk+zx4uPWtbbpTS3NZfdU75Kzw+MOSaHgEkuBnwv4dlyZXmGfWLCoPPbKOrtsGEHiked4lFnL+qDM9RQYc6zikwgIwxPnaQfidWIe8eV5dhJyxqlaRh6TGhEPNLNVA9HDBdBP/k2bpDRMcX3ne+buO92zENou9a4eka/cSRjLrH6Ejel3+TanByI/X6VGgEk/Yr+GmbGQqLeNbZC8AYtuu+72OQl6lmo9t4102CSJ1JXd2eZ+VK4mn9mRkL5XHJnIcf60x3lmkgxrCH3x1V8elVQ1IxErls5s6mQJ/ZYPkYKz2uKnHNb5d+1QlF0wd6SsqnSWb/ewq6K8DVl0xXvD8tDaWlcVrCxL5O9tiftPJMHzi8D5Nw/8RSfeS+9uw5dmVj49/YTkN3ClBWzlTjRiAHfJnL9Lut+xrzirrTD6cgE/LkrTztyYVFLuT9OEjjolBmDmMiFG2dbv7BjRlsbrXgUQVlSoBiSt03Oe+/ejC2CLZSEPd+XHbdfIHhIuNl+R1wGJqqt0JarrBE0ukwUvJAR7+R8vSG+gUeEk1GAnPzdVm4AnEWDKJKkn9ml4+hZ6RjRNduQpBkqZlr10fnNmlMTRNL9UegEZOjUo2IczAw1U0H5JQ+dEXRl2QvvvoYLFMPvFcfY9M/VkbHJm9F4Y0EzAFTjIwS7mL3j+MOOo2jXobyGo8ONubsq/6LnLBZGMDsf3AHjdi9sHoWMS0g6OX2iAfIX/yfsZVqhsVrYZIosOXYYnmOM8fw03CiEM/macOyuBiGsoErKOEF6R71PEsOJ+cIxHQbAXiuO8ndh2/J/NUbJm3GJU1q31X6BE2NmqOilfquI4XJv5m/Yu1wonIOVygKmvAvGBKfB0lM/BRqjPjlXwzze64bWduffulQPl03VflIVWBiw0pjq1lbnHLjQuCyFKq3M3ytbqu4JhGFYrmoceJep6H8YxDIPcUTEolUfZLCUScTy3O29aSx6Pc9g8qsR92b10Uk0S7Fu+UsS8CGn6Q5vOdzHbUIKz6OiyMbQrRa9ILw/e36Zmdd3wg7FiX8eTcjlaQ3W1PtCJ0tJCep7JQ9WkQoBE9H3QCVCKM9hNC5dim6ZMaM64LT/ss8KH1Tt1KNdqR/AKE7QKhc3WfZ5t2BJAX8Yr1W5IjCGI2K502q4Ew1u+DX/tfOjkiaIIujEhze3lpfPn+Ae7MEaCjXRzlxcQ5W5fWPH2nmVQVXm12xu7DBeHWK+XRF4ahAHPUhDJ1O9aBOMawY9nAOYvF9s9QJaTPz/yAn3ZxV4HsF8T69QxngDqyyGhoY7kyBWUdKOQ7neeZzn1BOEx0xYq9YtgnWemYfiY7TfTHtuHPJfT4fP0H/2bOiGq27Yw9HZDBSUCkVw531ZNzY3rSDtNY4s8VuVUDBjupwqPQ1p/dK0JYYHR2cga/10eMeMYOJZ08MiRjiBxwFtHkd/WpC1hHADH+BOyAFQgmsmDkFbwhQCkosfxDWndEBRYiYlrm/A1732XnRMdLRoRkh4Q5yBnKK9eUeH2IUDWWfcai/9NXBStQm1rN+ctN4XtZXm0jiB2iCq3bwJP3Gs5c61ITpGyo/hq78GzQXEGXzt8SFS8a2fMRomcYzDJ+H25aK/BM06cJ0sfDlzkkPGnZzyqaOjiZbnD/ZUZhc7AlmGbZQ0YEZWzwt0QEmqboSgHWWeOJfItd8o+b36kuqp5UvZnQ5wmSjDHkU2E+Jev8nnBA+u5xwniFyn/eNlVB/9HMfRqp67JFf9SBDjY33/Uzz647juqi3FlLEtj5prB4GVUqMLMU/7k8s7bGNcfrSJR0GLIxh17bTnZreRZnDd2DSXhUncIstdqR4bwjE0jFBV+cHk10k3SJfYuRQmmCsGe3PSS3qmzuE//ju34jHqUf0BvbH3JyysrnGVP7soM+2tjly90tOPmnRBiHP4Km59P4vrWUrd4GEGgZ3bOtVFgIR+ex1vEyTeVq7XKIi8d07gfSyaywpsl4oNEije77SKw//fCRY4m+0oL45gKQQDL3UxJeiIOJT0XuUE494EiKvB4HBHs+vKFKtuz5riCRC8yWg2LR/yMxWrxhYX4x5j4WFcRrYGUrFB3ZEAxZ2EuYI/x/wTeiXLI2GIaF4TKMTJn8Uz/7K74EoCfsdv8AN7XmzOY4NVLIAO+7nYdXuMrlgAPBp1ob/ACgZhTZEGlSfvHFyU3oYxxU2zYuP/235+FNqT6KHA7YggcjWqA2FvRDfkDwW4MWzFjN7yF9k1bqRM6rqM+QKFwQxxtAN06Qf5S+fh1KqRvC73u1rv6QIEdppWZBtZpQyrSiHDfReRZkihwixetvmBxNvy/GImqerVxio5Pu4kUN1L9Z1uNDK6GL7SFHBoeYb+mB/VPMtqMPOL0SpCTNQ4us7ewsXmfEhrnWXhggA7oUfld+viAyo9ynk0gLqA2MFGC/bKDS5WdXPPYIyRe7Eerb8VHHrhTx0R/a/Vk3vywAK6oh5LD1MAx8WbjC+jiRRCZ2e1ackRrs0dT4RQzVwEh9r4LKl29RhipHWC4yZLoC4gHBoYyM0UZdUTt2TWGzEa23vMtxODObQ3KPA5M6ykvHIwkf7irb6JNsMSLtamIiqHuXvOkI00OVPlmmZohwq1g0I0H+GjCTXj8xKdf7M4zaBH37XYPMQMPeIcR/h0S6KwSvVkQSgcUyKxsQ3TLB2CRGjCDZuLjjmZbTetJY9PA1fEhVSsT0sFI4+OHOQllOQ4hUHpZ+XrBZSmhVECCARofWvHcQ3CQQ6ieEjVr2vhl2LmQxTg1dCi9qNtS+Z73aoVJdmlNvE0YhucJ8peq4AagASC7ZO9t84NblJ2eMkS05jyFJyr6CUqVIu9kQ+rWg8dz40+Rb51SjCnb47yvwvDoReaI7qHd44eeLvOAnVPLQH9aLP2CqJKCsEk7lhifQj8b8RwLKMWSRw+FaxTAUPSd77rQ/EepkA3PaU08Nyg+IW1TWfm0DjdUACJxoOTWiTXM22aAFmKqNOsBCeLpjiD589mrhZZgvl2wQMohDKY1PG5jf3Njn8dY6ZU9y89MG08A0kuwHIX/QgRIVNZkv4PiLAGtJrUgi+bR4T4cJcrYQ37cy5EGuJP7S4cAJ+v/p9P+vJNhbFb5bDJw0NfeeIwnrX87m2JogllnzA3RsY9DvBFCmwdLYSNfCZJFU6fhYqVoQ6cTsv4Fnvp7wSgda5PqLYvWKWIjHSVeBrQZLX8pTWKp1BfrGcCrg+rEo/rG/1JKTPJE3fAHiPfYatI8MaBxi6sg59bH5r2eaRRytgg/jS/H0dzFM6mYYmqeIkruPkr7hKHBF1nXYEmUo7fhWyaODS4Ym0Kl11buzEAxL/E9F5YAQHkk2tblkh/gmNXkzszY1c8vgkqiE1qVFOVFxUmRPxoA1TfuMDwA4P23S0FieLuzXIU+0Ff1ytukF+OJoFK1ZQNlk290OOlMeY0eAex3S925TDFqtGZ/sjryTxOgBkZN31i0jGddz9CioMg2whou9PdRbpSOGVjzHxcAqS9VmdAhK3/r63VSemrtNXdZy1JVymsM7ABqT7IfIqd0gOZEmQecgXrA6unAQnDumNItkjplNbcp7L0wd5fiG35k7cMY2a9htOIE09Ez0AsweDgcMXSPmeOFRbI8s1bEnz8UXXVAz0VhlEIYhMmphuT6npqgSQV7TdpeZmkUkAADoSvlZsjiMPN4SGToVeyR1yebFsn6Dm93cWqWNuQKS89KN3S2RXiaITPs9GthzWsEd5Gf/+pa2aLRMOMuMJoojYXARGqzllpNME99NztuilsTf/3QAUeEXpu41mjsB1ntEYiSH8vQSFoRB2BvNBwkEag63DQDad2NeQdRfF8E+QAGch3tmftQv4s8lJ+X593dc68q2Y73kunodWpSapANgGmak/2cEl4oWWv87gqQ/vzawKg8jfubq3WskUW6hmcavk5ZZrcjuJQ0icdsZqb1EdzL7vE8XwNLkrijTgLLNWpnnBtcG0UHqdH5Cb3KNIP/cgDaQ4qyoMq9+mgIMqsrhNlkvoh0bY+JCe1dxRxParCJNME8nO91QUiPPn5cBPolbxkIW+MQBdKHJw15tCt/Ka4iUcBDPYfmTlnNa6J8mIFOoVo8HsklJ9ELVVyIMgOSgA2gGE3ocKajDOFJve5YwMNNLUn59nqTmbV3efozWD9c/o4vl1cm996ZEW/KW7QvRQOtnF3g4LufnyqNLQXutFg4zPNsL8Z34bnp/fA+UOr3+ydW//EY+Eg+l7pqJaxzLXGqut2S+KR7bnSJJEsxG+HUZe7T5h6RyfM6F4sgY/eCZbE6KXZE4dmapfMvlg3bHP1m9HDt3deIGulJovE0EsuQWDLGVNI4ZL/axqURV9xc1A1Y0win1QvGXhCEoT7jOVUe055cD35ekd4CI2B0uy4iFDipUhEyUvToqK8OQS4bwdHXFh6tITg8DDOjpcZoMJ6xFDk1dowCqaDClxBCfOnB8stAAm3Uj3RJPGgkWf20rMnZc5ezZcc7maqjO5iDewSOJw6D51/8xZptE3Zbh98whHpSPCQfCTdkPGUWo6dB+h1N2aRawK4WYvQdbG8JEzLRgQJdsE6dAQUFlrj1aD0SsNWPtpx1BTNUbsfZJoQfbERdKpcn5WuzOIPy220AQEPURrGQb+YbTE6gx8QAIB+2sFHwpUUjx8ej+scN/tUU568G6uApm2+2i8bUOsXwjeNIIKQOpDV2rQMSncocHM34YUQY5ey+PkxEuyTOTIjxTPVL9vuE8AOZSdlLMhMWxFbw+kBLL7Vq+DyUFKYGY//l7RLovQYCBOoE6zDbgXAopvzdGmZDklPn3OtGVn6QU//b62JCMbzGTQHnrojwLlrJuhCEGDxTHp0JtsCurcsh6I0rRTlmcOPYmXxfplUtaO6mo/wgB1Ai51hVKDOZ1DobbtBbfsSxQh4XoFnjffoQe+ermXn85S3RK1PbcVhOmpngfeir4KNvOi9azV7smTsyGwdZyaG93q7j+aGPWo+JGYissvSBBH7Ky142uZ12jWfPFYmUpv2dl3ScDMS/AbcETIAX/YYwikpY848WfCEQS9Mb05ba5/r77PH/3SjuAquUCShRMssgUuBon6IxA0z+at8qOLrOJajbdM+hGn8E8Iy7dxmywVMdr7DWx6wrJMU6EOFqLUei+hQsIcUVB2ivlDm3DYb4IcbgZplCJ4LvaaHYh3wFBQpDv0gtntiMRscMgFa3KHtoxjrSz2WHBnCRpEGLFKRqcMQh2khnQAFq9TDq8c3zZSuAg43P87+Dpk2nmkSVAphORg+P1oOPUxIeQPwZYe2mqrxTrhLzZzRVnvkXZscqfUG68+ye644VYpd5PDYl+CUJeYhQFxVh3cMUgLFnCBQ45pgZlqrJgibnGGjnF1WUA9NoYJWJFyk5w9J6u++vhtch82VbIb/Z6ehFMxqnkprOUMI5RR5zY+QOvs5YwGf2A5QhCLQNxTN70JiqlK2xp+wDhdzZl+bSxBaifU4SJagOsALQssPJEFGX/t2mldf6L1qkXBixc+5yIOwTQphzfpMODuY8Uo8UXIMQqx3u4MtNa/Zr1yY5i1Szw+N460qhlbqvmD8aHhOhjUWJbTDMbG+KqJmpfBZoMnHALY9T5VhhXQqrF66mST812m1Uc0yc6xu1m3cjV3qaMva5cxDQWcXKcOnQLKjL+vEFK02K0oM8Pm6K4FpaVD12q7F2GU3obbzpWcTXCRG5j+8jyOlqfGqy6Arou8aptrNjtU5vBRTZiEflfmg3dBmj4lBW6T/cB3ihUUG+V4GPRlRzx8a2P5I62Dw/ZW8Q3GCnnJ8nu2NPQ3+pGXosWSOSKT2oFNpVRlVP3Lbb15rNPYG2bQRh3zvAvbm/gSdTKAWnSbskNj8ZvN5nhowEWS4nRqe1w5ZAygsY6W8qA+sg0PxCIZow9WXLzzBSh/2upQOI4yfPO1eguGDnNfgHK9NyXmpUABPERHT3x1v7N+oH11qCcY3y2NLpK8WYmNbuA4wIRipb57j2V0fKn9ipesj29DtLO43tcan50RT+ZdOTV79aKGX1oRhf7P5FsAajhM2r+vb/2tv/E6F8TowVdqDUHtuc8iNnbG1x2022jdImj3WoXqMxqgKKVGLdgwaZVMlu+zSE/tqZ5EqnIDqvP2tz/XC+o25TsQbLohJ7vYsds6OYJ6vUzL9u/Q4yT3HLtF07oND//YS913/c5axmmn1I1MUBjpE/z2tlmaRWzE4I5yCVJd6xSoep7Qx1QfZ3cHE9kXWsPVtHAVXBdn1ZVK65swkEGUyiYHMVuqdfXmwXs6Dh+FbUCo/Y+T5QSWj+G3aTPOfJXSw2TZAPLpRsSl42D2dxMgGXoRTIeCOnto61+WUQsKkqfs+8uJAFNu5l8/+tueub+tlFn/2t/GN6vBYebQS6PL3blxEPApppGkOOyXa94g8CTODkEO0Xo3u7UYNNQJdOrCh+nr6PbKB7cYduLBjCkesyzh0uk7LyeBvcscbx/yznnglhs748PHnB208zr7sUy7fsuKAN+jlbqZmAgCqPJ3Ud01TYELxiemDbIJRIAGaV3IVPV868gaB5m7ZMMoZYLvFaHlgz7p3PJNW6ImPLdN/uZQ5ZT4r0G6BTFa5rC2w8nTAznOc01NFByu+X1O3HKzig2aTxmFdirhIHBfFpkd0LfEqKHUJ+N6ad5GUm/Xmiu41iEm2IImZKWzwefq8aQOSm5Kmbot+hWY2wRjwQNEo8SdXPZGq9uOQ0yXJUyQY/a+8mpFKKh1GKMhGK7e7rSHvBgHzPwPSj3D4O0d/EXALLp1Xi6yE8FvOyNJiFxNOrLdDSp6g6JUq5BWjFXCqj9ZA0mXdY4NEWVdJ3/6bUUkwAJRyHwWOhjDVY0UAwuoeRCPFialHKs05ZDHrJtn2c+1rJD0xB5FIRnicvgB8eg5nNT8yqL5V4/Rm+6XLOKn0+2O0HKvxWK1VRiSHald1AV5375EvKXXe9UuOmBIev78AszFXsALpnemhTQLbldiAuWFriM6UMqxVyHJ+Sn0oBVj2Xi1fuLSe8RcH3Lm4Xoy+sD0S59C1TM2/bMGhu8qnMJtvhM4dqm7RW1cXvu9sEuyi1o8pqxik8exZe/FLHZzJ2l/VnvdhxmXTkGJe2ZpBiFrypjCGVfl5ZOL3RaX5s9VC3nIoJfgOlGj3Sef/vDFHfSo6hkJirQUXLYM937GDV+KAPqzWgP6dswGG/0YCw+1Hwe3Whf3fgAcLwCFka2U5GGt0llwXHhs0WNAgJ5pEDycIbNQ5UMjlByip1vUn0QuxrrvZD8HhruM48fJsmA+NkGfY686yuA4uFnU+JyukRZtRLfq3DdhPWxbUGy965kZomGdFdSw/mBTrFbc0TSeLqjfX8nv18hiP9uU1BZZdA2DnTtZEX5W8rF1jS17ExiHGl0zlQTU/EC96QcBBRPZ2OmJ2pFs6sT6M5BMhrbW8zBsre8bwFACRGgusctCt+dTe026Vi1hVCaxC9mBC+nArqEyOlnqU2T1nTC9SKOaF4wI7bW2eDfPoEOdF9NgnIX6u1B/IW106sgVVpye+Nzba1LJnfCPJNUKG+5YCtp8Adnlz+OrgUC+IDLc6bonmK+VIgzj7JZ99EITdTdlZ07ReB+5hhwh1Puh1SV2mLECrZS2Xi+//P2R7nPZEotQyjIPqjDJ17hNIju1bEMm0ZiI3YSYRxU7B2nWBUM0pj2t4ROfoAveDwLMMRkgsN19OI4ziE3KETndsKcqayrRDOYEVEfIrMRU8pb92tQYYYRwBGYTY4ZPSFvIme5u2nQFLSHxKqwA0qACNIaWlBm8ew2ktBGFHMRaWfGNhMRrPR7oGTOTYDYRjc7Hhwtloz36pq0ty6MuTk1yHpCpsMEMAaUMlh1XW+F2qZYnEftwuf/YB0IgTCnUor4zVr7Lv6EBg7fl9/8icw4od0cxPRnNtdibD0FRZcJyofMqljiWCLdzJRcWsBqFLNezGjgdZsX3J2LStklusXCHxoxGio4h4qbPqZ05GGbe/aVo5/RTNyJiUAkBZDlcejXxsL+apfvP2QsD9NJfGC1ZemCy8XPlqk3kqsOI1yhLSQ69Akh1c2XGVV3cjGPz2Aou1vTIvyYSjWV6VMknXirfc+jo6inBdv82CJIgMUgt/APl4XXVRnsygxUHXP68BuXTb77uVsLnovtVx8AcqLlnzeHV7ggZo8Y9BXXGrf9Mi2xhjgoM6ygimxITNqJ1xSOhQmpbgOnF0ahJyx8IS6YcRgx8GRgBNaQLWgt1IIMme8akJnOliplbt4Pq5pwAXwyuF/OdfNGPfipz+/4xaeEILDtkgZJSbegRmT7XmkEDF3XNFsBGByUcZVXuO2gmRWjTng3FrHUY7ITBCCi2+8zJh+4kCM+yQ8+1Cu1hNvyGDcQblARRTucJ8gzweT0spHUrUCjRqJoxTVgULCKTLaomjp8njIFvIZfaN01fagPTR9xNY/QsaP1a9s0MazyBSAi34JerGYYoz6+G+V+Sq2wrgCmubjk3aiC3GZWCeIXgiPwBMlWf41aAug/LsVHuHEEoDyaoNvONfdIm1TgVBHW8ERYjcWWkEqQeqZenELIw87xE5XHknzGBfoSc+0Eg9AT5p38QnnG/WbCr7/EoPZ6On5W6LsI4q297+9zFdbYnso6Ad8H13bJ1gIH7DzIte+1AVdhXHASNnOkel/h1qtKYFDM0+2QZ8IuKxq5YXk9KOGOYPZyJBkCOkyecZkeCW34kFXJJEc/b59wQ+NJruHYPxPYYH/FaTBPwqI8FXWNdmKh1BlcfX/yx8+yk2ASK0aiPanTPw3iwru4zA9Gl9pYM0LQrF2prw9t/nBkjVfjD71X26iibDY8bAE2zBnZWzzWdL+NoV3m9rl6SyfDPbruYjto3lg2dyKSgJQv42epvv0xT3hsRdK442si5TantmjUVf/m0vAxdQtPV+d0Lb/aZhdcD31vjH0QVkjxM8yWbFy6xvnqef4n1JDyyTQY5JGlkgXeCiGxNgVtZX2PY824JLHKiZQUv464cR/jxKOk9O7HVQSPJxrYm3Xwsy3/W/s8otoAhuCzJKCU6FXLgGvckJySR9DImhkCc0U/6A1dKNfOcnwMqsTkroR/zGmKBnS0siWa+g7swZJkFJIg/MjmZuzcYz2OMn4Wy1+p9vdy2VDE4cNbWyDdedc5onUsHVsp249P0rClqYgxv5SJ9ZqwkWOXyrilzqi6Ld42AUrQ77VVm49CVW/fp3t6MzdHNe02sOubCSOz00bMfAzjyg/rR294h4GGELGKh4jZbbj98hsjZjKnFCn0eELIMaD+JdluXFq9PQk9EdZ7kxeM95o9FwPwtFvlKmJi/mU3/Ii6Cm4yxmCY41WGY9igrBFAOBmvczYk2yGS2gJg/OnHP/Bg3PM+CRIfCjJkvYWvL9Mgkgzy8WsNwYsZLUvYGBRn7GorbpREFIE/XY8RWWbaEODEDRZuuaU/ZfjL22BEpGH2CXZLvyn+N7B9MyyDlNOjJS69BHU/SJwJnRbp7kB6/V3dH9tkx/cBQQ9tymKQIbMCn7EwydbbqWk2mzPlLOjzLM4SlIxFraM2LZfJffzCpVmOzr+/vhyRm57i+jwg6gy6Pw6Z6Ztpy/OEwEcdzM1dNi3Ow0B5GFoQ9jrtCko+ReZA7O4H/oRKRn316PzLMS+SCuX6UbnrO1ADZy0PUUh0yL11pWJ1WIqB+5CkFVpLKpzRZ07OD3trNDL78FHzVc9+mkGi+SGAsPTthMgt6FgqPOcpAIaZxou2Tn0GwBtuThkqfAyEPaPj2PnODGAZ6UaWdFHe1KC5xqMeI8MoQcUO3aQxQooM+BHdD53ZPWsWNya7iGy5TXw9Q/E5W/OXVA6lUsSaaNSO/GyQBTKWmEN8UMbln0IWRC6Ri30iiLBr12yEZPIGOo8bOaXuWOrEkIm1swDhzJCga6uxG5cCXDOUn+gM3pYp5Rwy6fpZRSTnc8AESPZGo5Fvmf/H0FkX7j0QbIyK+bJqG1uKlcTT48NFE8nbDaTuRfzBI7Go+QjusMTsWiwLOPxnHrzVTVOEkkdVMbmYQlHPTHTSLfGyjVJzHdLBBZIJY4qhyq33SQ2fvdUJpsXRqSWRA7Fvard49IyoCv6ZnstRATpZDJjpqJft3JDobnkobs4FGtYrlF9zhRXE9xoKQtlPjFJVtT+9ZFktJBR+JRDW9TM/AoTmGJn2KExdh7U+RNCXMimZ2bEsa1ct92rmeXhHO495waHqzRI+a46yPp3W5328g2argm/mZo2iTjy8Nb1EGKxpOfiDZUn/Jm/3TKC8/+kuagmTqSv/7VXHIT45qEtsvjb5+4UpdnSqLbJCi6QYlBXOOcjM6q/2HJguRHBZEMo5QPvzfpZVPrXS0dNiEe7mVn1Lr8tW5r6of8jhQz7TyTMHfJD9a1oSCFfgdUS+/EDjtNX+LD/bMHSwZfoUBBrYtk7Ig1/XKLcLX/A4lZnXmalZWKTKNNoN24TCFiVnL3MIZE7n3Q0ENogUSTgojiK1MW4gMLnv7npGGugId2de1vGKNlv3ETd3eyZ2GvzBExKRNTZ6YKCggLZ1C8mfFmb0vPU64clmmXp1x1d75Es1TSV0jvNK1DqcA6INvSxFhTvro2qgcWxYop4iR3IMYWUB23mR1oxi4leWJwlMbGM151SGf+KSY6Wl/ei9j3BXaHc2Gx6PPk4PqrAeGc5YBjA0AuXmd8pCLFyim4yQ29cL0KXYp8/EJzez5xYdWOsAD89zPlsn+dGfpvNOCXyLoevBHnRH0Zwq6TyXd91KJ+hPMDU3oimUYTUlGm6KpZFTnp5t9Axvchm40FYfPgOF6oCTOhtcEEjaHHL3yrbX04u2BICg+VMah8yMKzUbNJglkmCgNiokNg2w69MjhJV8d86yQsxyqI99tjM/YkynnzuXwaWwDiapOewc+sfPY2jURI89X7Kn1bJSWj0EQscF7a+9+4gvqZKLVqgb4DAZkoyEcEYcqSb870I4sJuN4G/NabebOPt739mOOs+ka5YodOa1GT+Sr0rWsZRWQtNZW4WlJAyZLzYp60p2R9+UHz+IBomP8/T4rRsWvZwm1JtgdXBIxxWWpyhQfrhTa7svBVjeqPF/W6Qq2si1VZJ4kdDh+FA0/fjzw2AqQjL4ehPiQx9gO1DDLllNhf63akvyEFNWD1ORxP3TuCBzvvw7zUl2OI3Nt5DPr+hYUisFDuYV+7Z9fFWRbwpPbKFiGdpF2NsjHfXLfAsLT7TAKSTcwos4O7oE1NZp8aFtAxLrSdlpZrpQOaPHhqglCOSwyns7Df4yq5aNUrvJ8cng8HOA+W3G+A0knplLzv9eMPzxIaXLlr/2+r5xWQ8rtmMWCzhXQnzKai4EKmE/py5YslnndA0IgJPKf4DyBHFP5a+sbs3fOUt9vNjJiiv09rUh8wCySYeE4vwzb+d0wKEdqlQwypvbyqWmY+QU3VTHR8OdRl025i3q46RilTVbp8Horgrw362w2hjR0xMlFNPsE0Ibbwi+mdELuqCEQgzrdNYCeJZk98KxrYz856U1xBS8fz+YZRUFa2qqONZ4925AFAYoOdBTDYHHZqylJSv326DrHAdML95lfKKkyYB7cz/sKCL26ENwMYhWrm6NpTQ6NUE5l45ZKr0zutpacWLktiKo0unUZD6VH6Rvb8x1/qrRJaEe87xHNxWzmfOwCr5P+5zaJyi58qAk4WEVWT3pKxHqtHYbrFy9cNhCGXYl81nqhldlovskrcTFgXE73hLjEdo1gmRMZTm9ZUmKAKDw7aTdXkblrH3MGKHrSCFzIy/Y0ICQdkzP0Rb8TwIpsQ9rzTJuU5rUzHpUYQ+Slp1vQjvUPB3JHkqcfLC5U6ElGjjQdsEmPWlJOCNCovFtuLn0hqVLMBRrrVDbaa12kWxzhej9qiZwAdEP9UYfvZ/AHIj37qJil51u3yW/fZpWELK4QCM95qBcHBQn27g5WW4UlHqAwd3CPwxmBlyxMXzcaj3z/RWZn2wPhM6Xl+QytuaVOXzGmI4+cgLksp92iVkB0QxnmQa3JIYH9QBy+tCHhga+WdC5ymRkCSth75hHwEBs5Iwdj/ryTSOJh9HNQC1Bj350Uj28eNvFIsknPTTsyXR18DxHDtoCEGwcGpulnYC1TUHBR4fhElTq9zpJTUmy4tQ2uXt8qNGv+UHhifRO5myD+8+Iw1JUluqHnOUEe9urUv+eG+4rmfyEItHq0rBMYa2dtVSsa+Fi7DSd1IemwWeEUYoTt0z30n5Gj4SX4ae2HJPqSWB05SrGtpk47aiCEqEwUZXUhSRYeg2K33tc6bs+5O+H8ZbKI5koIJIU345U0yMrLiOGQBKrb+NoLUh0KY/5IrCPZuutUI3DAtGzLw/8mqQLcb+t5lAdDjieixdTCw0ayLsHmjJyrYVE6QC8BCGVCHxGklADbKH+zFQfilTrkeLCoJgdr7aryEt+ku6Pf12hMpqCeg6fO+wNe+ZRMrGVCyTsYeauCGIpp6UvEL0O5fso02DH+SBcgfX8J19+PX5MyL5VwgZ3m+n1zU8zcWoSzaoRs/J0/sUsRYBf8mgsJtd3ia+qptKRfbnCxjv5IF6VigdwG3x60H4JTFX1wuK8pGclrcphlwDUpDV66itYUIfyut30AbfgaHteploVoVH4MBCYvrv0meQV+o5XYFMRxVY4On2TESVoUvUdWX05t9Rh24yxYMpLP/KHdZG9NkoTkeeAeJxBOHQB9e9cGEAqJvfztBIlNCVOW1smL4Q63VCRt0x91Q/Jp31AcCD61Qpq57LZupFQ9o1+ur0pVbOesNuLxDZ+j9U47m/Rv5tqeTRr5VizmQIKRjO6aAB/zikfkroRjBN1t5hAtx+4NV3btOQUb+QwxMD7/qH7zT7XR3LTbsTV6xDd4xF/Yz+PCE/+/HVOdKjXTb3VAAKTETRvP7j8v+89RtRwHpZmcpZvZwN+3PBllMKnjuFHnzkseXTlT3BMxzs6Yxm72kCneRq8ENK1MqlFFKMNcStnzRxy7XV3TfMAS4KIJxmKngBudpQXkJj+quzR+BPxrXknTwH15MXHuubU8rCnClXQ7nLCKNSD9jKpBBfpndsJQa+gf4fLaqLFI/5xTCM/byO7VgRJ1Qlya8x8F9bDU/drIIC3TKcQE08CCNZn0yUyx+GwiSBT7RFCWHlcWXVtxNblDgtDv3j4D7/k3IYn65vm3LZHwVc0DvW6g7B0DiAo6r69+ihkjsQ0FxTBrDfDTUbl0gH9l+UZb96A6Dw3HLkyZY1UtpZ2NdJUJKCJ0kXSumYFsqcmAJVt4+sbNg0ttQfmNpHW6aWOESbwzDyNKTDyuZpYfmw46f75wHSv8DB6ubl75lVNCiMKI0NeIaFpst6i77z2u0l/6oMOt7n7jDGLbirYGb+E9t8klwgQV9Fvdwj+ROvSgQ8DVwiUbcfWV2Loljp9khidBKRe7cesb2F5N6imIRz2+qh2X6gOnpbODjmTiVZG4vkJHUHpOeLTYbVYlQ4jI8UAvQ2wMvnyOiwQkwAAA45E+C57bmRu8kTai1MIR7RM84B3zQQugd0dh0UEw8KoX9EITcDmUR5y5KvV1Un925AzChTRjsLwdr+7mqfF/q9K86RGhrhap3ae+qx5IjgyrInlAKinsFp6fUrDoTFFQCjtKWtFUAHRq7jaUxid6IduAjb0IBZkwdc1qOzl99caZMG9HE6cNhVKaq4CGy2ws3TIOSkqANhWeIR63E/TDYPfG/Nv2M1efwIuk8er3C9KlfLaHcjlMdQKtNiMOR6Xc4ztjcRaEbLZgJwqQFcPJZ7CEiUca/oyWpo8CaV+7PF1PNhh1hrNAaCQqUdVpbvAj+8kKnIZpMg9nEsUVONnXTq873mX4FfrW5Zb1+I6Em93td3ecqKecx0ooHaKgzrRit9T0Gez9SfDbav/l3dt5HBAM+wd1m0BW2asZtmfsDS/PQ9zOxdIesrNVu/KxrLtdHXDp/z6mvecA0LFjX/TUjHtHaM52quQCKfB4HGIz8zI+ZFX1zR3w9/cC+8mxR7hnpir/+RrbdaxGXKhwsiXuu6nGRIGxBDa/FFAcl5cr+pankHbzw1sR5GeDlB1XRuLXTdEn5tAT2aMYR4LJ5VTfy9PAB0DwqQp0r+aXn43pFYYvo1L0W9x6wk24wSMYovmaC798Xgov+J6GmqNmAUq+SOQb+VxRNhmMonHHrbENh7EUSdUP/32P9LImBidfteANmc6CO2YvL2AXdfaY73dW/XDBrq9k0bZVAqhkeG4fuf3iTYX6VQqoviRly3nhMwkGtd5AEaPRbk4/g6QntxvkPCb0x6OVYZtFjTi3Lg1rb2GhGT7gywVBEzfg64iLY7dSojQ12shcpY/jHi/LgTWcjZUXJvz7FZp3L1eFJtVXRzYhtuce8v68VGKQdfBwaAkExsjnP9AR8s5nB6wAo4MWATJCeFG8Lt/Bl2FbRNJsuYIRG62l7C0ENRXSdbZDz/qLk8cwQg6M6esXam4T8eiUIWtvNC9p5TbiaPoP3lyc9RnQ0A9LoOCyfT5waLwC3QlQdi31an4IYdVLUGkFXYiN4grdf5fOtVMiQ4u5RP7kQYFzSAdqY91p2lpbnKyFpF2SVHrVOJnj8zvCb353JS9GPJWj4LDUT5BFX7zUhMlkSJmnNuNrcX1dxKrAZNB4dOUbrYxlMhaIlsu85X7KjkskB2thXBH2pjmzfVD+fIPQurre4KcsEUq5G9gIK6XmND9D9ULblNfoklNZ7jOhoa+DHYJ9tJ78PE8r0D5HhCKwBPTMtVQkFU4yPXdIe9tlktYpCa6ff5GI/qBaEVIT7Sa7nooCj2bGfvqzuFD7xFL1AX0h7NtuTkbRNMRP/bAxSloeUt5K7XW0mNy8Ev40p46ndGLyuBP5d5K56YxHUNFz93RvmozxUI0jlYLiX0YaEEPLkv7yJuO2WCJMAjLSl9s0mugGVn8SHhVyE2tRhzsSJPJJY53jzg0cs3Exx0f1oICnjzZCQcnC7xNaY574Dv7jhbE8nBAQ7gJYQHiFVeX2DqJ20vKp0DU1ICjHyi0+Dm8RkibLzKtt/Ee2rPjB2xNGc2P+rWl2mgVsNgwRVZ8691CWSQOIL362wylfn6uy19IeuIgdT2tKjDmjzkFl0xxAvWjKTRVcKzP/EqSZuE4Wqv90DrBRsmNKh9VEt0/4xZ5TEqO98sEbE1q9AOPLV3OEZ3GL89h0kZTMzb8fHNZfKju6QVtwJRrA0szlmSOZRBE+/rFDa+DmmIsOQULFld2Y+PmbUbdZDH8VFkwCDAWFgDjM36MWrbi68HvYWKYFuJi7hugqcWJxBZY19PEaWyLF6UiRQrLRPsKZN6Rv0k6F82lWWFbI4gOu/HpjjErqdtbPMyCzQNzLZm0ZxD3pgWv/NeK17Zhj+899OV91kEamefWmsg/fCL4wPjdCAYOQCudRakkf+Db9AyK46LLnKXHgpg9L/oohM2Q9BK65nYhGUdX2xCEp6+4odASOxfbc7GvBqPTyMUiVx48X8NToHuAJJ31nvonHqalT/0VEV0bjQK5LY3EYRj8IA1JBVfEpO2srAUiscUqB4oqOVJCsgedJYuQ9Fheq//hlImNXdbBPqOE2ehV0NSwcpbiISgiibhq7WwvZAF/C8M9z85dZ0zb5bsmHzNY0EMjbBPm3ujsafe1GqbKtS+UzpRt908flhIv2bmeMU4BeHZow5EkMIhlck/j7ChA5Fqxy10cLB+gIoOlOLY4hvKy2RLgLcVFQQ4nH3CouDhX2ydCxSOGhC6f2cNnJ1ACtMjr2vezXasz5PyyHdvbYqamlI97aM/d/iAHko4ErCgXrLq4EZ/OqH5eKX8bNzCZ93E1s7rtCAQDiXrN05tIpofmZvzIBNRL9dS6rzGzy0chSozohy821NVvdYc9KHlXc3scj79Q5ibi1+dISNaVLD4nV/lWxgl4d1MwuvNA6B+xa1/oEYVcuqiR8Dwr1twRcFUOc8mnXagVEhfP9vWDe3ZNadR5W0koPnJ+zu2klTVgDXttpBuFcAZcHhPgT8vKi0HveSv/3KicYSQ28acuIqZzuekpqKC/eJjZFGgDB5PwD9tF9MmoyCEM3iqSVEMNX9KzSKFaR+CKPCNS4NnKBuC0xf7kWd+pl8tyHS4lbIMTFZSxzJHkyIQKeZAqQOLA6Uo5ua+cfI0BSe2ibdYUMMDrc6ihWrSZnqta8Am5ZEWpwOPIquRbv+jgIzRKncloQkLUghbMHUtddgbFZl5MngKj0rLG2nDKReD8hgV+oBQZ2/3bg2dVHP5gwJ+8cqd3NRtyG6r5hg7+6+daadJ+5S4SDlQ9YQLKcz83sr1r25yN2DGvR00MIEPwMDrUhpCzURwFfWBK+vYjNT/gIGeK3fN8F/Zs8yNRWCoSjvsU7/HbhK3N30IlN1oOeOlwJnpGKFAwWlLSxMjWAMwaPcm/5KuR6KruULAyYsNWUXsUUGMmqb9TVpQtqmSnhWaW70xqk4n61a22VfTmGj5ryouzBTM6fQfJIZp+ApfUVmBQcdwQjTtoh5BHPvqAuDxPjdtOJaUAYEWI/HAjv+ILHKA8VRsfxXH4IJinZajZA4PsJhD5gJIYAwvQNoA/6q/5TRe3HP2pccuuRcHDRW9Zbfc1f4pjmu/rXI3Is+i4x6p1LkqhWPLz5CIzDozuQmy6+MAUDA7mDsDVF89YO8F0FacbJJ+JlGQYcHs0p/F9ewfqWdqLmwl4dys47n8X0EpxHEascVWr+YbC84p365v8KZ465EdFt5Stwm6BLZl8d1rDzVznxiv3TwbpQiSx806/DTqJiSPE7dyEtVjHy46suqRojetJlnqexmGhlY+w0GDOnYOW3w4n9G7GKKOxPLhkFSLM4mnm+5+V/o975x4aYNHjZmNushl3n3nNEQQpkXMfxNyZuVBBUqs/VUwOedil4NwTVNiP8SqlRXKtXzq35+kJerdRFpcJ0I03X+/gjLTz5/2JmUv+3wzzMpZ0rY9uu5EaQ2p9NSpFsLuwPqtKU6xF/9kHdmGYTzHwZANTBC1aI5MIzr5+psO+exZY7RvkoQtVbhLds99NeIZUoqcO/2G6msn0pOYRpFJJkrj6whlp5hiE2FsXqeqHgv1JlTPVoajPuy1jb4/4C3Aoxegai1fMpUzYPdR3oDCOXsLZeZvxjjAQKW1B/j1h9Ybojid+TAP9uRBCiOtSMR0KRKg9X1fCzjUYg6NDp/f8ee5EIvUH6nN2h5Tgl2OM5WsJGJc8jL8Fn9L7rzMa2NxmyHltZEH8XPLD+37U43DuTo94zqvoTKk6oYgjw65WgBzsIvL16MQlyciSCgz5RWVn2H9uLc57uI+BNTU/nhP4UB9tVsnv8iDDqqYlANi6e60/iGE2QqSPEx+5bnkhIDCr3DaOWR2WnoJrSLwCMLCdHfiVqUYgcanLOLNoHFlnTl8pF3GmHZbi+OpjXzh+BnV3o9tLhuhFN4P57NjfV4eGf24e8NjG5fz88bVS6ZyopMNvfWOhhuwj/u/EbyideDqelUzWUI1LVgX2a/jc3G9TR8KoTC/VuCun7rNKQGdJNtsSxRn4nDMq5Tz1fhjcqq3ghcU80ZnS4RP7Aos5mFOvOZUERI4YK3IVE/22wchhCZHOMN0z5xo7Yj8e0BbqYRt55AHzOivrYUEzhI6eA4uLTYQ=="