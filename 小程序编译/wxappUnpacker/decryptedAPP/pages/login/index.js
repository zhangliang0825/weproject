(wx["webpackJsonp"] = wx["webpackJsonp"] || []).push([ [ 220 ], {
    319: function(e, t, a) {},
    524: function(e, t, a) {
        "use strict";
        a.r(t);
        var n, i, s = a(8), c = a(10), o = a(11), l = a(5), r = a(12), h = a(13), u = a(4), d = a(3), g = a(2), b = a.n(g), p = a(1), m = a(14), j = (a(319), 
        a(7)), f = a(28), x = a(29), O = a(17), v = a(34), k = a(0), N = Object(v["a"])("gio"), w = "https://canyan.kp-static.com/canyanLogo.png", I = (n = Object(m["b"])(function(e) {
            return {
                dialog: e.dialog,
                user: e.user
            };
        }, {
            dispatchSetUserInfo: f["a"],
            dispatchChangeDialogItem: x["a"]
        }), n(i = function(e) {
            Object(r["a"])(a, e);
            var t = Object(h["a"])(a);
            function a() {
                var e;
                Object(c["a"])(this, a);
                for (var n = arguments.length, i = new Array(n), s = 0; s < n; s++) i[s] = arguments[s];
                return e = t.call.apply(t, [ this ].concat(i)), Object(u["a"])(Object(l["a"])(e), "state", {
                    help: !1
                }), Object(u["a"])(Object(l["a"])(e), "getPhoneNumber", function(t) {
                    var a = t.detail, n = a.errMsg, i = a.encryptedData, s = a.iv;
                    -1 !== n.indexOf("ok") && (N("track", "sucGetPhoneNumber"), b.a.showLoading({
                        icon: "none",
                        title: "加载中..."
                    }), j["a"].bindMobile(i, s).then(function(t) {
                        (b.a.hideLoading(), t.data.success) ? (e.resetLoadUserInfo(), e.dialogShow(), b.a.getCurrentPages().length > 1 ? b.a.navigateBack() : b.a.switchTab({
                            url: "/pages/index/index"
                        })) : b.a.showToast({
                            title: t.data.error.message,
                            icon: "none"
                        });
                    }));
                }), e;
            }
            return Object(o["a"])(a, [ {
                key: "componentDidMount",
                value: function() {
                    var e = this.props.user;
                    e.loaded && e.nickname && e.mobile && (b.a.getCurrentPages().length > 1 ? b.a.navigateBack() : b.a.switchTab({
                        url: "/pages/index/index"
                    }));
                }
            }, {
                key: "getUserInfo",
                value: function(e) {
                    var t = this;
                    b.a.showLoading({
                        title: "加载中..."
                    }), b.a.getUserProfile({
                        desc: "用于完善注册用户资料",
                        success: function(e) {
                            "getUserProfile:ok" == e.errMsg && (N("track", "sucGetUserInfo"), j["a"].baseLogin({
                                encryptedData: e.encryptedData,
                                iv: e.iv
                            }).then(function(e) {
                                e.data.success && (b.a.hideLoading(), t.resetLoadUserInfo());
                            }).catch(function(e) {
                                console.log("error", e);
                            }));
                        }
                    });
                }
            }, {
                key: "resetLoadUserInfo",
                value: function() {
                    var e = this;
                    j["a"].loadUserInfo().then(function(t) {
                        e.props.dispatchSetUserInfo(t.data), t.data.nickname && t.data.mobile && e.props.dispatchChangeDialogItem({
                            showLoginButton: !1
                        });
                    });
                }
            }, {
                key: "dialogShow",
                value: function() {
                    this.props.dispatchChangeDialogItem({
                        loginSuccDialog: !0
                    });
                }
            }, {
                key: "handleClick",
                value: function(e) {
                    var t = e.currentTarget.dataset, a = t.url, n = t.title;
                    b.a.navigateTo({
                        url: "/pages/zhaimen/index?url=".concat(a, "&title=").concat(n)
                    });
                }
            }, {
                key: "render",
                value: function() {
                    var e = this.state.help, t = this.props.user, a = "weapp";
                    return Object(k["jsx"])(p["View"], {
                        children: e ? Object(k["jsxs"])(p["View"], {
                            className: "help-page",
                            children: [ Object(k["jsx"])(p["View"], {
                                className: "help-content",
                                children: "出错了，需要您把当前小程序删除重新下载，即可重新登录（微信主界面下拉即可找到我的小程序，删除操作可参考下图）"
                            }), Object(k["jsx"])(p["Image"], {
                                className: "help-img",
                                src: "https://canyan.kp-static.com/login-help.jpeg",
                                mode: "widthFix"
                            }) ]
                        }) : Object(k["jsxs"])(p["View"], {
                            className: "loginPage",
                            children: [ t.avatar ? Object(k["jsx"])(p["Image"], {
                                className: "avatar",
                                src: Object(O["c"])(t.avatar, 120),
                                mode: "aspectFill"
                            }) : Object(k["jsx"])(p["Image"], {
                                className: "logo",
                                src: w,
                                mode: "aspectFill"
                            }), Object(k["jsx"])(p["View"], {
                                className: "loginTitle",
                                children: "欢迎登录窄门餐眼"
                            }), t.nickname ? t.mobile ? "" : Object(k["jsx"])(p["View"], {
                                className: "loginDescribe",
                                children: Object(k["jsx"])(p["Text"], {
                                    className: "describeValue",
                                    children: "为了您的账号安全，请绑定手机号"
                                })
                            }) : Object(k["jsxs"])(p["View"], {
                                className: "loginDescribe",
                                children: [ Object(k["jsx"])(p["Text"], {
                                    className: "describeValue",
                                    children: "登录后可以关注项目，邀请朋友获得返利"
                                }), Object(k["jsx"])(p["Text"], {
                                    className: "describeValue",
                                    children: "享受更多的功能和服务"
                                }) ]
                            }), t.nickname ? t.mobile ? "" : "weapp" == a ? Object(k["jsxs"])(p["Button"], {
                                className: "loginButton customButton mobileButton",
                                openType: "getPhoneNumber",
                                onGetPhoneNumber: this.getPhoneNumber.bind(this),
                                children: [ Object(k["jsx"])(p["Text"], {
                                    className: "icomoon icon-mobile"
                                }), " 微信手机号一键绑定" ]
                            }) : Object(k["jsx"])(p["Button"], {
                                className: "loginButton customButton mobileButton",
                                openType: "getPhoneNumber",
                                onGetPhoneNumber: this.getPhoneNumber.bind(this),
                                children: "手机号一键绑定"
                            }) : "swan" != a ? Object(k["jsx"])(p["View"], {
                                className: "loginButton userInfoButton",
                                onClick: this.getUserInfo.bind(this),
                                children: "weapp" == a ? "微信一键登录" : "一键登录"
                            }) : Object(k["jsx"])(p["Button"], {
                                className: "loginButton customButton userInfoButton",
                                openType: "getUserInfo",
                                onGetUserInfo: this.getUserInfo.bind(this),
                                children: "一键登录"
                            }), Object(k["jsxs"])(p["View"], {
                                className: "bottom-hint",
                                children: [ "  登录即同意", Object(k["jsx"])(p["Text"], {
                                    className: "hint-highlight",
                                    "data-title": "用户协议",
                                    "data-url": "https://fa-dev.kaoputou.com/api/html/user-agreement",
                                    onClick: this.handleClick.bind(this),
                                    children: "《用户协议》"
                                }), "及", Object(k["jsx"])(p["Text"], {
                                    className: "hint-highlight",
                                    "data-title": "隐私政策",
                                    "data-url": "https://fa-dev.kaoputou.com/api/html/privacy-policy",
                                    onClick: this.handleClick.bind(this),
                                    children: "《隐私政策》"
                                }) ]
                            }) ]
                        })
                    });
                }
            } ]), a;
        }(d["Component"])) || i), y = I, B = {
            navigationBarTitleText: "窄门餐眼"
        };
        Page(Object(s["createPageConfig"])(y, "pages/login/index", {
            root: {
                cn: []
            }
        }, B || {}));
    }
}, [ [ 524, 0, 1, 2, 3 ] ] ]);