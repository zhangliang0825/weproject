(wx["webpackJsonp"] = wx["webpackJsonp"] || []).push([ [ 218 ], {
    325: function(e, a, t) {},
    525: function(e, a, t) {
        "use strict";
        t.r(a);
        var n, s, i = t(8), c = t(16), r = t.n(c), o = t(20), l = t(18), d = t(10), j = t(11), h = t(5), m = t(12), u = t(13), p = t(4), x = t(3), b = t(2), g = t.n(b), O = t(1), v = t(14), w = t(21), N = t.n(w), f = t(64), T = t(23), k = t(38), V = (t(325), 
        t(7)), y = t(17), C = t(29), D = t(0), I = function(e) {
            return N()(e).format("YYYY-MM-DD");
        }, M = (n = Object(v["b"])(function(e) {
            return {
                dialog: e.dialog,
                user: e.user,
                permission: e.permission,
                ui: e.ui
            };
        }, {
            dispatchChangeDialogItem: C["a"]
        }), n(s = function(e) {
            Object(m["a"])(t, e);
            var a = Object(u["a"])(t);
            function t() {
                var e;
                Object(d["a"])(this, t);
                for (var n = arguments.length, s = new Array(n), i = 0; i < n; i++) s[i] = arguments[i];
                return e = a.call.apply(a, [ this ].concat(s)), Object(p["a"])(Object(h["a"])(e), "state", {
                    emailId: null,
                    articles: [],
                    reports: [],
                    financingEvents: []
                }), Object(p["a"])(Object(h["a"])(e), "navClick", function(a) {
                    var t = e.props.user, n = a.currentTarget.dataset, s = n.url, i = n.limit;
                    return t.mobile ? !t.isVip && i ? g.a.navigateTo({
                        url: "/pages/vip/index"
                    }) : void g.a.navigateTo({
                        url: s
                    }) : g.a.navigateTo({
                        url: "/pages/login/index"
                    });
                }), e;
            }
            return Object(j["a"])(t, [ {
                key: "componentDidMount",
                value: function() {
                    this.ajaxLoad();
                }
            }, {
                key: "onShareAppMessage",
                value: function() {
                    return {
                        title: "窄门餐眼-餐饮人都在用的数据神器",
                        desc: "已收录1500万+餐饮门店数据",
                        path: "pages/information/index"
                    };
                }
            }, {
                key: "ajaxLoad",
                value: function() {
                    var e = this;
                    g.a.showLoading({
                        icon: "none",
                        title: "请等待..."
                    }), V["a"].initPopularInformation().then(function(a) {
                        if (g.a.hideLoading(), a.data.success) {
                            var t = a.data, n = t.articles, s = t.reports, i = t.financingEvents;
                            e.setState({
                                articles: Object(l["a"])(n),
                                reports: Object(l["a"])(s),
                                financingEvents: Object(l["a"])(i)
                            });
                        }
                    });
                }
            }, {
                key: "openReport",
                value: function() {
                    var e = Object(o["a"])(r.a.mark(function e(a) {
                        var t, n, s, i, c, o;
                        return r.a.wrap(function(e) {
                            while (1) switch (e.prev = e.next) {
                              case 0:
                                t = this.props.ui, n = a.currentTarget.dataset.id, e.next = 5;
                                break;

                              case 5:
                                return g.a.showLoading({
                                    icon: "none",
                                    title: "请稍等，下载中..."
                                }), e.prev = 6, e.next = 9, V["a"].queryReportUrl(n);

                              case 9:
                                if (s = e.sent, !s.data.success) {
                                    e.next = 19;
                                    break;
                                }
                                return i = s.data.record, e.next = 14, g.a.downloadFile({
                                    url: i
                                });

                              case 14:
                                c = e.sent, g.a.hideLoading(), g.a.openDocument({
                                    filePath: c.tempFilePath,
                                    fileType: "pdf",
                                    showMenu: !0
                                }), e.next = 22;
                                break;

                              case 19:
                                g.a.hideLoading(), o = s.data.error ? s.data.error.message : "加载失败", "超过每日访问限制" === o ? g.a.showModal({
                                    title: "提示",
                                    content: t.isIos ? "未解锁" : "非会员每日最多查看3个报告，会员无限制",
                                    confirmText: "查看详情",
                                    success: function(e) {
                                        e.confirm && g.a.navigateTo({
                                            url: "/pages/vip/index"
                                        });
                                    }
                                }) : g.a.showToast({
                                    title: o,
                                    icon: "none"
                                });

                              case 22:
                                e.next = 27;
                                break;

                              case 24:
                                e.prev = 24, e.t0 = e["catch"](6), g.a.hideLoading();

                              case 27:
                              case "end":
                                return e.stop();
                            }
                        }, e, this, [ [ 6, 24 ] ]);
                    }));
                    function a(a) {
                        return e.apply(this, arguments);
                    }
                    return a;
                }()
            }, {
                key: "sentEmail",
                value: function(e) {
                    var a = this, t = e.currentTarget.dataset.id;
                    this.setState({
                        emailId: t
                    }, function() {
                        g.a.hideTabBar({
                            animation: !0,
                            success: function() {
                                a.props.dispatchChangeDialogItem({
                                    emailDialog: !0
                                });
                            }
                        });
                    });
                }
            }, {
                key: "handleNoticeCopyToView",
                value: function(e) {
                    var a = e.currentTarget.dataset.url;
                    g.a.setClipboardData({
                        data: a
                    }).then(function(e) {
                        g.a.hideToast(), "setClipboardData:ok" === e.errMsg && g.a.showToast({
                            icon: "none",
                            title: "已复制到剪贴板，请打开浏览器访问"
                        });
                    });
                }
            }, {
                key: "navClick",
                value: function(e) {
                    var a = e.currentTarget.dataset.url;
                    a && g.a.navigateTo({
                        url: a
                    });
                }
            }, {
                key: "render",
                value: function() {
                    var e = this, a = this.state, t = a.emailId, n = a.articles, s = a.reports, i = a.financingEvents, c = this.props.dialog.emailDialog, r = this.props.permission, o = 0;
                    switch ("weapp") {
                      case "swan":
                        o = !r.swanShow;
                        break;

                      case "tt":
                        o = !r.isShow;
                        break;
                    }
                    return Object(D["jsx"])(k["a"], {
                        title: "热门资讯",
                        showHome: !1,
                        children: Object(D["jsxs"])(O["View"], {
                            className: "information-page",
                            children: [ Object(D["jsxs"])(O["View"], {
                                className: "page-header",
                                children: [ Object(D["jsxs"])(O["Navigator"], {
                                    className: "header-item",
                                    url: "/pages-extend/article/index",
                                    hoverClass: "none",
                                    children: [ Object(D["jsx"])(O["Image"], {
                                        className: "item-png",
                                        src: "https://canyan.kp-static.com/hot-news.png",
                                        mode: "widthFix"
                                    }), Object(D["jsx"])(O["View"], {
                                        className: "item-value",
                                        children: "新闻热点"
                                    }) ]
                                }), Object(D["jsxs"])(O["Navigator"], {
                                    className: "header-item",
                                    url: "/pages-extend/report/index",
                                    hoverClass: "none",
                                    children: [ Object(D["jsx"])(O["Image"], {
                                        className: "item-png",
                                        src: "https://canyan.kp-static.com/hot-reports.png",
                                        mode: "widthFix"
                                    }), Object(D["jsx"])(O["View"], {
                                        className: "item-value",
                                        children: "行研报告"
                                    }) ]
                                }), Object(D["jsxs"])(O["Navigator"], {
                                    className: "header-item",
                                    url: "/pages-extend/finance-event/index",
                                    hoverClass: "none",
                                    children: [ Object(D["jsx"])(O["Image"], {
                                        className: "item-png",
                                        src: "https://canyan.kp-static.com/hot-invests.png",
                                        mode: "widthFix"
                                    }), Object(D["jsx"])(O["View"], {
                                        className: "item-value",
                                        children: "投资事件"
                                    }) ]
                                }) ]
                            }), Object(D["jsx"])(T["a"], {
                                title: "新闻热点",
                                bottomNav: {
                                    name: "查看更多新闻热点",
                                    url: "/pages-extend/article/index"
                                },
                                nonePadding: !0,
                                children: n.map(function(e) {
                                    return Object(D["jsxs"])(O["Navigator"], {
                                        className: "articles",
                                        url: "/pages-extend/article/content?slug=".concat(e.slug),
                                        hoverClass: "none",
                                        children: [ Object(D["jsx"])(O["View"], {
                                            className: "title",
                                            children: e.title
                                        }), Object(D["jsx"])(O["Image"], {
                                            className: "cover",
                                            mode: "aspectFill",
                                            src: Object(y["c"])(e.cover, 100)
                                        }), Object(D["jsxs"])(O["View"], {
                                            className: "metas",
                                            children: [ Object(D["jsx"])(O["View"], {
                                                className: "author",
                                                children: e.author
                                            }), Object(D["jsx"])(O["View"], {
                                                className: "date",
                                                children: e.publishDate
                                            }), e.readNum > 0 && Object(D["jsxs"])(O["View"], {
                                                className: "pv",
                                                children: [ e.pv, "阅读" ]
                                            }) ]
                                        }) ]
                                    }, "slug");
                                })
                            }), Object(D["jsx"])(T["a"], {
                                title: "行研报告",
                                bottomNav: {
                                    name: "查看更多行研报告",
                                    url: "/pages-extend/report/index"
                                },
                                nonePadding: !0,
                                children: s.map(function(a) {
                                    return Object(D["jsxs"])(O["View"], {
                                        className: "report",
                                        children: [ Object(D["jsx"])(O["View"], {
                                            className: "cover",
                                            children: "PDF"
                                        }), Object(D["jsxs"])(O["View"], {
                                            className: "info",
                                            children: [ Object(D["jsx"])(O["View"], {
                                                className: "name",
                                                children: a.title
                                            }), Object(D["jsxs"])(O["View"], {
                                                className: "meta",
                                                children: [ Object(D["jsx"])(O["Text"], {
                                                    children: a.publisher
                                                }), Object(D["jsx"])(O["Text"], {
                                                    children: a.publishDate
                                                }) ]
                                            }), Object(D["jsxs"])(O["View"], {
                                                className: "size",
                                                children: [ Object(D["jsx"])(O["Text"], {
                                                    className: "size-value",
                                                    children: a.size
                                                }), !o && Object(D["jsxs"])(O["View"], {
                                                    className: "buttons center",
                                                    "data-id": a.id,
                                                    onClick: e.openReport.bind(e),
                                                    children: [ Object(D["jsx"])(O["Text"], {
                                                        className: "icomoon icon-cloud"
                                                    }), Object(D["jsx"])(O["Text"], {
                                                        children: "在线预览"
                                                    }) ]
                                                }), Object(D["jsxs"])(O["View"], {
                                                    className: "buttons",
                                                    "data-id": a.id,
                                                    onClick: e.sentEmail.bind(e),
                                                    children: [ Object(D["jsx"])(O["Text"], {
                                                        className: "icomoon icon-email"
                                                    }), Object(D["jsx"])(O["Text"], {
                                                        children: "发送到邮箱"
                                                    }) ]
                                                }) ]
                                            }) ]
                                        }) ]
                                    }, a.id);
                                })
                            }), Object(D["jsx"])(T["a"], {
                                title: "投资事件",
                                bottomNav: {
                                    name: "查看更多投资事件",
                                    url: "/pages-extend/finance-event/index"
                                },
                                nonePadding: !0,
                                children: i.map(function(a) {
                                    return Object(D["jsxs"])(O["View"], {
                                        className: "event",
                                        children: [ a.logo ? Object(D["jsx"])(O["View"], {
                                            className: "logo",
                                            style: {
                                                backgroundImage: "url(".concat(a.logo, ")")
                                            }
                                        }) : Object(D["jsx"])(O["View"], {
                                            className: "logo -empty",
                                            children: a.brand.slice(0, 1)
                                        }), Object(D["jsxs"])(O["View"], {
                                            className: "container",
                                            children: [ Object(D["jsx"])(O["View"], {
                                                className: "header",
                                                children: Object(D["jsx"])(O["Text"], {
                                                    className: "title",
                                                    children: a.brand
                                                })
                                            }), a.brief && Object(D["jsx"])(O["Text"], {
                                                className: "intros",
                                                children: a.brief
                                            }), Object(D["jsxs"])(O["Text"], {
                                                className: "finance-round",
                                                children: [ "完成", a.amount, a.round, "融资" ]
                                            }), Object(D["jsxs"])(O["Text"], {
                                                className: "agency",
                                                children: [ Object(D["jsx"])(O["Text"], {
                                                    className: "light",
                                                    children: a.investors
                                                }), "未披露" === a.investors ? "" : "投资" ]
                                            }), Object(D["jsxs"])(O["Text"], {
                                                className: "happen",
                                                children: [ I(a.finDate), " . ", a.location ]
                                            }) ]
                                        }), a.link && Object(D["jsx"])(O["View"], {
                                            className: "link",
                                            "data-url": a.link,
                                            onClick: e.handleNoticeCopyToView.bind(e),
                                            children: Object(D["jsx"])(O["View"], {
                                                className: "icon",
                                                children: Object(D["jsx"])(O["Text"], {
                                                    className: "icomoon icon-link"
                                                })
                                            })
                                        }) ]
                                    }, a.id);
                                })
                            }), c && Object(D["jsx"])(f["a"], {
                                url: "/research-report/".concat(t, "/send-email")
                            }) ]
                        })
                    });
                }
            } ]), t;
        }(x["Component"])) || s), P = M, L = {
            navigationBarTitleText: "热门资讯",
            enableShareAppMessage: !0,
            navigationStyle: "custom"
        };
        P.enableShareAppMessage = !0;
        Page(Object(i["createPageConfig"])(P, "pages/information/index", {
            root: {
                cn: []
            }
        }, L || {}));
    }
}, [ [ 525, 0, 1, 2, 3 ] ] ]);