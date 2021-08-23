let CryptoJS = require('crypto-js');


function t(e) {
            var t = CryptoJS.enc.Utf8.parse(e);
            var i = CryptoJS.enc.Utf8.parse("20171109124536982017110912453698")
          , o = CryptoJS.enc.Utf8.parse("2017110912453698");

            return CryptoJS.AES.encrypt(t, i, {
                iv: o,
                mode: CryptoJS.mode.CBC,
                padding: CryptoJS.pad.Pkcs7
            }).ciphertext.toString().toUpperCase()
        }



function getPwd(p){
    return t(p)
}