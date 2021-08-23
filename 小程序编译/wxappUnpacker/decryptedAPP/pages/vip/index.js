(wx["webpackJsonp"] = wx["webpackJsonp"] || []).push([ [ 222 ], {
    326: function(e, a, t) {},
    527: function(e, a, t) {
        "use strict";
        t.r(a);
        var s, c, i = t(8), n = t(16), r = t.n(n), o = t(20), l = t(10), d = t(11), u = t(5), p = t(12), j = t(13), h = t(4), m = t(3), x = t(2), b = t.n(x), v = t(1), y = t(21), g = t.n(y), O = t(6), w = t.n(O), f = t(14), N = (t(326), 
        t(7)), V = t(97), T = t.n(V), k = t(17), I = t(34), S = t(28), P = t(29), B = t(0), D = Object(I["a"])("gio"), C = [ {
            id: 0,
            data: [ "权益内容", "普通用户", "VIP用户" ]
        }, {
            id: 1,
            data: [ "品牌数据", "每日限3个", "无限制" ]
        }, {
            id: 2,
            data: [ "地区数据", "限省级数据", "无限制" ]
        }, {
            id: 3,
            data: [ "对比功能", "最多3个品牌", "无限制" ]
        }, {
            id: 4,
            data: [ "报告生成", "不支持", "支持" ]
        }, {
            id: 5,
            data: [ "报告数据", "每日限3个", "无限制" ]
        }, {
            id: 6,
            data: [ "外卖数据", "每日限5个", "无限制" ]
        }, {
            id: 7,
            data: [ "品牌列表", "限前20个", "无限制" ]
        }, {
            id: 8,
            data: [ "供应商页面", "部分可见", "无限制" ]
        } ], L = (s = Object(f["b"])(function(e) {
            return {
                user: e.user,
                ui: e.ui,
                dialog: e.dialog,
                permission: e.permission
            };
        }, {
            dispatchSetUserInfo: S["a"],
            dispatchChangeDialogItem: P["a"]
        }), s(c = function(e) {
            Object(p["a"])(t, e);
            var a = Object(j["a"])(t);
            function t() {
                var e;
                Object(l["a"])(this, t);
                for (var s = arguments.length, c = new Array(s), i = 0; i < s; i++) c[i] = arguments[i];
                return e = a.call.apply(a, [ this ].concat(c)), Object(h["a"])(Object(u["a"])(e), "state", {
                    discount: null,
                    useDiscount: !1,
                    isIos: !1,
                    priceType: 3,
                    price: 999,
                    priceClass: {
                        type1: 149,
                        type2: 399,
                        type3: 999,
                        type4: 1999
                    },
                    buyClass: {
                        type0: "",
                        type1: "month",
                        type2: "season_v2",
                        type3: "year",
                        type4: "three_years"
                    },
                    vipBuyList: [],
                    activityEntrance: null
                }), Object(h["a"])(Object(u["a"])(e), "requestPay", function(a) {
                    var t = e.props.user, s = e.state, c = s.priceType, i = s.buyClass;
                    if (t.nickname && t.mobile) {
                        var n = e.state, r = n.discount, o = n.useDiscount, l = "", d = i["type" + c];
                        r && o && (l = r.id), l || D("track", "clickPayButton"), e.weappPay(l, d, a);
                    } else b.a.navigateTo({
                        url: "/pages/login/index"
                    });
                }), e;
            }
            return Object(d["a"])(t, [ {
                key: "componentDidShow",
                value: function() {
                    var e = Object(o["a"])(r.a.mark(function e() {
                        return r.a.wrap(function(e) {
                            while (1) switch (e.prev = e.next) {
                              case 0:
                                this.loadVipBuyShowList(), this.loadUserInfo(), this.setState({
                                    isIos: "ios" == b.a.getSystemInfoSync().platform
                                });

                              case 3:
                              case "end":
                                return e.stop();
                            }
                        }, e, this);
                    }));
                    function a() {
                        return e.apply(this, arguments);
                    }
                    return a;
                }()
            }, {
                key: "onShareAppMessage",
                value: function() {
                    return {
                        title: "窄门餐眼-餐饮人都在用的数据神器",
                        desc: "已收录1500万+餐饮门店数据",
                        path: "pages/vip/index"
                    };
                }
            }, {
                key: "loadUserInfo",
                value: function() {
                    var e = this;
                    N["a"].loadUserInfo().then(function(a) {
                        e.props.dispatchSetUserInfo(a.data), a.data.isVip || e.loadDiscountInfo();
                    });
                }
            }, {
                key: "loadDiscountInfo",
                value: function() {
                    var e = this;
                    b.a.showLoading({
                        icon: "none",
                        title: "加载中..."
                    }), N["a"].queryDiscountInfo().then(function(a) {
                        a.data.success && a.data.record && e.setState({
                            price: a.data.record.amount,
                            priceType: 0,
                            discount: a.data.record,
                            useDiscount: !0
                        }), b.a.hideLoading();
                    });
                }
            }, {
                key: "loadVipBuyShowList",
                value: function() {
                    var e = this;
                    N["a"].vipBuyShowList().then(function(a) {
                        a.data.success && e.setState({
                            vipBuyList: a.data.records,
                            activityEntrance: a.data.activityEntrance
                        });
                    });
                }
            }, {
                key: "changeUseDiscount",
                value: function() {
                    var e, a, t = this.state, s = t.useDiscount, c = t.discount, i = !s;
                    i ? (e = c.amount, a = 0) : (e = "", a = 0), this.setState({
                        useDiscount: i,
                        price: e,
                        priceType: a
                    });
                }
            }, {
                key: "changePriceType",
                value: function(e) {
                    var a = this.state, t = a.priceType, s = a.priceClass, c = e.currentTarget.dataset.type;
                    t != c && this.setState({
                        priceType: c,
                        useDiscount: !1,
                        price: s["type" + c]
                    });
                }
            }, {
                key: "weappPay",
                value: function(e, a, t) {
                    var s = this;
                    b.a.showLoading({
                        icon: "none",
                        title: "加载中..."
                    }), N["a"].payOrder(e, a, t).then(function(a) {
                        if (b.a.hideLoading(), a.data.success) {
                            var t = a.data.record;
                            b.a.requestPayment({
                                timeStamp: String(t.timeStamp),
                                nonceStr: t.nonceStr,
                                package: t.package,
                                signType: t.signType,
                                paySign: t.paySign
                            }).then(function(a) {
                                a.errMsg.indexOf("ok") > -1 && (e || D("track", "sucPayVip"), b.a.showToast({
                                    title: "支付成功"
                                }), s.setState({
                                    priceType: 3,
                                    price: 999
                                }), s.loadUserInfo(), b.a.navigateTo({
                                    url: "/pages-extend/association/index"
                                }));
                            }).catch(function(e) {
                                console.log("error", e), "requestPayment:fail cancel" == e.errMsg && s.payFail();
                            });
                        } else b.a.showToast({
                            title: "请求支付失败",
                            icon: "none"
                        });
                    });
                }
            }, {
                key: "ttPay",
                value: function() {
                    var e = Object(o["a"])(r.a.mark(function e(a, t, s) {
                        var c, i, n = this;
                        return r.a.wrap(function(e) {
                            while (1) switch (e.prev = e.next) {
                              case 0:
                                return b.a.showLoading({
                                    icon: "none",
                                    title: "加载中..."
                                }), e.next = 3, N["a"].payOrder(a, t, s);

                              case 3:
                                c = e.sent, i = c.data, tt.pay({
                                    orderInfo: i.record,
                                    service: 4,
                                    getOrderStatus: function(e) {
                                        var a = e.out_order_no;
                                        return new Promise(function(e, t) {
                                            N["a"].waitPayTtStatus(a, "alipay").then(function(a) {
                                                e({
                                                    code: a.code
                                                });
                                            }).catch(function(e) {
                                                t(e);
                                            });
                                        });
                                    },
                                    success: function(e) {
                                        0 == e.code && (a || (D("track", "sucPayVip"), N["a"].tTGetRequest(2)), b.a.hideLoading(), 
                                        b.a.showToast({
                                            title: "支付成功",
                                            success: function() {
                                                n.setState({
                                                    priceType: 3,
                                                    price: 999
                                                }), setTimeout(function() {
                                                    n.loadUserInfo();
                                                }, 1500);
                                            }
                                        }));
                                    },
                                    fail: function(e) {
                                        console.log("error", e), b.a.hideLoading(), n.payFail();
                                    }
                                });

                              case 6:
                              case "end":
                                return e.stop();
                            }
                        }, e);
                    }));
                    function a(a, t, s) {
                        return e.apply(this, arguments);
                    }
                    return a;
                }()
            }, {
                key: "swanPay",
                value: function() {
                    var e = Object(o["a"])(r.a.mark(function e(a, t, s) {
                        var c, i, n = this;
                        return r.a.wrap(function(e) {
                            while (1) switch (e.prev = e.next) {
                              case 0:
                                return b.a.showLoading({
                                    icon: "none",
                                    title: "加载中..."
                                }), e.next = 3, N["a"].payOrder(a, t, s);

                              case 3:
                                c = e.sent, i = c.data, swan.requestPolymerPayment({
                                    orderInfo: i.record,
                                    success: function() {
                                        b.a.hideLoading(), a || D("track", "sucPayVip"), b.a.showToast({
                                            title: "支付成功",
                                            success: function() {
                                                n.setState({
                                                    priceType: 3,
                                                    price: 999
                                                }), setTimeout(function() {
                                                    n.loadUserInfo();
                                                }, 1500);
                                            }
                                        });
                                    },
                                    fail: function(e) {
                                        console.log("error", e), b.a.hideLoading(), n.payFail();
                                    }
                                });

                              case 6:
                              case "end":
                                return e.stop();
                            }
                        }, e);
                    }));
                    function a(a, t, s) {
                        return e.apply(this, arguments);
                    }
                    return a;
                }()
            }, {
                key: "payFail",
                value: function() {
                    b.a.showModal({
                        title: "提示",
                        content: "邀请新用户可获得免费会员时长",
                        confirmText: "查看规则",
                        success: function(e) {
                            e.confirm && b.a.navigateTo({
                                url: "/pages-extend/invite/index"
                            }), e.cancel;
                        }
                    });
                }
            }, {
                key: "customNavigateTo",
                value: function() {
                    b.a.navigateTo({
                        url: "/pages-extend/invite/poster"
                    });
                }
            }, {
                key: "navLoginPage",
                value: function() {
                    b.a.navigateTo({
                        url: "/pages/login/index"
                    });
                }
            }, {
                key: "navLink",
                value: function(e) {
                    var a = e.currentTarget.dataset.url;
                    a && b.a.navigateTo({
                        url: a
                    });
                }
            }, {
                key: "makePhoneCall",
                value: function() {
                    b.a.makePhoneCall({
                        phoneNumber: "13466794661"
                    });
                }
            }, {
                key: "copyWxAccount",
                value: function(e) {
                    var a = e.currentTarget.dataset.text;
                    b.a.setClipboardData({
                        data: a,
                        success: function() {
                            b.a.showToast({
                                title: "复制成功"
                            });
                        }
                    });
                }
            }, {
                key: "extendBuyVip",
                value: function() {
                    var e = this.props.user;
                    e.nickname && e.mobile ? this.requestPay() : b.a.navigateTo({
                        url: "/pages/login/index"
                    });
                }
            }, {
                key: "render",
                value: function() {
                    var e = this.props, a = e.user, t = e.ui, s = this.state, c = s.discount, i = s.useDiscount, n = s.priceType, r = s.price, o = s.vipBuyList, l = s.isIos, d = s.activityEntrance;
                    if (!a.loaded) return Object(B["jsx"])(v["View"], {});
                    var u = "", p = a.isVip, j = "", h = !1, m = "", x = "", b = "";
                    h = !l && !p, p || (m = "notVip" == a.vipStatus ? "会员未开通" : "vipExpired" == a.vipStatus ? "会员已过期" : "", 
                    m = l ? "您还不是会员" : m), p && (u = g()(a.vipExpiredDatetime).format("YYYY年MM月DD日")), 
                    c && (j = g()(c.expiredDatetime).format("YYYY年MM月DD日")), a.nickname && (b = a.nickname.length > 8 ? a.nickname.slice(0, 8) + "." : a.nickname), 
                    a.mobile && (x = a.mobile.replace(/^(\d{3})\d{4}(\d+)/, "$1****$2"));
                    var y = function(e) {
                        return e.length >= 5 ? e.substring(0, 2) + "***" : e.substring(0, 1) + "****";
                    };
                    return Object(B["jsxs"])(v["View"], {
                        className: "vip",
                        children: [ a.nickname && a.mobile ? p ? Object(B["jsx"])(v["View"], {
                            style: {
                                padding: "0 40rpx"
                            },
                            children: Object(B["jsxs"])(v["View"], {
                                className: "card active",
                                children: [ Object(B["jsx"])(v["Image"], {
                                    className: "cardBg",
                                    src: "https://canyan.kp-static.com/vipNewBg.png"
                                }), Object(B["jsxs"])(v["View"], {
                                    className: "userInfo",
                                    children: [ a.avatar ? Object(B["jsx"])(v["Image"], {
                                        className: "avatarBox",
                                        src: a.avatar
                                    }) : Object(B["jsx"])(v["View"], {
                                        className: "avatarBox",
                                        children: Object(B["jsx"])(v["Image"], {
                                            className: "avatar",
                                            src: T.a
                                        })
                                    }), Object(B["jsxs"])(v["View"], {
                                        className: "label",
                                        children: [ Object(B["jsxs"])(v["View"], {
                                            className: "lebelName",
                                            children: [ b + x, Object(B["jsx"])(v["Text"], {
                                                className: "icomoon icon-crown"
                                            }) ]
                                        }), Object(B["jsxs"])(v["View"], {
                                            className: "lebelExpired",
                                            children: [ "有效期至 ", u ]
                                        }) ]
                                    }) ]
                                }), Object(B["jsxs"])(v["Text"], {
                                    className: "association-entrance-box",
                                    onClick: this.navLink.bind(this),
                                    "data-url": "/pages-extend/association/index",
                                    children: [ Object(B["jsx"])(v["Text"], {
                                        className: "icomoon icon-association-entrance"
                                    }), Object(B["jsx"])(v["Text"], {
                                        className: "entrance-value",
                                        children: "加入餐眼社群"
                                    }) ]
                                }) ]
                            })
                        }) : Object(B["jsx"])(v["View"], {
                            style: {
                                padding: "0 40rpx"
                            },
                            children: Object(B["jsxs"])(v["View"], {
                                className: "card",
                                children: [ Object(B["jsx"])(v["Image"], {
                                    className: "cardBg",
                                    src: "https://canyan.kp-static.com/vipNewBg.png"
                                }), Object(B["jsxs"])(v["View"], {
                                    className: "userInfo",
                                    children: [ a.avatar ? Object(B["jsx"])(v["Image"], {
                                        className: "avatarBox",
                                        src: a.avatar
                                    }) : Object(B["jsx"])(v["View"], {
                                        className: "avatarBox",
                                        children: Object(B["jsx"])(v["Image"], {
                                            className: "avatar",
                                            src: T.a
                                        })
                                    }), Object(B["jsxs"])(v["View"], {
                                        className: "label",
                                        children: [ Object(B["jsxs"])(v["View"], {
                                            className: "lebelName",
                                            children: [ b + x, Object(B["jsx"])(v["Text"], {
                                                className: "icomoon icon-crown"
                                            }) ]
                                        }), Object(B["jsx"])(v["View"], {
                                            className: "lebelExpired",
                                            children: m
                                        }) ]
                                    }) ]
                                }) ]
                            })
                        }) : Object(B["jsx"])(v["View"], {
                            style: {
                                padding: "0 40rpx"
                            },
                            children: Object(B["jsxs"])(v["View"], {
                                className: "card",
                                onClick: this.navLoginPage.bind(this),
                                children: [ Object(B["jsx"])(v["Image"], {
                                    className: "cardBg",
                                    src: "https://canyan.kp-static.com/vipNewBg.png"
                                }), Object(B["jsxs"])(v["View"], {
                                    className: "userInfo",
                                    children: [ Object(B["jsx"])(v["View"], {
                                        className: "avatarBox",
                                        children: Object(B["jsx"])(v["Image"], {
                                            className: "avatar",
                                            src: T.a
                                        })
                                    }), Object(B["jsx"])(v["View"], {
                                        className: "label",
                                        children: Object(B["jsx"])(v["View"], {
                                            className: "lebelName",
                                            children: "点击登录"
                                        })
                                    }) ]
                                }) ]
                            })
                        }), d && Object(B["jsx"])(v["Image"], {
                            className: "lottery-entrance",
                            src: d.bg,
                            onClick: this.navLink.bind(this),
                            "data-url": d.path,
                            mode: "widthFix"
                        }), !l && Object(B["jsxs"])(v["View"], {
                            className: "vipDuration",
                            children: [ Object(B["jsx"])(v["View"], {
                                className: "vTitle",
                                children: "选择套餐："
                            }), Object(B["jsxs"])(v["View"], {
                                className: "vClass",
                                children: [ Object(B["jsxs"])(v["View"], {
                                    className: w()("classItem", {
                                        active: 2 == n
                                    }),
                                    "data-type": "2",
                                    onClick: this.changePriceType.bind(this),
                                    children: [ Object(B["jsx"])(v["Text"], {
                                        className: "date",
                                        children: "3个月"
                                    }), Object(B["jsxs"])(v["View"], {
                                        className: "price",
                                        children: [ "¥", Object(B["jsx"])(v["Text"], {
                                            className: "number",
                                            children: "399"
                                        }), " " ]
                                    }), Object(B["jsx"])(v["View"], {
                                        className: "oldPrice",
                                        children: "¥4.4/天"
                                    }) ]
                                }), Object(B["jsxs"])(v["View"], {
                                    className: w()("classItem", {
                                        active: 3 == n
                                    }),
                                    "data-type": "3",
                                    onClick: this.changePriceType.bind(this),
                                    children: [ Object(B["jsx"])(v["Text"], {
                                        className: "date",
                                        children: "12个月"
                                    }), Object(B["jsxs"])(v["View"], {
                                        className: "price",
                                        children: [ "¥", Object(B["jsx"])(v["Text"], {
                                            className: "number",
                                            children: "999"
                                        }), " " ]
                                    }), Object(B["jsx"])(v["View"], {
                                        className: "oldPrice",
                                        children: "¥2.8/天"
                                    }), Object(B["jsx"])(v["Text"], {
                                        className: "price-hint",
                                        children: "最多购买"
                                    }) ]
                                }), Object(B["jsxs"])(v["View"], {
                                    className: w()("classItem", {
                                        active: 4 == n
                                    }),
                                    "data-type": "4",
                                    onClick: this.changePriceType.bind(this),
                                    children: [ Object(B["jsx"])(v["Text"], {
                                        className: "date",
                                        children: "3年"
                                    }), Object(B["jsxs"])(v["View"], {
                                        className: "price",
                                        children: [ "¥", Object(B["jsx"])(v["Text"], {
                                            className: "number",
                                            children: "1999"
                                        }), " " ]
                                    }), Object(B["jsx"])(v["View"], {
                                        className: "oldPrice",
                                        children: "¥1.9/天"
                                    }), Object(B["jsx"])(v["Text"], {
                                        className: "price-hint",
                                        children: "超值"
                                    }) ]
                                }) ]
                            }), c && !a.isVip && Object(B["jsxs"])(v["View"], {
                                className: "discountMessage",
                                children: [ Object(B["jsxs"])(v["View"], {
                                    className: "row1",
                                    children: [ Object(B["jsx"])(v["View"], {
                                        className: "option",
                                        onClick: this.changeUseDiscount.bind(this),
                                        children: i && Object(B["jsx"])(v["Text"], {
                                            className: "icomoon icon-select"
                                        })
                                    }), Object(B["jsxs"])(v["View"], {
                                        className: "discountPrice",
                                        children: [ c.title, "特别优惠： ", c.amount, "元 / 年" ]
                                    }) ]
                                }), Object(B["jsx"])(v["View"], {
                                    className: "row2",
                                    children: Object(B["jsxs"])(v["View"], {
                                        className: "expired",
                                        children: [ "有效期至 ", j ]
                                    })
                                }) ]
                            }) ]
                        }), o.length > 0 && !l && Object(B["jsx"])(v["View"], {
                            className: "purchase-tip-box",
                            children: Object(B["jsx"])(v["Swiper"], {
                                className: "tip-swiper",
                                autoplay: !0,
                                interval: "2500",
                                circular: !0,
                                vertical: !0,
                                "easing-function": "easeInOutCubic",
                                children: o.map(function(e) {
                                    return Object(B["jsx"])(v["SwiperItem"], {
                                        children: Object(B["jsx"])(v["View"], {
                                            className: "tip-item",
                                            children: Object(B["jsxs"])(v["Text"], {
                                                className: "item-value",
                                                children: [ "".concat(y(e.name), " ").concat(Object(k["e"])(e.buyTime), "花费了"), Object(B["jsx"])(v["Text"], {
                                                    className: "count",
                                                    children: "".concat(e.amount, "元")
                                                }), "购买了会员" ]
                                            })
                                        })
                                    }, e.buyTime);
                                })
                            })
                        }), Object(B["jsxs"])(v["View"], {
                            className: "section",
                            children: [ Object(B["jsx"])(v["View"], {
                                className: "title",
                                children: "餐眼会员权益"
                            }), Object(B["jsx"])(v["View"], {
                                className: "content",
                                children: Object(B["jsx"])(v["View"], {
                                    className: "table",
                                    children: C.map(function(e, a) {
                                        return Object(B["jsx"])(v["View"], {
                                            className: "vip-row",
                                            children: e.data.map(function(e, t) {
                                                return Object(B["jsx"])(v["View"], {
                                                    className: "vip-cell",
                                                    children: e
                                                }, "".concat(a, ".").concat(t));
                                            })
                                        }, e.id);
                                    })
                                })
                            }) ]
                        }), Object(B["jsxs"])(v["View"], {
                            className: "section special",
                            children: [ Object(B["jsx"])(v["View"], {
                                className: "title",
                                children: "他们都在用窄门餐眼（部分会员）"
                            }), Object(B["jsx"])(v["Image"], {
                                className: "vip-evaluate",
                                src: "https://canyan.kp-static.com/vip-brands-new.png",
                                mode: "widthFix"
                            }), Object(B["jsx"])(v["View"], {
                                className: "title special",
                                children: "会员评价"
                            }), Object(B["jsx"])(v["Image"], {
                                className: "vip-evaluate",
                                src: "https://canyan.kp-static.com/vip-evaluate1-new.png",
                                mode: "widthFix"
                            }), Object(B["jsx"])(v["Image"], {
                                className: "vip-evaluate",
                                src: "https://canyan.kp-static.com/vip-evaluate2.png",
                                mode: "widthFix"
                            }) ]
                        }), h && Object(B["jsx"])(v["Image"], {
                            className: "inviterButton",
                            src: "https://canyan.kp-static.com/inviterButton.png",
                            onClick: this.customNavigateTo.bind(this)
                        }), Object(B["jsxs"])(v["View"], {
                            className: w()("buttons", {
                                "-iphonex": t.isIphonex
                            }),
                            children: [ !l && Object(B["jsxs"])(v["View"], {
                                className: "button ios-buy",
                                onClick: this.extendBuyVip.bind(this),
                                children: [ " ", "立即以 ", Object(B["jsx"])(v["Text"], {
                                    className: "pay-number",
                                    children: "".concat(r, "元")
                                }), " 价格购买" ]
                            }), Object(B["jsx"])(v["Button"], {
                                className: "button contact",
                                openType: "contact",
                                children: "联系客服"
                            }) ]
                        }) ]
                    });
                }
            } ]), t;
        }(m["Component"])) || c), M = L, U = {
            navigationBarTitleText: "会员服务",
            enableShareAppMessage: !0
        };
        M.enableShareAppMessage = !0;
        Page(Object(i["createPageConfig"])(M, "pages/vip/index", {
            root: {
                cn: []
            }
        }, U || {}));
    },
    97: function(e, a, t) {
        e.exports = t.p + "asset/images/user-active.png";
    }
}, [ [ 527, 0, 1, 2, 3 ] ] ]);