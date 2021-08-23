
var _n;

!function(i) {
    var s = {};
    function n(t) {
        if (s[t])
            return s[t].exports;
        var e = s[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        return i[t].call(e.exports, e, e.exports, n),
        e.l = !0,
        e.exports
    }
    _n = n;
}({


    },

    {
      jiami: function(t, e, r) {
    var i;
    (i = function(t, e, i) {
        var s = r(3);
        function n() {
            void 0 !== s && (this.jsencrypt = new s.JSEncrypt,
            this.jsencrypt.setPublicKey("-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDq04c6My441Gj0UFKgrqUhAUg+kQZeUeWSPlAU9fr4HBPDldAeqzx1UR92KJHuQh/zs1HOamE2dgX9z/2oXcJaqoRIA/FXysx+z2YlJkSk8XQLcQ8EBOkp//MZrixam7lCYpNOjadQBb2Ot0U/Ky+jF2p+Ie8gSZ7/u+Wnr5grywIDAQAB-----END PUBLIC KEY-----"))
        }
        n.prototype.encode = function(t, e) {
            var i = e ? e + "|" + t : t;
            return encodeURIComponent(this.jsencrypt.encrypt(i))
        }
        ,
        i.exports = n
    }
    .call(e, r, e, t)) === undefined || (t.exports = i)
}
    }
)

function get_(){
 var i = _n('jiami')
    console.log(i)
}

console.log(get_())
