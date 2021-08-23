(wx["webpackJsonp"] = wx["webpackJsonp"] || []).push([ [ 1 ], {
    1: function(e, t, n) {
        "use strict";
        n.r(t), n.d(t, "Ad", function() {
            return D;
        }), n.d(t, "AdCustom", function() {
            return Y;
        }), n.d(t, "Audio", function() {
            return A;
        }), n.d(t, "Block", function() {
            return M;
        }), n.d(t, "Button", function() {
            return s;
        }), n.d(t, "Camera", function() {
            return x;
        }), n.d(t, "Canvas", function() {
            return R;
        }), n.d(t, "Checkbox", function() {
            return u;
        }), n.d(t, "CheckboxGroup", function() {
            return l;
        }), n.d(t, "CoverImage", function() {
            return w;
        }), n.d(t, "CoverView", function() {
            return C;
        }), n.d(t, "CustomWrapper", function() {
            return V;
        }), n.d(t, "Editor", function() {
            return U;
        }), n.d(t, "Form", function() {
            return d;
        }), n.d(t, "FunctionalPageNavigator", function() {
            return z;
        }), n.d(t, "Icon", function() {
            return o;
        }), n.d(t, "Image", function() {
            return I;
        }), n.d(t, "Input", function() {
            return f;
        }), n.d(t, "Label", function() {
            return h;
        }), n.d(t, "LivePlayer", function() {
            return _;
        }), n.d(t, "LivePusher", function() {
            return H;
        }), n.d(t, "Map", function() {
            return F;
        }), n.d(t, "MatchMedia", function() {
            return q;
        }), n.d(t, "MovableArea", function() {
            return O;
        }), n.d(t, "MovableView", function() {
            return j;
        }), n.d(t, "NavigationBar", function() {
            return Q;
        }), n.d(t, "Navigator", function() {
            return B;
        }), n.d(t, "OfficialAccount", function() {
            return $;
        }), n.d(t, "OpenData", function() {
            return G;
        }), n.d(t, "PageContainer", function() {
            return X;
        }), n.d(t, "PageMeta", function() {
            return K;
        }), n.d(t, "Picker", function() {
            return p;
        }), n.d(t, "PickerView", function() {
            return v;
        }), n.d(t, "PickerViewColumn", function() {
            return g;
        }), n.d(t, "Progress", function() {
            return i;
        }), n.d(t, "Radio", function() {
            return b;
        }), n.d(t, "RadioGroup", function() {
            return m;
        }), n.d(t, "RichText", function() {
            return a;
        }), n.d(t, "ScrollView", function() {
            return T;
        }), n.d(t, "Slider", function() {
            return y;
        }), n.d(t, "Slot", function() {
            return W;
        }), n.d(t, "Swiper", function() {
            return P;
        }), n.d(t, "SwiperItem", function() {
            return E;
        }), n.d(t, "Switch", function() {
            return S;
        }), n.d(t, "Text", function() {
            return c;
        }), n.d(t, "Textarea", function() {
            return k;
        }), n.d(t, "Video", function() {
            return L;
        }), n.d(t, "View", function() {
            return r;
        }), n.d(t, "VoipRoom", function() {
            return J;
        }), n.d(t, "WebView", function() {
            return N;
        });
        var r = "view", o = "icon", i = "progress", a = "rich-text", c = "text", s = "button", u = "checkbox", l = "checkbox-group", d = "form", f = "input", h = "label", p = "picker", v = "picker-view", g = "picker-view-column", b = "radio", m = "radio-group", y = "slider", S = "switch", w = "cover-image", k = "textarea", C = "cover-view", O = "movable-area", j = "movable-view", T = "scroll-view", P = "swiper", E = "swiper-item", B = "navigator", A = "audio", x = "camera", I = "image", _ = "live-player", L = "video", R = "canvas", D = "ad", N = "web-view", M = "block", F = "map", W = "slot", V = "custom-wrapper", U = "editor", q = "match-media", z = "functional-page-navigator", H = "live-pusher", $ = "official-account", G = "open-data", Q = "navigation-bar", K = "page-meta", J = "voip-room", Y = "ad-custom", X = "page-container";
    },
    115: function(e, t, n) {
        "use strict";
        n.r(t), function(e, r) {
            var o = n(8);
            function i(e) {
                return i = "function" === typeof Symbol && "symbol" === typeof Symbol.iterator ? function(e) {
                    return typeof e;
                } : function(e) {
                    return e && "function" === typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e;
                }, i(e);
            }
            function a(e, t) {
                if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
            }
            function c(e, t) {
                for (var n = 0; n < t.length; n++) {
                    var r = t[n];
                    r.enumerable = r.enumerable || !1, r.configurable = !0, "value" in r && (r.writable = !0), 
                    Object.defineProperty(e, r.key, r);
                }
            }
            function s(e, t, n) {
                return t && c(e.prototype, t), n && c(e, n), e;
            }
            function u(e, t, n) {
                return t in e ? Object.defineProperty(e, t, {
                    value: n,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = n, e;
            }
            function l(e, t) {
                var n = Object.keys(e);
                if (Object.getOwnPropertySymbols) {
                    var r = Object.getOwnPropertySymbols(e);
                    t && (r = r.filter(function(t) {
                        return Object.getOwnPropertyDescriptor(e, t).enumerable;
                    })), n.push.apply(n, r);
                }
                return n;
            }
            function d(e) {
                for (var t = 1; t < arguments.length; t++) {
                    var n = null != arguments[t] ? arguments[t] : {};
                    t % 2 ? l(Object(n), !0).forEach(function(t) {
                        u(e, t, n[t]);
                    }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(n)) : l(Object(n)).forEach(function(t) {
                        Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(n, t));
                    });
                }
                return e;
            }
            "function" !== typeof Object.assign && (Object.assign = function(e) {
                if (null == e) throw new TypeError("Cannot convert undefined or null to object");
                for (var t = Object(e), n = 1; n < arguments.length; n++) {
                    var r = arguments[n];
                    if (null != r) for (var o in r) Object.prototype.hasOwnProperty.call(r, o) && (t[o] = r[o]);
                }
                return t;
            }), "function" !== typeof Object.defineProperties && (Object.defineProperties = function(e, t) {
                function n(e) {
                    function t(e, t) {
                        return Object.prototype.hasOwnProperty.call(e, t);
                    }
                    function n(e) {
                        return "function" === typeof e;
                    }
                    if ("object" !== i(e) || null === e) throw new TypeError("bad desc");
                    var r = {};
                    if (t(e, "enumerable") && (r.enumerable = !!e.enumerable), t(e, "configurable") && (r.configurable = !!e.configurable), 
                    t(e, "value") && (r.value = e.value), t(e, "writable") && (r.writable = !!e.writable), 
                    t(e, "get")) {
                        var o = e.get;
                        if (!n(o) && "undefined" !== typeof o) throw new TypeError("bad get");
                        r.get = o;
                    }
                    if (t(e, "set")) {
                        var a = e.set;
                        if (!n(a) && "undefined" !== typeof a) throw new TypeError("bad set");
                        r.set = a;
                    }
                    if (("get" in r || "set" in r) && ("value" in r || "writable" in r)) throw new TypeError("identity-confused descriptor");
                    return r;
                }
                if ("object" !== i(e) || null === e) throw new TypeError("bad obj");
                t = Object(t);
                for (var r = Object.keys(t), o = [], a = 0; a < r.length; a++) o.push([ r[a], n(t[r[a]]) ]);
                for (var c = 0; c < o.length; c++) Object.defineProperty(e, o[c][0], o[c][1]);
                return e;
            });
            var f = {
                WEAPP: "WEAPP",
                WEB: "WEB",
                RN: "RN",
                SWAN: "SWAN",
                ALIPAY: "ALIPAY",
                TT: "TT",
                QQ: "QQ",
                JD: "JD"
            }, h = null;
            function p() {
                return h || ("undefined" !== typeof jd && jd.getSystemInfo ? (h = f.JD, f.JD) : "undefined" !== typeof qq && qq.getSystemInfo ? (h = f.QQ, 
                f.QQ) : "undefined" !== typeof tt && tt.getSystemInfo ? (h = f.TT, f.TT) : "undefined" !== typeof wx && wx.getSystemInfo ? (h = f.WEAPP, 
                f.WEAPP) : "undefined" !== typeof swan && swan.getSystemInfo ? (h = f.SWAN, f.SWAN) : "undefined" !== typeof my && my.getSystemInfo ? (h = f.ALIPAY, 
                f.ALIPAY) : "undefined" !== typeof e && e.__fbGenNativeModule ? (h = f.RN, f.RN) : "undefined" !== typeof r ? (h = f.WEB, 
                f.WEB) : "Unknown environment");
            }
            function v() {}
            var g = function() {
                function e(t) {
                    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : [], r = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : 0;
                    a(this, e), this.index = r, this.requestParams = t, this.interceptors = n;
                }
                return s(e, [ {
                    key: "proceed",
                    value: function(e) {
                        if (this.requestParams = e, this.index >= this.interceptors.length) throw new Error("chain 参数错误, 请勿直接修改 request.chain");
                        var t = this._getNextInterceptor(), n = this._getNextChain(), r = t(n), o = r["catch"](function(e) {
                            return Promise.reject(e);
                        });
                        return "function" === typeof r.abort && (o.abort = r.abort), o;
                    }
                }, {
                    key: "_getNextInterceptor",
                    value: function() {
                        return this.interceptors[this.index];
                    }
                }, {
                    key: "_getNextChain",
                    value: function() {
                        return new e(this.requestParams, this.interceptors, this.index + 1);
                    }
                } ]), e;
            }(), b = function() {
                function e(t) {
                    a(this, e), this.taroInterceptor = t, this.chain = new g();
                }
                return s(e, [ {
                    key: "request",
                    value: function(e) {
                        var t = this;
                        return this.chain.interceptors = this.chain.interceptors.filter(function(e) {
                            return e !== t.taroInterceptor;
                        }), this.chain.interceptors.push(this.taroInterceptor), this.chain.proceed(d({}, e));
                    }
                }, {
                    key: "addInterceptor",
                    value: function(e) {
                        this.chain.interceptors.push(e);
                    }
                }, {
                    key: "cleanInterceptors",
                    value: function() {
                        this.chain = new g();
                    }
                } ]), e;
            }();
            function m(e) {
                var t, n = e.requestParams, r = new Promise(function(r, o) {
                    var i = setTimeout(function() {
                        i = null, o(new Error("网络链接超时,请稍后再试！"));
                    }, n && n.timeout || 6e4);
                    t = e.proceed(n), t.then(function(e) {
                        i && (clearTimeout(i), r(e));
                    })["catch"](function(e) {
                        i && clearTimeout(i), o(e);
                    });
                });
                return void 0 !== t && "function" === typeof t.abort && (r.abort = t.abort), r;
            }
            function y(e) {
                var t = e.requestParams, n = t.method, r = t.data, o = t.url;
                console.log("http ".concat(n || "GET", " --\x3e ").concat(o, " data: "), r);
                var i = e.proceed(t), a = i.then(function(e) {
                    return console.log("http <-- ".concat(o, " result:"), e), e;
                });
                return "function" === typeof i.abort && (a.abort = i.abort), a;
            }
            var S = Object.freeze({
                __proto__: null,
                timeoutInterceptor: m,
                logInterceptor: y
            }), w = {
                onSocketOpen: !0,
                onSocketError: !0,
                onSocketMessage: !0,
                onSocketClose: !0,
                onBackgroundAudioPlay: !0,
                onBackgroundAudioPause: !0,
                onBackgroundAudioStop: !0,
                onNetworkStatusChange: !0,
                onAccelerometerChange: !0,
                onCompassChange: !0,
                onBluetoothAdapterStateChange: !0,
                onBluetoothDeviceFound: !0,
                onBLEConnectionStateChange: !0,
                onBLECharacteristicValueChange: !0,
                onBeaconUpdate: !0,
                onBeaconServiceChange: !0,
                onUserCaptureScreen: !0,
                onHCEMessage: !0,
                onGetWifiList: !0,
                onWifiConnected: !0,
                onDeviceMotionChange: !0,
                setStorageSync: !0,
                getStorageSync: !0,
                getStorageInfoSync: !0,
                removeStorageSync: !0,
                clearStorageSync: !0,
                getSystemInfoSync: !0,
                getExtConfigSync: !0,
                getLogManager: !0,
                onMemoryWarning: !0,
                reportMonitor: !0,
                reportAnalytics: !0,
                navigateToSmartGameProgram: !0,
                getFileSystemManager: !0,
                getLaunchOptionsSync: !0,
                onPageNotFound: !0,
                onError: !0,
                onAppShow: !0,
                onAppHide: !0,
                offPageNotFound: !0,
                offError: !0,
                offAppShow: !0,
                offAppHide: !0,
                onAudioInterruptionEnd: !0,
                onAudioInterruptionBegin: !0,
                onLocationChange: !0,
                offLocationChange: !0,
                onUnhandledRejection: !0,
                offUnhandledRejection: !0,
                onThemeChange: !0,
                offThemeChange: !0,
                onKeyboardHeightChange: !0,
                offKeyboardHeightChange: !0
            }, k = {
                stopRecord: !0,
                getRecorderManager: !0,
                pauseVoice: !0,
                stopVoice: !0,
                pauseBackgroundAudio: !0,
                stopBackgroundAudio: !0,
                getBackgroundAudioManager: !0,
                createAudioContext: !0,
                createInnerAudioContext: !0,
                createVideoContext: !0,
                createCameraContext: !0,
                createLivePlayerContext: !0,
                createLivePusherContext: !0,
                createMapContext: !0,
                canIUse: !0,
                startAccelerometer: !0,
                stopAccelerometer: !0,
                startCompass: !0,
                stopCompass: !0,
                hideToast: !0,
                hideLoading: !0,
                showNavigationBarLoading: !0,
                hideNavigationBarLoading: !0,
                createAnimation: !0,
                createSelectorQuery: !0,
                createOffscreenCanvas: !0,
                createCanvasContext: !0,
                drawCanvas: !0,
                hideKeyboard: !0,
                stopPullDownRefresh: !0,
                createIntersectionObserver: !0,
                getMenuButtonBoundingClientRect: !0,
                onWindowResize: !0,
                offWindowResize: !0,
                arrayBufferToBase64: !0,
                base64ToArrayBuffer: !0,
                getAccountInfoSync: !0,
                getUpdateManager: !0,
                createWorker: !0,
                createRewardedVideoAd: !0,
                createInterstitialAd: !0
            }, C = {
                uploadFile: !0,
                downloadFile: !0,
                connectSocket: !0,
                sendSocketMessage: !0,
                closeSocket: !0,
                chooseImage: !0,
                chooseMessageFile: !0,
                previewImage: !0,
                getImageInfo: !0,
                compressImage: !0,
                saveImageToPhotosAlbum: !0,
                startRecord: !0,
                playVoice: !0,
                setInnerAudioOption: !0,
                getAvailableAudioSources: !0,
                getBackgroundAudioPlayerState: !0,
                playBackgroundAudio: !0,
                seekBackgroundAudio: !0,
                chooseVideo: !0,
                saveVideoToPhotosAlbum: !0,
                loadFontFace: !0,
                saveFile: !0,
                getFileInfo: !0,
                getSavedFileList: !0,
                getSavedFileInfo: !0,
                removeSavedFile: !0,
                openDocument: !0,
                setStorage: !0,
                getStorage: !0,
                getStorageInfo: !0,
                removeStorage: !0,
                clearStorage: !0,
                navigateBack: !0,
                navigateTo: !0,
                redirectTo: !0,
                switchTab: !0,
                reLaunch: !0,
                startLocationUpdate: !0,
                startLocationUpdateBackground: !0,
                stopLocationUpdate: !0,
                getLocation: !0,
                chooseLocation: !0,
                openLocation: !0,
                getSystemInfo: !0,
                getNetworkType: !0,
                makePhoneCall: !0,
                scanCode: !0,
                setClipboardData: !0,
                getClipboardData: !0,
                openBluetoothAdapter: !0,
                closeBluetoothAdapter: !0,
                getBluetoothAdapterState: !0,
                startBluetoothDevicesDiscovery: !0,
                stopBluetoothDevicesDiscovery: !0,
                getBluetoothDevices: !0,
                getConnectedBluetoothDevices: !0,
                createBLEConnection: !0,
                closeBLEConnection: !0,
                getBLEDeviceServices: !0,
                getBLEDeviceCharacteristics: !0,
                readBLECharacteristicValue: !0,
                writeBLECharacteristicValue: !0,
                notifyBLECharacteristicValueChange: !0,
                startBeaconDiscovery: !0,
                stopBeaconDiscovery: !0,
                getBeacons: !0,
                setScreenBrightness: !0,
                getScreenBrightness: !0,
                setKeepScreenOn: !0,
                vibrateLong: !0,
                vibrateShort: !0,
                addPhoneContact: !0,
                getHCEState: !0,
                startHCE: !0,
                stopHCE: !0,
                sendHCEMessage: !0,
                startWifi: !0,
                stopWifi: !0,
                connectWifi: !0,
                getWifiList: !0,
                setWifiList: !0,
                getConnectedWifi: !0,
                startDeviceMotionListening: !0,
                stopDeviceMotionListening: !0,
                pageScrollTo: !0,
                showToast: !0,
                showLoading: !0,
                showModal: !0,
                showActionSheet: !0,
                setNavigationBarTitle: !0,
                setNavigationBarColor: !0,
                setTabBarBadge: !0,
                removeTabBarBadge: !0,
                showTabBarRedDot: !0,
                hideTabBarRedDot: !0,
                setTabBarStyle: !0,
                setTabBarItem: !0,
                showTabBar: !0,
                hideTabBar: !0,
                setTopBarText: !0,
                startPullDownRefresh: !0,
                canvasToTempFilePath: !0,
                canvasGetImageData: !0,
                canvasPutImageData: !0,
                setBackgroundColor: !0,
                setBackgroundTextStyle: !0,
                getSelectedTextRange: !0,
                hideHomeButton: !0,
                getExtConfig: !0,
                login: !0,
                checkSession: !0,
                authorize: !0,
                getUserInfo: !0,
                checkIsSupportFacialRecognition: !0,
                startFacialRecognitionVerify: !0,
                startFacialRecognitionVerifyAndUploadVideo: !0,
                faceVerifyForPay: !0,
                requestPayment: !0,
                showShareMenu: !0,
                hideShareMenu: !0,
                updateShareMenu: !0,
                getShareInfo: !0,
                chooseAddress: !0,
                addCard: !0,
                openCard: !0,
                openSetting: !0,
                getSetting: !0,
                getWeRunData: !0,
                navigateToMiniProgram: !0,
                navigateBackMiniProgram: !0,
                chooseInvoice: !0,
                chooseInvoiceTitle: !0,
                checkIsSupportSoterAuthentication: !0,
                startSoterAuthentication: !0,
                checkIsSoterEnrolledInDevice: !0,
                requestSubscribeMessage: !0,
                setEnableDebug: !0,
                getOpenUserInfo: !0,
                ocrIdCard: !0,
                ocrBankCard: !0,
                ocrDrivingLicense: !0,
                ocrVehicleLicense: !0,
                textReview: !0,
                textToAudio: !0,
                imageAudit: !0,
                advancedGeneralIdentify: !0,
                objectDetectIdentify: !0,
                carClassify: !0,
                dishClassify: !0,
                logoClassify: !0,
                animalClassify: !0,
                plantClassify: !0,
                setPageInfo: !0,
                getSwanId: !0,
                requestPolymerPayment: !0,
                navigateToSmartProgram: !0,
                navigateBackSmartProgram: !0,
                preloadSubPackage: !0
            };
            function O(e) {
                var t = e.designWidth, n = void 0 === t ? 700 : t, r = e.deviceRatio, o = void 0 === r ? {
                    640: 1.17,
                    750: 1,
                    828: .905
                } : r;
                this.config = this.config || {}, this.config.designWidth = n, this.config.deviceRatio = o;
            }
            var j = {
                Events: o["Events"],
                eventCenter: o["eventCenter"],
                getEnv: p,
                ENV_TYPE: f,
                render: v,
                noPromiseApis: k,
                onAndSyncApis: w,
                otherApis: C,
                initPxTransform: O,
                Link: b,
                interceptors: S,
                Current: o["Current"],
                getCurrentInstance: o["getCurrentInstance"],
                useDidShow: o["useDidShow"],
                useDidHide: o["useDidHide"],
                usePullDownRefresh: o["usePullDownRefresh"],
                useReachBottom: o["useReachBottom"],
                usePageScroll: o["usePageScroll"],
                useResize: o["useResize"],
                useShareAppMessage: o["useShareAppMessage"],
                useTabItemTap: o["useTabItemTap"],
                useTitleClick: o["useTitleClick"],
                useOptionMenuClick: o["useOptionMenuClick"],
                usePullIntercept: o["usePullIntercept"],
                useShareTimeline: o["useShareTimeline"],
                useAddToFavorites: o["useAddToFavorites"],
                useReady: o["useReady"],
                useRouter: o["useRouter"],
                options: o["options"],
                nextTick: o["nextTick"]
            };
            t["default"] = j;
        }.call(this, n(45), n(8)["window"]);
    },
    15: function(e, t, n) {
        "use strict";
        n.d(t, "a", function() {
            return oe;
        }), n.d(t, "b", function() {
            return re;
        }), n.d(t, "c", function() {
            return ue;
        }), n.d(t, "d", function() {
            return te;
        }), n.d(t, "e", function() {
            return ae;
        }), n.d(t, "f", function() {
            return he;
        }), n.d(t, "g", function() {
            return de;
        }), n.d(t, "h", function() {
            return ee;
        }), n.d(t, "i", function() {
            return d;
        }), n.d(t, "j", function() {
            return l;
        }), n.d(t, "k", function() {
            return s;
        }), n.d(t, "l", function() {
            return u;
        }), n.d(t, "m", function() {
            return c;
        }), n.d(t, "n", function() {
            return i;
        }), n.d(t, "o", function() {
            return a;
        }), n.d(t, "p", function() {
            return me;
        }), n.d(t, "q", function() {
            return ye;
        }), n.d(t, "r", function() {
            return ie;
        }), n.d(t, "s", function() {
            return Te;
        }), n.d(t, "t", function() {
            return p;
        }), n.d(t, "u", function() {
            return se;
        }), n.d(t, "v", function() {
            return ce;
        }), n.d(t, "w", function() {
            return pe;
        });
        var r = n(18), o = (n(12), n(13), n(10), n(11), n(25));
        function i(e) {
            return "string" === typeof e;
        }
        function a(e) {
            return "undefined" === typeof e;
        }
        function c(e) {
            return null !== e && "object" === Object(o["a"])(e);
        }
        function s(e) {
            return "function" === typeof e;
        }
        function u(e) {
            return "number" === typeof e;
        }
        function l(e) {
            return "true" === e || "false" === e;
        }
        var d = Array.isArray, f = ("i.".concat("st"), "i.".concat("cl"), {
            bindTouchStart: "",
            bindTouchMove: "",
            bindTouchEnd: "",
            bindTouchCancel: "",
            bindLongTap: ""
        }), h = {
            bindAnimationStart: "",
            bindAnimationIteration: "",
            bindAnimationEnd: "",
            bindTransitionEnd: ""
        };
        new Set([ "htouchmove", "vtouchmove" ]);
        function p(e) {
            return "'".concat(e, "'");
        }
        var v = Object.assign(Object.assign({
            "hover-class": p("none"),
            "hover-stop-propagation": "false",
            "hover-start-time": "50",
            "hover-stay-time": "400",
            animation: ""
        }, f), h), g = {
            type: "",
            size: "23",
            color: ""
        }, b = Object.assign({
            longitude: "",
            latitude: "",
            scale: "16",
            markers: "[]",
            covers: "",
            polyline: "[]",
            circles: "[]",
            controls: "[]",
            "include-points": "[]",
            "show-location": "",
            "layer-style": "1",
            bindMarkerTap: "",
            bindControlTap: "",
            bindCalloutTap: "",
            bindUpdated: ""
        }, f), m = {
            percent: "",
            "stroke-width": "6",
            color: p("#09BB07"),
            activeColor: p("#09BB07"),
            backgroundColor: p("#EBEBEB"),
            active: "false",
            "active-mode": p("backwards"),
            "show-info": "false"
        }, y = {
            nodes: "[]"
        }, S = {
            selectable: "false",
            space: "",
            decode: "false"
        }, w = {
            size: p("default"),
            type: "",
            plain: "false",
            disabled: "",
            loading: "false",
            "form-type": "",
            "open-type": "",
            "hover-class": p("button-hover"),
            "hover-stop-propagation": "false",
            "hover-start-time": "20",
            "hover-stay-time": "70",
            name: ""
        }, k = {
            value: "",
            disabled: "",
            checked: "false",
            color: p("#09BB07"),
            name: ""
        }, C = {
            bindChange: "",
            name: ""
        }, O = {
            "report-submit": "false",
            bindSubmit: "",
            bindReset: "",
            name: ""
        }, j = {
            value: "",
            type: p(""),
            password: "false",
            placeholder: "",
            "placeholder-style": "",
            "placeholder-class": p("input-placeholder"),
            disabled: "",
            maxlength: "140",
            "cursor-spacing": "0",
            focus: "false",
            "confirm-type": p("done"),
            "confirm-hold": "false",
            cursor: "i.value.length",
            "selection-start": "-1",
            "selection-end": "-1",
            bindInput: "",
            bindFocus: "",
            bindBlur: "",
            bindConfirm: "",
            name: ""
        }, T = {
            for: "",
            name: ""
        }, P = {
            mode: p("selector"),
            disabled: "",
            range: "",
            "range-key": "",
            value: "",
            start: "",
            end: "",
            fields: p("day"),
            "custom-item": "",
            name: "",
            bindCancel: "",
            bindChange: "",
            bindColumnChange: ""
        }, E = {
            value: "",
            "indicator-style": "",
            "indicator-class": "",
            "mask-style": "",
            "mask-class": "",
            bindChange: "",
            name: ""
        }, B = {
            name: ""
        }, A = {
            value: "",
            checked: "false",
            disabled: "",
            color: p("#09BB07"),
            name: ""
        }, x = {
            bindChange: "",
            name: ""
        }, I = {
            min: "0",
            max: "100",
            step: "1",
            disabled: "",
            value: "0",
            activeColor: p("#1aad19"),
            backgroundColor: p("#e9e9e9"),
            "block-size": "28",
            "block-color": p("#ffffff"),
            "show-value": "false",
            bindChange: "",
            bindChanging: "",
            name: ""
        }, _ = {
            checked: "false",
            disabled: "",
            type: p("switch"),
            color: p("#04BE02"),
            bindChange: "",
            name: ""
        }, L = {
            value: "",
            placeholder: "",
            "placeholder-style": "",
            "placeholder-class": p("textarea-placeholder"),
            disabled: "",
            maxlength: "140",
            "auto-focus": "false",
            focus: "false",
            "auto-height": "false",
            fixed: "false",
            "cursor-spacing": "0",
            cursor: "-1",
            "selection-start": "-1",
            "selection-end": "-1",
            bindFocus: "",
            bindBlur: "",
            bindLineChange: "",
            bindInput: "",
            bindConfirm: "",
            name: ""
        }, R = {
            src: "",
            bindLoad: "eh",
            bindError: "eh"
        }, D = Object.assign({
            "scroll-top": "false"
        }, f), N = {
            "scale-area": "false"
        }, M = Object.assign(Object.assign({
            direction: "none",
            inertia: "false",
            "out-of-bounds": "false",
            x: "",
            y: "",
            damping: "20",
            friction: "2",
            disabled: "",
            scale: "false",
            "scale-min": "0.5",
            "scale-max": "10",
            "scale-value": "1",
            animation: "true",
            bindChange: "",
            bindScale: "",
            htouchmove: "",
            vtouchmove: "",
            width: p("10px"),
            height: p("10px")
        }, f), h), F = Object.assign(Object.assign({
            "scroll-x": "false",
            "scroll-y": "false",
            "upper-threshold": "50",
            "lower-threshold": "50",
            "scroll-top": "",
            "scroll-left": "",
            "scroll-into-view": "",
            "scroll-with-animation": "false",
            "enable-back-to-top": "false",
            bindScrollToUpper: "",
            bindScrollToLower: "",
            bindScroll: ""
        }, f), h), W = Object.assign({
            "indicator-dots": "false",
            "indicator-color": p("rgba(0, 0, 0, .3)"),
            "indicator-active-color": p("#000000"),
            autoplay: "false",
            current: "0",
            interval: "5000",
            duration: "500",
            circular: "false",
            vertical: "false",
            "previous-margin": "'0px'",
            "next-margin": "'0px'",
            "display-multiple-items": "1",
            bindChange: "",
            bindTransition: "",
            bindAnimationFinish: ""
        }, f), V = {
            "item-id": ""
        }, U = {
            url: "",
            "open-type": p("navigate"),
            delta: "1",
            "hover-class": p("navigator-hover"),
            "hover-stop-propagation": "false",
            "hover-start-time": "50",
            "hover-stay-time": "600",
            bindSuccess: "",
            bindFail: "",
            bindComplete: ""
        }, q = {
            id: "",
            src: "",
            loop: "false",
            controls: "false",
            poster: "",
            name: "",
            author: "",
            bindError: "",
            bindPlay: "",
            bindPause: "",
            bindTimeUpdate: "",
            bindEnded: ""
        }, z = {
            "device-position": p("back"),
            flash: p("auto"),
            bindStop: "",
            bindError: ""
        }, H = Object.assign({
            src: "",
            mode: p("scaleToFill"),
            "lazy-load": "false",
            bindError: "",
            bindLoad: ""
        }, f), $ = {
            src: "",
            autoplay: "false",
            muted: "false",
            orientation: p("vertical"),
            "object-fit": p("contain"),
            "background-mute": "false",
            "min-cache": "1",
            "max-cache": "3",
            animation: "",
            bindStateChange: "",
            bindFullScreenChange: "",
            bindNetStatus: ""
        }, G = {
            src: "",
            duration: "",
            controls: "true",
            "danmu-list": "",
            "danmu-btn": "",
            "enable-danmu": "",
            autoplay: "false",
            loop: "false",
            muted: "false",
            "initial-time": "0",
            "page-gesture": "false",
            direction: "",
            "show-progress": "true",
            "show-fullscreen-btn": "true",
            "show-play-btn": "true",
            "show-center-play-btn": "true",
            "enable-progress-gesture": "true",
            "object-fit": p("contain"),
            poster: "",
            "show-mute-btn": "false",
            animation: "",
            bindPlay: "",
            bindPause: "",
            bindEnded: "",
            bindTimeUpdate: "",
            bindFullScreenChange: "",
            bindWaiting: "",
            bindError: ""
        }, Q = Object.assign({
            "canvas-id": "",
            "disable-scroll": "false",
            bindError: ""
        }, f), K = {
            "unit-id": "",
            "ad-intervals": "",
            bindLoad: "",
            bindError: "",
            bindClose: ""
        }, J = {
            src: "",
            bindMessage: "",
            bindLoad: "",
            bindError: ""
        }, Y = {}, X = {
            name: ""
        }, Z = {
            name: ""
        }, ee = {
            View: v,
            Icon: g,
            Progress: m,
            RichText: y,
            Text: S,
            Button: w,
            Checkbox: k,
            CheckboxGroup: C,
            Form: O,
            Input: j,
            Label: T,
            Picker: P,
            PickerView: E,
            PickerViewColumn: B,
            Radio: A,
            RadioGroup: x,
            Slider: I,
            Switch: _,
            CoverImage: R,
            Textarea: L,
            CoverView: D,
            MovableArea: N,
            MovableView: M,
            ScrollView: F,
            Swiper: W,
            SwiperItem: V,
            Navigator: U,
            Audio: q,
            Camera: z,
            Image: H,
            LivePlayer: $,
            Video: G,
            Canvas: Q,
            Ad: K,
            WebView: J,
            Block: Y,
            Map: b,
            Slot: Z,
            SlotView: X
        }, te = new Set([ "input", "checkbox", "picker", "picker-view", "radio", "slider", "switch", "textarea" ]), ne = (new Set([ "input", "textarea" ]), 
        new Set([ "progress", "icon", "rich-text", "input", "textarea", "slider", "switch", "audio", "ad", "official-account", "open-data", "navigation-bar" ]), 
        new Map([ [ "view", -1 ], [ "catch-view", -1 ], [ "cover-view", -1 ], [ "static-view", -1 ], [ "pure-view", -1 ], [ "block", -1 ], [ "text", -1 ], [ "static-text", 6 ], [ "slot", 8 ], [ "slot-view", 8 ], [ "label", 6 ], [ "form", 4 ], [ "scroll-view", 4 ], [ "swiper", 4 ], [ "swiper-item", 4 ] ]), 
        new Set([ "touchstart", "touchmove", "touchcancel", "touchend", "touchforcechange", "tap", "longpress", "longtap", "transitionend", "animationstart", "animationiteration", "animationend" ])), re = {}, oe = [], ie = function() {}, ae = {
            isBubbleEvent: function(e) {
                return ne.has(e);
            }
        };
        function ce(e) {
            return e.replace(/([a-z0-9])([A-Z])/g, "$1-$2").toLowerCase();
        }
        function se(e) {
            for (var t = "", n = !1, r = 0; r < e.length; r++) "-" !== e[r] ? (t += n ? e[r].toUpperCase() : e[r], 
            n = !1) : n = !0;
            return t;
        }
        function ue(e) {
            return e.charAt(0).toUpperCase() + e.slice(1);
        }
        var le = Object.prototype.hasOwnProperty, de = function(e, t) {
            return le.call(e, t);
        }, fe = "如有疑问，请提交 issue 至：https://github.com/nervjs/taro/issues";
        function he(e, t) {
            if (!e) throw new Error(t + "\n" + fe);
        }
        function pe(e, t) {
            0;
        }
        var ve = 1, ge = new Date().getTime().toString();
        function be() {
            return ge + ve++;
        }
        function me(e) {
            Object.keys(e).forEach(function(t) {
                t in ee ? Object.assign(ee[t], e[t]) : ee[t] = e[t];
            });
        }
        function ye(e) {
            Object.assign(ae, e);
        }
        function Se(e) {
            return function() {
                console.warn("小程序暂不支持 ".concat(e));
            };
        }
        function we(e, t) {
            var n = "__key_", r = [ "navigateTo", "redirectTo", "reLaunch", "switchTab" ];
            if (r.indexOf(e) > -1) {
                var o = t.url = t.url || "", i = o.indexOf("?") > -1, a = be();
                t.url += (i ? "&" : "?") + "".concat(n, "=").concat(a);
            }
        }
        var ke = new Set([ "clearStorageSync", "getBatteryInfoSync", "getExtConfigSync", "getFileSystemManager", "getLaunchOptionsSync", "getStorageInfoSync", "getStorageSync", "getSystemInfoSync", "offAccelerometerChange", "offAppHide", "offAppShow", "offAudioInterruptionBegin", "offAudioInterruptionEnd", "offBLECharacteristicValueChange", "offBLEConnectionStateChange", "offBluetoothAdapterStateChange", "offBluetoothDeviceFound", "offCompassChange", "offError", "offGetWifiList", "offGyroscopeChange", "offMemoryWarning", "offNetworkStatusChange", "offPageNotFound", "offUnhandledRejection", "offUserCaptureScreen", "onAccelerometerChange", "onAppHide", "onAppShow", "onAudioInterruptionBegin", "onAudioInterruptionEnd", "onBLECharacteristicValueChange", "onBLEConnectionStateChange", "onBeaconServiceChange", "onBeaconUpdate", "onBluetoothAdapterStateChange", "onBluetoothDeviceFound", "onCompassChange", "onDeviceMotionChange", "onError", "onGetWifiList", "onGyroscopeChange", "onMemoryWarning", "onNetworkStatusChange", "onPageNotFound", "onSocketClose", "onSocketError", "onSocketMessage", "onSocketOpen", "onUnhandledRejection", "onUserCaptureScreen", "removeStorageSync", "reportAnalytics", "setStorageSync", "arrayBufferToBase64", "base64ToArrayBuffer", "canIUse", "createAnimation", "createCameraContext", "createCanvasContext", "createInnerAudioContext", "createIntersectionObserver", "createInterstitialAd", "createLivePlayerContext", "createMapContext", "createSelectorQuery", "createVideoContext", "getBackgroundAudioManager", "getMenuButtonBoundingClientRect", "getRecorderManager", "getUpdateManager" ]), Ce = new Set([ "addPhoneContact", "authorize", "canvasGetImageData", "canvasPutImageData", "canvasToTempFilePath", "checkSession", "chooseAddress", "chooseImage", "chooseInvoiceTitle", "chooseLocation", "chooseVideo", "clearStorage", "closeBLEConnection", "closeBluetoothAdapter", "closeSocket", "compressImage", "connectSocket", "createBLEConnection", "downloadFile", "getAvailableAudioSources", "getBLEDeviceCharacteristics", "getBLEDeviceServices", "getBatteryInfo", "getBeacons", "getBluetoothAdapterState", "getBluetoothDevices", "getClipboardData", "getConnectedBluetoothDevices", "getConnectedWifi", "getExtConfig", "getFileInfo", "getImageInfo", "getLocation", "getNetworkType", "getSavedFileInfo", "getSavedFileList", "getScreenBrightness", "getSetting", "getStorage", "getStorageInfo", "getSystemInfo", "getUserInfo", "getWifiList", "hideHomeButton", "hideShareMenu", "hideTabBar", "hideTabBarRedDot", "loadFontFace", "login", "makePhoneCall", "navigateBack", "navigateBackMiniProgram", "navigateTo", "navigateToBookshelf", "navigateToMiniProgram", "notifyBLECharacteristicValueChange", "hideKeyboard", "hideLoading", "hideNavigationBarLoading", "hideToast", "openBluetoothAdapter", "openDocument", "openLocation", "openSetting", "pageScrollTo", "previewImage", "queryBookshelf", "reLaunch", "readBLECharacteristicValue", "redirectTo", "removeSavedFile", "removeStorage", "removeTabBarBadge", "requestSubscribeMessage", "saveFile", "saveImageToPhotosAlbum", "saveVideoToPhotosAlbum", "scanCode", "sendSocketMessage", "setBackgroundColor", "setBackgroundTextStyle", "setClipboardData", "setEnableDebug", "setInnerAudioOption", "setKeepScreenOn", "setNavigationBarColor", "setNavigationBarTitle", "setScreenBrightness", "setStorage", "setTabBarBadge", "setTabBarItem", "setTabBarStyle", "showActionSheet", "showFavoriteGuide", "showLoading", "showModal", "showShareMenu", "showTabBar", "showTabBarRedDot", "showToast", "startBeaconDiscovery", "startBluetoothDevicesDiscovery", "startDeviceMotionListening", "startPullDownRefresh", "stopBeaconDiscovery", "stopBluetoothDevicesDiscovery", "stopCompass", "startCompass", "startAccelerometer", "stopAccelerometer", "showNavigationBarLoading", "stopDeviceMotionListening", "stopPullDownRefresh", "switchTab", "uploadFile", "vibrateLong", "vibrateShort", "writeBLECharacteristicValue" ]);
        function Oe(e) {
            return function() {
                if ("function" !== typeof e.getSystemInfoSync) return console.error("不支持 API canIUseWebp"), 
                !1;
                var t = e.getSystemInfoSync(), n = t.platform, r = n.toLowerCase();
                return "android" === r || "devtools" === r;
            };
        }
        function je(e) {
            return function(t) {
                t = t || {}, "string" === typeof t && (t = {
                    url: t
                });
                var n, r = t.success, o = t.fail, i = t.complete, a = new Promise(function(a, c) {
                    t.success = function(e) {
                        r && r(e), a(e);
                    }, t.fail = function(e) {
                        o && o(e), c(e);
                    }, t.complete = function(e) {
                        i && i(e);
                    }, n = e.request(t);
                });
                return a.abort = function(e) {
                    return e && e(), n && n.abort(), a;
                }, a;
            };
        }
        function Te(e, t) {
            var n = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : {}, o = n.noPromiseApis || [], i = n.needPromiseApis || [], a = new Set([].concat(Object(r["a"])(o), Object(r["a"])(ke))), c = new Set([].concat(Object(r["a"])(i), Object(r["a"])(Ce))), s = [].concat(Object(r["a"])(a), Object(r["a"])(c));
            s.forEach(function(r) {
                if (c.has(r)) {
                    var o = r;
                    e[o] = function() {
                        for (var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {}, r = arguments.length, i = new Array(r > 1 ? r - 1 : 0), a = 1; a < r; a++) i[a - 1] = arguments[a];
                        var c = o;
                        if ("string" === typeof e) return i.length ? t[c].apply(t, [ e ].concat(i)) : t[c](e);
                        if (n.transformMeta) {
                            var s = n.transformMeta(c, e);
                            if (c = s.key, e = s.options, !t.hasOwnProperty(c)) return Se(c)();
                        }
                        var u = null, l = Object.assign({}, e);
                        we(c, e);
                        var d = new Promise(function(r, o) {
                            l.success = function(t) {
                                var o, i;
                                null === (o = n.modifyAsyncResult) || void 0 === o || o.call(n, c, t), null === (i = e.success) || void 0 === i || i.call(e, t), 
                                r("connectSocket" === c ? Promise.resolve().then(function() {
                                    return Object.assign(u, t);
                                }) : t);
                            }, l.fail = function(t) {
                                var n;
                                null === (n = e.fail) || void 0 === n || n.call(e, t), o(t);
                            }, l.complete = function(t) {
                                var n;
                                null === (n = e.complete) || void 0 === n || n.call(e, t);
                            }, u = i.length ? t[c].apply(t, [ l ].concat(i)) : t[c](l);
                        });
                        return "uploadFile" !== c && "downloadFile" !== c || (d.progress = function(e) {
                            return null === u || void 0 === u || u.onProgressUpdate(e), d;
                        }, d.abort = function(e) {
                            return null === e || void 0 === e || e(), null === u || void 0 === u || u.abort(), 
                            d;
                        }), d;
                    };
                } else {
                    if (!t.hasOwnProperty(r)) return void (e[r] = Se(r));
                    e[r] = function() {
                        for (var e = arguments.length, o = new Array(e), i = 0; i < e; i++) o[i] = arguments[i];
                        return n.handleSyncApis ? n.handleSyncApis(r, t, o) : t[r].apply(t, o);
                    };
                }
            }), !n.isOnlyPromisify && Pe(e, t, n);
        }
        function Pe(e, t) {
            var n = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : {};
            e.canIUseWebp = Oe(e), e.getCurrentPages = getCurrentPages || Se("getCurrentPages"), 
            e.getApp = getApp || Se("getApp"), e.env = t.env || {};
            try {
                e.requirePlugin = requirePlugin || Se("requirePlugin");
            } catch (t) {
                e.requirePlugin = Se("requirePlugin");
            }
            var r = n.request ? n.request : je(t);
            function o(e) {
                return r(e.requestParams);
            }
            var i = new e.Link(o);
            e.request = i.request.bind(i), e.addInterceptor = i.addInterceptor.bind(i), e.cleanInterceptors = i.cleanInterceptors.bind(i), 
            e.miniGlobal = t;
        }
    },
    2: function(e, t, n) {
        var r = n(8), o = r.CurrentReconciler, i = n(272).default;
        "function" === typeof o.initNativeApi && o.initNativeApi(i), e.exports = i, e.exports.default = e.exports;
    },
    271: function(e, t, n) {
        "use strict";
        var r = n(15), o = new Set([ "getAccountInfoSync", "getEnterOptionsSync", "offBLEPeripheralConnectionStateChanged", "offBeaconServiceChange", "offBeaconUpdate", "offDeviceMotionChange", "offHCEMessage", "offKeyboardHeightChange", "offLocalServiceDiscoveryStop", "offLocalServiceFound", "offLocalServiceLost", "offLocalServiceResolveFail", "offLocationChange", "offThemeChange", "offVoIPChatInterrupted", "offVoIPChatMembersChanged", "offVoIPVideoMembersChanged", "offWifiConnected", "offWindowResize", "onBLEPeripheralConnectionStateChanged", "onBackgroundAudioPause", "onBackgroundAudioPlay", "onBackgroundAudioStop", "onBackgroundFetchData", "onHCEMessage", "onKeyboardHeightChange", "onLocalServiceDiscoveryStop", "onLocalServiceFound", "onLocalServiceLost", "onLocalServiceResolveFail", "onLocationChange", "onThemeChange", "onVoIPChatInterrupted", "onVoIPChatMembersChanged", "onVoIPChatSpeakersChanged", "onVoIPVideoMembersChanged", "onWifiConnected", "onWindowResize", "reportMonitor", "onGyroscopeChange", "offGyroscopeChange", "createAudioContext", "createLivePusherContext", "createMediaContainer", "createMediaRecorder", "createOffscreenCanvas", "createRewardedVideoAd", "createUDPSocket", "createVideoDecoder", "createWorker", "getLogManager", "getNFCAdapter", "getPerformance", "getRealtimeLogManager", "pauseBackgroundAudio", "pauseVoice", "reportPerformance", "stopBackgroundAudio", "stopRecord", "stopVoice", "onBluetoothDeviceFound", "onBluetoothAdapterStateChange", "offBluetoothDeviceFound", "offBluetoothAdapterStateChange", "onBLEConnectionStateChange", "onBLECharacteristicValueChange", "offBLEConnectionStateChange", "offBLECharacteristicValueChange", "onCopyUrl", "offCopyUrl" ]), i = new Set([ "addCard", "authPrivateMessage", "checkIsOpenAccessibility", "checkIsSoterEnrolledInDevice", "checkIsSupportSoterAuthentication", "chooseInvoice", "chooseMedia", "chooseMessageFile", "compressVideo", "connectWifi", "createBLEPeripheralServer", "disableAlertBeforeUnload", "enableAlertBeforeUnload", "exitVoIPChat", "getBLEDeviceRSSI", "getBackgroundAudioPlayerState", "getBackgroundFetchData", "getBackgroundFetchToken", "getGroupEnterInfo", "getHCEState", "getSelectedTextRange", "getShareInfo", "getVideoInfo", "getWeRunData", "join1v1Chat", "joinVoIPChat", "makeBluetoothPair", "openCard", "openVideoEditor", "playBackgroundAudio", "playVoice", "previewMedia", "requestPayment", "saveFileToDisk", "scanItem", "seekBackgroundAudio", "sendHCEMessage", "setBLEMTU", "setBackgroundFetchToken", "setEnable1v1Chat", "setTopBarText", "setWifiList", "setWindowSize", "showRedPackage", "startGyroscope", "startHCE", "startLocalServiceDiscovery", "startLocationUpdate", "startLocationUpdateBackground", "startRecord", "startSoterAuthentication", "startWifi", "stopGyroscope", "stopHCE", "stopLocalServiceDiscovery", "stopLocationUpdate", "stopWifi", "subscribeVoIPVideoMembers", "updateShareMenu", "updateVoIPChatMuteConfig", "updateWeChatApp", "sendBizRedPacket", "getUserProfile", "stopBluetoothDevicesDiscovery", "startBluetoothDevicesDiscovery", "openBluetoothAdapter", "getConnectedBluetoothDevices", "getBluetoothDevices", "getBluetoothAdapterState", "closeBluetoothAdapter", "writeBLECharacteristicValue", "readBLECharacteristicValue", "notifyBLECharacteristicValueChange", "getBLEDeviceServices", "getBLEDeviceCharacteristics", "createBLEConnection", "closeBLEConnection", "startFacialRecognitionVerify" ]);
        function a(e) {
            Object(r["s"])(e, wx, {
                noPromiseApis: o,
                needPromiseApis: i
            }), e.cloud = wx.cloud;
        }
        var c = {
            Progress: {
                "border-radius": "0",
                "font-size": "16",
                duration: "30",
                bindActiveEnd: ""
            },
            RichText: {
                space: ""
            },
            Text: {
                "user-select": "false"
            },
            Map: {
                polygons: "[]",
                subkey: "",
                rotate: "0",
                skew: "0",
                "enable-3D": "false",
                "show-compass": "false",
                "show-scale": "false",
                "enable-overlooking": "false",
                "enable-zoom": "true",
                "enable-scroll": "true",
                "enable-rotate": "false",
                "enable-satellite": "false",
                "enable-traffic": "false",
                setting: "[]",
                bindLabelTap: "",
                bindRegionChange: "",
                bindPoiTap: ""
            },
            Button: {
                lang: "en",
                "session-from": "",
                "send-message-title": "",
                "send-message-path": "",
                "send-message-img": "",
                "app-parameter": "",
                "show-message-card": "false",
                "business-id": "",
                bindGetUserInfo: "",
                bindContact: "",
                bindGetPhoneNumber: "",
                bindError: "",
                bindOpenSetting: "",
                bindLaunchApp: ""
            },
            Form: {
                "report-submit-timeout": "0"
            },
            Input: {
                "always-embed": "false",
                "adjust-position": "true",
                "hold-keyboard": "false",
                bindKeyboardHeightChange: ""
            },
            Picker: {
                "header-text": ""
            },
            PickerView: {
                bindPickStart: "",
                bindPickEnd: ""
            },
            Slider: {
                color: Object(r["t"])("#e9e9e9"),
                "selected-color": Object(r["t"])("#1aad19")
            },
            Textarea: {
                "show-confirm-bar": "true",
                "adjust-position": "true",
                "hold-keyboard": "false",
                "disable-default-padding": "false",
                bindKeyboardHeightChange: ""
            },
            ScrollView: {
                "enable-flex": "false",
                "scroll-anchoring": "false",
                "refresher-enabled": "false",
                "refresher-threshold": "45",
                "refresher-default-style": Object(r["t"])("black"),
                "refresher-background": Object(r["t"])("#FFF"),
                "refresher-triggered": "false",
                enhanced: "false",
                bounces: "true",
                "show-scrollbar": "true",
                "paging-enabled": "false",
                "fast-deceleration": "false",
                bindDragStart: "",
                bindDragging: "",
                bindDragEnd: "",
                bindRefresherPulling: "",
                bindRefresherRefresh: "",
                bindRefresherRestore: "",
                bindRefresherAbort: ""
            },
            Swiper: {
                "snap-to-edge": "false",
                "easing-function": Object(r["t"])("default")
            },
            SwiperItem: {
                "skip-hidden-item-layout": "false"
            },
            Navigator: {
                target: Object(r["t"])("self"),
                "app-id": "",
                path: "",
                "extra-data": "",
                version: Object(r["t"])("version")
            },
            Camera: {
                mode: Object(r["t"])("normal"),
                resolution: Object(r["t"])("medium"),
                "frame-size": Object(r["t"])("medium"),
                bindInitDone: "",
                bindScanCode: ""
            },
            Image: {
                webp: "false",
                "show-menu-by-longpress": "false"
            },
            LivePlayer: {
                mode: Object(r["t"])("live"),
                "sound-mode": Object(r["t"])("speaker"),
                "auto-pause-if-navigate": "true",
                "auto-pause-if-open-native": "true",
                "picture-in-picture-mode": "[]",
                bindstatechange: "",
                bindfullscreenchange: "",
                bindnetstatus: "",
                bindAudioVolumeNotify: "",
                bindEnterPictureInPicture: "",
                bindLeavePictureInPicture: ""
            },
            Video: {
                title: "",
                "play-btn-position": Object(r["t"])("bottom"),
                "enable-play-gesture": "false",
                "auto-pause-if-navigate": "true",
                "auto-pause-if-open-native": "true",
                "vslide-gesture": "false",
                "vslide-gesture-in-fullscreen": "true",
                "ad-unit-id": "",
                "poster-for-crawler": "",
                "show-casting-button": "false",
                "picture-in-picture-mode": "[]",
                "enable-auto-rotation": "false",
                "show-screen-lock-button": "false",
                bindProgress: "",
                bindLoadedMetadata: "",
                bindControlsToggle: "",
                bindEnterPictureInPicture: "",
                bindLeavePictureInPicture: "",
                bindSeekComplete: "",
                bindAdLoad: "",
                bindAdError: "",
                bindAdClose: "",
                bindAdPlay: ""
            },
            Canvas: {
                type: ""
            },
            Ad: {
                "ad-type": Object(r["t"])("banner"),
                "ad-theme": Object(r["t"])("white")
            },
            CoverView: {
                "marker-id": "",
                slot: ""
            },
            Editor: {
                "read-only": "false",
                placeholder: "",
                "show-img-size": "false",
                "show-img-toolbar": "false",
                "show-img-resize": "false",
                focus: "false",
                bindReady: "",
                bindFocus: "",
                bindBlur: "",
                bindInput: "",
                bindStatusChange: "",
                name: ""
            },
            MatchMedia: {
                "min-width": "",
                "max-width": "",
                width: "",
                "min-height": "",
                "max-height": "",
                height: "",
                orientation: ""
            },
            FunctionalPageNavigator: {
                version: Object(r["t"])("release"),
                name: "",
                args: "",
                bindSuccess: "",
                bindFail: "",
                bindCancel: ""
            },
            LivePusher: {
                url: "",
                mode: Object(r["t"])("RTC"),
                autopush: "false",
                muted: "false",
                "enable-camera": "true",
                "auto-focus": "true",
                orientation: Object(r["t"])("vertical"),
                beauty: "0",
                whiteness: "0",
                aspect: Object(r["t"])("9:16"),
                "min-bitrate": "200",
                "max-bitrate": "1000",
                "audio-quality": Object(r["t"])("high"),
                "waiting-image": "",
                "waiting-image-hash": "",
                zoom: "false",
                "device-position": Object(r["t"])("front"),
                "background-mute": "false",
                mirror: "false",
                "remote-mirror": "false",
                "local-mirror": "false",
                "audio-reverb-type": "0",
                "enable-mic": "true",
                "enable-agc": "false",
                "enable-ans": "false",
                "audio-volume-type": Object(r["t"])("voicecall"),
                "video-width": "360",
                "video-height": "640",
                "beauty-style": Object(r["t"])("smooth"),
                filter: Object(r["t"])("standard"),
                animation: "",
                bindStateChange: "",
                bindNetStatus: "",
                bindBgmStart: "",
                bindBgmProgress: "",
                bindBgmComplete: "",
                bindAudioVolumeNotify: ""
            },
            OfficialAccount: {
                bindLoad: "",
                bindError: ""
            },
            OpenData: {
                type: "",
                "open-gid": "",
                lang: Object(r["t"])("en"),
                "default-text": "",
                "default-avatar": "",
                bindError: ""
            },
            NavigationBar: {
                title: "",
                loading: "false",
                "front-color": "",
                "background-color": "",
                "color-animation-duration": "0",
                "color-animation-timing-func": Object(r["t"])("linear")
            },
            PageMeta: {
                "background-text-style": "",
                "background-color": "",
                "background-color-top": "",
                "background-color-bottom": "",
                "scroll-top": Object(r["t"])(""),
                "scroll-duration": "300",
                "page-style": Object(r["t"])(""),
                "root-font-size": Object(r["t"])(""),
                bindResize: "",
                bindScroll: "",
                bindScrollDone: ""
            },
            VoipRoom: {
                openid: "",
                mode: Object(r["t"])("camera"),
                "device-position": Object(r["t"])("front"),
                bindError: ""
            },
            AdCustom: {
                "unit-id": "",
                "ad-intervals": "",
                bindLoad: "",
                bindError: ""
            },
            PageContainer: {
                show: "false",
                duration: "300",
                "z-index": "100",
                overlay: "true",
                position: Object(r["t"])("bottom"),
                round: "false",
                "close-on-slideDown": "false",
                "overlay-style": "",
                "custom-style": "",
                bindBeforeEnter: "",
                bindEnter: "",
                bindAfterEnter: "",
                bindBeforeLeave: "",
                bindLeave: "",
                bindAfterLeave: "",
                bindClickOverlay: ""
            }
        }, s = {
            initNativeApi: a,
            onTaroElementCreate: function(e) {
                Object(r["w"])("MAP" === e, "微信小程序 map 组件的 `setting` 属性需要传递一个默认值。详情：\n https://developers.weixin.qq.com/miniprogram/dev/component/map.html");
            }
        };
        Object(r["q"])(s), Object(r["p"])(c);
    },
    272: function(e, t, n) {
        "use strict";
        n.r(t), function(e, r) {
            var o = n(8);
            function i(e) {
                return i = "function" === typeof Symbol && "symbol" === typeof Symbol.iterator ? function(e) {
                    return typeof e;
                } : function(e) {
                    return e && "function" === typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e;
                }, i(e);
            }
            function a(e, t) {
                if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
            }
            function c(e, t) {
                for (var n = 0; n < t.length; n++) {
                    var r = t[n];
                    r.enumerable = r.enumerable || !1, r.configurable = !0, "value" in r && (r.writable = !0), 
                    Object.defineProperty(e, r.key, r);
                }
            }
            function s(e, t, n) {
                return t && c(e.prototype, t), n && c(e, n), e;
            }
            function u(e, t, n) {
                return t in e ? Object.defineProperty(e, t, {
                    value: n,
                    enumerable: !0,
                    configurable: !0,
                    writable: !0
                }) : e[t] = n, e;
            }
            function l(e, t) {
                var n = Object.keys(e);
                if (Object.getOwnPropertySymbols) {
                    var r = Object.getOwnPropertySymbols(e);
                    t && (r = r.filter(function(t) {
                        return Object.getOwnPropertyDescriptor(e, t).enumerable;
                    })), n.push.apply(n, r);
                }
                return n;
            }
            function d(e) {
                for (var t = 1; t < arguments.length; t++) {
                    var n = null != arguments[t] ? arguments[t] : {};
                    t % 2 ? l(Object(n), !0).forEach(function(t) {
                        u(e, t, n[t]);
                    }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(n)) : l(Object(n)).forEach(function(t) {
                        Object.defineProperty(e, t, Object.getOwnPropertyDescriptor(n, t));
                    });
                }
                return e;
            }
            "function" !== typeof Object.assign && (Object.assign = function(e) {
                if (null == e) throw new TypeError("Cannot convert undefined or null to object");
                for (var t = Object(e), n = 1; n < arguments.length; n++) {
                    var r = arguments[n];
                    if (null != r) for (var o in r) Object.prototype.hasOwnProperty.call(r, o) && (t[o] = r[o]);
                }
                return t;
            }), "function" !== typeof Object.defineProperties && (Object.defineProperties = function(e, t) {
                function n(e) {
                    function t(e, t) {
                        return Object.prototype.hasOwnProperty.call(e, t);
                    }
                    function n(e) {
                        return "function" === typeof e;
                    }
                    if ("object" !== i(e) || null === e) throw new TypeError("bad desc");
                    var r = {};
                    if (t(e, "enumerable") && (r.enumerable = !!e.enumerable), t(e, "configurable") && (r.configurable = !!e.configurable), 
                    t(e, "value") && (r.value = e.value), t(e, "writable") && (r.writable = !!e.writable), 
                    t(e, "get")) {
                        var o = e.get;
                        if (!n(o) && "undefined" !== typeof o) throw new TypeError("bad get");
                        r.get = o;
                    }
                    if (t(e, "set")) {
                        var a = e.set;
                        if (!n(a) && "undefined" !== typeof a) throw new TypeError("bad set");
                        r.set = a;
                    }
                    if (("get" in r || "set" in r) && ("value" in r || "writable" in r)) throw new TypeError("identity-confused descriptor");
                    return r;
                }
                if ("object" !== i(e) || null === e) throw new TypeError("bad obj");
                t = Object(t);
                for (var r = Object.keys(t), o = [], a = 0; a < r.length; a++) o.push([ r[a], n(t[r[a]]) ]);
                for (var c = 0; c < o.length; c++) Object.defineProperty(e, o[c][0], o[c][1]);
                return e;
            });
            var f = {
                WEAPP: "WEAPP",
                WEB: "WEB",
                RN: "RN",
                SWAN: "SWAN",
                ALIPAY: "ALIPAY",
                TT: "TT",
                QQ: "QQ",
                JD: "JD"
            }, h = null;
            function p() {
                return h || ("undefined" !== typeof jd && jd.getSystemInfo ? (h = f.JD, f.JD) : "undefined" !== typeof qq && qq.getSystemInfo ? (h = f.QQ, 
                f.QQ) : "undefined" !== typeof tt && tt.getSystemInfo ? (h = f.TT, f.TT) : "undefined" !== typeof wx && wx.getSystemInfo ? (h = f.WEAPP, 
                f.WEAPP) : "undefined" !== typeof swan && swan.getSystemInfo ? (h = f.SWAN, f.SWAN) : "undefined" !== typeof my && my.getSystemInfo ? (h = f.ALIPAY, 
                f.ALIPAY) : "undefined" !== typeof e && e.__fbGenNativeModule ? (h = f.RN, f.RN) : "undefined" !== typeof r ? (h = f.WEB, 
                f.WEB) : "Unknown environment");
            }
            var v = function() {
                function e(t) {
                    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : [], r = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : 0;
                    a(this, e), this.index = r, this.requestParams = t, this.interceptors = n;
                }
                return s(e, [ {
                    key: "proceed",
                    value: function(e) {
                        if (this.requestParams = e, this.index >= this.interceptors.length) throw new Error("chain 参数错误, 请勿直接修改 request.chain");
                        var t = this._getNextInterceptor(), n = this._getNextChain(), r = t(n), o = r["catch"](function(e) {
                            return Promise.reject(e);
                        });
                        return "function" === typeof r.abort && (o.abort = r.abort), o;
                    }
                }, {
                    key: "_getNextInterceptor",
                    value: function() {
                        return this.interceptors[this.index];
                    }
                }, {
                    key: "_getNextChain",
                    value: function() {
                        return new e(this.requestParams, this.interceptors, this.index + 1);
                    }
                } ]), e;
            }(), g = function() {
                function e(t) {
                    a(this, e), this.taroInterceptor = t, this.chain = new v();
                }
                return s(e, [ {
                    key: "request",
                    value: function(e) {
                        var t = this;
                        return this.chain.interceptors = this.chain.interceptors.filter(function(e) {
                            return e !== t.taroInterceptor;
                        }), this.chain.interceptors.push(this.taroInterceptor), this.chain.proceed(d({}, e));
                    }
                }, {
                    key: "addInterceptor",
                    value: function(e) {
                        this.chain.interceptors.push(e);
                    }
                }, {
                    key: "cleanInterceptors",
                    value: function() {
                        this.chain = new v();
                    }
                } ]), e;
            }();
            function b(e) {
                var t, n = e.requestParams, r = new Promise(function(r, o) {
                    var i = setTimeout(function() {
                        i = null, o(new Error("网络链接超时,请稍后再试！"));
                    }, n && n.timeout || 6e4);
                    t = e.proceed(n), t.then(function(e) {
                        i && (clearTimeout(i), r(e));
                    })["catch"](function(e) {
                        i && clearTimeout(i), o(e);
                    });
                });
                return void 0 !== t && "function" === typeof t.abort && (r.abort = t.abort), r;
            }
            function m(e) {
                var t = e.requestParams, n = t.method, r = t.data, o = t.url;
                console.log("http ".concat(n || "GET", " --\x3e ").concat(o, " data: "), r);
                var i = e.proceed(t), a = i.then(function(e) {
                    return console.log("http <-- ".concat(o, " result:"), e), e;
                });
                return "function" === typeof i.abort && (a.abort = i.abort), a;
            }
            var y = Object.freeze({
                __proto__: null,
                timeoutInterceptor: b,
                logInterceptor: m
            });
            function S(e) {
                return e;
            }
            function w(e) {
                return function(t, n) {
                    "object" === i(t) ? e.preloadData = t : void 0 !== t && void 0 !== n && (e.preloadData = u({}, t, n));
                };
            }
            function k(e) {
                return function(t) {
                    var n = t.designWidth, r = void 0 === n ? 750 : n, o = t.deviceRatio, i = void 0 === o ? {
                        640: 1.17,
                        750: 1,
                        828: .905
                    } : o;
                    e.config = e.config || {}, e.config.designWidth = r, e.config.deviceRatio = i;
                };
            }
            function C(e) {
                return function(t) {
                    var n = e.config || {}, r = n.designWidth, o = void 0 === r ? 750 : r, i = n.deviceRatio, a = void 0 === i ? {
                        640: 1.17,
                        750: 1,
                        828: .905
                    } : i;
                    if (!(o in a)) throw new Error("deviceRatio 配置中不存在 ".concat(o, " 的设置！"));
                    return parseInt(t, 10) * a[o] + "rpx";
                };
            }
            var O = {
                Behavior: S,
                getEnv: p,
                ENV_TYPE: f,
                Link: g,
                interceptors: y,
                Current: o["Current"],
                getCurrentInstance: o["getCurrentInstance"],
                options: o["options"],
                nextTick: o["nextTick"],
                eventCenter: o["eventCenter"],
                Events: o["Events"],
                useDidShow: o["useDidShow"],
                useDidHide: o["useDidHide"],
                usePullDownRefresh: o["usePullDownRefresh"],
                useReachBottom: o["useReachBottom"],
                usePageScroll: o["usePageScroll"],
                useResize: o["useResize"],
                useShareAppMessage: o["useShareAppMessage"],
                useTabItemTap: o["useTabItemTap"],
                useTitleClick: o["useTitleClick"],
                useOptionMenuClick: o["useOptionMenuClick"],
                usePullIntercept: o["usePullIntercept"],
                useShareTimeline: o["useShareTimeline"],
                useAddToFavorites: o["useAddToFavorites"],
                useReady: o["useReady"],
                useRouter: o["useRouter"],
                getInitPxTransform: k
            };
            O.initPxTransform = k(O), O.preload = w(o["Current"]), O.pxTransform = C(O), t["default"] = O;
        }.call(this, n(45), n(8)["window"]);
    },
    341: function(e, t, n) {
        var r, o = n(115).default;
        r = n(342);
        var i = r && r.default ? r.default : r;
        "function" === typeof i && i(o), e.exports = o, e.exports.default = e.exports;
    },
    342: function(e, t, n) {
        "use strict";
        Object.defineProperty(t, "__esModule", {
            value: !0
        }), t["default"] = S;
        var r = a(n(115)), o = n(343), i = n(344);
        function a(e) {
            return e && e.__esModule ? e : {
                default: e
            };
        }
        var c = r["default"].noPromiseApis, s = r["default"].onAndSyncApis, u = r["default"].otherApis, l = r["default"].initPxTransform, d = r["default"].Link, f = {
            MAX_REQUEST: 5,
            queue: [],
            request: function(e) {
                return this.push(e), this.run();
            },
            push: function(e) {
                this.queue.push(e);
            },
            run: function() {
                var e = this;
                if (this.queue.length && this.queue.length <= this.MAX_REQUEST) {
                    var t = this.queue.shift(), n = t.complete;
                    return t.complete = function() {
                        for (var r = arguments.length, o = new Array(r), i = 0; i < r; i++) o[i] = arguments[i];
                        n && n.apply(t, o), e.run();
                    }, wx.request(t);
                }
            }
        };
        function h(e) {
            return v(e.requestParams);
        }
        var p = new d(h);
        function v(e) {
            e = e || {}, "string" === typeof e && (e = {
                url: e
            });
            var t, n = e.success, r = e.fail, o = e.complete, i = new Promise(function(i, a) {
                e.success = function(e) {
                    n && n(e), i(e);
                }, e.fail = function(e) {
                    r && r(e), a(e);
                }, e.complete = function(e) {
                    o && o(e);
                }, t = f.request(e);
            });
            return i.abort = function(e) {
                return e && e(), t && t.abort(), i;
            }, i;
        }
        function g(e) {
            var t = Object.assign({}, s, c, u), n = {
                navigateTo: !0,
                redirectTo: !0,
                reLaunch: !0
            }, r = "__key_", a = "__preload_", l = "$preloadComponent";
            Object.keys(t).forEach(function(t) {
                t in wx ? s[t] || c[t] ? e[t] = function() {
                    for (var e = arguments.length, n = new Array(e), r = 0; r < e; r++) n[r] = arguments[r];
                    var o = n.length, i = n.concat(), a = i[o - 1];
                    return a && a.isTaroComponent && a.$scope && i.splice(o - 1, 1, a.$scope), wx[t].apply(wx, i);
                } : e[t] = function(e) {
                    for (var c = arguments.length, s = new Array(c > 1 ? c - 1 : 0), u = 1; u < c; u++) s[u - 1] = arguments[u];
                    e = e || {};
                    var d, f = null, h = Object.assign({}, e);
                    if ("string" === typeof e) return s.length ? (d = wx)[t].apply(d, [ e ].concat(s)) : wx[t](e);
                    if ("navigateTo" === t || "redirectTo" === t || "switchTab" === t) {
                        var p = h.url ? h.url.replace(/^\//, "") : "";
                        p.indexOf("?") > -1 && (p = p.split("?")[0]);
                        var v = (0, o.cacheDataGet)(p);
                        if (v) {
                            var g = new v();
                            if (g.componentWillPreload) {
                                var b = (0, i.getUniqueKey)(), m = h.url.indexOf("?"), y = m > -1, S = y ? h.url.substring(m + 1, h.url.length) : "", w = (0, 
                                i.queryToJson)(S);
                                h.url += (y ? "&" : "?") + "".concat(a, "=").concat(b), (0, o.cacheDataSet)(b, g.componentWillPreload(w)), 
                                (0, o.cacheDataSet)(l, g);
                            }
                        }
                    }
                    if (n[t]) {
                        var k = h.url = h.url || "", C = k.indexOf("?"), O = C > -1, j = O ? k.substring(C + 1, k.length) : "", T = (0, 
                        i.queryToJson)(j), P = (0, i.getUniqueKey)();
                        h.url += (O ? "&" : "?") + "".concat(r, "=").concat(P), (0, o.cacheDataSet)(P, T);
                    }
                    var E = new Promise(function(n, r) {
                        var o;
                        ([ "fail", "success", "complete" ].forEach(function(o) {
                            h[o] = function(i) {
                                e[o] && e[o](i), "success" === o ? n("connectSocket" === t ? Promise.resolve().then(function() {
                                    return Object.assign(f, i);
                                }) : i) : "fail" === o && r(i);
                            };
                        }), s.length) ? f = (o = wx)[t].apply(o, [ h ].concat(s)) : f = wx[t](h);
                    });
                    return "uploadFile" !== t && "downloadFile" !== t || (E.progress = function(e) {
                        return f && f.onProgressUpdate(e), E;
                    }, E.abort = function(e) {
                        return e && e(), f && f.abort(), E;
                    }), E;
                } : e[t] = function() {
                    console.warn("微信小程序暂不支持 ".concat(t));
                };
            });
        }
        function b(e) {
            var t = this.config || {}, n = t.designWidth, r = void 0 === n ? 750 : n, o = t.deviceRatio, i = void 0 === o ? {
                640: 1.17,
                750: 1,
                828: .905
            } : o;
            if (!(r in i)) throw new Error("deviceRatio 配置中不存在 ".concat(r, " 的设置！"));
            return parseInt(e, 10) / i[r] + "rpx";
        }
        function m() {
            var e = wx.getSystemInfoSync(), t = e.platform, n = t.toLowerCase();
            return "android" === n || "devtools" === n;
        }
        function y(e) {
            var t = wx.cloud || {}, n = {}, r = [ "init", "database", "uploadFile", "downloadFile", "getTempFileURL", "deleteFile", "callFunction", "CloudID" ];
            r.forEach(function(e) {
                n[e] = t[e];
            }), e.cloud = n;
        }
        function S(e) {
            g(e), e.request = p.request.bind(p), e.addInterceptor = p.addInterceptor.bind(p), 
            e.cleanInterceptors = p.cleanInterceptors.bind(p), e.getCurrentPages = getCurrentPages, 
            e.getApp = getApp, e.requirePlugin = requirePlugin, e.initPxTransform = l.bind(e), 
            e.pxTransform = b.bind(e), e.canIUseWebp = m, y(e);
        }
    },
    343: function(e, t, n) {
        "use strict";
        Object.defineProperty(t, "__esModule", {
            value: !0
        }), t.cacheDataSet = o, t.cacheDataGet = i, t.cacheDataHas = a;
        var r = {};
        function o(e, t) {
            r[e] = t;
        }
        function i(e, t) {
            var n = r[e];
            return t && delete r[e], n;
        }
        function a(e) {
            return e in r;
        }
    },
    344: function(e, t, n) {
        "use strict";
        function r(e) {
            for (var t, n, r, o = decodeURIComponent, i = e.split("&"), a = {}, c = 0, s = i.length; c < s; ++c) if (r = i[c], 
            r.length) {
                var u = r.indexOf("=");
                u < 0 ? (t = o(r), n = "") : (t = o(r.slice(0, u)), n = o(r.slice(u + 1))), "string" === typeof a[t] && (a[t] = [ a[t] ]), 
                Array.isArray(a[t]) ? a[t].push(n) : a[t] = n;
            }
            return a;
        }
        Object.defineProperty(t, "__esModule", {
            value: !0
        }), t.queryToJson = r, t.getUniqueKey = a;
        var o = 1, i = new Date().getTime().toString();
        function a() {
            return i + o++;
        }
    },
    613: function(e, t, n) {
        "use strict";
        n.r(t);
        var r = n(8);
        Component(Object(r["createRecursiveComponentConfig"])());
    },
    614: function(e, t, n) {
        "use strict";
        Object.defineProperty(t, "__esModule", {
            value: !0
        });
        var r = n(8);
        Component(r.createRecursiveComponentConfig("custom-wrapper"));
    },
    74: function(e, t, n) {
        "use strict";
        n.d(t, "b", function() {
            return j;
        });
        var r = n(10), o = n(11), i = n(122), a = n.n(i), c = n(96), s = n(8), u = n(15);
        function l(e) {
            return "o" === e[0] && "n" === e[1];
        }
        var d = /acit|ex(?:s|g|n|p|$)|rph|grid|ows|mnc|ntw|ine[ch]|zoo|^ord/i;
        function f(e, t, n) {
            var r;
            for (r in t) r in n || v(e, r, null, t[r]);
            var o = e instanceof s["FormElement"];
            for (r in n) (t[r] !== n[r] || o && "value" === r) && v(e, r, n[r], t[r]);
        }
        function h(e, t, n, r) {
            var o = t.endsWith("Capture"), i = t.toLowerCase().slice(2);
            o && (i = i.slice(0, -7));
            var a = Object(u["c"])(Object(u["u"])(e.tagName.toLowerCase()));
            "click" === i && a in u["h"] && (i = "tap"), Object(u["k"])(n) ? (r || e.addEventListener(i, n, o), 
            "regionchange" === i ? (e.__handlers.begin[0] = n, e.__handlers.end[0] = n) : e.__handlers[i][0] = n) : e.removeEventListener(i, r);
        }
        function p(e, t, n) {
            "-" === t[0] && e.setProperty(t, n.toString()), e[t] = Object(u["l"])(n) && !1 === d.test(t) ? n + "px" : null == n ? "" : n;
        }
        function v(e, t, n, r) {
            var o, i, a, c;
            if (t = "className" === t ? "class" : t, "key" === t || "children" === t || "ref" === t) ; else if ("style" === t) {
                var s = e.style;
                if (Object(u["n"])(n)) s.cssText = n; else {
                    if (Object(u["n"])(r) && (s.cssText = "", r = null), Object(u["m"])(r)) for (var d in r) n && d in n || p(s, d, "");
                    if (Object(u["m"])(n)) for (var f in n) r && n[f] === r[f] || p(s, f, n[f]);
                }
            } else if (l(t)) h(e, t, n, r); else if ("dangerouslySetInnerHTML" === t) {
                var v = null !== (i = null === (o = n) || void 0 === o ? void 0 : o.__html) && void 0 !== i ? i : "", g = null !== (c = null === (a = r) || void 0 === a ? void 0 : a.__html) && void 0 !== c ? c : "";
                (v || g) && g !== v && (e.innerHTML = v);
            } else Object(u["k"])(n) || (null == n ? e.removeAttribute(t) : e.setAttribute(t, n));
        }
        var g = c["unstable_scheduleCallback"], b = c["unstable_cancelCallback"], m = c["unstable_now"];
        function y() {
            return !1;
        }
        var S = {
            createInstance: function(e) {
                return s["document"].createElement(e);
            },
            createTextInstance: function(e) {
                return s["document"].createTextNode(e);
            },
            getPublicInstance: function(e) {
                return e;
            },
            getRootHostContext: function() {
                return {};
            },
            getChildHostContext: function() {
                return {};
            },
            appendChild: function(e, t) {
                e.appendChild(t);
            },
            appendInitialChild: function(e, t) {
                e.appendChild(t);
            },
            appendChildToContainer: function(e, t) {
                e.appendChild(t);
            },
            removeChild: function(e, t) {
                e.removeChild(t);
            },
            removeChildFromContainer: function(e, t) {
                e.removeChild(t);
            },
            insertBefore: function(e, t, n) {
                e.insertBefore(t, n);
            },
            insertInContainerBefore: function(e, t, n) {
                e.insertBefore(t, n);
            },
            commitTextUpdate: function(e, t, n) {
                e.nodeValue = n;
            },
            finalizeInitialChildren: function(e, t, n) {
                return f(e, {}, n), !1;
            },
            prepareUpdate: function() {
                return u["a"];
            },
            commitUpdate: function(e, t, n, r, o) {
                f(e, r, o);
            },
            hideInstance: function(e) {
                var t = e.style;
                t.setProperty("display", "none");
            },
            unhideInstance: function(e, t) {
                var n = t.style, r = (null === n || void 0 === n ? void 0 : n.hasOwnProperty("display")) ? n.display : null;
                r = null == r || "boolean" === typeof r || "" === r ? "" : ("" + r).trim(), e.style["display"] = r;
            },
            shouldSetTextContent: y,
            shouldDeprioritizeSubtree: y,
            prepareForCommit: u["r"],
            resetAfterCommit: u["r"],
            commitMount: u["r"],
            now: m,
            scheduleDeferredCallback: g,
            cancelDeferredCallback: b,
            clearTimeout: clearTimeout,
            setTimeout: setTimeout,
            noTimeout: -1,
            supportsMutation: !0,
            supportsPersistence: !1,
            isPrimaryRenderer: !0,
            supportsHydration: !1
        }, w = a()(S), k = new WeakMap(), C = function() {
            function e(t, n) {
                Object(r["a"])(this, e), this.renderer = t, this.internalRoot = t.createContainer(n, !1, !1);
            }
            return Object(o["a"])(e, [ {
                key: "render",
                value: function(e, t) {
                    return this.renderer.updateContainer(e, this.internalRoot, null, t), this.renderer.getPublicRootInstance(this.internalRoot);
                }
            }, {
                key: "unmount",
                value: function(e) {
                    this.renderer.updateContainer(null, this.internalRoot, null, e);
                }
            } ]), e;
        }();
        function O(e, t, n) {
            var r = k.get(t);
            if (null != r) return r.render(e, n);
            var o = new C(w, t);
            return k.set(t, o), o.render(e, n);
        }
        var j = w.batchedUpdates;
        function T(e) {
            Object(u["f"])(e && [ 1, 8, 9, 11 ].includes(e.nodeType), "unmountComponentAtNode(...): Target container is not a DOM element.");
            var t = k.get(e);
            return !!t && (j(function() {
                t.unmount(function() {
                    k.delete(e);
                });
            }), !0);
        }
        function P(e) {
            if (null == e) return null;
            var t = e.nodeType;
            return 1 === t || 3 === t ? e : w.findHostInstance(e);
        }
        var E = "function" === typeof Symbol && Symbol.for ? Symbol.for("react.portal") : 60106;
        function B(e, t, n) {
            return {
                $$typeof: E,
                key: null == n ? null : String(n),
                children: e,
                containerInfo: t,
                implementation: null
            };
        }
        var A = {
            render: O,
            unstable_batchedUpdates: j,
            unmountComponentAtNode: T,
            findDOMNode: P,
            createPortal: B
        };
        t["a"] = A;
    },
    8: function(e, t, n) {
        "use strict";
        n.r(t), function(e, r, o, i, a) {
            n.d(t, "Current", function() {
                return Qn;
            }), n.d(t, "CurrentReconciler", function() {
                return k;
            }), n.d(t, "Events", function() {
                return Pn;
            }), n.d(t, "FormElement", function() {
                return De;
            }), n.d(t, "HOOKS_APP_ID", function() {
                return lr;
            }), n.d(t, "Style", function() {
                return Ae;
            }), n.d(t, "TaroElement", function() {
                return Re;
            }), n.d(t, "TaroEvent", function() {
                return A;
            }), n.d(t, "TaroNode", function() {
                return Oe;
            }), n.d(t, "TaroRootElement", function() {
                return An;
            }), n.d(t, "TaroText", function() {
                return je;
            }), n.d(t, "cancelAnimationFrame", function() {
                return zn;
            }), n.d(t, "connectReactPage", function() {
                return Ir;
            }), n.d(t, "connectVuePage", function() {
                return Wr;
            }), n.d(t, "createComponentConfig", function() {
                return sr;
            }), n.d(t, "createDocument", function() {
                return Rn;
            }), n.d(t, "createEvent", function() {
                return x;
            }), n.d(t, "createNativeComponentConfig", function() {
                return Fr;
            }), n.d(t, "createPageConfig", function() {
                return cr;
            }), n.d(t, "createReactApp", function() {
                return Rr;
            }), n.d(t, "createRecursiveComponentConfig", function() {
                return ur;
            }), n.d(t, "createVue3App", function() {
                return Hr;
            }), n.d(t, "createVueApp", function() {
                return Ur;
            }), n.d(t, "document", function() {
                return Nn;
            }), n.d(t, "eventCenter", function() {
                return En;
            }), n.d(t, "getComputedStyle", function() {
                return Hn;
            }), n.d(t, "getCurrentInstance", function() {
                return Kn;
            }), n.d(t, "hydrate", function() {
                return M;
            }), n.d(t, "injectPageInstance", function() {
                return Yn;
            }), n.d(t, "navigator", function() {
                return Vn;
            }), n.d(t, "nextTick", function() {
                return Gr;
            }), n.d(t, "now", function() {
                return Dn;
            }), n.d(t, "options", function() {
                return F;
            }), n.d(t, "requestAnimationFrame", function() {
                return qn;
            }), n.d(t, "stringify", function() {
                return nr;
            }), n.d(t, "useAddToFavorites", function() {
                return Or;
            }), n.d(t, "useDidHide", function() {
                return hr;
            }), n.d(t, "useDidShow", function() {
                return fr;
            }), n.d(t, "useOptionMenuClick", function() {
                return wr;
            }), n.d(t, "usePageScroll", function() {
                return gr;
            }), n.d(t, "usePullDownRefresh", function() {
                return pr;
            }), n.d(t, "usePullIntercept", function() {
                return kr;
            }), n.d(t, "useReachBottom", function() {
                return vr;
            }), n.d(t, "useReady", function() {
                return jr;
            }), n.d(t, "useResize", function() {
                return br;
            }), n.d(t, "useRouter", function() {
                return Tr;
            }), n.d(t, "useScope", function() {
                return Pr;
            }), n.d(t, "useShareAppMessage", function() {
                return mr;
            }), n.d(t, "useShareTimeline", function() {
                return Cr;
            }), n.d(t, "useTabItemTap", function() {
                return yr;
            }), n.d(t, "useTitleClick", function() {
                return Sr;
            }), n.d(t, "window", function() {
                return $n;
            });
            var c = n(120), s = n(18), u = n(41), l = n(27), d = n(160), f = n(121), h = n(25), p = n(5), v = n(12), g = n(13), b = n(9), m = n(4), y = n(10), S = n(11), w = n(15), k = Object.assign({
                getLifecyle: function(e, t) {
                    return e[t];
                },
                getPathIndex: function(e) {
                    return "[".concat(e, "]");
                },
                getEventCenter: function(e) {
                    return new e();
                }
            }, w["e"]), C = function() {
                var e = 0;
                return function() {
                    return (e++).toString();
                };
            };
            function O(e) {
                return 1 === e.nodeType;
            }
            function j(e) {
                return 3 === e.nodeType;
            }
            function T(e) {
                var t = Object.keys(e.props).find(function(e) {
                    return !(/^(class|style|id)$/.test(e) || e.startsWith("data-"));
                });
                return Boolean(t);
            }
            function P(e, t) {
                var n, r;
                if (!1 === (null === (n = k.isBubbleEvent) || void 0 === n ? void 0 : n.call(k, t, e.tagName))) return !1;
                var o = !1;
                while ((null === e || void 0 === e ? void 0 : e.parentElement) && "root" !== e.parentElement._path) {
                    if (null === (r = e.parentElement.__handlers[t]) || void 0 === r ? void 0 : r.length) {
                        o = !0;
                        break;
                    }
                    e = e.parentElement;
                }
                return o;
            }
            var E = function() {
                function e() {
                    Object(y["a"])(this, e), this.__handlers = {};
                }
                return Object(S["a"])(e, [ {
                    key: "addEventListener",
                    value: function(e, t, n) {
                        var r;
                        if (null === (r = k.onAddEvent) || void 0 === r || r.call(k, e, t, n), "regionchange" === e) return this.addEventListener("begin", t, n), 
                        void this.addEventListener("end", t, n);
                        e = e.toLowerCase();
                        var o = this.__handlers[e], i = Boolean(n), a = !1;
                        if (Object(w["m"])(n) && (i = Boolean(n.capture), a = Boolean(n.once)), a) {
                            var c = function n() {
                                t.apply(this, arguments), this.removeEventListener(e, n);
                            };
                            this.addEventListener(e, c, Object.assign(Object.assign({}, n), {
                                once: !1
                            }));
                        } else Object(w["w"])(i, "The event capture feature is unimplemented."), Object(w["i"])(o) ? o.push(t) : this.__handlers[e] = [ t ];
                    }
                }, {
                    key: "removeEventListener",
                    value: function(e, t) {
                        if (e = e.toLowerCase(), null != t) {
                            var n = this.__handlers[e];
                            if (Object(w["i"])(n)) {
                                var r = n.indexOf(t);
                                Object(w["w"])(-1 === r, "事件: '".concat(e, "' 没有注册在 DOM 中，因此不会被移除。")), n.splice(r, 1);
                            }
                        }
                    }
                }, {
                    key: "isAnyEventBinded",
                    value: function() {
                        var e = this, t = Object.keys(this.__handlers).find(function(t) {
                            var n = e.__handlers[t];
                            return n.length;
                        });
                        return t;
                    }
                } ]), e;
            }(), B = new Map(), A = function() {
                function e(t, n, r) {
                    Object(y["a"])(this, e), this._stop = !1, this._end = !1, this.defaultPrevented = !1, 
                    this.timeStamp = Date.now(), this.type = t.toLowerCase(), this.mpEvent = r, this.bubbles = Boolean(n && n.bubbles), 
                    this.cancelable = Boolean(n && n.cancelable);
                }
                return Object(S["a"])(e, [ {
                    key: "stopPropagation",
                    value: function() {
                        this._stop = !0;
                    }
                }, {
                    key: "stopImmediatePropagation",
                    value: function() {
                        this._end = this._stop = !0;
                    }
                }, {
                    key: "preventDefault",
                    value: function() {
                        this.defaultPrevented = !0;
                    }
                }, {
                    key: "target",
                    get: function() {
                        var e, t, n, r = Nn.getElementById(null === (e = this.mpEvent) || void 0 === e ? void 0 : e.target.id);
                        return Object.assign(Object.assign(Object.assign({}, null === (t = this.mpEvent) || void 0 === t ? void 0 : t.target), null === (n = this.mpEvent) || void 0 === n ? void 0 : n.detail), {
                            dataset: null !== r ? r.dataset : w["b"]
                        });
                    }
                }, {
                    key: "currentTarget",
                    get: function() {
                        var e, t, n, r = Nn.getElementById(null === (e = this.mpEvent) || void 0 === e ? void 0 : e.currentTarget.id);
                        return null === r ? this.target : Object.assign(Object.assign(Object.assign({}, null === (t = this.mpEvent) || void 0 === t ? void 0 : t.currentTarget), null === (n = this.mpEvent) || void 0 === n ? void 0 : n.detail), {
                            dataset: r.dataset
                        });
                    }
                } ]), e;
            }();
            function x(e, t) {
                if ("string" === typeof e) return new A(e, {
                    bubbles: !0,
                    cancelable: !0
                });
                var n = new A(e.type, {
                    bubbles: !0,
                    cancelable: !0
                }, e);
                for (var r in e) "currentTarget" !== r && "target" !== r && "type" !== r && "timeStamp" !== r && (n[r] = e[r]);
                return n;
            }
            var I = {};
            function _(e) {
                var t;
                null === (t = k.modifyEventType) || void 0 === t || t.call(k, e), null == e.currentTarget && (e.currentTarget = e.target);
                var n = Nn.getElementById(e.currentTarget.id);
                if (null != n) {
                    var r = function() {
                        n.dispatchEvent(x(e));
                    };
                    if ("function" === typeof k.batchedEventUpdates) {
                        var o = e.type;
                        !P(n, o) || "touchmove" === o && n.props.catchMove ? k.batchedEventUpdates(function() {
                            I[o] && (I[o].forEach(function(e) {
                                return e();
                            }), delete I[o]), r();
                        }) : (I[o] || (I[o] = [])).push(r);
                    } else r();
                }
            }
            var L = 2046, R = "小程序 setData", D = "页面初始化", N = [ "view", "text", "image" ];
            function M(e) {
                var t, n, r = e.nodeName;
                if (j(e)) return n = {}, Object(m["a"])(n, "v", e.nodeValue), Object(m["a"])(n, "nn", r), 
                n;
                var o = (t = {}, Object(m["a"])(t, "nn", r), Object(m["a"])(t, "uid", e.uid), t), i = e.props, a = e.childNodes;
                for (var c in !e.isAnyEventBinded() && N.indexOf(r) > -1 && (o["nn"] = "static-".concat(r), 
                "view" !== r || T(e) || (o["nn"] = "pure-view")), i) {
                    var s = Object(w["u"])(c);
                    c.startsWith("data-") || "class" === c || "style" === c || "id" === c || "catchMove" === s || (o[s] = i[c]), 
                    "view" === r && "catchMove" === s && "false" !== i[c] && (o["nn"] = "catch-view");
                }
                return a.length > 0 ? o["cn"] = a.map(M) : o["cn"] = [], "" !== e.className && (o["cl"] = e.className), 
                "" !== e.cssText && "swiper-item" !== r && (o["st"] = e.cssText), o;
            }
            var F = {
                prerender: !0,
                debug: !1,
                html: {
                    skipElements: new Set([ "style", "script" ]),
                    voidElements: new Set([ "!doctype", "area", "base", "br", "col", "command", "embed", "hr", "img", "input", "keygen", "link", "meta", "param", "source", "track", "wbr" ]),
                    closingElements: new Set([ "html", "head", "body", "p", "dt", "dd", "li", "option", "thead", "th", "tbody", "tr", "td", "tfoot", "colgroup" ]),
                    renderHTMLTag: !1
                },
                reconciler: function(e) {
                    Object.assign(k, e);
                }
            };
            function W() {
                return {
                    index: 0,
                    column: 0,
                    line: 0
                };
            }
            function V(e, t, n) {
                for (var r = e.index, o = e.index = r + n, i = r; i < o; i++) {
                    var a = t.charAt(i);
                    "\n" === a ? (e.line++, e.column = 0) : e.column++;
                }
            }
            function U(e, t, n) {
                var r = n - e.index;
                return V(e, t, r);
            }
            function q(e) {
                return {
                    index: e.index,
                    line: e.line,
                    column: e.column
                };
            }
            var z = /\s/;
            function H(e) {
                return z.test(e);
            }
            var $ = /=/;
            function G(e) {
                return $.test(e);
            }
            function Q(e) {
                var t = e.toLowerCase();
                return !!F.html.skipElements.has(t);
            }
            var K = /[A-Za-z0-9]/;
            function J(e, t) {
                while (1) {
                    var n = e.indexOf("<", t);
                    if (-1 === n) return n;
                    var r = e.charAt(n + 1);
                    if ("/" === r || "!" === r || K.test(r)) return n;
                    t = n + 1;
                }
            }
            function Y(e, t, n) {
                if (!H(n.charAt(e))) return !1;
                for (var r = n.length, o = e - 1; o > t; o--) {
                    var i = n.charAt(o);
                    if (!H(i)) {
                        if (G(i)) return !1;
                        break;
                    }
                }
                for (var a = e + 1; a < r; a++) {
                    var c = n.charAt(a);
                    if (!H(c)) return !G(c);
                }
            }
            var X = function() {
                function e(t) {
                    Object(y["a"])(this, e), this.tokens = [], this.position = W(), this.html = t;
                }
                return Object(S["a"])(e, [ {
                    key: "scan",
                    value: function() {
                        var e = this.html, t = this.position, n = e.length;
                        while (t.index < n) {
                            var r = t.index;
                            if (this.scanText(), t.index === r) {
                                var o = e.startsWith("!--", r + 1);
                                if (o) this.scanComment(); else {
                                    var i = this.scanTag();
                                    Q(i) && this.scanSkipTag(i);
                                }
                            }
                        }
                        return this.tokens;
                    }
                }, {
                    key: "scanText",
                    value: function() {
                        var e = "text", t = this.html, n = this.position, r = J(t, n.index);
                        if (r !== n.index) {
                            -1 === r && (r = t.length);
                            var o = q(n), i = t.slice(n.index, r);
                            U(n, t, r);
                            var a = q(n);
                            this.tokens.push({
                                type: e,
                                content: i,
                                position: {
                                    start: o,
                                    end: a
                                }
                            });
                        }
                    }
                }, {
                    key: "scanComment",
                    value: function() {
                        var e = "comment", t = this.html, n = this.position, r = q(n);
                        V(n, t, 4);
                        var o = t.indexOf("--\x3e", n.index), i = o + 3;
                        -1 === o && (o = i = t.length);
                        var a = t.slice(n.index, o);
                        U(n, t, i), this.tokens.push({
                            type: e,
                            content: a,
                            position: {
                                start: r,
                                end: q(n)
                            }
                        });
                    }
                }, {
                    key: "scanTag",
                    value: function() {
                        this.scanTagStart();
                        var e = this.scanTagName();
                        return this.scanAttrs(), this.scanTagEnd(), e;
                    }
                }, {
                    key: "scanTagStart",
                    value: function() {
                        var e = "tag-start", t = this.html, n = this.position, r = t.charAt(n.index + 1), o = "/" === r, i = q(n);
                        V(n, t, o ? 2 : 1), this.tokens.push({
                            type: e,
                            close: o,
                            position: {
                                start: i
                            }
                        });
                    }
                }, {
                    key: "scanTagEnd",
                    value: function() {
                        var e = "tag-end", t = this.html, n = this.position, r = t.charAt(n.index), o = "/" === r;
                        V(n, t, o ? 2 : 1);
                        var i = q(n);
                        this.tokens.push({
                            type: e,
                            close: o,
                            position: {
                                end: i
                            }
                        });
                    }
                }, {
                    key: "scanTagName",
                    value: function() {
                        var e = "tag", t = this.html, n = this.position, r = t.length, o = n.index;
                        while (o < r) {
                            var i = t.charAt(o), a = !(H(i) || "/" === i || ">" === i);
                            if (a) break;
                            o++;
                        }
                        var c = o + 1;
                        while (c < r) {
                            var s = t.charAt(c), u = !(H(s) || "/" === s || ">" === s);
                            if (!u) break;
                            c++;
                        }
                        U(n, t, c);
                        var l = t.slice(o, c);
                        return this.tokens.push({
                            type: e,
                            content: l
                        }), l;
                    }
                }, {
                    key: "scanAttrs",
                    value: function() {
                        var e = this.html, t = this.position, n = this.tokens, r = t.index, o = null, i = r, a = [], c = e.length;
                        while (r < c) {
                            var s = e.charAt(r);
                            if (o) {
                                var u = s === o;
                                u && (o = null), r++;
                            } else {
                                var l = "/" === s || ">" === s;
                                if (l) {
                                    r !== i && a.push(e.slice(i, r));
                                    break;
                                }
                                if (Y(r, i, e)) r !== i && a.push(e.slice(i, r)), i = r + 1, r++; else {
                                    var d = "'" === s || '"' === s;
                                    d ? (o = s, r++) : r++;
                                }
                            }
                        }
                        U(t, e, r);
                        for (var f = a.length, h = "attribute", p = 0; p < f; p++) {
                            var v = a[p], g = v.includes("=");
                            if (g) {
                                var b = a[p + 1];
                                if (b && b.startsWith("=")) {
                                    if (b.length > 1) {
                                        var m = v + b;
                                        n.push({
                                            type: h,
                                            content: m
                                        }), p += 1;
                                        continue;
                                    }
                                    var y = a[p + 2];
                                    if (p += 1, y) {
                                        var S = v + "=" + y;
                                        n.push({
                                            type: h,
                                            content: S
                                        }), p += 1;
                                        continue;
                                    }
                                }
                            }
                            if (v.endsWith("=")) {
                                var w = a[p + 1];
                                if (w && !w.includes("=")) {
                                    var k = v + w;
                                    n.push({
                                        type: h,
                                        content: k
                                    }), p += 1;
                                    continue;
                                }
                                var C = v.slice(0, -1);
                                n.push({
                                    type: h,
                                    content: C
                                });
                            } else n.push({
                                type: h,
                                content: v
                            });
                        }
                    }
                }, {
                    key: "scanSkipTag",
                    value: function(e) {
                        var t = this.html, n = this.position, r = e.toLowerCase(), o = t.length;
                        while (n.index < o) {
                            var i = t.indexOf("</", n.index);
                            if (-1 === i) {
                                this.scanText();
                                break;
                            }
                            U(n, t, i);
                            var a = this.scanTag();
                            if (r === a.toLowerCase()) break;
                        }
                    }
                } ]), e;
            }();
            function Z(e, t) {
                for (var n = Object.create(null), r = e.split(","), o = 0; o < r.length; o++) n[r[o]] = !0;
                return t ? function(e) {
                    return !!n[e.toLowerCase()];
                } : function(e) {
                    return !!n[e];
                };
            }
            var ee = {
                img: "image",
                iframe: "web-view"
            }, te = Object.keys(w["h"]).map(function(e) {
                return e.toLowerCase();
            }).join(","), ne = Z(te, !0), re = Z("a,i,abbr,iframe,select,acronym,slot,small,span,bdi,kbd,strong,big,map,sub,sup,br,mark,mark,meter,template,canvas,textarea,cite,object,time,code,output,u,data,picture,tt,datalist,var,dfn,del,q,em,s,embed,samp,b", !0), oe = Z("address,fieldset,li,article,figcaption,main,aside,figure,nav,blockquote,footer,ol,details,form,p,dialog,h1,h2,h3,h4,h5,h6,pre,dd,header,section,div,hgroup,table,dl,hr,ul,dt", !0), ie = "{", ae = "}", ce = ".", se = "#", ue = ">", le = "~", de = "+", fe = function() {
                function e() {
                    Object(y["a"])(this, e), this.styles = [];
                }
                return Object(S["a"])(e, [ {
                    key: "extractStyle",
                    value: function(e) {
                        var t = this, n = /<style\s?[^>]*>((.|\n|\s)+?)<\/style>/g, r = e;
                        return r = r.replace(n, function(e, n) {
                            var r = n.trim();
                            return t.stringToSelector(r), "";
                        }), r.trim();
                    }
                }, {
                    key: "stringToSelector",
                    value: function(e) {
                        var t = this, n = e.indexOf(ie), r = function() {
                            var r = e.indexOf(ae), o = e.slice(0, n).trim(), i = e.slice(n + 1, r).replace(/ /g, "");
                            /;$/.test(i) || (i += ";"), o.split(",").forEach(function(e) {
                                var n = t.parseSelector(e);
                                t.styles.push({
                                    content: i,
                                    selectorList: n
                                });
                            }), e = e.slice(r + 1), n = e.indexOf(ie);
                        };
                        while (n > -1) r();
                    }
                }, {
                    key: "parseSelector",
                    value: function(e) {
                        var t = e.trim().replace(/ *([>~+]) */g, " $1").replace(/ +/g, " ").split(" "), n = t.map(function(e) {
                            var t = e.charAt(0), n = {
                                isChild: t === ue,
                                isGeneralSibling: t === le,
                                isAdjacentSibling: t === de,
                                tag: null,
                                id: null,
                                class: [],
                                attrs: []
                            };
                            return e = e.replace(/^[>~+]/, ""), e = e.replace(/\[(.+?)\]/g, function(e, t) {
                                var r = t.split("="), o = Object(b["a"])(r, 2), i = o[0], a = o[1], c = -1 === t.indexOf("="), s = {
                                    all: c,
                                    key: i,
                                    value: c ? null : a
                                };
                                return n.attrs.push(s), "";
                            }), e = e.replace(/([.#][A-Za-z0-9-_]+)/g, function(e, t) {
                                return t[0] === se ? n.id = t.substr(1) : t[0] === ce && n.class.push(t.substr(1)), 
                                "";
                            }), "" !== e && (n.tag = e), n;
                        });
                        return n;
                    }
                }, {
                    key: "matchStyle",
                    value: function(e, t, n) {
                        var r = this, o = this.styles.reduce(function(o, i, a) {
                            var c = i.content, s = i.selectorList, u = n[a], l = s[u], d = s[u + 1];
                            ((null === d || void 0 === d ? void 0 : d.isGeneralSibling) || (null === d || void 0 === d ? void 0 : d.isAdjacentSibling)) && (l = d, 
                            u += 1, n[a] += 1);
                            var f = r.matchCurrent(e, t, l);
                            if (f && l.isGeneralSibling) {
                                var h = he(t);
                                while (h) {
                                    if (h.h5tagName && r.matchCurrent(h.h5tagName, h, s[u - 1])) {
                                        f = !0;
                                        break;
                                    }
                                    h = he(h), f = !1;
                                }
                            }
                            if (f && l.isAdjacentSibling) {
                                var p = he(t);
                                if (p && p.h5tagName) {
                                    var v = r.matchCurrent(p.h5tagName, p, s[u - 1]);
                                    v || (f = !1);
                                } else f = !1;
                            }
                            if (f) {
                                if (u === s.length - 1) return o + c;
                                u < s.length - 1 && (n[a] += 1);
                            } else l.isChild && u > 0 && (n[a] -= 1, r.matchCurrent(e, t, s[n[a]]) && (n[a] += 1));
                            return o;
                        }, "");
                        return o;
                    }
                }, {
                    key: "matchCurrent",
                    value: function(e, t, n) {
                        if (n.tag && n.tag !== e) return !1;
                        if (n.id && n.id !== t.id) return !1;
                        if (n.class.length) for (var r = t.className.split(" "), o = 0; o < n.class.length; o++) {
                            var i = n.class[o];
                            if (-1 === r.indexOf(i)) return !1;
                        }
                        if (n.attrs.length) for (var a = 0; a < n.attrs.length; a++) {
                            var c = n.attrs[a], s = c.all, u = c.key, l = c.value;
                            if (s && !t.hasAttribute(u)) return !1;
                            var d = t.getAttribute(u);
                            if (d !== ge(l || "")) return !1;
                        }
                        return !0;
                    }
                } ]), e;
            }();
            function he(e) {
                var t = e.parentElement;
                if (!t) return null;
                var n = e.previousSibling;
                return n ? 1 === n.nodeType ? n : he(n) : null;
            }
            var pe = {
                li: [ "ul", "ol", "menu" ],
                dt: [ "dl" ],
                dd: [ "dl" ],
                tbody: [ "table" ],
                thead: [ "table" ],
                tfoot: [ "table" ],
                tr: [ "table" ],
                td: [ "table" ]
            };
            function ve(e, t) {
                var n = pe[e];
                if (n) {
                    var r = t.length - 1;
                    while (r >= 0) {
                        var o = t[r].tagName;
                        if (o === e) break;
                        if (n && n.includes(o)) return !0;
                        r--;
                    }
                }
                return !1;
            }
            function ge(e) {
                var t = e.charAt(0), n = e.length - 1, r = '"' === t || "'" === t;
                return r && t === e.charAt(n) ? e.slice(1, n) : e;
            }
            function be(e) {
                return F.html.renderHTMLTag ? e : ee[e] ? ee[e] : ne(e) ? e : oe(e) ? "view" : re(e) ? "text" : "view";
            }
            function me(e) {
                var t = "=", n = e.indexOf(t);
                if (-1 === n) return [ e ];
                var r = e.slice(0, n).trim(), o = e.slice(n + t.length).trim();
                return [ r, o ];
            }
            function ye(e, t, n) {
                return e.filter(function(e) {
                    return "comment" !== e.type && ("text" !== e.type || "" !== e.content);
                }).map(function(e) {
                    if ("text" === e.type) {
                        var r = Nn.createTextNode(e.content);
                        return Object(w["k"])(F.html.transformText) ? F.html.transformText(r, e) : (null === n || void 0 === n || n.appendChild(r), 
                        r);
                    }
                    var o = Nn.createElement(be(e.tagName));
                    o.h5tagName = e.tagName, null === n || void 0 === n || n.appendChild(o), F.html.renderHTMLTag || (o.className = e.tagName);
                    for (var i = 0; i < e.attributes.length; i++) {
                        var a = e.attributes[i], c = me(a), s = Object(b["a"])(c, 2), u = s[0], l = s[1];
                        if ("class" === u) o.className += " " + ge(l); else {
                            if ("o" === u[0] && "n" === u[1]) continue;
                            o.setAttribute(u, null == l || ge(l));
                        }
                    }
                    var d = t.styleTagParser, f = t.descendantList, h = f.slice(), p = d.matchStyle(e.tagName, o, h);
                    return o.setAttribute("style", p + o.style.cssText), ye(e.children, {
                        styleTagParser: d,
                        descendantList: h
                    }, o), Object(w["k"])(F.html.transformElement) ? F.html.transformElement(o, e) : o;
                });
            }
            function Se(e) {
                var t = new fe();
                e = t.extractStyle(e);
                var n = new X(e).scan(), r = {
                    tagName: "",
                    children: [],
                    type: "element",
                    attributes: []
                }, o = {
                    tokens: n,
                    options: F,
                    cursor: 0,
                    stack: [ r ]
                };
                return we(o), ye(r.children, {
                    styleTagParser: t,
                    descendantList: Array(t.styles.length).fill(0)
                });
            }
            function we(e) {
                var t = e.tokens, n = e.stack, r = e.cursor, o = t.length, i = n[n.length - 1].children;
                while (r < o) {
                    var a = t[r];
                    if ("tag-start" === a.type) {
                        var c = t[++r];
                        r++;
                        var s = c.content.toLowerCase();
                        if (a.close) {
                            var u = n.length, l = !1;
                            while (--u > -1) if (n[u].tagName === s) {
                                l = !0;
                                break;
                            }
                            while (r < o) {
                                var d = t[r];
                                if ("tag-end" !== d.type) break;
                                r++;
                            }
                            if (l) {
                                n.splice(u);
                                break;
                            }
                        } else {
                            var f = F.html.closingElements.has(s), h = f;
                            if (h && (h = !ve(s, n)), h) {
                                var p = n.length - 1;
                                while (p > 0) {
                                    if (s === n[p].tagName) {
                                        n.splice(p);
                                        var v = p - 1;
                                        i = n[v].children;
                                        break;
                                    }
                                    p -= 1;
                                }
                            }
                            var g = [], b = void 0;
                            while (r < o) {
                                if (b = t[r], "tag-end" === b.type) break;
                                g.push(b.content), r++;
                            }
                            r++;
                            var m = [], y = {
                                type: "element",
                                tagName: c.content,
                                attributes: g,
                                children: m
                            };
                            i.push(y);
                            var S = !(b.close || F.html.voidElements.has(s));
                            if (S) {
                                n.push({
                                    tagName: s,
                                    children: m
                                });
                                var w = {
                                    tokens: t,
                                    cursor: r,
                                    stack: n
                                };
                                we(w), r = w.cursor;
                            }
                        }
                    } else i.push(a), r++;
                }
                e.cursor = r;
            }
            function ke(e, t) {
                e.childNodes.forEach(function(t) {
                    e.removeChild(t);
                });
                for (var n = Se(t), r = 0; r < n.length; r++) e.appendChild(n[r]);
            }
            var Ce = C(), Oe = function(e) {
                Object(v["a"])(n, e);
                var t = Object(g["a"])(n);
                function n(e, r) {
                    var o;
                    return Object(y["a"])(this, n), o = t.call(this), o.parentNode = null, o.childNodes = [], 
                    o.hydrate = function(e) {
                        return function() {
                            return M(e);
                        };
                    }, o.nodeType = e, o.nodeName = r, o.uid = "_n_".concat(Ce()), B.set(o.uid, Object(p["a"])(o)), 
                    o;
                }
                return Object(S["a"])(n, [ {
                    key: "_path",
                    get: function() {
                        if (null !== this.parentNode) {
                            var e = this.parentNode.childNodes.indexOf(this), t = k.getPathIndex(e);
                            return "".concat(this.parentNode._path, ".", "cn", ".").concat(t);
                        }
                        return "";
                    }
                }, {
                    key: "_root",
                    get: function() {
                        return null !== this.parentNode ? this.parentNode._root : null;
                    }
                }, {
                    key: "parentElement",
                    get: function() {
                        var e = this.parentNode;
                        return null != e && 1 === e.nodeType ? e : null;
                    }
                }, {
                    key: "nextSibling",
                    get: function() {
                        var e = this.parentNode;
                        return e && e.childNodes[this.findIndex(e.childNodes, this) + 1] || null;
                    }
                }, {
                    key: "previousSibling",
                    get: function() {
                        var e = this.parentNode;
                        return e && e.childNodes[this.findIndex(e.childNodes, this) - 1] || null;
                    }
                }, {
                    key: "insertBefore",
                    value: function(e, t, n) {
                        var r, o, i = this;
                        if (e.remove(), e.parentNode = this, t) {
                            var a = this.findIndex(this.childNodes, t);
                            this.childNodes.splice(a, 0, e), o = !0 === n ? {
                                path: e._path,
                                value: this.hydrate(e)
                            } : {
                                path: "".concat(this._path, ".", "cn"),
                                value: function() {
                                    return i.childNodes.map(M);
                                }
                            };
                        } else this.childNodes.push(e), o = {
                            path: e._path,
                            value: this.hydrate(e)
                        };
                        return null === (r = k.insertBefore) || void 0 === r || r.call(k, this, e, t), this.enqueueUpdate(o), 
                        B.has(e.uid) || B.set(e.uid, e), e;
                    }
                }, {
                    key: "appendChild",
                    value: function(e) {
                        var t;
                        this.insertBefore(e), null === (t = k.appendChild) || void 0 === t || t.call(k, this, e);
                    }
                }, {
                    key: "replaceChild",
                    value: function(e, t) {
                        var n;
                        if (t.parentNode === this) return this.insertBefore(e, t, !0), t.remove(!0), t;
                        null === (n = k.removeChild) || void 0 === n || n.call(k, this, e, t);
                    }
                }, {
                    key: "removeChild",
                    value: function(e, t) {
                        var n = this, r = this.findIndex(this.childNodes, e);
                        return this.childNodes.splice(r, 1), !0 !== t && this.enqueueUpdate({
                            path: "".concat(this._path, ".", "cn"),
                            value: function() {
                                return n.childNodes.map(M);
                            }
                        }), e.parentNode = null, B.delete(e.uid), e;
                    }
                }, {
                    key: "remove",
                    value: function(e) {
                        this.parentNode && this.parentNode.removeChild(this, e);
                    }
                }, {
                    key: "firstChild",
                    get: function() {
                        return this.childNodes[0] || null;
                    }
                }, {
                    key: "lastChild",
                    get: function() {
                        var e = this.childNodes;
                        return e[e.length - 1] || null;
                    }
                }, {
                    key: "hasChildNodes",
                    value: function() {
                        return this.childNodes.length > 0;
                    }
                }, {
                    key: "enqueueUpdate",
                    value: function(e) {
                        null !== this._root && this._root.enqueueUpdate(e);
                    }
                }, {
                    key: "_empty",
                    value: function() {
                        while (this.childNodes.length > 0) {
                            var e = this.childNodes[0];
                            e.parentNode = null, B.delete(e.uid), this.childNodes.shift();
                        }
                    }
                }, {
                    key: "textContent",
                    set: function(e) {
                        this._empty(), "" === e ? this.enqueueUpdate({
                            path: "".concat(this._path, ".", "cn"),
                            value: function() {
                                return [];
                            }
                        }) : this.appendChild(Nn.createTextNode(e));
                    }
                }, {
                    key: "innerHTML",
                    get: function() {
                        return "";
                    },
                    set: function(e) {
                        ke(this, e);
                    }
                }, {
                    key: "findIndex",
                    value: function(e, t) {
                        var n = e.indexOf(t);
                        return Object(w["f"])(-1 !== n, "The node to be replaced is not a child of this node."), 
                        n;
                    }
                }, {
                    key: "cloneNode",
                    value: function() {
                        var e, t = arguments.length > 0 && void 0 !== arguments[0] && arguments[0], n = this.constructor;
                        for (var r in 1 === this.nodeType ? e = new n(this.nodeType, this.nodeName) : 3 === this.nodeType && (e = new n("")), 
                        this) {
                            var o = this[r];
                            [ "props", "dataset" ].includes(r) && "object" === Object(h["a"])(o) ? e[r] = Object.assign({}, o) : "_value" === r ? e[r] = o : "style" === r && (e.style._value = Object.assign({}, o._value), 
                            e.style._usedStyleProp = new Set(Array.from(o._usedStyleProp)));
                        }
                        return t && (e.childNodes = this.childNodes.map(function(e) {
                            return e.cloneNode(!0);
                        })), e;
                    }
                } ]), n;
            }(E), je = function(e) {
                Object(v["a"])(n, e);
                var t = Object(g["a"])(n);
                function n(e) {
                    var r;
                    return Object(y["a"])(this, n), r = t.call(this, 3, "#text"), r._value = e, r;
                }
                return Object(S["a"])(n, [ {
                    key: "textContent",
                    get: function() {
                        return this._value;
                    },
                    set: function(e) {
                        this._value = e, this.enqueueUpdate({
                            path: "".concat(this._path, ".", "v"),
                            value: e
                        });
                    }
                }, {
                    key: "nodeValue",
                    get: function() {
                        return this._value;
                    },
                    set: function(e) {
                        this.textContent = e;
                    }
                } ]), n;
            }(Oe), Te = [ "alignContent", "alignItems", "alignSelf", "alignmentAdjust", "alignmentBaseline", "all", "animation", "animationDelay", "animationDirection", "animationDuration", "animationFillMode", "animationIterationCount", "animationName", "animationPlayState", "animationTimingFunction", "appearance", "azimuth", "backfaceVisibility", "background", "backgroundAttachment", "backgroundBlendMode", "backgroundClip", "backgroundColor", "backgroundImage", "backgroundOrigin", "backgroundPosition", "backgroundRepeat", "backgroundSize", "baselineShift", "blockOverflow", "blockSize", "bookmarkLabel", "bookmarkLevel", "bookmarkState", "border", "borderBlock", "borderBlockColor", "borderBlockEnd", "borderBlockEndColor", "borderBlockEndStyle", "borderBlockEndWidth", "borderBlockStart", "borderBlockStartColor", "borderBlockStartStyle", "borderBlockStartWidth", "borderBlockStyle", "borderBlockWidth", "borderBottom", "borderBottomColor", "borderBottomFitLength", "borderBottomFitWidth", "borderBottomImage", "borderBottomLeftFitWidth", "borderBottomLeftImage", "borderBottomLeftRadius", "borderBottomRightFitLength", "borderBottomRightFitWidth", "borderBottomRightImage", "borderBottomRightRadius", "borderBottomStyle", "borderBottomWidth", "borderBottomlEftFitLength", "borderBoundary", "borderBreak", "borderCollapse", "borderColor", "borderCornerFit", "borderCornerImage", "borderCornerImageTransform", "borderEndEndRadius", "borderEndStartRadius", "borderFit", "borderFitLength", "borderFitWidth", "borderImage", "borderImageOutset", "borderImageRepeat", "borderImageSlice", "borderImageSource", "borderImageTransform", "borderImageWidth", "borderInline", "borderInlineColor", "borderInlineEnd", "borderInlineEndColor", "borderInlineEndStyle", "borderInlineEndWidth", "borderInlineStart", "borderInlineStartColor", "borderInlineStartStyle", "borderInlineStartWidth", "borderInlineStyle", "borderInlineWidth", "borderLeft", "borderLeftColor", "borderLeftFitLength", "borderLeftFitWidth", "borderLeftImage", "borderLeftStyle", "borderLeftWidth", "borderRadius", "borderRight", "borderRightColor", "borderRightFitLength", "borderRightFitWidth", "borderRightImage", "borderRightStyle", "borderRightWidth", "borderSpacing", "borderStartEndRadius", "borderStartStartRadius", "borderStyle", "borderTop", "borderTopColor", "borderTopFitLength", "borderTopFitWidth", "borderTopImage", "borderTopLeftFitLength", "borderTopLeftFitWidth", "borderTopLeftImage", "borderTopLeftRadius", "borderTopRightFitLength", "borderTopRightFitWidth", "borderTopRightImage", "borderTopRightRadius", "borderTopStyle", "borderTopWidth", "borderWidth", "bottom", "boxDecorationBreak", "boxShadow", "boxSizing", "boxSnap", "breakAfter", "breakBefore", "breakInside", "captionSide", "caret", "caretColor", "caretShape", "chains", "clear", "clip", "clipPath", "clipRule", "color", "colorAdjust", "colorInterpolationFilters", "colorScheme", "columnCount", "columnFill", "columnGap", "columnRule", "columnRuleColor", "columnRuleStyle", "columnRuleWidth", "columnSpan", "columnWidth", "columns", "contain", "content", "continue", "counterIncrement", "counterReset", "counterSet", "cue", "cueAfter", "cueBefore", "cursor", "direction", "display", "dominantBaseline", "dropInitialAfterAdjust", "dropInitialAfterAlign", "dropInitialBeforeAdjust", "dropInitialBeforeAlign", "dropInitialSize", "dropInitialValue", "elevation", "emptyCells", "filter", "flex", "flexBasis", "flexDirection", "flexFlow", "flexGrow", "flexShrink", "flexWrap", "float", "floodColor", "floodOpacity", "flow", "flowFrom", "flowInto", "font", "fontFamily", "fontFeatureSettings", "fontKerning", "fontLanguageOverride", "fontMaxSize", "fontMinSize", "fontOpticalSizing", "fontPalette", "fontSize", "fontSizeAdjust", "fontStretch", "fontStyle", "fontSynthesis", "fontSynthesisSmallCaps", "fontSynthesisStyle", "fontSynthesisWeight", "fontVariant", "fontVariantAlternates", "fontVariantCaps", "fontVariantEastAsian", "fontVariantEmoji", "fontVariantLigatures", "fontVariantNumeric", "fontVariantPosition", "fontVariationSettings", "fontWeight", "footnoteDisplay", "footnotePolicy", "forcedColorAdjust", "gap", "glyphOrientationVertical", "grid", "gridArea", "gridAutoColumns", "gridAutoFlow", "gridAutoRows", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "gridTemplate", "gridTemplateAreas", "gridTemplateColumns", "gridTemplateRows", "hangingPunctuation", "height", "hyphenateCharacter", "hyphenateLimitChars", "hyphenateLimitLast", "hyphenateLimitLines", "hyphenateLimitZone", "hyphens", "imageOrientation", "imageResolution", "initialLetters", "initialLettersAlign", "initialLettersWrap", "inlineBoxAlign", "inlineSize", "inlineSizing", "inset", "insetBlock", "insetBlockEnd", "insetBlockStart", "insetInline", "insetInlineEnd", "insetInlineStart", "isolation", "justifyContent", "justifyItems", "justifySelf", "left", "letterSpacing", "lightingColor", "lineBreak", "lineClamp", "lineGrid", "lineHeight", "linePadding", "lineSnap", "lineStacking", "lineStackingRuby", "lineStackingShift", "lineStackingStrategy", "listStyle", "listStyleImage", "listStylePosition", "listStyleType", "margin", "marginBlock", "marginBlockEnd", "marginBlockStart", "marginBottom", "marginInline", "marginInlineEnd", "marginInlineStart", "marginLeft", "marginRight", "marginTop", "marginTrim", "markerSide", "mask", "maskBorder", "maskBorderMode", "maskBorderOutset", "maskBorderRepeat", "maskBorderSlice", "maskBorderSource", "maskBorderWidth", "maskClip", "maskComposite", "maskImage", "maskMode", "maskOrigin", "maskPosition", "maskRepeat", "maskSize", "maskType", "maxBlockSize", "maxHeight", "maxInlineSize", "maxLines", "maxWidth", "minBlockSize", "minHeight", "minInlineSize", "minWidth", "mixBlendMode", "navDown", "navLeft", "navRight", "navUp", "objectFit", "objectPosition", "offset", "offsetAfter", "offsetAnchor", "offsetBefore", "offsetDistance", "offsetEnd", "offsetPath", "offsetPosition", "offsetRotate", "offsetStart", "opacity", "order", "orphans", "outline", "outlineColor", "outlineOffset", "outlineStyle", "outlineWidth", "overflow", "overflowBlock", "overflowInline", "overflowWrap", "overflowX", "overflowY", "padding", "paddingBlock", "paddingBlockEnd", "paddingBlockStart", "paddingBottom", "paddingInline", "paddingInlineEnd", "paddingInlineStart", "paddingLeft", "paddingRight", "paddingTop", "page", "pageBreakAfter", "pageBreakBefore", "pageBreakInside", "pause", "pauseAfter", "pauseBefore", "perspective", "perspectiveOrigin", "pitch", "pitchRange", "placeContent", "placeItems", "placeSelf", "playDuring", "pointerEvents", "position", "quotes", "regionFragment", "resize", "richness", "right", "rowGap", "rubyAlign", "rubyMerge", "rubyPosition", "running", "scrollBehavior", "scrollMargin", "scrollMarginBlock", "scrollMarginBlockEnd", "scrollMarginBlockStart", "scrollMarginBottom", "scrollMarginInline", "scrollMarginInlineEnd", "scrollMarginInlineStart", "scrollMarginLeft", "scrollMarginRight", "scrollMarginTop", "scrollPadding", "scrollPaddingBlock", "scrollPaddingBlockEnd", "scrollPaddingBlockStart", "scrollPaddingBottom", "scrollPaddingInline", "scrollPaddingInlineEnd", "scrollPaddingInlineStart", "scrollPaddingLeft", "scrollPaddingRight", "scrollPaddingTop", "scrollSnapAlign", "scrollSnapStop", "scrollSnapType", "shapeImageThreshold", "shapeInside", "shapeMargin", "shapeOutside", "speak", "speakHeader", "speakNumeral", "speakPunctuation", "speechRate", "stress", "stringSet", "tabSize", "tableLayout", "textAlign", "textAlignAll", "textAlignLast", "textCombineUpright", "textDecoration", "textDecorationColor", "textDecorationLine", "textDecorationStyle", "textEmphasis", "textEmphasisColor", "textEmphasisPosition", "textEmphasisStyle", "textGroupAlign", "textHeight", "textIndent", "textJustify", "textOrientation", "textOverflow", "textShadow", "textSpaceCollapse", "textSpaceTrim", "textSpacing", "textTransform", "textUnderlinePosition", "textWrap", "top", "transform", "transformBox", "transformOrigin", "transformStyle", "transition", "transitionDelay", "transitionDuration", "transitionProperty", "transitionTimingFunction", "unicodeBidi", "userSelect", "verticalAlign", "visibility", "voiceFamily", "volume", "whiteSpace", "widows", "width", "willChange", "wordBreak", "wordSpacing", "wordWrap", "wrapAfter", "wrapBefore", "wrapFlow", "wrapInside", "wrapThrough", "writingMode", "zIndex" ];
            function Pe(e, t) {
                var n = this[t];
                e && this._usedStyleProp.add(t), Object(w["w"])(Object(w["n"])(e) && e.length > L, "Style 属性 ".concat(t, " 的值数据量过大，可能会影响渲染性能，考虑使用 CSS 类或其它方案替代。")), 
                n !== e && (this._value[t] = e, this._element.enqueueUpdate({
                    path: "".concat(this._element._path, ".", "st"),
                    value: this.cssText
                }));
            }
            function Ee(e) {
                for (var t = {}, n = function(e) {
                    var n = Te[e];
                    t[n] = {
                        get: function() {
                            return this._value[n] || "";
                        },
                        set: function(e) {
                            Pe.call(this, e, n);
                        }
                    };
                }, r = 0; r < Te.length; r++) n(r);
                Object.defineProperties(e.prototype, t);
            }
            function Be(e) {
                return /^--/.test(e);
            }
            var Ae = function() {
                function e(t) {
                    Object(y["a"])(this, e), this._element = t, this._usedStyleProp = new Set(), this._value = {};
                }
                return Object(S["a"])(e, [ {
                    key: "setCssVariables",
                    value: function(e) {
                        var t = this;
                        this.hasOwnProperty(e) || Object.defineProperty(this, e, {
                            enumerable: !0,
                            configurable: !0,
                            get: function() {
                                return t._value[e] || "";
                            },
                            set: function(n) {
                                Pe.call(t, n, e);
                            }
                        });
                    }
                }, {
                    key: "cssText",
                    get: function() {
                        var e = this, t = "";
                        return this._usedStyleProp.forEach(function(n) {
                            var r = e[n];
                            if (r) {
                                var o = Be(n) ? n : Object(w["v"])(n);
                                t += "".concat(o, ": ").concat(r, ";");
                            }
                        }), t;
                    },
                    set: function(e) {
                        var t = this;
                        if (null == e && (e = ""), this._usedStyleProp.forEach(function(e) {
                            t.removeProperty(e);
                        }), "" !== e) for (var n = e.split(";"), r = 0; r < n.length; r++) {
                            var o = n[r].trim();
                            if ("" !== o) {
                                var i = o.split(":"), a = Object(f["a"])(i), c = a[0], s = a.slice(1), u = s.join(":");
                                Object(w["o"])(u) || this.setProperty(c.trim(), u.trim());
                            }
                        }
                    }
                }, {
                    key: "setProperty",
                    value: function(e, t) {
                        "-" === e[0] ? this.setCssVariables(e) : e = Object(w["u"])(e), Object(w["o"])(t) || (null === t || "" === t ? this.removeProperty(e) : this[e] = t);
                    }
                }, {
                    key: "removeProperty",
                    value: function(e) {
                        if (e = Object(w["u"])(e), !this._usedStyleProp.has(e)) return "";
                        var t = this[e];
                        return this[e] = "", this._usedStyleProp.delete(e), t;
                    }
                }, {
                    key: "getPropertyValue",
                    value: function(e) {
                        e = Object(w["u"])(e);
                        var t = this[e];
                        return t || "";
                    }
                } ]), e;
            }();
            function xe() {
                return !0;
            }
            function Ie(e, t) {
                var n = [], r = null !== t && void 0 !== t ? t : xe, o = e;
                while (o) 1 === o.nodeType && r(o) && n.push(o), o = _e(o, e);
                return n;
            }
            function _e(e, t) {
                var n = e.firstChild;
                if (n) return n;
                var r = e;
                do {
                    if (r === t) return null;
                    var o = r.nextSibling;
                    if (o) return o;
                    r = r.parentElement;
                } while (r);
                return null;
            }
            Ee(Ae);
            var Le = function(e) {
                Object(v["a"])(n, e);
                var t = Object(g["a"])(n);
                function n(e, r) {
                    var o, i;
                    return Object(y["a"])(this, n), i = t.call(this), e.trim().split(/\s+/).forEach(Object(u["a"])((o = Object(p["a"])(i), 
                    Object(l["a"])(n.prototype)), "add", o).bind(Object(p["a"])(i))), i.el = r, i;
                }
                return Object(S["a"])(n, [ {
                    key: "value",
                    get: function() {
                        return Object(s["a"])(this).join(" ");
                    }
                }, {
                    key: "add",
                    value: function(e) {
                        return Object(u["a"])(Object(l["a"])(n.prototype), "add", this).call(this, e), this._update(), 
                        this;
                    }
                }, {
                    key: "remove",
                    value: function(e) {
                        Object(u["a"])(Object(l["a"])(n.prototype), "delete", this).call(this, e), this._update();
                    }
                }, {
                    key: "toggle",
                    value: function(e) {
                        Object(u["a"])(Object(l["a"])(n.prototype), "has", this).call(this, e) ? Object(u["a"])(Object(l["a"])(n.prototype), "delete", this).call(this, e) : Object(u["a"])(Object(l["a"])(n.prototype), "add", this).call(this, e), 
                        this._update();
                    }
                }, {
                    key: "replace",
                    value: function(e, t) {
                        Object(u["a"])(Object(l["a"])(n.prototype), "delete", this).call(this, e), Object(u["a"])(Object(l["a"])(n.prototype), "add", this).call(this, t), 
                        this._update();
                    }
                }, {
                    key: "contains",
                    value: function(e) {
                        return Object(u["a"])(Object(l["a"])(n.prototype), "has", this).call(this, e);
                    }
                }, {
                    key: "toString",
                    value: function() {
                        return this.value;
                    }
                }, {
                    key: "_update",
                    value: function() {
                        this.el.className = this.value;
                    }
                } ]), n;
            }(Object(d["a"])(Set)), Re = function(e) {
                Object(v["a"])(n, e);
                var t = Object(g["a"])(n);
                function n(e, r) {
                    var o, i;
                    return Object(y["a"])(this, n), o = t.call(this, e || 1, r), o.props = {}, o.dataset = w["b"], 
                    o.tagName = r.toUpperCase(), o.style = new Ae(Object(p["a"])(o)), null === (i = k.onTaroElementCreate) || void 0 === i || i.call(k, o.tagName, e), 
                    o;
                }
                return Object(S["a"])(n, [ {
                    key: "id",
                    get: function() {
                        return this.getAttribute("id");
                    },
                    set: function(e) {
                        this.setAttribute("id", e);
                    }
                }, {
                    key: "classList",
                    get: function() {
                        return new Le(this.className, this);
                    }
                }, {
                    key: "className",
                    get: function() {
                        return this.getAttribute("class") || "";
                    },
                    set: function(e) {
                        this.setAttribute("class", e);
                    }
                }, {
                    key: "cssText",
                    get: function() {
                        return this.getAttribute("style") || "";
                    }
                }, {
                    key: "children",
                    get: function() {
                        return this.childNodes.filter(O);
                    }
                }, {
                    key: "hasAttribute",
                    value: function(e) {
                        return !Object(w["o"])(this.props[e]);
                    }
                }, {
                    key: "hasAttributes",
                    value: function() {
                        return this.attributes.length > 0;
                    }
                }, {
                    key: "focus",
                    value: function() {
                        this.setAttribute("focus", !0);
                    }
                }, {
                    key: "blur",
                    value: function() {
                        this.setAttribute("focus", !1);
                    }
                }, {
                    key: "setAttribute",
                    value: function(e, t) {
                        var n;
                        Object(w["w"])(Object(w["n"])(t) && t.length > L, "元素 ".concat(this.nodeName, " 的 属性 ").concat(e, " 的值数据量过大，可能会影响渲染性能。考虑降低图片转为 base64 的阈值或在 CSS 中使用 base64。")), 
                        "style" === e ? (this.style.cssText = t, e = "st") : "id" === e ? (B.delete(this.uid), 
                        t = String(t), this.props[e] = this.uid = t, B.set(t, this), e = "uid") : ("view" !== this.nodeName || T(this) || /class|style|id/.test(e) || this.isAnyEventBinded() || this.enqueueUpdate({
                            path: "".concat(this._path, ".", "nn"),
                            value: "static-view"
                        }), this.props[e] = t, "class" === e ? e = "cl" : e.startsWith("data-") && (this.dataset === w["b"] && (this.dataset = Object.create(null)), 
                        this.dataset[Object(w["u"])(e.replace(/^data-/, ""))] = t)), null === (n = k.setAttribute) || void 0 === n || n.call(k, this, e, t), 
                        this.enqueueUpdate({
                            path: "".concat(this._path, ".").concat(Object(w["u"])(e)),
                            value: t
                        });
                    }
                }, {
                    key: "removeAttribute",
                    value: function(e) {
                        var t;
                        "style" === e ? this.style.cssText = "" : (delete this.props[e], "class" === e && (e = "cl")), 
                        null === (t = k.removeAttribute) || void 0 === t || t.call(k, this, e), this.enqueueUpdate({
                            path: "".concat(this._path, ".").concat(Object(w["u"])(e)),
                            value: ""
                        }), "view" !== this.nodeName || T(this) || this.isAnyEventBinded() || this.enqueueUpdate({
                            path: "".concat(this._path, ".", "nn"),
                            value: "pure-view"
                        });
                    }
                }, {
                    key: "getAttribute",
                    value: function(e) {
                        var t = "style" === e ? this.style.cssText : this.props[e];
                        return null !== t && void 0 !== t ? t : "";
                    }
                }, {
                    key: "attributes",
                    get: function() {
                        var e = this, t = Object.keys(this.props), n = this.style.cssText, r = t.map(function(t) {
                            return {
                                name: t,
                                value: e.props[t]
                            };
                        });
                        return r.concat(n ? {
                            name: "style",
                            value: n
                        } : []);
                    }
                }, {
                    key: "getElementsByTagName",
                    value: function(e) {
                        var t = this;
                        return Ie(this, function(n) {
                            return n.nodeName === e || "*" === e && t !== n;
                        });
                    }
                }, {
                    key: "getElementsByClassName",
                    value: function(e) {
                        return Ie(this, function(t) {
                            var n = t.classList, r = e.trim().split(/\s+/);
                            return r.every(function(e) {
                                return n.has(e);
                            });
                        });
                    }
                }, {
                    key: "dispatchEvent",
                    value: function(e) {
                        var t = e.cancelable;
                        Object(w["k"])(k.modifyDispatchEvent) && k.modifyDispatchEvent(e, this.tagName);
                        var n = this.__handlers[e.type];
                        if (Object(w["i"])(n)) {
                            for (var r = n.length; r--; ) {
                                var o = n[r], i = void 0;
                                if (o._stop ? o._stop = !1 : i = o.call(this, e), (!1 === i || e._end) && t && (e.defaultPrevented = !0), 
                                e._end && e._stop) break;
                            }
                            return e._stop ? this._stopPropagation(e) : e._stop = !0, null != n;
                        }
                    }
                }, {
                    key: "textContent",
                    get: function() {
                        for (var e = "", t = 0; t < this.childNodes.length; t++) {
                            var n = this.childNodes[t];
                            e += n.textContent;
                        }
                        return e;
                    },
                    set: function(e) {
                        Object(c["a"])(Object(l["a"])(n.prototype), "textContent", e, this, !0);
                    }
                }, {
                    key: "_stopPropagation",
                    value: function(e) {
                        var t = this;
                        while (t = t.parentNode) {
                            var n = t.__handlers[e.type];
                            if (Object(w["i"])(n)) for (var r = n.length; r--; ) {
                                var o = n[r];
                                o._stop = !0;
                            }
                        }
                    }
                }, {
                    key: "addEventListener",
                    value: function(e, t, r) {
                        var o = this.nodeName;
                        !this.isAnyEventBinded() && N.indexOf(o) > -1 && this.enqueueUpdate({
                            path: "".concat(this._path, ".", "nn"),
                            value: o
                        }), Object(u["a"])(Object(l["a"])(n.prototype), "addEventListener", this).call(this, e, t, r);
                    }
                }, {
                    key: "removeEventListener",
                    value: function(e, t) {
                        Object(u["a"])(Object(l["a"])(n.prototype), "removeEventListener", this).call(this, e, t);
                        var r = this.nodeName;
                        !this.isAnyEventBinded() && N.indexOf(r) > -1 && this.enqueueUpdate({
                            path: "".concat(this._path, ".", "nn"),
                            value: T(this) ? "static-".concat(r) : "pure-".concat(r)
                        });
                    }
                } ]), n;
            }(Oe), De = function(e) {
                Object(v["a"])(n, e);
                var t = Object(g["a"])(n);
                function n() {
                    return Object(y["a"])(this, n), t.apply(this, arguments);
                }
                return Object(S["a"])(n, [ {
                    key: "value",
                    get: function() {
                        var e = this.props["value"];
                        return null == e ? "" : e;
                    },
                    set: function(e) {
                        this.setAttribute("value", e);
                    }
                }, {
                    key: "dispatchEvent",
                    value: function(e) {
                        if (("input" === e.type || "change" === e.type) && e.mpEvent) {
                            var t = e.mpEvent.detail.value;
                            this.props.value = t;
                        }
                        return Object(u["a"])(Object(l["a"])(n.prototype), "dispatchEvent", this).call(this, e);
                    }
                } ]), n;
            }(Re), Ne = Array.isArray, Me = "object" == ("undefined" === typeof e ? "undefined" : Object(h["a"])(e)) && e && e.Object === Object && e, Fe = "object" == ("undefined" === typeof self ? "undefined" : Object(h["a"])(self)) && self && self.Object === Object && self, We = Me || Fe || Function("return this")(), Ve = We.Symbol, Ue = Object.prototype, qe = Ue.hasOwnProperty, ze = Ue.toString, He = Ve ? Ve.toStringTag : void 0;
            function $e(e) {
                var t = qe.call(e, He), n = e[He];
                try {
                    e[He] = void 0;
                    var r = !0;
                } catch (e) {}
                var o = ze.call(e);
                return r && (t ? e[He] = n : delete e[He]), o;
            }
            var Ge = Object.prototype, Qe = Ge.toString;
            function Ke(e) {
                return Qe.call(e);
            }
            var Je = "[object Null]", Ye = "[object Undefined]", Xe = Ve ? Ve.toStringTag : void 0;
            function Ze(e) {
                return null == e ? void 0 === e ? Ye : Je : Xe && Xe in Object(e) ? $e(e) : Ke(e);
            }
            function et(e) {
                return null != e && "object" == Object(h["a"])(e);
            }
            var tt = "[object Symbol]";
            function nt(e) {
                return "symbol" == Object(h["a"])(e) || et(e) && Ze(e) == tt;
            }
            var rt = /\.|\[(?:[^[\]]*|(["'])(?:(?!\1)[^\\]|\\.)*?\1)\]/, ot = /^\w*$/;
            function it(e, t) {
                if (Ne(e)) return !1;
                var n = Object(h["a"])(e);
                return !("number" != n && "symbol" != n && "boolean" != n && null != e && !nt(e)) || (ot.test(e) || !rt.test(e) || null != t && e in Object(t));
            }
            function at(e) {
                var t = Object(h["a"])(e);
                return null != e && ("object" == t || "function" == t);
            }
            var ct = "[object AsyncFunction]", st = "[object Function]", ut = "[object GeneratorFunction]", lt = "[object Proxy]";
            function dt(e) {
                if (!at(e)) return !1;
                var t = Ze(e);
                return t == st || t == ut || t == ct || t == lt;
            }
            var ft = We["__core-js_shared__"], ht = function() {
                var e = /[^.]+$/.exec(ft && ft.keys && ft.keys.IE_PROTO || "");
                return e ? "Symbol(src)_1." + e : "";
            }();
            function pt(e) {
                return !!ht && ht in e;
            }
            var vt = Function.prototype, gt = vt.toString;
            function bt(e) {
                if (null != e) {
                    try {
                        return gt.call(e);
                    } catch (e) {}
                    try {
                        return e + "";
                    } catch (e) {}
                }
                return "";
            }
            var mt = /[\\^$.*+?()[\]{}|]/g, yt = /^\[object .+?Constructor\]$/, St = Function.prototype, wt = Object.prototype, kt = St.toString, Ct = wt.hasOwnProperty, Ot = RegExp("^" + kt.call(Ct).replace(mt, "\\$&").replace(/hasOwnProperty|(function).*?(?=\\\()| for .+?(?=\\\])/g, "$1.*?") + "$");
            function jt(e) {
                if (!at(e) || pt(e)) return !1;
                var t = dt(e) ? Ot : yt;
                return t.test(bt(e));
            }
            function Tt(e, t) {
                return null == e ? void 0 : e[t];
            }
            function Pt(e, t) {
                var n = Tt(e, t);
                return jt(n) ? n : void 0;
            }
            var Et = Pt(Object, "create");
            function Bt() {
                this.__data__ = Et ? Et(null) : {}, this.size = 0;
            }
            function At(e) {
                var t = this.has(e) && delete this.__data__[e];
                return this.size -= t ? 1 : 0, t;
            }
            var xt = "__lodash_hash_undefined__", It = Object.prototype, _t = It.hasOwnProperty;
            function Lt(e) {
                var t = this.__data__;
                if (Et) {
                    var n = t[e];
                    return n === xt ? void 0 : n;
                }
                return _t.call(t, e) ? t[e] : void 0;
            }
            var Rt = Object.prototype, Dt = Rt.hasOwnProperty;
            function Nt(e) {
                var t = this.__data__;
                return Et ? void 0 !== t[e] : Dt.call(t, e);
            }
            var Mt = "__lodash_hash_undefined__";
            function Ft(e, t) {
                var n = this.__data__;
                return this.size += this.has(e) ? 0 : 1, n[e] = Et && void 0 === t ? Mt : t, this;
            }
            function Wt(e) {
                var t = -1, n = null == e ? 0 : e.length;
                this.clear();
                while (++t < n) {
                    var r = e[t];
                    this.set(r[0], r[1]);
                }
            }
            function Vt() {
                this.__data__ = [], this.size = 0;
            }
            function Ut(e, t) {
                return e === t || e !== e && t !== t;
            }
            function qt(e, t) {
                var n = e.length;
                while (n--) if (Ut(e[n][0], t)) return n;
                return -1;
            }
            Wt.prototype.clear = Bt, Wt.prototype["delete"] = At, Wt.prototype.get = Lt, Wt.prototype.has = Nt, 
            Wt.prototype.set = Ft;
            var zt = Array.prototype, Ht = zt.splice;
            function $t(e) {
                var t = this.__data__, n = qt(t, e);
                if (n < 0) return !1;
                var r = t.length - 1;
                return n == r ? t.pop() : Ht.call(t, n, 1), --this.size, !0;
            }
            function Gt(e) {
                var t = this.__data__, n = qt(t, e);
                return n < 0 ? void 0 : t[n][1];
            }
            function Qt(e) {
                return qt(this.__data__, e) > -1;
            }
            function Kt(e, t) {
                var n = this.__data__, r = qt(n, e);
                return r < 0 ? (++this.size, n.push([ e, t ])) : n[r][1] = t, this;
            }
            function Jt(e) {
                var t = -1, n = null == e ? 0 : e.length;
                this.clear();
                while (++t < n) {
                    var r = e[t];
                    this.set(r[0], r[1]);
                }
            }
            Jt.prototype.clear = Vt, Jt.prototype["delete"] = $t, Jt.prototype.get = Gt, Jt.prototype.has = Qt, 
            Jt.prototype.set = Kt;
            var Yt = Pt(We, "Map");
            function Xt() {
                this.size = 0, this.__data__ = {
                    hash: new Wt(),
                    map: new (Yt || Jt)(),
                    string: new Wt()
                };
            }
            function Zt(e) {
                var t = Object(h["a"])(e);
                return "string" == t || "number" == t || "symbol" == t || "boolean" == t ? "__proto__" !== e : null === e;
            }
            function en(e, t) {
                var n = e.__data__;
                return Zt(t) ? n["string" == typeof t ? "string" : "hash"] : n.map;
            }
            function tn(e) {
                var t = en(this, e)["delete"](e);
                return this.size -= t ? 1 : 0, t;
            }
            function nn(e) {
                return en(this, e).get(e);
            }
            function rn(e) {
                return en(this, e).has(e);
            }
            function on(e, t) {
                var n = en(this, e), r = n.size;
                return n.set(e, t), this.size += n.size == r ? 0 : 1, this;
            }
            function an(e) {
                var t = -1, n = null == e ? 0 : e.length;
                this.clear();
                while (++t < n) {
                    var r = e[t];
                    this.set(r[0], r[1]);
                }
            }
            an.prototype.clear = Xt, an.prototype["delete"] = tn, an.prototype.get = nn, an.prototype.has = rn, 
            an.prototype.set = on;
            var cn = "Expected a function";
            function sn(e, t) {
                if ("function" != typeof e || null != t && "function" != typeof t) throw new TypeError(cn);
                var n = function n() {
                    var r = arguments, o = t ? t.apply(this, r) : r[0], i = n.cache;
                    if (i.has(o)) return i.get(o);
                    var a = e.apply(this, r);
                    return n.cache = i.set(o, a) || i, a;
                };
                return n.cache = new (sn.Cache || an)(), n;
            }
            sn.Cache = an;
            var un = 500;
            function ln(e) {
                var t = sn(e, function(e) {
                    return n.size === un && n.clear(), e;
                }), n = t.cache;
                return t;
            }
            var dn = /[^.[\]]+|\[(?:(-?\d+(?:\.\d+)?)|(["'])((?:(?!\2)[^\\]|\\.)*?)\2)\]|(?=(?:\.|\[\])(?:\.|\[\]|$))/g, fn = /\\(\\)?/g, hn = ln(function(e) {
                var t = [];
                return 46 === e.charCodeAt(0) && t.push(""), e.replace(dn, function(e, n, r, o) {
                    t.push(r ? o.replace(fn, "$1") : n || e);
                }), t;
            });
            function pn(e, t) {
                var n = -1, r = null == e ? 0 : e.length, o = Array(r);
                while (++n < r) o[n] = t(e[n], n, e);
                return o;
            }
            var vn = 1 / 0, gn = Ve ? Ve.prototype : void 0, bn = gn ? gn.toString : void 0;
            function mn(e) {
                if ("string" == typeof e) return e;
                if (Ne(e)) return pn(e, mn) + "";
                if (nt(e)) return bn ? bn.call(e) : "";
                var t = e + "";
                return "0" == t && 1 / e == -vn ? "-0" : t;
            }
            function yn(e) {
                return null == e ? "" : mn(e);
            }
            function Sn(e, t) {
                return Ne(e) ? e : it(e, t) ? [ e ] : hn(yn(e));
            }
            var wn = 1 / 0;
            function kn(e) {
                if ("string" == typeof e || nt(e)) return e;
                var t = e + "";
                return "0" == t && 1 / e == -wn ? "-0" : t;
            }
            function Cn(e, t) {
                t = Sn(t, e);
                var n = 0, r = t.length;
                while (null != e && n < r) e = e[kn(t[n++])];
                return n && n == r ? e : void 0;
            }
            function On(e, t, n) {
                var r = null == e ? void 0 : Cn(e, t);
                return void 0 === r ? n : r;
            }
            var jn = function() {
                function e() {
                    Object(y["a"])(this, e), this.recorder = new Map();
                }
                return Object(S["a"])(e, [ {
                    key: "start",
                    value: function(e) {
                        F.debug && this.recorder.set(e, Date.now());
                    }
                }, {
                    key: "stop",
                    value: function(e) {
                        if (F.debug) {
                            var t = Date.now(), n = this.recorder.get(e), r = t - n;
                            console.log("".concat(e, " 时长： ").concat(r, "ms"));
                        }
                    }
                } ]), e;
            }(), Tn = new jn(), Pn = function() {
                function e(t) {
                    Object(y["a"])(this, e), "undefined" !== typeof t && t.callbacks ? this.callbacks = t.callbacks : this.callbacks = {};
                }
                return Object(S["a"])(e, [ {
                    key: "on",
                    value: function(t, n, r) {
                        var o, i, a, c;
                        if (!n) return this;
                        t = t.split(e.eventSplitter), this.callbacks || (this.callbacks = {});
                        var s = this.callbacks;
                        while (o = t.shift()) c = s[o], i = c ? c.tail : {}, i.next = a = {}, i.context = r, 
                        i.callback = n, s[o] = {
                            tail: a,
                            next: c ? c.next : i
                        };
                        return this;
                    }
                }, {
                    key: "once",
                    value: function(e, t, n) {
                        var r = this, o = function o() {
                            for (var i = arguments.length, a = new Array(i), c = 0; c < i; c++) a[c] = arguments[c];
                            t.apply(r, a), r.off(e, o, n);
                        };
                        return this.on(e, o, n), this;
                    }
                }, {
                    key: "off",
                    value: function(t, n, r) {
                        var o, i, a, c, s, u;
                        if (!(i = this.callbacks)) return this;
                        if (!(t || n || r)) return delete this.callbacks, this;
                        t = t ? t.split(e.eventSplitter) : Object.keys(i);
                        while (o = t.shift()) if (a = i[o], delete i[o], a && (n || r)) {
                            c = a.tail;
                            while ((a = a.next) !== c) s = a.callback, u = a.context, (n && s !== n || r && u !== r) && this.on(o, s, u);
                        }
                        return this;
                    }
                }, {
                    key: "trigger",
                    value: function(t) {
                        var n, r, o, i;
                        if (!(o = this.callbacks)) return this;
                        t = t.split(e.eventSplitter);
                        var a = [].slice.call(arguments, 1);
                        while (n = t.shift()) if (r = o[n]) {
                            i = r.tail;
                            while ((r = r.next) !== i) r.callback.apply(r.context || this, a);
                        }
                        return this;
                    }
                } ]), e;
            }();
            Pn.eventSplitter = /\s+/;
            var En = k.getEventCenter(Pn), Bn = C(), An = function(e) {
                Object(v["a"])(n, e);
                var t = Object(g["a"])(n);
                function n() {
                    var e;
                    return Object(y["a"])(this, n), e = t.call(this, 1, "root"), e.pendingUpdate = !1, 
                    e.updatePayloads = [], e.pendingFlush = !1, e.updateCallbacks = [], e.ctx = null, 
                    e;
                }
                return Object(S["a"])(n, [ {
                    key: "_path",
                    get: function() {
                        return "root";
                    }
                }, {
                    key: "_root",
                    get: function() {
                        return this;
                    }
                }, {
                    key: "enqueueUpdate",
                    value: function(e) {
                        this.updatePayloads.push(e), this.pendingUpdate || null === this.ctx || this.performUpdate();
                    }
                }, {
                    key: "performUpdate",
                    value: function() {
                        var e = this, t = arguments.length > 0 && void 0 !== arguments[0] && arguments[0], n = arguments.length > 1 ? arguments[1] : void 0;
                        this.pendingUpdate = !0;
                        var r = this.ctx;
                        setTimeout(function() {
                            var o, i;
                            Tn.start(R);
                            var a = Object.create(null), c = new Set(t ? [ "root.cn.[0]", "root.cn[0]" ] : []);
                            while (e.updatePayloads.length > 0) {
                                var s = e.updatePayloads.shift(), u = s.path, l = s.value;
                                u.endsWith("cn") && c.add(u), a[u] = l;
                            }
                            var d = function(e) {
                                c.forEach(function(t) {
                                    e.includes(t) && e !== t && delete a[e];
                                });
                                var t = a[e];
                                Object(w["k"])(t) && (a[e] = t());
                            };
                            for (var f in a) d(f);
                            if (null === (o = k.prepareUpdateData) || void 0 === o || o.call(k, a, e), t && (null === (i = k.appendInitialPage) || void 0 === i || i.call(k, a, e)), 
                            Object(w["k"])(n)) n(a); else {
                                e.pendingUpdate = !1;
                                var h = [], p = {};
                                if (!t) for (var v in a) {
                                    for (var g = v.split("."), b = !1, y = g.length; y > 0; y--) {
                                        var S = g.slice(0, y).join("."), C = On(r.__data__ || r.data, S);
                                        if (C && C.nn && "custom-wrapper" === C.nn) {
                                            var O = C.uid, j = r.selectComponent("#".concat(O)), T = g.slice(y).join(".");
                                            j && (b = !0, h.push({
                                                ctx: r.selectComponent("#".concat(O)),
                                                data: Object(m["a"])({}, "i.".concat(T), a[v])
                                            }));
                                            break;
                                        }
                                    }
                                    b || (p[v] = a[v]);
                                }
                                var P = h.length;
                                if (P) {
                                    var E = "".concat(e._path, "_update_").concat(Bn()), B = 0;
                                    En.once(E, function() {
                                        B++, B === P + 1 && (Tn.stop(R), e.pendingFlush || e.flushUpdateCallback(), t && Tn.stop(D));
                                    }, En), h.forEach(function(e) {
                                        e.ctx.setData(e.data, function() {
                                            En.trigger(E);
                                        });
                                    }), Object.keys(p).length && r.setData(p, function() {
                                        En.trigger(E);
                                    });
                                } else r.setData(a, function() {
                                    Tn.stop(R), e.pendingFlush || e.flushUpdateCallback(), t && Tn.stop(D);
                                });
                            }
                        }, 0);
                    }
                }, {
                    key: "enqueueUpdateCallback",
                    value: function(e, t) {
                        this.updateCallbacks.push(function() {
                            t ? e.call(t) : e();
                        });
                    }
                }, {
                    key: "flushUpdateCallback",
                    value: function() {
                        this.pendingFlush = !1;
                        var e = this.updateCallbacks.slice(0);
                        this.updateCallbacks.length = 0;
                        for (var t = 0; t < e.length; t++) e[t]();
                    }
                } ]), n;
            }(Re), xn = "undefined" !== typeof r && !!r.scripts, In = xn ? r : w["b"], _n = xn ? o : w["b"], Ln = function(e) {
                Object(v["a"])(n, e);
                var t = Object(g["a"])(n);
                function n() {
                    return Object(y["a"])(this, n), t.call(this, 9, "#document");
                }
                return Object(S["a"])(n, [ {
                    key: "createElement",
                    value: function(e) {
                        return "root" === e ? new An() : w["d"].has(e) ? new De(1, e) : new Re(1, e);
                    }
                }, {
                    key: "createElementNS",
                    value: function(e, t) {
                        return this.createElement(t);
                    }
                }, {
                    key: "createTextNode",
                    value: function(e) {
                        return new je(e);
                    }
                }, {
                    key: "getElementById",
                    value: function(e) {
                        var t = B.get(e);
                        return Object(w["o"])(t) ? null : t;
                    }
                }, {
                    key: "getElementsByTagName",
                    value: function(e) {
                        var t = this, n = [];
                        return B.forEach(function(r) {
                            1 === r.nodeType && (r.nodeName === e || "*" === e && r !== t) && n.push(r);
                        }), n;
                    }
                }, {
                    key: "querySelector",
                    value: function(e) {
                        return /^#/.test(e) ? this.getElementById(e.slice(1)) : null;
                    }
                }, {
                    key: "createComment",
                    value: function() {
                        return new je("");
                    }
                } ]), n;
            }(Re);
            function Rn() {
                var e = new Ln();
                e.appendChild(e.documentElement = e.createElement("html")), e.documentElement.appendChild(e.head = e.createElement("head"));
                var t = e.createElement("body");
                e.documentElement.appendChild(t), e.body = t;
                var n = e.createElement("app");
                n.id = "app";
                var r = e.createElement("container");
                return r.appendChild(n), e.documentElement.lastChild.appendChild(r), e.createEvent = x, 
                e;
            }
            var Dn, Nn = xn ? In : Rn(), Mn = "Macintosh", Fn = "Intel Mac OS X 10_14_5", Wn = "AppleWebKit/534.36 (KHTML, like Gecko) NodeJS/v4.1.0 Chrome/76.0.3809.132 Safari/534.36", Vn = xn ? _n.navigator : {
                appCodeName: "Mozilla",
                appName: "Netscape",
                appVersion: "5.0 (" + Mn + "; " + Fn + ") " + Wn,
                cookieEnabled: !0,
                mimeTypes: [],
                onLine: !0,
                platform: "MacIntel",
                plugins: [],
                product: "Taro",
                productSub: "20030107",
                userAgent: "Mozilla/5.0 (" + Mn + "; " + Fn + ") " + Wn,
                vendor: "Joyent",
                vendorSub: ""
            };
            (function() {
                var e;
                "undefined" !== typeof performance && null !== performance && performance.now ? Dn = function() {
                    return performance.now();
                } : Date.now ? (Dn = function() {
                    return Date.now() - e;
                }, e = Date.now()) : (Dn = function() {
                    return new Date().getTime() - e;
                }, e = new Date().getTime());
            })();
            var Un = 0, qn = "undefined" !== typeof i && null !== i ? i : function(e) {
                var t = Dn(), n = Math.max(Un + 16, t);
                return setTimeout(function() {
                    e(Un = n);
                }, n - t);
            }, zn = "undefined" !== typeof a && null !== a ? a : clearTimeout;
            function Hn(e) {
                return new Ae(e);
            }
            "undefined" !== typeof e && (qn = qn.bind(e), zn = zn.bind(e));
            var $n = xn ? _n : {
                navigator: Vn,
                document: Nn
            };
            if (!xn) {
                var Gn = [].concat(Object(s["a"])(Object.getOwnPropertyNames(e || _n)), Object(s["a"])(Object.getOwnPropertySymbols(e || _n)));
                Gn.forEach(function(t) {
                    Object.prototype.hasOwnProperty.call($n, t) || ($n[t] = e[t]);
                });
            }
            $n.requestAnimationFrame = qn, $n.cancelAnimationFrame = zn, $n.getComputedStyle = Hn, 
            "Date" in $n || ($n.Date = Date), "setTimeout" in $n || ($n.setTimeout = setTimeout);
            var Qn = {
                app: null,
                router: null,
                page: null
            }, Kn = function() {
                return Qn;
            }, Jn = new Map();
            function Yn(e, t) {
                var n;
                null === (n = k.mergePageInstance) || void 0 === n || n.call(k, Jn.get(t), e), Jn.set(t, e);
            }
            function Xn(e) {
                return Jn.get(e);
            }
            function Zn(e) {
                return null == e ? "" : "/" === e.charAt(0) ? e : "/" + e;
            }
            var er = C();
            function tr(e, t) {
                for (var n = arguments.length, r = new Array(n > 2 ? n - 2 : 0), o = 2; o < n; o++) r[o - 2] = arguments[o];
                var i = Jn.get(e);
                if (null != i) {
                    var a = k.getLifecyle(i, t);
                    if (Object(w["i"])(a)) {
                        var c = a.map(function(e) {
                            return e.apply(i, r);
                        });
                        return c[0];
                    }
                    if (Object(w["k"])(a)) return a.apply(i, r);
                }
            }
            function nr(e) {
                if (null == e) return "";
                var t = Object.keys(e).map(function(t) {
                    return t + "=" + e[t];
                }).join("&");
                return "" === t ? t : "?" + t;
            }
            function rr(e, t) {
                var n = e;
                return xn || (n = e + nr(t)), n;
            }
            function or(e) {
                return e + ".onReady";
            }
            function ir(e) {
                return e + ".onShow";
            }
            function ar(e) {
                return e + ".onHide";
            }
            function cr(e, t, n, r) {
                var o, i, a = null !== t && void 0 !== t ? t : "taro_page_".concat(er()), c = null, s = !1, u = [], l = {
                    onLoad: function(t, n) {
                        var o = this;
                        Tn.start(D), Qn.page = this, this.config = r || {}, null == this.options && (this.options = t), 
                        this.options.$taroTimestamp = Date.now();
                        var i = rr(a, this.options), l = xn ? i : this.route || this.__route__;
                        Qn.router = {
                            params: this.options,
                            path: Zn(l),
                            onReady: or(a),
                            onShow: ir(a),
                            onHide: ar(a)
                        };
                        var d = function() {
                            Qn.app.mount(e, i, function() {
                                c = Nn.getElementById(i), Object(w["f"])(null !== c, "没有找到页面实例。"), tr(i, "onLoad", o.options), 
                                xn || (c.ctx = o, c.performUpdate(!0, n));
                            });
                        };
                        s ? u.push(d) : d();
                    },
                    onReady: function() {
                        var e = rr(a, this.options);
                        qn(function() {
                            En.trigger(or(a));
                        }), tr(e, "onReady"), this.onReady.called = !0;
                    },
                    onUnload: function() {
                        var e = rr(a, this.options);
                        s = !0, Qn.app.unmount(e, function() {
                            s = !1, Jn.delete(e), c && (c.ctx = null), u.length && (u.forEach(function(e) {
                                return e();
                            }), u = []);
                        });
                    },
                    onShow: function() {
                        Qn.page = this, this.config = r || {};
                        var e = rr(a, this.options), t = xn ? e : this.route || this.__route__;
                        Qn.router = {
                            params: this.options,
                            path: Zn(t),
                            onReady: or(a),
                            onShow: ir(a),
                            onHide: ar(a)
                        }, qn(function() {
                            En.trigger(ir(a));
                        }), tr(e, "onShow");
                    },
                    onHide: function() {
                        Qn.page = null, Qn.router = null;
                        var e = rr(a, this.options);
                        tr(e, "onHide"), En.trigger(ar(a));
                    },
                    onPullDownRefresh: function() {
                        var e = rr(a, this.options);
                        return tr(e, "onPullDownRefresh");
                    },
                    onReachBottom: function() {
                        var e = rr(a, this.options);
                        return tr(e, "onReachBottom");
                    },
                    onPageScroll: function(e) {
                        var t = rr(a, this.options);
                        return tr(t, "onPageScroll", e);
                    },
                    onResize: function(e) {
                        var t = rr(a, this.options);
                        return tr(t, "onResize", e);
                    },
                    onTabItemTap: function(e) {
                        var t = rr(a, this.options);
                        return tr(t, "onTabItemTap", e);
                    },
                    onTitleClick: function() {
                        var e = rr(a, this.options);
                        return tr(e, "onTitleClick");
                    },
                    onOptionMenuClick: function() {
                        var e = rr(a, this.options);
                        return tr(e, "onOptionMenuClick");
                    },
                    onPopMenuClick: function() {
                        var e = rr(a, this.options);
                        return tr(e, "onPopMenuClick");
                    },
                    onPullIntercept: function() {
                        var e = rr(a, this.options);
                        return tr(e, "onPullIntercept");
                    },
                    onAddToFavorites: function() {
                        var e = rr(a, this.options);
                        return tr(e, "onAddToFavorites");
                    }
                };
                return (e.onShareAppMessage || (null === (o = e.prototype) || void 0 === o ? void 0 : o.onShareAppMessage) || e.enableShareAppMessage) && (l.onShareAppMessage = function(e) {
                    var t = e.target;
                    if (null != t) {
                        var n = t.id, r = Nn.getElementById(n);
                        null != r && (e.target.dataset = r.dataset);
                    }
                    var o = rr(a, this.options);
                    return tr(o, "onShareAppMessage", e);
                }), (e.onShareTimeline || (null === (i = e.prototype) || void 0 === i ? void 0 : i.onShareTimeline) || e.enableShareTimeline) && (l.onShareTimeline = function() {
                    var e = rr(a, this.options);
                    return tr(e, "onShareTimeline");
                }), l.eh = _, Object(w["o"])(n) || (l.data = n), xn && (l.path = a), l;
            }
            function sr(e, t, n) {
                var r, o, i, a = null !== t && void 0 !== t ? t : "taro_component_".concat(er()), c = null, s = {
                    attached: function() {
                        var t = this;
                        Tn.start(D);
                        var n = rr(a, {
                            id: this.getPageId()
                        });
                        Qn.app.mount(e, n, function() {
                            c = Nn.getElementById(n), Object(w["f"])(null !== c, "没有找到组件实例。"), tr(n, "onLoad"), 
                            xn || (c.ctx = t, c.performUpdate(!0));
                        });
                    },
                    detached: function() {
                        var e = rr(a, {
                            id: this.getPageId()
                        });
                        Qn.app.unmount(e, function() {
                            Jn.delete(e), c && (c.ctx = null);
                        });
                    },
                    pageLifetimes: {
                        show: function() {
                            tr(a, "onShow");
                        },
                        hide: function() {
                            tr(a, "onHide");
                        }
                    },
                    methods: {
                        eh: _
                    }
                };
                return Object(w["o"])(n) || (s.data = n), s["options"] = null !== (r = null === e || void 0 === e ? void 0 : e["options"]) && void 0 !== r ? r : w["b"], 
                s["externalClasses"] = null !== (o = null === e || void 0 === e ? void 0 : e["externalClasses"]) && void 0 !== o ? o : w["b"], 
                s["behaviors"] = null !== (i = null === e || void 0 === e ? void 0 : e["behaviors"]) && void 0 !== i ? i : w["b"], 
                s;
            }
            function ur(e) {
                return {
                    properties: {
                        i: {
                            type: Object,
                            value: Object(m["a"])({}, "nn", "view")
                        },
                        l: {
                            type: String,
                            value: ""
                        }
                    },
                    observers: {
                        i: function(e) {
                            Object(w["w"])("#text" === e["nn"], "请在此元素外再套一层非 Text 元素：<text>".concat(e["v"], "</text>，详情：https://github.com/NervJS/taro/issues/6054"));
                        }
                    },
                    options: {
                        addGlobalClass: !0,
                        virtualHost: "custom-wrapper" !== e
                    },
                    methods: {
                        eh: _
                    }
                };
            }
            var lr = "taro-app", dr = function(e) {
                return function(t) {
                    var n = Ar.useContext(xr) || lr, r = Ar.useRef(t);
                    r.current !== t && (r.current = t), Ar.useLayoutEffect(function() {
                        var t = Xn(n), o = !1;
                        null == t && (o = !0, t = Object.create(null)), t = t;
                        var i = function() {
                            return r.current.apply(r, arguments);
                        };
                        return Object(w["k"])(t[e]) ? t[e] = [ t[e], i ] : t[e] = [].concat(Object(s["a"])(t[e] || []), [ i ]), 
                        o && Yn(t, n), function() {
                            var t = Xn(n), r = t[e];
                            r === i ? t[e] = void 0 : Object(w["i"])(r) && (t[e] = r.filter(function(e) {
                                return e !== i;
                            }));
                        };
                    }, []);
                };
            }, fr = dr("componentDidShow"), hr = dr("componentDidHide"), pr = dr("onPullDownRefresh"), vr = dr("onReachBottom"), gr = dr("onPageScroll"), br = dr("onResize"), mr = dr("onShareAppMessage"), yr = dr("onTabItemTap"), Sr = dr("onTitleClick"), wr = dr("onOptionMenuClick"), kr = dr("onPullIntercept"), Cr = dr("onShareTimeline"), Or = dr("onAddToFavorites"), jr = dr("onReady"), Tr = function() {
                var e = arguments.length > 0 && void 0 !== arguments[0] && arguments[0];
                return e ? Qn.router : Ar.useMemo(function() {
                    return Qn.router;
                }, []);
            }, Pr = function() {};
            function Er(e, t) {
                var n;
                return Object(w["k"])(t.render) || !!(null === (n = t.prototype) || void 0 === n ? void 0 : n.isReactComponent) || t.prototype instanceof e.Component;
            }
            var Br, Ar = w["b"], xr = w["b"];
            function Ir(e, t) {
                var n = e.createElement;
                return function(r) {
                    var o = Er(e, r), i = function(e) {
                        return e && Yn(e, t);
                    }, a = o ? {
                        ref: i
                    } : {
                        forwardedRef: i,
                        reactReduxForwardedRef: i
                    };
                    return xr === w["b"] && (xr = e.createContext("")), function(e) {
                        Object(v["a"])(i, e);
                        var o = Object(g["a"])(i);
                        function i() {
                            var e;
                            return Object(y["a"])(this, i), e = o.apply(this, arguments), e.state = {
                                hasError: !1
                            }, e;
                        }
                        return Object(S["a"])(i, [ {
                            key: "componentDidCatch",
                            value: function(e, t) {
                                console.warn(e), console.error(t.componentStack);
                            }
                        }, {
                            key: "render",
                            value: function() {
                                var e = this.state.hasError ? [] : n(xr.Provider, {
                                    value: t
                                }, n(r, Object.assign(Object.assign({}, this.props), a)));
                                return xn ? n("div", {
                                    id: t,
                                    className: "taro_page"
                                }, e) : n("root", {
                                    id: t
                                }, e);
                            }
                        } ], [ {
                            key: "getDerivedStateFromError",
                            value: function(e) {
                                return console.warn(e), {
                                    hasError: !0
                                };
                            }
                        } ]), i;
                    }(e.Component);
                };
            }
            function _r() {
                var e = {
                    getLifecyle: function(e, t) {
                        return "onShow" === t ? t = "componentDidShow" : "onHide" === t && (t = "componentDidHide"), 
                        e[t];
                    },
                    mergePageInstance: function(e, t) {
                        e && t && ("constructor" in e || Object.keys(e).forEach(function(n) {
                            Object(w["k"])(t[n]) ? t[n] = [ t[n] ].concat(Object(s["a"])(e[n])) : t[n] = [].concat(Object(s["a"])(t[n] || []), Object(s["a"])(e[n]));
                        }));
                    },
                    modifyEventType: function(e) {
                        e.type = e.type.replace(/-/g, "");
                    },
                    batchedEventUpdates: function(e) {
                        Br.unstable_batchedUpdates(e);
                    }
                };
                xn && (e.createPullDownComponent = function(e, t, n, r) {
                    var o = Er(n, e);
                    return n.forwardRef(function(t, i) {
                        var a = Object.assign({}, t), c = o ? {
                            ref: i
                        } : {
                            forwardedRef: i,
                            reactReduxForwardedRef: i
                        };
                        return n.createElement(r || "taro-pull-to-refresh", null, n.createElement(e, Object.assign(Object.assign({}, a), c)));
                    });
                }, e.findDOMNode = function(e) {
                    return Br.findDOMNode(e);
                }), F.reconciler(e);
            }
            var Lr = C();
            function Rr(e, t, n, r) {
                Ar = t, Br = n, Object(w["f"])(!!Br, "构建 React/Nerv 项目请把 process.env.FRAMEWORK 设置为 'react'/'nerv' ");
                var o, i = Ar.createRef(), a = Er(Ar, e);
                _r();
                var c = function(t) {
                    Object(v["a"])(r, t);
                    var n = Object(g["a"])(r);
                    function r() {
                        var e;
                        return Object(y["a"])(this, r), e = n.apply(this, arguments), e.pages = [], e.elements = [], 
                        e;
                    }
                    return Object(S["a"])(r, [ {
                        key: "mount",
                        value: function(e, t, n) {
                            var r = t + Lr(), o = function() {
                                return Ar.createElement(e, {
                                    key: r,
                                    tid: t
                                });
                            };
                            this.pages.push(o), this.forceUpdate(n);
                        }
                    }, {
                        key: "unmount",
                        value: function(e, t) {
                            for (var n = 0; n < this.elements.length; n++) {
                                var r = this.elements[n];
                                if (r.props.tid === e) {
                                    this.elements.splice(n, 1);
                                    break;
                                }
                            }
                            this.forceUpdate(t);
                        }
                    }, {
                        key: "render",
                        value: function() {
                            while (this.pages.length > 0) {
                                var t = this.pages.pop();
                                this.elements.push(t());
                            }
                            var n = null;
                            return a && (n = {
                                ref: i
                            }), Ar.createElement(e, n, xn ? Ar.createElement("div", null, this.elements.slice()) : this.elements.slice());
                        }
                    } ]), r;
                }(Ar.Component), s = Object.create({
                    render: function(e) {
                        o.forceUpdate(e);
                    },
                    mount: function(e, t, n) {
                        var r = Ir(Ar, t)(e);
                        o.mount(r, t, n);
                    },
                    unmount: function(e, t) {
                        o.unmount(e, t);
                    }
                }, {
                    config: {
                        writable: !0,
                        enumerable: !0,
                        configurable: !0,
                        value: r
                    },
                    onLaunch: {
                        enumerable: !0,
                        writable: !0,
                        value: function(e) {
                            var t = this;
                            Qn.router = Object.assign({
                                params: null === e || void 0 === e ? void 0 : e.query
                            }, e), o = Br.render(Ar.createElement(c), Nn.getElementById("app"));
                            var n = i.current;
                            if (null === n || void 0 === n ? void 0 : n.taroGlobalData) {
                                var r = n.taroGlobalData, a = Object.keys(r), s = Object.getOwnPropertyDescriptors(r);
                                a.forEach(function(e) {
                                    Object.defineProperty(t, e, {
                                        configurable: !0,
                                        enumerable: !0,
                                        get: function() {
                                            return r[e];
                                        },
                                        set: function(t) {
                                            r[e] = t;
                                        }
                                    });
                                }), Object.defineProperties(this, s);
                            }
                            this.$app = n, null != n && Object(w["k"])(n.onLaunch) && n.onLaunch(e);
                        }
                    },
                    onShow: {
                        enumerable: !0,
                        writable: !0,
                        value: function(e) {
                            var t = i.current;
                            Qn.router = Object.assign({
                                params: null === e || void 0 === e ? void 0 : e.query
                            }, e), null != t && Object(w["k"])(t.componentDidShow) && t.componentDidShow(e), 
                            u("componentDidShow");
                        }
                    },
                    onHide: {
                        enumerable: !0,
                        writable: !0,
                        value: function(e) {
                            var t = i.current;
                            null != t && Object(w["k"])(t.componentDidHide) && t.componentDidHide(e), u("componentDidHide");
                        }
                    },
                    onPageNotFound: {
                        enumerable: !0,
                        writable: !0,
                        value: function(e) {
                            var t = i.current;
                            null != t && Object(w["k"])(t.onPageNotFound) && t.onPageNotFound(e);
                        }
                    }
                });
                function u(e) {
                    var t = Xn(lr);
                    if (t) {
                        var n = i.current, r = k.getLifecyle(t, e);
                        Array.isArray(r) && r.forEach(function(e) {
                            return e.apply(n);
                        });
                    }
                }
                return Qn.app = s, Qn.app;
            }
            var Dr, Nr = C();
            function Mr(e, t) {
                var n = function(t) {
                    Object(v["a"])(r, t);
                    var n = Object(g["a"])(r);
                    function r() {
                        var t;
                        return Object(y["a"])(this, r), t = n.apply(this, arguments), t.root = e.createRef(), 
                        t.ctx = t.props.getCtx(), t;
                    }
                    return Object(S["a"])(r, [ {
                        key: "componentDidMount",
                        value: function() {
                            this.ctx.component = this;
                            var e = this.root.current;
                            e.ctx = this.ctx, e.performUpdate(!0);
                        }
                    }, {
                        key: "render",
                        value: function() {
                            return e.createElement("root", {
                                ref: this.root
                            }, this.props.renderComponent(this.ctx));
                        }
                    } ]), r;
                }(e.Component), r = function(t) {
                    Object(v["a"])(o, t);
                    var r = Object(g["a"])(o);
                    function o() {
                        var e;
                        return Object(y["a"])(this, o), e = r.apply(this, arguments), e.state = {
                            components: []
                        }, e;
                    }
                    return Object(S["a"])(o, [ {
                        key: "componentDidMount",
                        value: function() {
                            Qn.app = this;
                        }
                    }, {
                        key: "mount",
                        value: function(t, r, o) {
                            var i = Er(e, t), a = function(e) {
                                return e && Yn(e, r);
                            }, c = i ? {
                                ref: a
                            } : {
                                forwardedRef: a,
                                reactReduxForwardedRef: a
                            }, u = {
                                compId: r,
                                element: e.createElement(n, {
                                    key: r,
                                    getCtx: o,
                                    renderComponent: function(n) {
                                        return e.createElement(t, Object.assign(Object.assign({}, (n.data || (n.data = {})).props), c));
                                    }
                                })
                            };
                            this.setState({
                                components: [].concat(Object(s["a"])(this.state.components), [ u ])
                            });
                        }
                    }, {
                        key: "unmount",
                        value: function(e) {
                            var t = this.state.components, n = t.findIndex(function(t) {
                                return t.compId === e;
                            }), r = [].concat(Object(s["a"])(t.slice(0, n)), Object(s["a"])(t.slice(n + 1)));
                            this.setState({
                                components: r
                            });
                        }
                    }, {
                        key: "render",
                        value: function() {
                            var e = this.state.components;
                            return e.map(function(e) {
                                var t = e.element;
                                return t;
                            });
                        }
                    } ]), o;
                }(e.Component);
                _r();
                var o = Nn.getElementById("app");
                t.render(e.createElement(r, {}), o);
            }
            function Fr(e, t, n, r) {
                Ar = t, Br = n;
                var o = {
                    properties: {
                        props: {
                            type: null,
                            value: null,
                            observer: function(e, t) {
                                t && this.component.forceUpdate();
                            }
                        }
                    },
                    created: function() {
                        Qn.app || Mr(Ar, Br);
                    },
                    attached: function() {
                        var t = this;
                        i(), this.compId = Nr(), this.config = r, Qn.app.mount(e, this.compId, function() {
                            return t;
                        });
                    },
                    ready: function() {
                        tr(this.compId, "onReady");
                    },
                    detached: function() {
                        Qn.app.unmount(this.compId);
                    },
                    pageLifetimes: {
                        show: function() {
                            tr(this.compId, "onShow");
                        },
                        hide: function() {
                            tr(this.compId, "onHide");
                        }
                    },
                    methods: {
                        eh: _
                    }
                };
                function i() {
                    var e = getCurrentPages(), t = e[e.length - 1];
                    if (Qn.page !== t) {
                        Qn.page = t;
                        var n = t.route || t.__route__, r = {
                            params: t.options || {},
                            path: Zn(n),
                            onReady: "",
                            onHide: "",
                            onShow: ""
                        };
                        Qn.router = r, t.options || Object.defineProperty(t, "options", {
                            enumerable: !0,
                            configurable: !0,
                            get: function() {
                                return this._optionsValue;
                            },
                            set: function(e) {
                                r.params = e, this._optionsValue = e;
                            }
                        });
                    }
                }
                return o;
            }
            function Wr(e, t) {
                return function(n) {
                    var r = e.extend({
                        props: {
                            tid: String
                        },
                        mixins: [ n, {
                            created: function() {
                                Yn(this, t);
                            }
                        } ]
                    }), o = {
                        render: function(e) {
                            return e(xn ? "div" : "root", {
                                attrs: {
                                    id: t,
                                    class: xn ? "taro_page" : ""
                                }
                            }, [ e(r, {
                                props: {
                                    tid: t
                                }
                            }) ]);
                        }
                    };
                    return o;
                };
            }
            function Vr() {
                var e = {
                    getLifecyle: function(e, t) {
                        return e.$options[t];
                    },
                    removeAttribute: function(e, t) {
                        var n = Object(w["c"])(Object(w["u"])(e.tagName.toLowerCase()));
                        n in w["h"] && Object(w["g"])(w["h"][n], t) && Object(w["j"])(w["h"][n][t]) ? e.setAttribute(t, !1) : delete e.props[t];
                    }
                };
                xn && (e.createPullDownComponent = function(e, t, n) {
                    var r = n.extend({
                        props: {
                            tid: String
                        },
                        mixins: [ e, {
                            created: function() {
                                Yn(this, t);
                            }
                        } ]
                    }), o = {
                        name: "PullToRefresh",
                        render: function(e) {
                            return e("taro-pull-to-refresh", {
                                class: [ "hydrated" ]
                            }, [ e(r, this.$slots.default) ]);
                        }
                    };
                    return o;
                }, e.findDOMNode = function(e) {
                    return e.$el;
                }), F.reconciler(e);
            }
            function Ur(e, t, n) {
                Dr = t, Object(w["f"])(!!Dr, "构建 Vue 项目请把 process.env.FRAMEWORK 设置为 'vue'"), Vr(), 
                Dr.config.getTagNamespace = w["r"];
                var r, o = [], i = [], a = new Dr({
                    render: function(t) {
                        while (i.length > 0) {
                            var n = i.pop();
                            o.push(n(t));
                        }
                        return t(e, {
                            ref: "app"
                        }, o.slice());
                    },
                    methods: {
                        mount: function(e, t, n) {
                            i.push(function(n) {
                                return n(e, {
                                    key: t
                                });
                            }), this.updateSync(n);
                        },
                        updateSync: function(e) {
                            this._update(this._render(), !1), this.$children.forEach(function(e) {
                                return e._update(e._render(), !1);
                            }), e();
                        },
                        unmount: function(e, t) {
                            for (var n = 0; n < o.length; n++) {
                                var r = o[n];
                                if (r.key === e) {
                                    o.splice(n, 1);
                                    break;
                                }
                            }
                            this.updateSync(t);
                        }
                    }
                }), c = Object.create({
                    mount: function(e, t, n) {
                        var r = Wr(Dr, t)(e);
                        a.mount(r, t, n);
                    },
                    unmount: function(e, t) {
                        a.unmount(e, t);
                    }
                }, {
                    config: {
                        writable: !0,
                        enumerable: !0,
                        configurable: !0,
                        value: n
                    },
                    onLaunch: {
                        writable: !0,
                        enumerable: !0,
                        value: function(e) {
                            Qn.router = Object.assign({
                                params: null === e || void 0 === e ? void 0 : e.query
                            }, e), a.$mount(Nn.getElementById("app")), r = a.$refs.app, null != r && Object(w["k"])(r.$options.onLaunch) && r.$options.onLaunch.call(r, e);
                        }
                    },
                    onShow: {
                        writable: !0,
                        enumerable: !0,
                        value: function(e) {
                            Qn.router = Object.assign({
                                params: null === e || void 0 === e ? void 0 : e.query
                            }, e), null != r && Object(w["k"])(r.$options.onShow) && r.$options.onShow.call(r, e);
                        }
                    },
                    onHide: {
                        writable: !0,
                        enumerable: !0,
                        value: function(e) {
                            null != r && Object(w["k"])(r.$options.onHide) && r.$options.onHide.call(r, e);
                        }
                    }
                });
                return Qn.app = c, Qn.app;
            }
            function qr(e, t) {
                return function(n) {
                    var r, o = {
                        props: {
                            tid: String
                        },
                        created: function() {
                            Yn(this, t), this.$nextTick(function() {
                                tr(t, "onShow");
                            });
                        }
                    };
                    if (Object(w["i"])(n.mixins)) {
                        var i = n.mixins, a = i.length - 1;
                        (null === (r = i[a].props) || void 0 === r ? void 0 : r.tid) ? n.mixins[a] = o : n.mixins.push(o);
                    } else n.mixins = [ o ];
                    return e(xn ? "div" : "root", {
                        key: t,
                        id: t,
                        class: xn ? "taro_page" : ""
                    }, [ e(n, {
                        tid: t
                    }) ]);
                };
            }
            function zr() {
                var e = {
                    getLifecyle: function(e, t) {
                        return e.$options[t];
                    },
                    removeAttribute: function(e, t) {
                        var n = Object(w["c"])(Object(w["u"])(e.tagName.toLowerCase()));
                        n in w["h"] && Object(w["g"])(w["h"][n], t) && Object(w["j"])(w["h"][n][t]) ? e.setAttribute(t, !1) : delete e.props[t];
                    },
                    modifyEventType: function(e) {
                        e.type = e.type.replace(/-/g, "");
                    }
                };
                xn && (e.createPullDownComponent = function(e, t, n) {
                    var r = {
                        props: {
                            tid: String
                        },
                        created: function() {
                            Yn(this, t);
                        }
                    };
                    return e.mixins = Object(w["i"])(e.mixins) ? e.mixins.push(r) : [ r ], {
                        render: function() {
                            return n("taro-pull-to-refresh", {
                                class: "hydrated"
                            }, [ n(e, this.$slots.default) ]);
                        }
                    };
                }, e.findDOMNode = function(e) {
                    return e.$el;
                }), F.reconciler(e);
            }
            function Hr(e, t, n) {
                var r, o = [];
                Object(w["f"])(!Object(w["k"])(e._component), "入口组件不支持使用函数式组件"), zr(), e._component.render = function() {
                    return o.slice();
                };
                var i = Object.create({
                    mount: function(e, n, r) {
                        var i = qr(t, n)(e);
                        o.push(i), this.updateAppInstance(r);
                    },
                    unmount: function(e, t) {
                        o = o.filter(function(t) {
                            return t.key !== e;
                        }), this.updateAppInstance(t);
                    },
                    updateAppInstance: function(e) {
                        r.$forceUpdate(), r.$nextTick(e);
                    }
                }, {
                    config: {
                        writable: !0,
                        enumerable: !0,
                        configurable: !0,
                        value: n
                    },
                    onLaunch: {
                        writable: !0,
                        enumerable: !0,
                        value: function(t) {
                            var n;
                            Qn.router = Object.assign({
                                params: null === t || void 0 === t ? void 0 : t.query
                            }, t), r = e.mount("#app");
                            var o = null === (n = null === r || void 0 === r ? void 0 : r.$options) || void 0 === n ? void 0 : n.onLaunch;
                            Object(w["k"])(o) && o.call(r, t);
                        }
                    },
                    onShow: {
                        writable: !0,
                        enumerable: !0,
                        value: function(e) {
                            var t;
                            Qn.router = Object.assign({
                                params: null === e || void 0 === e ? void 0 : e.query
                            }, e);
                            var n = null === (t = null === r || void 0 === r ? void 0 : r.$options) || void 0 === t ? void 0 : t.onShow;
                            Object(w["k"])(n) && n.call(r, e);
                        }
                    },
                    onHide: {
                        writable: !0,
                        enumerable: !0,
                        value: function(e) {
                            var t, n = null === (t = null === r || void 0 === r ? void 0 : r.$options) || void 0 === t ? void 0 : t.onHide;
                            Object(w["k"])(n) && n.call(r, e);
                        }
                    }
                });
                return Qn.app = i, Qn.app;
            }
            function $r(e) {
                return null == e ? "" : "/" === e.charAt(0) ? e.slice(1) : e;
            }
            var Gr = function(e, t) {
                var n, r, o, i = Qn.router, a = function() {
                    setTimeout(function() {
                        t ? e.call(t) : e();
                    }, 1);
                };
                if (null !== i) {
                    var c = null, s = rr($r(i.path), i.params);
                    c = Nn.getElementById(s), null !== c ? xn ? null !== (o = null === (r = null === (n = c.firstChild) || void 0 === n ? void 0 : n["componentOnReady"]) || void 0 === r ? void 0 : r.call(n).then(function() {
                        a();
                    })) && void 0 !== o || a() : c.enqueueUpdateCallback(e, t) : a();
                } else a();
            };
        }.call(this, n(45), n(8)["document"], n(8)["window"], n(8)["requestAnimationFrame"], n(8)["cancelAnimationFrame"]);
    }
} ]);