(wx["webpackJsonp"] = wx["webpackJsonp"] || []).push([ [ 214 ], {
    132: function(e, a, c) {
        e.exports = c.p + "asset/images/vip-entry.jpg";
    },
    315: function(e, a, c) {},
    316: function(e, a, c) {},
    317: function(e, a, c) {},
    318: function(e, a, c) {},
    504: function(e, a, c) {
        "use strict";
        c.r(a);
        var t = c(8), s = c(10), n = c(11), i = c(12), l = c(13), o = c(3), r = c(2), j = c.n(r), d = c(1), m = c(14), x = c(21), b = c.n(x), u = c(17), p = (c(315), 
        c(0));
        function h() {
            var e = "https://canyan.kp-static.com/Fi0-1N_ye7p54tFzaOmD8lgiZiLM", a = "https://canyan.kp-static.com/noLogin.png", c = Object(m["d"])(function(e) {
                return e.user;
            });
            return c.nickname && c.mobile ? Object(p["jsxs"])(d["Navigator"], {
                className: "avatar-cell",
                url: "/pages-extend/user/index",
                hoverClass: "none",
                style: {
                    backgroundImage: "url(".concat(e, ")")
                },
                children: [ Object(p["jsx"])(d["Image"], {
                    className: "avatar",
                    src: Object(u["c"])(c.avatar, 120),
                    mode: "aspectFill"
                }), Object(p["jsxs"])(d["View"], {
                    className: "cell-bd",
                    children: [ Object(p["jsxs"])(d["View"], {
                        className: "username",
                        children: [ c.nickname, c.isVip ? Object(p["jsx"])(d["View"], {
                            className: "badge",
                            children: "VIP会员"
                        }) : null ]
                    }), Object(p["jsx"])(d["View"], {
                        className: "mobile",
                        children: "".concat(c.mobile.slice(0, 3), "****").concat(c.mobile.slice(7, 11))
                    }) ]
                }), Object(p["jsx"])(d["Text"], {
                    className: "icomoon icon-enter"
                }), Object(p["jsx"])(d["View"], {
                    className: "env",
                    children: ""
                }) ]
            }) : Object(p["jsxs"])(d["Navigator"], {
                className: "avatar-cell",
                style: {
                    backgroundImage: "url(".concat(e, ")")
                },
                url: "/pages/login/index",
                hoverClass: "none",
                children: [ Object(p["jsx"])(d["Image"], {
                    className: "avatar",
                    src: a,
                    mode: "aspectFill"
                }), Object(p["jsx"])(d["View"], {
                    className: "cell-bd",
                    children: Object(p["jsx"])(d["View"], {
                        className: "noLogin",
                        children: "点击注册 / 登录"
                    })
                }) ]
            });
        }
        h.options = {
            addGlobalClass: !0
        };
        var g = c(9);
        c(316);
        function O(e) {
            var a = e.option, c = e.user, t = Object(o["useState"])(!1), s = Object(g["a"])(t, 2), n = s[0], i = s[1];
            function l(e) {
                c.nickname && c.mobile ? (a.showNew && (j.a.setStorageSync(a.storageKey, !0), i(!1)), 
                j.a.navigateTo({
                    url: e.currentTarget.dataset.url
                })) : j.a.navigateTo({
                    url: "/pages/login/index"
                });
            }
            return Object(o["useEffect"])(function() {
                a.showNew && (j.a.getStorageSync(a.storageKey) || i(!0));
            }, []), "feedback" === a.name ? Object(p["jsxs"])(d["View"], {
                className: "com-default-cell",
                children: [ Object(p["jsx"])(d["View"], {
                    className: "cell-hd",
                    children: Object(p["jsx"])(d["Text"], {
                        className: "icomoon icon-" + a.name,
                        style: a.style
                    })
                }), Object(p["jsx"])(d["View"], {
                    className: "cell-bd",
                    children: Object(p["jsx"])(d["Button"], {
                        className: "text",
                        openType: "feedback",
                        children: "意见反馈"
                    })
                }), Object(p["jsx"])(d["Text"], {
                    className: "cell-ft icomoon icon-enter"
                }) ]
            }) : "meeting-active" === a.name ? Object(p["jsxs"])(d["View"], {
                className: "com-default-cell",
                children: [ Object(p["jsx"])(d["View"], {
                    className: "cell-hd",
                    children: Object(p["jsx"])(d["Text"], {
                        className: "icomoon icon-" + a.name,
                        style: a.style
                    })
                }), Object(p["jsx"])(d["View"], {
                    className: "cell-bd",
                    children: Object(p["jsx"])(d["Button"], {
                        className: "text",
                        openType: "contact",
                        children: "客服咨询"
                    })
                }), Object(p["jsx"])(d["Text"], {
                    className: "cell-ft icomoon icon-enter"
                }) ]
            }) : "invite" === a.name ? Object(p["jsxs"])(d["View"], {
                className: "com-default-cell",
                "data-url": a.url,
                onClick: l,
                children: [ Object(p["jsx"])(d["View"], {
                    className: "cell-hd",
                    children: Object(p["jsx"])(d["Text"], {
                        className: "icomoon icon-" + a.name,
                        style: a.style
                    })
                }), Object(p["jsx"])(d["View"], {
                    className: "cell-bd",
                    children: Object(p["jsx"])(d["Text"], {
                        className: "text",
                        children: a.text
                    })
                }), Object(p["jsx"])(d["Text"], {
                    className: "cell-ft icomoon icon-enter"
                }) ]
            }) : a.showNew && n ? Object(p["jsxs"])(d["View"], {
                className: "com-default-cell",
                "data-url": a.url,
                onClick: l,
                children: [ Object(p["jsx"])(d["View"], {
                    className: "cell-hd",
                    children: Object(p["jsx"])(d["Text"], {
                        className: "icomoon icon-" + a.name,
                        style: a.style
                    })
                }), Object(p["jsx"])(d["View"], {
                    className: "cell-bd",
                    children: Object(p["jsx"])(d["Text"], {
                        className: "text",
                        children: a.text
                    })
                }), Object(p["jsx"])(d["Text"], {
                    className: "cell-ft icomoon icon-enter"
                }), Object(p["jsx"])(d["Text"], {
                    className: "new",
                    children: "NEW"
                }) ]
            }) : Object(p["jsxs"])(d["Navigator"], {
                className: "com-default-cell",
                url: a.url,
                children: [ Object(p["jsx"])(d["View"], {
                    className: "cell-hd",
                    children: Object(p["jsx"])(d["Text"], {
                        className: "icomoon icon-" + a.name,
                        style: a.style
                    })
                }), Object(p["jsx"])(d["View"], {
                    className: "cell-bd",
                    children: Object(p["jsx"])(d["Text"], {
                        className: "text",
                        children: a.text
                    })
                }), Object(p["jsx"])(d["Text"], {
                    className: "cell-ft icomoon icon-enter"
                }) ]
            });
        }
        O.defaultProps = {
            option: {},
            user: {}
        };
        var N = c(132), f = c.n(N), v = c(38), w = c(6), y = c.n(w), V = (c(317), c(31));
        function T() {
            var e = Object(o["useState"])(!1), a = Object(g["a"])(e, 2), c = a[0], t = a[1], s = Object(m["c"])();
            function n() {
                t(!0), setTimeout(function() {
                    j.a.showTabBar({
                        animation: !0,
                        success: function() {
                            s({
                                type: V["a"],
                                dialog: {
                                    loginSuccDialog: !1
                                }
                            });
                        }
                    });
                }, 250);
            }
            return Object(p["jsxs"])(d["View"], {
                className: y()("com-register-succ", "com-dialog"),
                children: [ Object(p["jsx"])(d["View"], {
                    className: y()("dialog-bg", "opacity-in", {
                        "opacity-out": c
                    }),
                    onClick: n
                }), Object(p["jsxs"])(d["View"], {
                    className: y()("register-box", "opacity-in", {
                        "opacity-out": c
                    }),
                    children: [ Object(p["jsxs"])(d["View"], {
                        className: "registerTitle",
                        children: [ " ", Object(p["jsx"])(d["Text"], {
                            className: "line"
                        }), " 注册成功" ]
                    }), Object(p["jsx"])(d["View"], {
                        className: "registerDescribe",
                        children: "欢迎来到窄门餐眼，您已成功绑定手机号，这个手机号也可以登录窄门餐眼头条小程序"
                    }), Object(p["jsx"])(d["View"], {
                        className: "registerButtons",
                        children: Object(p["jsx"])(d["View"], {
                            className: "buttonCancel dialogButton",
                            onClick: n,
                            children: "我知道了"
                        })
                    }) ]
                }) ]
            });
        }
        c(318);
        var k, S, D = c(7), C = c(28), I = [ {
            text: "我的关注",
            name: "care",
            access: !0,
            url: "/pages-extend/attention/index",
            style: {
                fontSize: "40rpx"
            }
        }, {
            text: "我的企业",
            name: "dbrand",
            access: !0,
            showNew: !1,
            storageKey: "mybrand",
            url: "/pages-extend/my-brand/index",
            style: {
                fontSize: "40rpx",
                marginTop: "6rpx"
            }
        }, {
            text: "邀请得会员",
            name: "invite",
            access: !0,
            url: "/pages-extend/invite/index",
            style: {
                fontSize: "36rpx",
                marginTop: "3rpx"
            }
        }, {
            text: "我的发票",
            name: "invoice",
            access: !0,
            url: "/pages-extend2/invoice/invoice-list/index?type=cy"
        }, {
            text: "提交反馈",
            name: "feedback",
            access: !0,
            url: "",
            style: {
                marginTop: "3rpx"
            }
        }, {
            text: "客服咨询",
            name: "meeting-active",
            access: !0,
            url: "",
            style: {
                fontSize: "36rpx"
            }
        }, {
            text: "关于我们",
            name: "brand-people",
            url: "/pages-extend/about/index",
            style: {
                fontSize: "36rpx"
            }
        } ], L = I, B = (k = Object(m["b"])(function(e) {
            return {
                dialog: e.dialog,
                user: e.user
            };
        }, {
            dispatchSetUserInfo: C["a"]
        }), k(S = function(e) {
            Object(i["a"])(c, e);
            var a = Object(l["a"])(c);
            function c() {
                return Object(s["a"])(this, c), a.apply(this, arguments);
            }
            return Object(n["a"])(c, [ {
                key: "componentDidMount",
                value: function() {
                    var e = this.props.user;
                    e.loaded || this.ajaxLoad(), e.loaded && !e.nickname && this.ajaxLoad();
                }
            }, {
                key: "componentDidShow",
                value: function() {
                    var e = this.props.dialog;
                    e.loginSuccDialog && j.a.hideTabBar({
                        animation: !0
                    });
                }
            }, {
                key: "ajaxLoad",
                value: function() {
                    var e = this, a = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : null;
                    j.a.showLoading({
                        icon: "none",
                        title: "请等待..."
                    }), D["a"].loadUserInfo().then(function(c) {
                        j.a.hideLoading(), e.props.dispatchSetUserInfo(c.data), a && a();
                    });
                }
            }, {
                key: "onPullDownRefresh",
                value: function() {
                    this.ajaxLoad(function() {
                        j.a.stopPullDownRefresh();
                    });
                }
            }, {
                key: "vipNavigateTo",
                value: function() {
                    var e = this.props.user;
                    e.nickname && e.mobile ? j.a.navigateTo({
                        url: "/pages/vip/index"
                    }) : j.a.navigateTo({
                        url: "/pages/login/index"
                    });
                }
            }, {
                key: "render",
                value: function() {
                    var e, a = this.props.user, c = this.props.dialog.loginSuccDialog;
                    return a.loaded ? (a.isVip && (e = b()(a.vipExpiredDatetime).format("YYYY年MM月DD日")), 
                    Object(p["jsx"])(v["a"], {
                        title: "个人中心",
                        showHome: !1,
                        children: Object(p["jsxs"])(d["View"], {
                            className: "dashboard",
                            children: [ Object(p["jsx"])(h, {}), Object(p["jsx"])(d["View"], {
                                className: "vip",
                                children: Object(p["jsxs"])(d["View"], {
                                    className: "vipEntry",
                                    onClick: this.vipNavigateTo.bind(this),
                                    children: [ Object(p["jsx"])(d["Image"], {
                                        className: "vipImage",
                                        src: f.a
                                    }), Object(p["jsxs"])(d["View"], {
                                        className: "vipLabel",
                                        children: [ Object(p["jsx"])(d["View"], {
                                            children: "会员服务"
                                        }), a.isVip && Object(p["jsxs"])(d["View"], {
                                            className: "expired",
                                            children: [ e, " 到期" ]
                                        }) ]
                                    }) ]
                                })
                            }), Object(p["jsx"])(d["View"], {
                                className: "cells",
                                children: L.map(function(e) {
                                    return Object(p["jsx"])(O, {
                                        option: e,
                                        user: a
                                    }, e.name);
                                })
                            }), c && Object(p["jsx"])(T, {}) ]
                        })
                    })) : Object(p["jsx"])(d["View"], {});
                }
            } ]), c;
        }(o["Component"])) || S), P = B, z = {
            navigationBarTitleText: "个人中心",
            enablePullDownRefresh: !0,
            backgroundTextStyle: "dark",
            navigationStyle: "custom"
        };
        Page(Object(t["createPageConfig"])(P, "pages/dashboard/index", {
            root: {
                cn: []
            }
        }, z || {}));
    }
}, [ [ 504, 0, 1, 2, 3 ] ] ]);