(wx["webpackJsonp"] = wx["webpackJsonp"] || []).push([ [ 216 ], {
    124: function(e, a, t) {
        e.exports = t.p + "asset/images/index-brand.png";
    },
    125: function(e, a, t) {
        e.exports = t.p + "asset/images/index-region.png";
    },
    126: function(e, a, t) {
        e.exports = t.p + "asset/images/index-waimai.png";
    },
    127: function(e, a, t) {
        e.exports = t.p + "asset/images/index-premium.png";
    },
    128: function(e, a, t) {
        e.exports = t.p + "asset/images/index-zhaimen.png";
    },
    129: function(e, a, t) {
        e.exports = t.p + "asset/images/index-supplier.png";
    },
    130: function(e, a, t) {
        e.exports = t.p + "asset/images/index-food.png";
    },
    131: function(e, a, t) {
        e.exports = t.p + "asset/images/index-shopping.png";
    },
    309: function(e, a, t) {},
    312: function(e, a, t) {},
    313: function(e, a, t) {
        e.exports = t.p + "asset/images/index-report.png";
    },
    314: function(e, a, t) {},
    505: function(e, a, t) {
        "use strict";
        t.r(a);
        var n = t(8), s = t(10), i = t(11), r = t(5), c = t(12), o = t(13), l = t(4), p = t(3), d = t(2), g = t.n(d), u = t(1), h = t(14), m = t(6), x = t.n(m), b = (t(309), 
        t(7)), j = t(38), w = t(36), f = (t(312), t(0)), O = function(e) {
            Object(c["a"])(t, e);
            var a = Object(o["a"])(t);
            function t() {
                return Object(s["a"])(this, t), a.apply(this, arguments);
            }
            return Object(i["a"])(t, [ {
                key: "render",
                value: function() {
                    var e = this.props, a = e.text, t = e.style, n = e.id, s = e.url;
                    return Object(f["jsx"])(u["Navigator"], {
                        className: "comp-project-search",
                        id: n,
                        style: t,
                        url: s,
                        hoverClass: "none",
                        children: Object(f["jsxs"])(u["View"], {
                            className: "search",
                            children: [ Object(f["jsx"])(u["Text"], {
                                className: "icomoon icon-search2"
                            }), Object(f["jsx"])(u["Text"], {
                                className: "desc",
                                children: a
                            }) ]
                        })
                    });
                }
            } ]), t;
        }(p["Component"]);
        Object(l["a"])(O, "options", {
            addGlobalClass: !0
        }), O.defaultProps = {
            text: "",
            url: "",
            id: ""
        };
        var v = O, y = t(124), N = t.n(y), C = t(125), k = t.n(C), S = t(126), T = t.n(S), V = (t(313), 
        t(127)), I = t.n(V), H = t(128), D = t.n(H), U = t(129), A = t.n(U), L = t(130), B = t.n(L), _ = t(131), R = t.n(_), M = t(9), P = (t(314), 
        t(31)), F = t(34);
        function J(e) {
            var a = Object(F["a"])("gio"), t = Object(p["useState"])(!1), n = Object(M["a"])(t, 2), s = n[0], i = n[1], r = Object(h["c"])(), c = e.poster;
            function o() {
                i(!0), setTimeout(function() {
                    g.a.showTabBar({
                        animation: !0,
                        success: function() {
                            r({
                                type: P["a"],
                                dialog: {
                                    indexAdverDialog: !1
                                }
                            });
                        }
                    });
                }, 1e3);
            }
            function l(e) {
                var t = e.currentTarget.dataset, n = t.url, s = t.action;
                n && (a("track", "adsHome"), g.a[s || "navigateTo"]({
                    url: n
                }));
            }
            return Object(f["jsx"])(u["View"], {
                className: x()("index-adver-page", {
                    "scale-in-y": !s,
                    "scale-out-y": s
                }),
                children: Object(f["jsxs"])(u["View"], {
                    className: "page-box",
                    children: [ Object(f["jsx"])(u["Image"], {
                        className: "box-poster",
                        src: c.url,
                        mode: "widthFix",
                        onClick: l,
                        "data-url": c.path
                    }), Object(f["jsx"])(u["Text"], {
                        className: "icomoon icon-answer-pass-close",
                        onClick: o
                    }) ]
                })
            });
        }
        J.defaultProps = {
            poster: ""
        };
        var q, W, z = t(28), E = t(29), G = [ {
            name: "食材版块",
            src: "supplier-index-food.png",
            bgColor: "rgba(138,210,127,0.10)",
            hot: !0,
            width: 24,
            height: 25
        }, {
            name: "门店装修设计",
            src: "supplier-index-fitment.png",
            bgColor: "rgba(242,194,103,0.10)",
            width: 23,
            height: 25
        }, {
            name: "设备设施",
            src: "supplier-index-facility.png",
            bgColor: "rgba(163,174,226,0.10)",
            width: 25,
            height: 25
        }, {
            name: "餐饮家具",
            src: "supplier-index-furniture.png",
            bgColor: "rgba(224,147,103,0.10)",
            width: 32,
            height: 25
        }, {
            name: "信息化软硬件",
            src: "supplier-index-message.png",
            bgColor: "rgba(81,108,177,0.10)",
            width: 24,
            height: 25
        }, {
            name: "厨房用具",
            src: "supplier-index-kitchen.png",
            bgColor: "rgba(220,147,158,0.10)",
            width: 23,
            height: 25
        }, {
            name: "低值易耗品",
            src: "supplier-index-consumables.png",
            bgColor: "rgba(223,186,128,0.10)",
            width: 27,
            height: 25
        }, {
            name: "仓储信息",
            src: "supplier-index-storage.png",
            bgColor: "rgba(204,176,149,0.10)",
            width: 25,
            height: 25
        }, {
            name: "冷链物流",
            src: "supplier-index-logistics.png",
            bgColor: "rgba(135,179,219,0.10)",
            width: 34,
            height: 25
        }, {
            name: "中央厨房/工厂",
            src: "supplier-index-plant.png",
            bgColor: "rgba(182,185,195,0.10)",
            width: 25,
            height: 25
        } ], K = [ {
            name: "茶饮设备",
            src: "supplier-index-tea.png",
            bgColor: "rgba(163,174,226,0.10)",
            width: 28,
            height: 25
        }, {
            name: "包装耗材",
            src: "supplier-index-pack.png",
            bgColor: "rgba(242,194,103,0.10)",
            width: 25,
            height: 25
        }, {
            name: "茶叶",
            src: "supplier-index-tea-leaf.png",
            bgColor: "rgba(204,176,149,0.10)",
            width: 21,
            height: 25
        }, {
            name: "乳制品",
            src: "supplier-index-dairy.png",
            bgColor: "rgba(193,179,244,0.10)",
            width: 16,
            height: 25
        }, {
            name: "水果制品",
            src: "supplier-index-fruits.png",
            bgColor: "rgba(220,160,147,0.10)",
            width: 25,
            height: 25
        }, {
            name: "糖浆制品",
            src: "supplier-index-syrup.png",
            bgColor: "rgba(223,173,128,0.10)",
            width: 16,
            height: 25
        }, {
            name: "各类小料",
            src: "supplier-index-flavour.png",
            bgColor: "rgba(201,167,133,0.10)",
            width: 32,
            height: 23
        } ], Q = (q = Object(h["b"])(function(e) {
            return {
                user: e.user,
                dialog: e.dialog,
                permission: e.permission
            };
        }, {
            dispatchSetUserInfo: z["a"],
            dispatchChangeDialogItem: E["a"]
        }), q(W = function(e) {
            Object(c["a"])(t, e);
            var a = Object(o["a"])(t);
            function t() {
                var e;
                Object(s["a"])(this, t);
                for (var n = arguments.length, i = new Array(n), c = 0; c < n; c++) i[c] = arguments[c];
                return e = a.call.apply(a, [ this ].concat(i)), Object(l["a"])(Object(r["a"])(e), "state", {
                    hasNext: !0,
                    brands: [],
                    banners: [],
                    suppliers: [],
                    poster: null,
                    showCollectHint: !1,
                    identity: 1,
                    entryData: [ {
                        name: "index_brand",
                        title: "查品牌",
                        src: N.a,
                        url: "/pages-extend/brands/index",
                        new: !1
                    }, {
                        name: "index_region",
                        title: "省市分析",
                        src: k.a,
                        url: "/pages-extend/region/main",
                        new: !1
                    }, {
                        name: "index_waimai",
                        title: "外卖榜单",
                        src: T.a,
                        url: "/pages-extend/waimai/ranking",
                        new: !1
                    }, {
                        name: "index_supplier",
                        title: "找供应商",
                        src: A.a,
                        url: "/pages-extend/supplier/index",
                        new: !1
                    }, {
                        name: "index_premium",
                        title: "加盟优选",
                        src: I.a,
                        url: "/pages-extend/premium-brands/index",
                        new: !g.a.getStorageSync("index_premium")
                    }, {
                        name: "index_food",
                        title: "每日菜价",
                        src: B.a,
                        url: "/pages-extend/food/index",
                        new: !1
                    }, {
                        name: "index_shopping",
                        title: "购物中心",
                        src: R.a,
                        url: "/pages-extend/shopping/index",
                        new: !1
                    }, {
                        name: "index_zhaimen",
                        title: "餐饮培训",
                        src: D.a,
                        url: "/pages-extend2/home/index",
                        new: !1
                    } ]
                }), Object(l["a"])(Object(r["a"])(e), "current", Object(d["getCurrentInstance"])()), 
                Object(l["a"])(Object(r["a"])(e), "loading", !1), Object(l["a"])(Object(r["a"])(e), "page", 1), 
                Object(l["a"])(Object(r["a"])(e), "displayNotice", !1), Object(l["a"])(Object(r["a"])(e), "clock", null), 
                e;
            }
            return Object(i["a"])(t, [ {
                key: "componentWillMount",
                value: function() {
                    var e = this;
                    console.log("index====", this.current.router);
                    var a, t, n = this.current.router.params.query;
                    if (n && n.scene) {
                        var s = decodeURIComponent(n.scene), i = s.split("&");
                        i.map(function(e) {
                            e.indexOf("slug") > -1 && (a = e.replace("slug=", "")), e.indexOf("page") > -1 && (t = e.replace("page=", ""));
                        });
                    }
                    "answer" == t && g.a.navigateTo({
                        url: "/pages-extend/activity/answer-pass/index"
                    }), a && t && "answer" != t && g.a.navigateTo({
                        url: "/pages/".concat(t, "/index?slug=").concat(a)
                    }), g.a.getStorageSync("showCollectHint") || (this.setState({
                        showCollectHint: !0
                    }), this.collectHintClock = setTimeout(function() {
                        e.setState({
                            showCollectHint: !1
                        }), clearTimeout(e.collectHintClock);
                    }, 3e4));
                }
            }, {
                key: "componentDidMount",
                value: function() {
                    var e = g.a.getUpdateManager();
                    e.onCheckForUpdate(function(e) {
                        e.hasUpdate && g.a.showLoading({
                            icon: "none",
                            title: "新版本下载中..."
                        });
                    }), e.onUpdateReady(function() {
                        g.a.hideLoading(), g.a.showModal({
                            title: "更新提示",
                            content: "有新版本发布，是否立即体验新版?",
                            complete: function(a) {
                                a.confirm && e.applyUpdate();
                            }
                        });
                    }), this.ajaxLoad();
                }
            }, {
                key: "componentWillUnmount",
                value: function() {
                    clearTimeout(this.collectHintClock);
                }
            }, {
                key: "onPullDownRefresh",
                value: function() {
                    this.ajaxLoad(function() {
                        g.a.stopPullDownRefresh();
                    });
                }
            }, {
                key: "onReachBottom",
                value: function() {
                    !this.loading && this.state.hasNext && (this.page += 1, this.loadBrands(this.page));
                }
            }, {
                key: "onShareAppMessage",
                value: function() {
                    var e = this.props.user, a = "";
                    return e.nickname && e.mobile && (a = e.slug), {
                        title: "窄门餐眼",
                        desc: "已收录1500万+餐饮门店数据",
                        path: a ? "pages/index/index?inviter=".concat(a) : "pages/index/index"
                    };
                }
            }, {
                key: "loadUserInfo",
                value: function() {
                    var e = this, a = this.props.user;
                    a.loaded || b["a"].loadUserInfo().then(function(a) {
                        a.data.success && e.props.dispatchSetUserInfo(a.data);
                    });
                }
            }, {
                key: "onTabItemTap",
                value: function(e) {
                    0 === e.index && g.a.pageScrollTo({
                        scrollTop: 0,
                        duration: 300
                    });
                }
            }, {
                key: "ajaxLoad",
                value: function() {
                    var e = this, a = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : null;
                    this.loading = !0, g.a.showLoading({
                        icon: "none",
                        title: "请等待..."
                    }), b["a"].queryIndex().then(function(t) {
                        e.loading = !1, g.a.hideLoading(), t.data.success ? (e.setState({
                            brands: t.data.brands,
                            banners: t.data.banners || [],
                            poster: t.data.poster,
                            suppliers: t.data.suppliers
                        }, function() {
                            t.data.poster && t.data.poster.url && (g.a.getStorageSync("indexAdv") && g.a.getStorageSync("indexAdv") == t.data.poster.url || g.a.hideTabBar({
                                animation: !0,
                                success: function() {
                                    e.props.dispatchChangeDialogItem({
                                        indexAdverDialog: !0
                                    }), g.a.setStorageSync("indexAdv", t.data.poster.url);
                                }
                            }));
                        }), e.loadUserInfo()) : g.a.showToast({
                            title: t.data.error ? t.data.error.message : "加载失败",
                            icon: "none"
                        }), a && a();
                    });
                }
            }, {
                key: "loadBrands",
                value: function() {
                    var e = this, a = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 1;
                    this.loading = !0, g.a.showLoading({
                        icon: "none",
                        title: "请等待..."
                    }), b["a"].queryHotBrands({
                        page: a
                    }).then(function(a) {
                        e.loading = !1, g.a.hideLoading();
                        var t = e.state.brands;
                        if (a.data.success) {
                            var n = t.concat(a.data.records);
                            e.setState({
                                brands: n,
                                hasNext: a.data.hasNext
                            });
                        } else g.a.showToast({
                            title: a.data.error ? a.data.error.message : "加载失败",
                            icon: "none"
                        });
                    });
                }
            }, {
                key: "navToCategory",
                value: function(e) {
                    var a = e.currentTarget.dataset.slug;
                    a && g.a.navigateTo({
                        url: "/pages-extend/category/index?slug=".concat(a)
                    });
                }
            }, {
                key: "navClick",
                value: function(e) {
                    var a = e.currentTarget.dataset, t = a.url, n = a.key, s = JSON.parse(JSON.stringify(this.state.entryData));
                    n && (g.a.setStorageSync(n, !0), s.map(function(e) {
                        e.name == n && (e.new = !1);
                    }), this.setState({
                        entryData: s
                    })), t && g.a.navigateTo({
                        url: t
                    });
                }
            }, {
                key: "goCategoryList",
                value: function() {
                    g.a.navigateTo({
                        url: "/pages/category-list/index"
                    });
                }
            }, {
                key: "onCollectHint",
                value: function() {
                    g.a.setStorageSync("showCollectHint", !0), this.setState({
                        showCollectHint: !1
                    });
                }
            }, {
                key: "render",
                value: function() {
                    var e = this, a = this.state, t = a.hasNext, n = a.brands, s = a.suppliers, i = a.banners, r = a.poster, c = a.showCollectHint, o = a.identity, l = a.entryData, p = this.props.permission, d = this.props.dialog.indexAdverDialog, g = 0;
                    switch ("weapp") {
                      case "swan":
                        g = !p.swanShow;
                        break;

                      case "tt":
                        g = !p.isShow;
                        break;
                    }
                    return Object(f["jsx"])(j["a"], {
                        showHome: !1,
                        children: Object(f["jsxs"])(u["View"], {
                            className: "portal-page",
                            style: {
                                paddingBottom: t ? "0" : "40rpx"
                            },
                            children: [ c && Object(f["jsx"])(u["View"], {
                                className: "add-tip",
                                onClick: this.onCollectHint.bind(this),
                                children: "添加到「我的小程序」更快找到我"
                            }), Object(f["jsxs"])(u["View"], {
                                className: "search-box",
                                children: [ Object(f["jsx"])(u["Text"], {
                                    className: "link",
                                    children: "已收录1500万+餐饮门店数据"
                                }), Object(f["jsx"])(v, {
                                    text: "请输入餐饮品牌或者品类",
                                    url: "/pages-extend/public-page/search?type=3"
                                }) ]
                            }), Object(f["jsx"])(u["View"], {
                                className: x()("entry-list", {
                                    tt: g
                                }),
                                children: l.map(function(a) {
                                    return a.new ? Object(f["jsxs"])(u["View"], {
                                        className: "entry active",
                                        "data-url": a.url,
                                        "data-key": a.name,
                                        onClick: e.navClick.bind(e),
                                        children: [ Object(f["jsx"])(u["Image"], {
                                            src: a.src,
                                            className: "icon"
                                        }), Object(f["jsx"])(u["View"], {
                                            className: "label",
                                            children: a.title
                                        }), Object(f["jsx"])(u["Text"], {
                                            className: "point",
                                            children: "NEW"
                                        }) ]
                                    }, a.name) : Object(f["jsxs"])(u["Navigator"], {
                                        className: "entry",
                                        url: a.url,
                                        hoverClass: "none",
                                        children: [ Object(f["jsx"])(u["Image"], {
                                            src: a.src,
                                            className: "icon"
                                        }), Object(f["jsx"])(u["View"], {
                                            className: "label",
                                            children: a.title
                                        }) ]
                                    }, a.name);
                                })
                            }), 1 == i.length && Object(f["jsx"])(u["Navigator"], {
                                className: "banner",
                                url: i[0].path,
                                hoverClass: "none",
                                children: Object(f["jsx"])(u["Image"], {
                                    src: i[0].url,
                                    className: "cover",
                                    mode: "widthFix"
                                })
                            }), i.length > 1 && Object(f["jsx"])(u["Swiper"], {
                                className: "banners",
                                circular: !0,
                                autoplay: !0,
                                children: i.map(function(e) {
                                    return Object(f["jsx"])(u["SwiperItem"], {
                                        children: Object(f["jsx"])(u["Navigator"], {
                                            className: "banner",
                                            url: e.path,
                                            hoverClass: "none",
                                            children: Object(f["jsx"])(u["Image"], {
                                                src: e.url,
                                                className: "cover",
                                                mode: "widthFix"
                                            })
                                        })
                                    }, e.url);
                                })
                            }), s.length > 0 && Object(f["jsxs"])(u["View"], {
                                className: "hot-supplier",
                                children: [ Object(f["jsx"])(u["View"], {
                                    className: "hot-title",
                                    children: "餐饮&茶饮供应商"
                                }), Object(f["jsxs"])(u["Swiper"], {
                                    className: "supplier-swiper",
                                    circular: !0,
                                    autoplay: !0,
                                    indicatorDots: !0,
                                    interval: 1e4,
                                    indicatorActiveColor: "rgba(0, 0, 0, .6)",
                                    children: [ Object(f["jsx"])(u["SwiperItem"], {
                                        children: Object(f["jsx"])(u["View"], {
                                            className: "supplier-list",
                                            children: G.map(function(e) {
                                                return Object(f["jsxs"])(u["Navigator"], {
                                                    className: "list-item cate",
                                                    url: "/pages-extend/supplier/all?classify=".concat(e.name, "&type=cate"),
                                                    hoverClass: "none",
                                                    children: [ Object(f["jsx"])(u["Image"], {
                                                        style: "width: ".concat(e.width, "px;height: ").concat(e.height, "px"),
                                                        className: "icon-src",
                                                        src: "https://canyan.kp-static.com/".concat(e.src)
                                                    }), Object(f["jsx"])(u["View"], {
                                                        className: "item-name",
                                                        children: e.name
                                                    }), e.hot && Object(f["jsx"])(u["Text"], {
                                                        className: "tag",
                                                        children: "热门"
                                                    }) ]
                                                }, e.name);
                                            })
                                        })
                                    }), Object(f["jsx"])(u["SwiperItem"], {
                                        children: Object(f["jsxs"])(u["View"], {
                                            className: "supplier-list",
                                            children: [ K.map(function(e) {
                                                return Object(f["jsxs"])(u["Navigator"], {
                                                    className: "list-item tea",
                                                    url: "/pages-extend/supplier/all?classify=".concat(e.name, "&type=tea"),
                                                    hoverClass: "none",
                                                    children: [ Object(f["jsx"])(u["Image"], {
                                                        style: "width: ".concat(e.width, "px;height: ").concat(e.height, "px"),
                                                        className: "icon-src",
                                                        src: "https://canyan.kp-static.com/".concat(e.src)
                                                    }), Object(f["jsx"])(u["View"], {
                                                        className: "item-name",
                                                        children: e.name
                                                    }), e.hot && Object(f["jsx"])(u["Text"], {
                                                        className: "tag",
                                                        children: "热门"
                                                    }) ]
                                                }, e.name);
                                            }), Object(f["jsx"])(u["View"], {
                                                className: "list-item tea"
                                            }), Object(f["jsx"])(u["View"], {
                                                className: "list-item tea"
                                            }), Object(f["jsx"])(u["View"], {
                                                className: "list-item tea"
                                            }) ]
                                        })
                                    }) ]
                                }) ]
                            }), Object(f["jsxs"])(u["View"], {
                                className: "hot-brands",
                                children: [ Object(f["jsx"])(u["View"], {
                                    className: "typeBar",
                                    children: Object(f["jsx"])(u["View"], {
                                        className: x()("typeItem", "row1", {
                                            active: "1" == o
                                        }),
                                        children: " 热门品牌 "
                                    })
                                }), Object(f["jsx"])(u["View"], {
                                    className: "brands-list",
                                    children: n && n.map(function(e) {
                                        return Object(f["jsx"])(w["a"], {
                                            goodRate: e.goodRate,
                                            evaluation: e.evaluation,
                                            logo: e.logo,
                                            name: e.name,
                                            shopCount: e.shopCount,
                                            company: e.company,
                                            categories: e.categories,
                                            slug: e.slug
                                        }, e.slug);
                                    })
                                }) ]
                            }), d && Object(f["jsx"])(J, {
                                poster: r
                            }) ]
                        })
                    });
                }
            } ]), t;
        }(p["Component"])) || W), X = Q, Y = {
            navigationBarTitleText: "窄门餐眼",
            enablePullDownRefresh: !0,
            backgroundTextStyle: "dark",
            enableShareAppMessage: !0,
            navigationStyle: "custom"
        };
        X.enableShareAppMessage = !0;
        Page(Object(n["createPageConfig"])(X, "pages/index/index", {
            root: {
                cn: []
            }
        }, Y || {}));
    }
}, [ [ 505, 0, 1, 2, 3 ] ] ]);