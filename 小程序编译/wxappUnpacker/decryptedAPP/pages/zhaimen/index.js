(wx["webpackJsonp"] = wx["webpackJsonp"] || []).push([ [ 224 ], {
    526: function(e, t, a) {
        "use strict";
        a.r(t);
        var n = a(8), r = a(10), i = a(11), c = a(5), s = a(12), u = a(13), l = a(4), o = a(3), h = a(2), p = a.n(h), b = a(1), g = a(0), j = {
            title: "窄门学社",
            url: "https://zhaimenxueshe.com"
        }, v = function(e) {
            Object(s["a"])(a, e);
            var t = Object(u["a"])(a);
            function a() {
                var e;
                Object(r["a"])(this, a);
                for (var n = arguments.length, i = new Array(n), s = 0; s < n; s++) i[s] = arguments[s];
                return e = t.call.apply(t, [ this ].concat(i)), Object(l["a"])(Object(c["a"])(e), "state", {
                    url: ""
                }), Object(l["a"])(Object(c["a"])(e), "current", Object(h["getCurrentInstance"])()), 
                e;
            }
            return Object(i["a"])(a, [ {
                key: "componentDidMount",
                value: function() {
                    var e = this.current.router.params, t = e.url, a = e.title;
                    this.url = t, this.title = a, a && p.a.setNavigationBarTitle({
                        title: a
                    }), this.setState({
                        url: t || j.url
                    });
                }
            }, {
                key: "onShareAppMessage",
                value: function() {
                    return {
                        title: "窄门餐眼-餐饮人都在用的数据神器",
                        desc: "已收录1500万+餐饮门店数据",
                        path: "pages/zhaimen/index?url=".concat(this.url, "&title=").concat(this.title)
                    };
                }
            }, {
                key: "render",
                value: function() {
                    var e = this.state.url;
                    return Object(g["jsx"])(b["WebView"], {
                        src: e
                    });
                }
            } ]), a;
        }(o["Component"]), O = {
            navigationBarTitleText: "窄门学社",
            enableShareAppMessage: !0
        };
        v.enableShareAppMessage = !0;
        Page(Object(n["createPageConfig"])(v, "pages/zhaimen/index", {
            root: {
                cn: []
            }
        }, O || {}));
    }
}, [ [ 526, 0, 1, 2 ] ] ]);