require("./runtime"), require("./common"), require("./vendors"), require("./taro"), 
(wx["webpackJsonp"] = wx["webpackJsonp"] || []).push([ [ 4 ], {
    100: function(e, t, n) {
        var i = n(112);
        function r(e, t) {
            if (e) {
                if ("string" === typeof e) return i(e, t);
                var n = Object.prototype.toString.call(e).slice(8, -1);
                return "Object" === n && e.constructor && (n = e.constructor.name), "Map" === n || "Set" === n ? Array.from(e) : "Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? i(e, t) : void 0;
            }
        }
        e.exports = r, e.exports["default"] = e.exports, e.exports.__esModule = !0;
    },
    101: function(e, t, n) {
        var i = n(100);
        function r(e, t) {
            var n = "undefined" !== typeof Symbol && e[Symbol.iterator] || e["@@iterator"];
            if (!n) {
                if (Array.isArray(e) || (n = i(e)) || t && e && "number" === typeof e.length) {
                    n && (e = n);
                    var r = 0, o = function() {};
                    return {
                        s: o,
                        n: function() {
                            return r >= e.length ? {
                                done: !0
                            } : {
                                done: !1,
                                value: e[r++]
                            };
                        },
                        e: function(e) {
                            throw e;
                        },
                        f: o
                    };
                }
                throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
            }
            var a, s = !0, u = !1;
            return {
                s: function() {
                    n = n.call(e);
                },
                n: function() {
                    var e = n.next();
                    return s = e.done, e;
                },
                e: function(e) {
                    u = !0, a = e;
                },
                f: function() {
                    try {
                        s || null == n["return"] || n["return"]();
                    } finally {
                        if (u) throw a;
                    }
                }
            };
        }
        e.exports = r, e.exports["default"] = e.exports, e.exports.__esModule = !0;
    },
    102: function(e, t, n) {
        var i = n(297), r = n(298), o = n(100), a = n(299);
        function s(e, t) {
            return i(e) || r(e, t) || o(e, t) || a();
        }
        e.exports = s, e.exports["default"] = e.exports, e.exports.__esModule = !0;
    },
    106: function(e, t, n) {
        "use strict";
        (function(t, i) {
            var r = n(285), o = "undefined" !== typeof t ? t : "undefined" !== typeof i ? i : "undefined" !== typeof self ? self : {}, a = o.Raven, s = new r();
            s.noConflict = function() {
                return o.Raven = a, s;
            }, s.afterLoad(), e.exports = s;
        }).call(this, n(8)["window"], n(45));
    },
    109: function(e, t, n) {
        "use strict";
        var i = function(e) {
            return "object" === typeof e && null !== e;
        }, r = function(e) {
            switch (Object.prototype.toString.call(e)) {
              case "[object Error]":
                return !0;

              case "[object Exception]":
                return !0;

              case "[object DOMException]":
                return !0;

              default:
                return e instanceof Error;
            }
        }, o = function(e) {
            function t(t, n) {
                var i = e(t) || t;
                return n && n(i) || i;
            }
            return t;
        };
        e.exports = {
            isObject: i,
            isError: r,
            wrappedCallback: o
        };
    },
    112: function(e, t) {
        function n(e, t) {
            (null == t || t > e.length) && (t = e.length);
            for (var n = 0, i = new Array(t); n < t; n++) i[n] = e[n];
            return i;
        }
        e.exports = n, e.exports["default"] = e.exports, e.exports.__esModule = !0;
    },
    285: function(e, t, n) {
        "use strict";
        (function(t, i) {
            var r = n(286), o = n(287), a = n(288), s = n(109), u = s.isError, c = s.isObject, l = n(289).wrapMethod, g = "source protocol user pass host port path".split(" "), p = /^(?:(\w+):)?\/\/(?:(\w+)(:\w+)?@)?([\w\.-]+)(?::(\d+))?(\/.*)/;
            function f() {
                return +new Date();
            }
            var h = "undefined" !== typeof t ? t : "undefined" !== typeof i ? i : "undefined" !== typeof self ? self : {}, d = h.document, v = h.navigator;
            function y(e, t) {
                return _(t) ? function(n) {
                    return t(n, e);
                } : t;
            }
            function m() {
                for (var e in this._hasJSON = !("object" !== typeof JSON || !JSON.stringify), this._hasDocument = !w(d), 
                this._hasNavigator = !w(v), this._lastCapturedException = null, this._lastData = null, 
                this._lastEventId = null, this._globalServer = null, this._globalKey = null, this._globalProject = null, 
                this._globalContext = {}, this._globalOptions = {
                    logger: "javascript",
                    ignoreErrors: [],
                    ignoreUrls: [],
                    whitelistUrls: [],
                    includePaths: [],
                    crossOrigin: "anonymous",
                    collectWindowErrors: !0,
                    maxMessageLength: 0,
                    maxUrlLength: 250,
                    stackTraceLimit: 50,
                    autoBreadcrumbs: !0,
                    instrument: !0,
                    sampleRate: 1
                }, this._ignoreOnError = 0, this._isRavenInstalled = !1, this._originalErrorStackTraceLimit = Error.stackTraceLimit, 
                this._originalConsole = h.console || {}, this._originalConsoleMethods = {}, this._plugins = [], 
                this._startTime = f(), this._wrappedBuiltIns = [], this._breadcrumbs = [], this._lastCapturedEvent = null, 
                this._keypressTimeout, this._location = h.location, this._lastHref = this._location && this._location.href, 
                this._resetBackoff(), this._originalConsole) this._originalConsoleMethods[e] = this._originalConsole[e];
            }
            m.prototype = {
                VERSION: "0.0.7",
                debug: !1,
                TraceKit: r,
                config: function(e, t) {
                    var n = this;
                    if (n._globalServer) return this._logDebug("error", "Error: Raven has already been configured"), 
                    n;
                    if (!e) return n;
                    var i = n._globalOptions;
                    t && P(t, function(e, t) {
                        "tags" === e || "extra" === e || "user" === e ? n._globalContext[e] = t : i[e] = t;
                    }), n.setDSN(e), i.ignoreErrors.push(/^Script error\.?$/), i.ignoreErrors.push(/^Javascript error: Script error\.? on line 0$/), 
                    i.ignoreErrors = I(i.ignoreErrors), i.ignoreUrls = !!i.ignoreUrls.length && I(i.ignoreUrls), 
                    i.whitelistUrls = !!i.whitelistUrls.length && I(i.whitelistUrls), i.includePaths = I(i.includePaths), 
                    i.maxBreadcrumbs = Math.max(0, Math.min(i.maxBreadcrumbs || 100, 100));
                    var o = {
                        xhr: !1,
                        console: !0,
                        dom: !1,
                        location: !1
                    }, a = i.autoBreadcrumbs;
                    "[object Object]" === {}.toString.call(a) ? a = C(o, a) : !1 !== a && (a = o), i.autoBreadcrumbs = a;
                    var s = {
                        tryCatch: !0
                    }, u = i.instrument;
                    return "[object Object]" === {}.toString.call(u) ? u = C(s, u) : !1 !== u && (u = s), 
                    i.instrument = u, r.collectWindowErrors = !!i.collectWindowErrors, n;
                },
                install: function() {
                    var e = this;
                    return e.isSetup() && !e._isRavenInstalled && (r.report.subscribe(function() {
                        e._handleOnErrorStackInfo.apply(e, arguments);
                    }), e._globalOptions.instrument && e._globalOptions.instrument.tryCatch && e._instrumentTryCatch(), 
                    e._globalOptions.autoBreadcrumbs && e._instrumentBreadcrumbs(), e._drainPlugins(), 
                    this.installWeapp(), e._isRavenInstalled = !0), Error.stackTraceLimit = e._globalOptions.stackTraceLimit, 
                    this;
                },
                installWeapp: function() {
                    var e = this;
                    wx.getSystemInfo({
                        success: function(t) {
                            e.setTagsContext({
                                device: t.model,
                                system: t.system,
                                WXversion: t.version,
                                SDKversion: t.SDKVersion
                            });
                        }
                    }), wx.getNetworkType({
                        success: function(t) {
                            e.setTagsContext({
                                network: t.networkType
                            });
                        }
                    });
                },
                setDSN: function(e) {
                    var t = this, n = t._parseDSN(e), i = n.path.lastIndexOf("/"), r = n.path.substr(1, i);
                    t._dsn = e, t._globalKey = n.user, t._globalSecret = n.pass && n.pass.substr(1), 
                    t._globalProject = n.path.substr(i + 1), t._globalServer = t._getGlobalServer(n), 
                    t._globalEndpoint = t._globalServer + "/" + r + "api/" + t._globalProject + "/store/", 
                    this._resetBackoff();
                },
                context: function(e, t, n) {
                    return _(e) && (n = t || [], t = e, e = void 0), this.wrap(e, t).apply(this, n);
                },
                wrap: function(e, t, n) {
                    var i = this;
                    if (w(t) && !_(e)) return e;
                    if (_(e) && (t = e, e = void 0), !_(t)) return t;
                    try {
                        if (t.__raven__) return t;
                        if (t.__raven_wrapper__) return t.__raven_wrapper__;
                    } catch (e) {
                        return t;
                    }
                    function r() {
                        var r = [], o = arguments.length, a = !e || e && !1 !== e.deep;
                        n && _(n) && n.apply(this, arguments);
                        while (o--) r[o] = a ? i.wrap(e, arguments[o]) : arguments[o];
                        try {
                            return t.apply(this, r);
                        } catch (t) {
                            throw i._ignoreNextOnError(), i.captureException(t, e), t;
                        }
                    }
                    for (var o in t) O(t, o) && (r[o] = t[o]);
                    return r.prototype = t.prototype, t.__raven_wrapper__ = r, r.__raven__ = !0, r.__inner__ = t, 
                    r;
                },
                uninstall: function() {
                    return r.report.uninstall(), this._restoreBuiltIns(), Error.stackTraceLimit = this._originalErrorStackTraceLimit, 
                    this._isRavenInstalled = !1, this;
                },
                captureException: function(e, t) {
                    if ("[object String]" === Object.prototype.toString.call(e) && -1 !== e.indexOf("thirdScriptError")) {
                        var n = e.split("\n");
                        e = new Error(n[1]), e.name = n[0], n.shift(), n.shift(), e.stack = n.join("\n");
                    }
                    if (!u(e)) return this.captureMessage(e, C({
                        trimHeadFrames: 1,
                        stacktrace: !0
                    }, t));
                    this._lastCapturedException = e;
                    try {
                        var i = r.computeStackTrace(e);
                        this._handleStackInfo(i, t);
                    } catch (t) {
                        if (e !== t) throw t;
                    }
                    return this;
                },
                captureMessage: function(e, t) {
                    if (!this._globalOptions.ignoreErrors.test || !this._globalOptions.ignoreErrors.test(e)) {
                        t = t || {};
                        var n = C({
                            message: e + ""
                        }, t);
                        if (this._globalOptions.stacktrace || t && t.stacktrace) {
                            var i;
                            try {
                                throw new Error(e);
                            } catch (e) {
                                i = e;
                            }
                            i.name = null, t = C({
                                fingerprint: e,
                                trimHeadFrames: (t.trimHeadFrames || 0) + 1
                            }, t);
                            var o = r.computeStackTrace(i), a = this._prepareFrames(o, t);
                            n.stacktrace = {
                                frames: a.reverse()
                            };
                        }
                        return this._send(n), this;
                    }
                },
                captureBreadcrumb: function(e) {
                    var t = C({
                        timestamp: f() / 1e3
                    }, e);
                    if (_(this._globalOptions.breadcrumbCallback)) {
                        var n = this._globalOptions.breadcrumbCallback(t);
                        if (c(n) && !x(n)) t = n; else if (!1 === n) return this;
                    }
                    return this._breadcrumbs.push(t), this._breadcrumbs.length > this._globalOptions.maxBreadcrumbs && this._breadcrumbs.shift(), 
                    this;
                },
                addPlugin: function(e) {
                    var t = [].slice.call(arguments, 1);
                    return this._plugins.push([ e, t ]), this._isRavenInstalled && this._drainPlugins(), 
                    this;
                },
                setUserContext: function(e) {
                    return this._globalContext.user = e, this;
                },
                setExtraContext: function(e) {
                    return this._mergeContext("extra", e), this;
                },
                setTagsContext: function(e) {
                    return this._mergeContext("tags", e), this;
                },
                clearContext: function() {
                    return this._globalContext = {}, this;
                },
                getContext: function() {
                    return JSON.parse(o(this._globalContext));
                },
                setEnvironment: function(e) {
                    return this._globalOptions.environment = e, this;
                },
                setRelease: function(e) {
                    return this._globalOptions.release = e, this;
                },
                setDataCallback: function(e) {
                    var t = this._globalOptions.dataCallback;
                    return this._globalOptions.dataCallback = y(t, e), this;
                },
                setBreadcrumbCallback: function(e) {
                    var t = this._globalOptions.breadcrumbCallback;
                    return this._globalOptions.breadcrumbCallback = y(t, e), this;
                },
                setShouldSendCallback: function(e) {
                    var t = this._globalOptions.shouldSendCallback;
                    return this._globalOptions.shouldSendCallback = y(t, e), this;
                },
                setTransport: function(e) {
                    return this._globalOptions.transport = e, this;
                },
                lastException: function() {
                    return this._lastCapturedException;
                },
                lastEventId: function() {
                    return this._lastEventId;
                },
                isSetup: function() {
                    return !!this._hasJSON && (!!this._globalServer || (this.ravenNotConfiguredError || (this.ravenNotConfiguredError = !0, 
                    this._logDebug("error", "Error: Raven has not been configured.")), !1));
                },
                afterLoad: function() {
                    var e = h.RavenConfig;
                    e && this.config(e.dsn, e.config).install();
                },
                _ignoreNextOnError: function() {
                    var e = this;
                    this._ignoreOnError += 1, setTimeout(function() {
                        e._ignoreOnError -= 1;
                    });
                },
                _triggerEvent: function(e, t) {
                    var n, i;
                    if (this._hasDocument) {
                        for (i in t = t || {}, e = "raven" + e.substr(0, 1).toUpperCase() + e.substr(1), 
                        d.createEvent ? (n = d.createEvent("HTMLEvents"), n.initEvent(e, !0, !0)) : (n = d.createEventObject(), 
                        n.eventType = e), t) O(t, i) && (n[i] = t[i]);
                        if (d.createEvent) d.dispatchEvent(n); else try {
                            d.fireEvent("on" + n.eventType.toLowerCase(), n);
                        } catch (e) {}
                    }
                },
                _captureUrlChange: function(e, t) {
                    var n = A(this._location.href), i = A(t), r = A(e);
                    this._lastHref = t, n.protocol === i.protocol && n.host === i.host && (t = i.relative), 
                    n.protocol === r.protocol && n.host === r.host && (e = r.relative), this.captureBreadcrumb({
                        category: "navigation",
                        data: {
                            to: t,
                            from: e
                        }
                    });
                },
                _instrumentTryCatch: function() {
                    var e = this, t = e._wrappedBuiltIns;
                    function n(t) {
                        return function(n, i) {
                            for (var r = new Array(arguments.length), o = 0; o < r.length; ++o) r[o] = arguments[o];
                            var a = r[0];
                            return _(a) && (r[0] = e.wrap(a)), t.apply ? t.apply(this, r) : t(r[0], r[1]);
                        };
                    }
                    q(h, "setTimeout", n, t), q(h, "setInterval", n, t), h.requestAnimationFrame && q(h, "requestAnimationFrame", function(t) {
                        return function(n) {
                            return t(e.wrap(n));
                        };
                    }, t);
                },
                _instrumentBreadcrumbs: function() {
                    var e = this, t = this._globalOptions.autoBreadcrumbs, n = e._wrappedBuiltIns, i = h.chrome, r = i && i.app && i.app.runtime, o = !r && h.history && history.pushState;
                    if (t.location && o) {
                        var a = h.onpopstate;
                        h.onpopstate = function() {
                            var t = e._location.href;
                            if (e._captureUrlChange(e._lastHref, t), a) return a.apply(this, arguments);
                        }, q(history, "pushState", function(t) {
                            return function() {
                                var n = arguments.length > 2 ? arguments[2] : void 0;
                                return n && e._captureUrlChange(e._lastHref, n + ""), t.apply(this, arguments);
                            };
                        }, n);
                    }
                    if (t.console && console && console.log) {
                        var s = function(t, n) {
                            e.captureBreadcrumb({
                                message: t,
                                level: n.level,
                                category: "console"
                            });
                        };
                        P([ "debug", "info", "warn", "error", "log" ], function(e, t) {
                            l(console, t, s);
                        });
                    }
                },
                _restoreBuiltIns: function() {
                    var e;
                    while (this._wrappedBuiltIns.length) {
                        e = this._wrappedBuiltIns.shift();
                        var t = e[0], n = e[1], i = e[2];
                        t[n] = i;
                    }
                },
                _drainPlugins: function() {
                    var e = this;
                    P(this._plugins, function(t, n) {
                        var i = n[0], r = n[1];
                        i.apply(e, [ e ].concat(r));
                    });
                },
                _parseDSN: function(e) {
                    var t = p.exec(e), n = {}, i = 7;
                    try {
                        while (i--) n[g[i]] = t[i] || "";
                    } catch (t) {
                        throw new a("Invalid DSN: " + e);
                    }
                    if (n.pass && !this._globalOptions.allowSecretKey) throw new a("Do not specify your secret key in the DSN. See: http://bit.ly/raven-secret-key");
                    return n;
                },
                _getGlobalServer: function(e) {
                    var t = "//" + e.host + (e.port ? ":" + e.port : "");
                    return e.protocol && (t = e.protocol + ":" + t), t;
                },
                _handleOnErrorStackInfo: function() {
                    this._ignoreOnError || this._handleStackInfo.apply(this, arguments);
                },
                _handleStackInfo: function(e, t) {
                    var n = this._prepareFrames(e, t);
                    this._triggerEvent("handle", {
                        stackInfo: e,
                        options: t
                    }), this._processException(e.name, e.message, e.url, e.lineno, n, t);
                },
                _prepareFrames: function(e, t) {
                    var n = this, i = [];
                    if (e.stack && e.stack.length && (P(e.stack, function(t, r) {
                        var o = n._normalizeFrame(r, e.url);
                        o && i.push(o);
                    }), t && t.trimHeadFrames)) for (var r = 0; r < t.trimHeadFrames && r < i.length; r++) i[r].in_app = !1;
                    return i = i.slice(0, this._globalOptions.stackTraceLimit), i;
                },
                _normalizeFrame: function(e, t) {
                    var n = {
                        filename: e.url,
                        lineno: e.line,
                        colno: e.column,
                        function: e.func || "?"
                    };
                    return e.url || (n.filename = t), n.in_app = !(this._globalOptions.includePaths.test && !this._globalOptions.includePaths.test(n.filename) || /(Raven|TraceKit)\./.test(n["function"]) || /raven\.(min\.)?js$/.test(n.filename)), 
                    n;
                },
                _processException: function(e, t, n, i, r, o) {
                    var a;
                    if ((!this._globalOptions.ignoreErrors.test || !this._globalOptions.ignoreErrors.test(t)) && (t += "", 
                    r && r.length ? (n = r[0].filename || n, r.reverse(), a = {
                        frames: r
                    }) : n && (a = {
                        frames: [ {
                            filename: n,
                            lineno: i,
                            in_app: !0
                        } ]
                    }), (!this._globalOptions.ignoreUrls.test || !this._globalOptions.ignoreUrls.test(n)) && (!this._globalOptions.whitelistUrls.test || this._globalOptions.whitelistUrls.test(n)))) {
                        var s = C({
                            exception: {
                                values: [ {
                                    type: e,
                                    value: t,
                                    stacktrace: a
                                } ]
                            },
                            culprit: n
                        }, o);
                        this._send(s);
                    }
                },
                _trimPacket: function(e) {
                    var t = this._globalOptions.maxMessageLength;
                    if (e.message && (e.message = E(e.message, t)), e.exception) {
                        var n = e.exception.values[0];
                        n.value = E(n.value, t);
                    }
                    var i = e.request;
                    return i && (i.url && (i.url = E(i.url, this._globalOptions.maxUrlLength)), i.Referer && (i.Referer = E(i.Referer, this._globalOptions.maxUrlLength))), 
                    e.breadcrumbs && e.breadcrumbs.values && this._trimBreadcrumbs(e.breadcrumbs), e;
                },
                _trimBreadcrumbs: function(e) {
                    for (var t, n, i, r = [ "to", "from", "url" ], o = 0; o < e.values.length; ++o) if (n = e.values[o], 
                    n.hasOwnProperty("data") && c(n.data) && !S(n.data)) {
                        i = C({}, n.data);
                        for (var a = 0; a < r.length; ++a) t = r[a], i.hasOwnProperty(t) && i[t] && (i[t] = E(i[t], this._globalOptions.maxUrlLength));
                        e.values[o].data = i;
                    }
                },
                _getHttpData: function() {
                    var e = {
                        headers: {
                            "User-Agent": "weapp"
                        }
                    }, t = getCurrentPages();
                    return t && t.length && (e.url = t[t.length - 1].route), e;
                },
                _resetBackoff: function() {
                    this._backoffDuration = 0, this._backoffStart = null;
                },
                _shouldBackoff: function() {
                    return this._backoffDuration && f() - this._backoffStart < this._backoffDuration;
                },
                _isRepeatData: function(e) {
                    var t = this._lastData;
                    return !(!t || e.message !== t.message || e.culprit !== t.culprit) && (e.stacktrace || t.stacktrace ? L(e.stacktrace, t.stacktrace) : !e.exception && !t.exception || V(e.exception, t.exception));
                },
                _setBackoffState: function(e) {
                    if (!this._shouldBackoff()) {
                        var t = e.status;
                        if (400 === t || 401 === t || 429 === t) {
                            var n;
                            try {
                                n = e.getResponseHeader("Retry-After"), n = 1e3 * parseInt(n, 10);
                            } catch (e) {}
                            this._backoffDuration = n || (2 * this._backoffDuration || 1e3), this._backoffStart = f();
                        }
                    }
                },
                _send: function(e) {
                    var t = this._globalOptions, n = {
                        project: this._globalProject,
                        logger: t.logger,
                        platform: "javascript"
                    }, i = this._getHttpData();
                    i && (n.request = i), e.trimHeadFrames && delete e.trimHeadFrames, e = C(n, e), 
                    e.tags = C(C({}, this._globalContext.tags), e.tags), e.extra = C(C({}, this._globalContext.extra), e.extra), 
                    e.extra["session:duration"] = f() - this._startTime, this._breadcrumbs && this._breadcrumbs.length > 0 && (e.breadcrumbs = {
                        values: [].slice.call(this._breadcrumbs, 0)
                    }), x(e.tags) && delete e.tags, this._globalContext.user && (e.user = this._globalContext.user), 
                    t.environment && (e.environment = t.environment), t.release && (e.release = t.release), 
                    t.serverName && (e.server_name = t.serverName), _(t.dataCallback) && (e = t.dataCallback(e) || e), 
                    e && !x(e) && (_(t.shouldSendCallback) && !t.shouldSendCallback(e) || (this._shouldBackoff() ? this._logDebug("warn", "Raven dropped error due to backoff: ", e) : "number" === typeof t.sampleRate ? Math.random() < t.sampleRate && this._sendProcessedPayload(e) : this._sendProcessedPayload(e)));
                },
                _getUuid: function() {
                    return j();
                },
                _sendProcessedPayload: function(e, t) {
                    var n = this, i = this._globalOptions;
                    if (this.isSetup()) if (e = this._trimPacket(e), this._globalOptions.allowDuplicates || !this._isRepeatData(e)) {
                        this._lastEventId = e.event_id || (e.event_id = this._getUuid()), this._lastData = e, 
                        this._logDebug("debug", "Raven about to send:", e);
                        var r = {
                            sentry_version: "7",
                            sentry_client: "raven-weapp/" + this.VERSION,
                            sentry_key: this._globalKey
                        };
                        this._globalSecret && (r.sentry_secret = this._globalSecret);
                        var o = e.exception && e.exception.values[0];
                        this.captureBreadcrumb({
                            category: "sentry",
                            message: o ? (o.type ? o.type + ": " : "") + o.value : e.message,
                            event_id: e.event_id,
                            level: e.level || "error"
                        });
                        var a = this._globalEndpoint;
                        (i.transport || this._makeRequest).call(this, {
                            url: a,
                            auth: r,
                            data: e,
                            options: i,
                            onSuccess: function() {
                                n._resetBackoff(), n._triggerEvent("success", {
                                    data: e,
                                    src: a
                                }), t && t();
                            },
                            onError: function(i) {
                                n._logDebug("error", "Raven transport failed to send: ", i), i.request && n._setBackoffState(i.request), 
                                n._triggerEvent("failure", {
                                    data: e,
                                    src: a
                                }), i = i || new Error("Raven send failed (no additional details provided)"), t && t(i);
                            }
                        });
                    } else this._logDebug("warn", "Raven dropped repeat event: ", e);
                },
                _makeRequest: function(e) {
                    "production" === this._globalOptions.environment && (console.log("request-error"), 
                    wx.request({
                        url: e.url + "?" + T(e.auth),
                        method: "POST",
                        header: {
                            "content-type": "text/plain;charset=UTF-8"
                        },
                        data: o(e.data),
                        success: function() {
                            e.onSuccess && e.onSuccess();
                        },
                        fail: function(t) {
                            e.onError && e.onError(t);
                        }
                    }));
                },
                _logDebug: function(e) {
                    this._originalConsoleMethods[e] && this.debug && Function.apply.call(this._originalConsoleMethods[e], this._originalConsole, [].slice.call(arguments, 1));
                },
                _mergeContext: function(e, t) {
                    w(t) ? delete this._globalContext[e] : this._globalContext[e] = C(this._globalContext[e] || {}, t);
                }
            };
            var b = Object.prototype;
            function w(e) {
                return void 0 === e;
            }
            function _(e) {
                return "function" === typeof e;
            }
            function k(e) {
                return "[object String]" === b.toString.call(e);
            }
            function x(e) {
                for (var t in e) return !1;
                return !0;
            }
            function P(e, t) {
                var n, i;
                if (w(e.length)) for (n in e) O(e, n) && t.call(null, n, e[n]); else if (i = e.length, 
                i) for (n = 0; n < i; n++) t.call(null, n, e[n]);
            }
            function C(e, t) {
                return t ? (P(t, function(t, n) {
                    e[t] = n;
                }), e) : e;
            }
            function S(e) {
                return !!Object.isFrozen && Object.isFrozen(e);
            }
            function E(e, t) {
                return !t || e.length <= t ? e : e.substr(0, t) + "…";
            }
            function O(e, t) {
                return b.hasOwnProperty.call(e, t);
            }
            function I(e) {
                for (var t, n = [], i = 0, r = e.length; i < r; i++) t = e[i], k(t) ? n.push(t.replace(/([.*+?^=!:${}()|\[\]\/\\])/g, "\\$1")) : t && t.source && n.push(t.source);
                return new RegExp(n.join("|"), "i");
            }
            function T(e) {
                var t = [];
                return P(e, function(e, n) {
                    t.push(encodeURIComponent(e) + "=" + encodeURIComponent(n));
                }), t.join("&");
            }
            function A(e) {
                var t = e.match(/^(([^:\/?#]+):)?(\/\/([^\/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?$/);
                if (!t) return {};
                var n = t[6] || "", i = t[8] || "";
                return {
                    protocol: t[2],
                    host: t[4],
                    path: t[5],
                    relative: t[5] + n + i
                };
            }
            function j() {
                var e = h.crypto || h.msCrypto;
                if (!w(e) && e.getRandomValues) {
                    var t = new Uint16Array(8);
                    e.getRandomValues(t), t[3] = 4095 & t[3] | 16384, t[4] = 16383 & t[4] | 32768;
                    var n = function(e) {
                        var t = e.toString(16);
                        while (t.length < 4) t = "0" + t;
                        return t;
                    };
                    return n(t[0]) + n(t[1]) + n(t[2]) + n(t[3]) + n(t[4]) + n(t[5]) + n(t[6]) + n(t[7]);
                }
                return "xxxxxxxxxxxx4xxxyxxxxxxxxxxxxxxx".replace(/[xy]/g, function(e) {
                    var t = 16 * Math.random() | 0, n = "x" === e ? t : 3 & t | 8;
                    return n.toString(16);
                });
            }
            function G(e, t) {
                return !!(!!e ^ !!t);
            }
            function V(e, t) {
                return !G(e, t) && (e = e.values[0], t = t.values[0], e.type === t.type && e.value === t.value && L(e.stacktrace, t.stacktrace));
            }
            function L(e, t) {
                if (G(e, t)) return !1;
                var n, i, r = e.frames, o = t.frames;
                if (r.length !== o.length) return !1;
                for (var a = 0; a < r.length; a++) if (n = r[a], i = o[a], n.filename !== i.filename || n.lineno !== i.lineno || n.colno !== i.colno || n["function"] !== i["function"]) return !1;
                return !0;
            }
            function q(e, t, n, i) {
                var r = e[t];
                e[t] = n(r), i && i.push([ e, t, r ]);
            }
            "undefined" !== typeof __DEV__ && __DEV__ && (m.utils = {
                isUndefined: w,
                isFunction: _,
                isString: k,
                isObject: c,
                isEmptyObject: x,
                isError: u,
                each: P,
                objectMerge: C,
                truncate: E,
                hasKey: O,
                joinRegExp: I,
                urlencode: T,
                uuid4: j,
                parseUrl: A,
                fill: q
            }), m.prototype.setUser = m.prototype.setUserContext, m.prototype.setReleaseContext = m.prototype.setRelease, 
            e.exports = m;
        }).call(this, n(8)["window"], n(45));
    },
    286: function(e, t, n) {
        "use strict";
        (function(t, i) {
            var r = n(109), o = {
                collectWindowErrors: !0,
                debug: !1
            }, a = "undefined" !== typeof t ? t : "undefined" !== typeof i ? i : "undefined" !== typeof self ? self : {}, s = [].slice, u = "?", c = /^(?:[Uu]ncaught (?:exception: )?)?(?:((?:Eval|Internal|Range|Reference|Syntax|Type|URI|)Error): )?(.*)$/, l = function() {
                var e = getCurrentPages();
                return e && e.length ? e[e.length - 1].route : "";
            };
            o.report = function() {
                var e, t, n = [], i = null, g = null, p = null;
                function f(e) {
                    m(), n.push(e);
                }
                function h(e) {
                    for (var t = n.length - 1; t >= 0; --t) n[t] === e && n.splice(t, 1);
                }
                function d() {
                    b(), n = [];
                }
                function v(e, t) {
                    var i = null;
                    if (!t || o.collectWindowErrors) {
                        for (var r in n) if (n.hasOwnProperty(r)) try {
                            n[r].apply(null, [ e ].concat(s.call(arguments, 2)));
                        } catch (e) {
                            i = e;
                        }
                        if (i) throw i;
                    }
                }
                function y(t, n, i, a, s) {
                    var g = null;
                    if (p) o.computeStackTrace.augmentStackTraceWithInitialElement(p, n, i, t), w(); else if (s && r.isError(s)) g = o.computeStackTrace(s), 
                    v(g, !0); else {
                        var f = {
                            url: n,
                            line: i,
                            column: a
                        }, h = void 0, d = t;
                        if ("[object String]" === {}.toString.call(t)) {
                            var y = t.match(c);
                            y && (h = y[1], d = y[2]);
                        }
                        f.func = u, g = {
                            name: h,
                            message: d,
                            url: l(),
                            stack: [ f ]
                        }, v(g, !0);
                    }
                    return !!e && e.apply(this, arguments);
                }
                function m() {
                    t || (e = a.onerror, a.onerror = y, t = !0);
                }
                function b() {
                    t && (a.onerror = e, t = !1, e = void 0);
                }
                function w() {
                    var e = p, t = i;
                    i = null, p = null, g = null, v.apply(null, [ e, !1 ].concat(t));
                }
                function _(e, t) {
                    var n = s.call(arguments, 1);
                    if (p) {
                        if (g === e) return;
                        w();
                    }
                    var r = o.computeStackTrace(e);
                    if (p = r, g = e, i = n, setTimeout(function() {
                        g === e && w();
                    }, r.incomplete ? 2e3 : 0), !1 !== t) throw e;
                }
                return _.subscribe = f, _.unsubscribe = h, _.uninstall = d, _;
            }(), o.computeStackTrace = function() {
                function e(e) {
                    if ("undefined" !== typeof e.stack && e.stack) {
                        for (var t, n, i, r = /^\s*at (.*?) ?\(((?:file|https?|blob|chrome-extension|native|eval|webpack|<anonymous>|\/).*?)(?::(\d+))?(?::(\d+))?\)?\s*$/i, o = /\((\S*)(?::(\d+))(?::(\d+))\)/, a = e.stack.split("\n"), s = [], c = (/^(.*) is undefined$/.exec(e.message), 
                        0), g = a.length; c < g; ++c) if (n = r.exec(a[c])) {
                            var p = n[2] && 0 === n[2].indexOf("native"), f = n[2] && 0 === n[2].indexOf("eval");
                            f && (t = o.exec(n[2])) && (n[2] = t[1], n[3] = t[2], n[4] = t[3]), i = {
                                url: p ? null : n[2],
                                func: n[1] || u,
                                args: p ? [ n[2] ] : [],
                                line: n[3] ? +n[3] : null,
                                column: n[4] ? +n[4] : null
                            }, !i.func && i.line && (i.func = u), s.push(i);
                        }
                        return s.length ? {
                            name: e.name,
                            message: e.message,
                            url: l(),
                            stack: s
                        } : null;
                    }
                }
                function t(e, t, n, i) {
                    var r = {
                        url: t,
                        line: n
                    };
                    if (r.url && r.line) {
                        if (e.incomplete = !1, r.func || (r.func = u), e.stack.length > 0 && e.stack[0].url === r.url) {
                            if (e.stack[0].line === r.line) return !1;
                            if (!e.stack[0].line && e.stack[0].func === r.func) return e.stack[0].line = r.line, 
                            !1;
                        }
                        return e.stack.unshift(r), e.partial = !0, !0;
                    }
                    return e.incomplete = !0, !1;
                }
                function n(e, r) {
                    for (var a, s, c = /function\s+([_$a-zA-Z\xA0-\uFFFF][_$a-zA-Z0-9\xA0-\uFFFF]*)?\s*\(/i, g = [], p = {}, f = !1, h = n.caller; h && !f; h = h.caller) if (h !== i && h !== o.report) {
                        if (s = {
                            url: null,
                            func: u,
                            line: null,
                            column: null
                        }, h.name ? s.func = h.name : (a = c.exec(h.toString())) && (s.func = a[1]), "undefined" === typeof s.func) try {
                            s.func = a.input.substring(0, a.input.indexOf("{"));
                        } catch (e) {}
                        p["" + h] ? f = !0 : p["" + h] = !0, g.push(s);
                    }
                    r && g.splice(0, r);
                    var d = {
                        name: e.name,
                        message: e.message,
                        url: l(),
                        stack: g
                    };
                    return t(d, e.sourceURL || e.fileName, e.line || e.lineNumber, e.message || e.description), 
                    d;
                }
                function i(t, i) {
                    var r = null;
                    i = null == i ? 0 : +i;
                    try {
                        if (r = e(t), r) return r;
                    } catch (e) {
                        if (o.debug) throw e;
                    }
                    try {
                        if (r = n(t, i + 1), r) return r;
                    } catch (e) {
                        if (o.debug) throw e;
                    }
                    return {
                        name: t.name,
                        message: t.message,
                        url: l()
                    };
                }
                return i.augmentStackTraceWithInitialElement = t, i.computeStackTraceFromStackProp = e, 
                i;
            }(), e.exports = o;
        }).call(this, n(8)["window"], n(45));
    },
    287: function(e, t, n) {
        "use strict";
        function i(e, t) {
            for (var n = 0; n < e.length; ++n) if (e[n] === t) return n;
            return -1;
        }
        function r(e, t, n, i) {
            return JSON.stringify(e, o(t, i), n);
        }
        function o(e, t) {
            var n = [], r = [];
            return null == t && (t = function(e, t) {
                return n[0] === t ? "[Circular ~]" : "[Circular ~." + r.slice(0, i(n, t)).join(".") + "]";
            }), function(o, a) {
                if (n.length > 0) {
                    var s = i(n, this);
                    ~s ? n.splice(s + 1) : n.push(this), ~s ? r.splice(s, 1 / 0, o) : r.push(o), ~i(n, a) && (a = t.call(this, o, a));
                } else n.push(a);
                return null == e ? a : e.call(this, o, a);
            };
        }
        t = e.exports = r, t.getSerialize = o;
    },
    288: function(e, t, n) {
        "use strict";
        function i(e) {
            this.name = "RavenConfigError", this.message = e;
        }
        i.prototype = new Error(), i.prototype.constructor = i, e.exports = i;
    },
    289: function(e, t, n) {
        "use strict";
        var i = function(e, t, n) {
            var i = e[t], r = e;
            if (t in e) {
                var o = "warn" === t ? "warning" : t;
                e[t] = function() {
                    var e = [].slice.call(arguments), a = "" + e.join(" "), s = {
                        level: o,
                        logger: "console",
                        extra: {
                            arguments: e
                        }
                    };
                    "assert" === t ? !1 === e[0] && (a = "Assertion failed: " + (e.slice(1).join(" ") || "console.assert"), 
                    s.extra.arguments = e.slice(1), n && n(a, s)) : n && n(a, s), i && Function.apply.call(i, r, e);
                };
            }
        };
        e.exports = {
            wrapMethod: i
        };
    },
    292: function(e, t, n) {},
    293: function(e, t, n) {
        "use strict";
        (function(e) {
            var i = n(99), r = n(101), o = n(102), a = n(67), s = n(68), u = n(59), c = n(60), l = n(52);
            Object.defineProperty(t, "__esModule", {
                value: !0
            });
            var g, p = {
                devVer: 1,
                guid: function() {
                    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(e) {
                        var t = 16 * Math.random() | 0;
                        return ("x" == e ? t : 3 & t | 8).toString(16);
                    });
                },
                getScreenHeight: function(e) {
                    return e.pixelRatio ? Math.round(e.screenHeight * e.pixelRatio) : e.screenHeight;
                },
                getScreenWidth: function(e) {
                    return e.pixelRatio ? Math.round(e.screenWidth * e.pixelRatio) : e.screenWidth;
                },
                getOS: function(e) {
                    if (e) {
                        var t = e.toLowerCase();
                        return -1 != t.indexOf("android") ? "".concat(gioGlobal.platformConfig.name, "-Android") : -1 != t.indexOf("ios") ? "".concat(gioGlobal.platformConfig.name, "-iOS") : e;
                    }
                },
                getOSV: function(e) {
                    return "".concat(gioGlobal.platformConfig.name, " ").concat(e);
                },
                isEmpty: function(e) {
                    for (var t in e) if (Object.prototype.hasOwnProperty.call(e, t)) return !1;
                    return !0;
                },
                compareVersion: function(e, t) {
                    e = e.split("."), t = t.split(".");
                    for (var n = Math.max(e.length, t.length); n > e.length; ) e.push("0");
                    for (;n > t.length; ) t.push("0");
                    for (var i = 0; n > i; i++) {
                        var r = parseInt(e[i]), o = parseInt(t[i]);
                        if (r > o) return 1;
                        if (o > r) return -1;
                    }
                    return 0;
                }
            }, f = function(t) {
                Object.defineProperty(Object.prototype, "gioGlobal", {
                    get: function() {
                        return "quickApp" === t ? e.__proto__ : "my" === t ? $global : e;
                    },
                    configurable: !1,
                    enumerable: !1
                });
            }, h = function(e, t) {
                if (!e) return e;
                for (var n = t.split("."), i = e[n.shift()], r = 0, o = n.length; o > r; r++) {
                    var a = n.shift();
                    if (!i) return i;
                    i = i[a];
                }
                return i;
            }, d = function(e) {
                var t = {
                    eventId: void 0,
                    properties: {}
                };
                try {
                    if (e.hasOwnProperty("gioTrack") && "object" == l(e.gioTrack)) return t.eventId = e.gioTrack.name, 
                    t.properties = e.gioTrack.properties, t;
                    if (!e.gioImpTrack) return t;
                    t.eventId = e.gioImpTrack;
                    var n = /^gioTrack(.+)/, i = /^\w+$/;
                    for (var r in e) {
                        var o = void 0, a = r.match(n);
                        if (a && ("track" === (o = a[1].toLowerCase()) ? t.eventId = e[r] : t.properties[o] = e[r]), 
                        !i.test(t.eventId) || 10 > parseInt(t.eventId[0])) throw t.eventId = null, Error();
                    }
                } catch (e) {
                    console.warn("半打点IMP格式不正确, 事件名只能包含数字，字母和下划线，且不以数字开头, 请参考文档");
                }
                return t;
            }, v = function(e) {
                return e && "string" == typeof e && e.constructor === String;
            };
            Object.hasOwnProperty("getOwnPropertyDescriptors") || (g = "object" == ("undefined" === typeof Reflect ? "undefined" : l(Reflect)) && "function" == typeof Reflect.ownKeys ? Reflect.ownKeys : "function" == typeof Object.getOwnPropertySymbols ? function(e) {
                return Object.getOwnPropertyNames(e).concat(Object.getOwnPropertySymbols(e));
            } : Object.getOwnPropertyNames, Object.defineProperty(Object, "getOwnPropertyDescriptors", {
                configurable: !0,
                writable: !0,
                value: function(e) {
                    return g(e).reduce(function(t, n) {
                        return Object.defineProperty(t, n, {
                            configurable: !0,
                            enumerable: !0,
                            writable: !0,
                            value: Object.getOwnPropertyDescriptor(e, n)
                        });
                    }, {});
                }
            }));
            var y = function(e) {
                var t = m.observer.growingio;
                t && t.vdsConfig.followShare && e && e.path && (e.path = -1 === e.path.indexOf("?") ? e.path + "?suid=" + t.info.uid : e.path + "&suid=" + t.info.uid);
            }, m = {
                defaultPageCallbacks: {},
                defaultAppCallbacks: {},
                appHandlers: null,
                pageHandlers: null,
                actionEventTypes: null,
                originalPage: null,
                originalApp: null,
                originalComponent: null,
                originalBehavior: null,
                observer: null,
                hook: function(e, t) {
                    return function() {
                        var n, i = arguments ? arguments[0] : void 0;
                        if (i && (i.currentTarget || i.target) && -1 != m.actionEventTypes.indexOf(i.type)) try {
                            m.observer.actionListener(i, e);
                        } catch (e) {
                            console.error(e);
                        }
                        var r = gioGlobal.platformConfig.lisiteners.app, o = gioGlobal.platformConfig.lisiteners.page;
                        if (this._growing_app_ && e !== r.appShow || this._growing_page_ && -1 === [ o.pageShow, o.pageClose, o.pageLoad, o.pageHide, o.tabTap ].indexOf(e) ? n = t.apply(this, arguments) : this._growing_app_ || this._growing_page_ || (n = t.apply(this, arguments)), 
                        this._growing_app_ && -1 !== m.appHandlers.indexOf(e)) {
                            try {
                                m.defaultAppCallbacks[e].apply(this, arguments);
                            } catch (e) {
                                console.error(e);
                            }
                            e === r.appShow && (n = t.apply(this, arguments));
                        }
                        if (this._growing_page_ && -1 !== m.pageHandlers.indexOf(e)) {
                            var a = Array.prototype.slice.call(arguments);
                            n && a.push(n);
                            try {
                                m.defaultPageCallbacks[e].apply(this, a);
                            } catch (e) {
                                console.error(e);
                            }
                            -1 !== [ o.pageShow, o.pageClose, o.pageLoad, o.pageHide, o.tabTap ].indexOf(e) ? n = t.apply(this, arguments) : y(n);
                        }
                        return n;
                    };
                },
                hookComponent: function(e, t) {
                    return function() {
                        var n = arguments ? arguments[0] : void 0;
                        if (n && (n.currentTarget || n.target) && -1 != m.actionEventTypes.indexOf(n.type)) try {
                            m.observer.actionListener(n, e);
                        } catch (e) {
                            console.error(e);
                        }
                        return t.apply(this, arguments);
                    };
                },
                instrument: function(e) {
                    for (var t in e) "function" == typeof e[t] && (e[t] = this.hook(t, e[t]));
                    return e._growing_app_ && m.appHandlers.map(function(t) {
                        e[t] || (e[t] = m.defaultAppCallbacks[t]);
                    }), e._growing_page_ && m.pageHandlers.map(function(t) {
                        e[t] || t === gioGlobal.platformConfig.lisiteners.page.shareApp || (e[t] = m.defaultPageCallbacks[t]);
                    }), e;
                },
                instrumentPageComponent: function(e) {
                    if (e) return m.pageHandlers.map(function(t) {
                        if ("function" == typeof e[t]) {
                            var n = e[t];
                            e[t] = function() {
                                var e = n.apply(this, arguments), i = Array.prototype.slice.call(arguments);
                                return e && i.push(e), m.observer.pageListener(this, t, i), t === gioGlobal.platformConfig.lisiteners.page.shareApp && y(e), 
                                e;
                            };
                        } else t !== gioGlobal.platformConfig.lisiteners.page.shareApp && (e[t] = function() {
                            m.observer.pageListener(this, t, arguments);
                        });
                    }), e;
                },
                instrumentComponent: function(e) {
                    if (e.methods) {
                        var t = e.methods;
                        for (var n in t) "function" == typeof t[n] && (e.methods[n] = this.hookComponent(n, t[n]));
                    }
                    return e;
                },
                GrowingPage: function(e) {
                    return e._growing_page_ = !0, m.originalPage(m.instrument(e));
                },
                GrowingComponent: function(e) {
                    return m.originalComponent(m.instrumentComponent(e));
                },
                GrowingBehavior: function(e) {
                    return m.originalBehavior(m.instrumentComponent(e));
                },
                GrowingApp: function(e) {
                    return e._growing_app_ = !0, m.originalApp(m.instrument(e));
                },
                initPlatformInfo: function(e) {
                    m.appHandlers = e.appHandlers, m.pageHandlers = e.pageHandlers, m.actionEventTypes = e.actionEventTypes, 
                    m.originalApp = e.originalApp, m.originalPage = e.originalPage, m.originalComponent = e.originalComponent, 
                    m.originalBehavior = e.originalBehavior;
                },
                initInstrument: function(e) {
                    if (m.initPlatformInfo(gioGlobal.platformConfig), m.observer = e, m.pageHandlers.forEach(function(e) {
                        m.defaultPageCallbacks[e] = function() {
                            m.observer.pageListener(this, e, arguments);
                        };
                    }), m.appHandlers.forEach(function(e) {
                        m.defaultAppCallbacks[e] = function() {
                            m.observer.appListener(this, e, arguments);
                        };
                    }), gioGlobal.platformConfig.canHook) {
                        var t = gioGlobal.platformConfig.hooks;
                        t.App && !gioGlobal.growingAppInited && (App = function() {
                            return m.GrowingApp(arguments[0]);
                        }, gioGlobal.growingAppInited = !0), t.Page && !gioGlobal.growingPageInited && (Page = function() {
                            return m.GrowingPage(arguments[0]);
                        }, gioGlobal.growingPageInited = !0), t.Component && !gioGlobal.growingComponentInited && (Component = function() {
                            return m.GrowingComponent(arguments[0]);
                        }, gioGlobal.growingComponentInited = !0), t.Behavior && !gioGlobal.growingBehaviorInited && (Behavior = function() {
                            return m.GrowingBehavior(arguments[0]);
                        }, gioGlobal.growingBehaviorInited = !0);
                    }
                    gioGlobal.GioPage = m.GrowingPage, gioGlobal.GioApp = m.GrowingApp, gioGlobal.GioComponent = m.GrowingComponent, 
                    gioGlobal.GioBehavior = m.GrowingBehavior, gioGlobal.trackApp = function() {
                        var e = arguments[0];
                        return e._growing_app_ = !0, m.instrument(e);
                    }, gioGlobal.trackPage = function() {
                        var e = arguments[0];
                        return e._growing_page_ = !0, m.instrument(e);
                    }, gioGlobal.trackComponent = function() {
                        return m.instrument(arguments[0]);
                    }, gioGlobal.trackBehavior = function() {
                        return m.instrument(arguments[0]);
                    };
                }
            }, b = function() {
                function e() {
                    u(this, e), this.queries = {}, this.pvar = {};
                }
                return c(e, [ {
                    key: "touch",
                    value: function(e) {
                        this.path = e.route, this.time = Date.now(), this.query = this.queries[e.route] ? this.queries[e.route] : void 0;
                    }
                }, {
                    key: "addQuery",
                    value: function(e, t) {
                        this.queries[e.route] = t ? this._getQuery(t) : null;
                    }
                }, {
                    key: "_getQuery",
                    value: function(e) {
                        return Object.keys(e).filter(function(e) {
                            return "wxShoppingListScene" !== e;
                        }).map(function(t) {
                            return "".concat(t, "=").concat(e[t]);
                        }).join("&");
                    }
                }, {
                    key: "touchRelatedPvarData",
                    value: function(e) {
                        var t = "".concat(e.p, "?").concat(e.q);
                        this.pvar[t] ? this.pvar[t].push(e) : this.pvar[t] = [ e ];
                    }
                } ]), e;
            }(), w = {
                tap: [ "tap", "click" ],
                longtap: [ "longtap" ],
                input: [ "input" ],
                blur: [ "change", "blur" ],
                submit: [ "submit" ],
                focus: [ "focus" ]
            }, _ = /^function[^\(]*\([^\)]+\).*[^\.]+\.([^\(]+)\(.*/;
            function k(e) {
                return e && e.$attrs ? e.$attrs.mpcomid : "0";
            }
            function x(e, t, n) {
                return !(!e || !t) && (t === e || 0 === t.indexOf(e + n));
            }
            function P(e, t, n) {
                void 0 === t && (t = []);
                var i = t.slice(1);
                if (!i.length) return e;
                var r = i.join(n), o = "";
                return i.reduce(function(e, t) {
                    for (var i = e.$children.length, a = 0; i > a; a++) {
                        var s = e.$children[a], u = k(s);
                        if (o && (u = o + n + u), x(u, r, n)) return o = u, s;
                    }
                    return e;
                }, e);
            }
            function C(e, t, n) {
                void 0 === n && (n = []);
                var i = [];
                if (!e || !e.tag) return i;
                var r = e || {}, o = r.data;
                void 0 === o && (o = {});
                var a = r.children;
                void 0 === a && (a = []);
                var s = r.componentInstance;
                s ? Object.keys(s.$slots).forEach(function(e) {
                    var r = s.$slots[e];
                    (Array.isArray(r) ? r : [ r ]).forEach(function(e) {
                        i = i.concat(C(e, t, n));
                    });
                }) : a.forEach(function(e) {
                    i = i.concat(C(e, t, n));
                });
                var u = o.attrs, c = o.on;
                return u && c && u.eventid === t && n.forEach(function(e) {
                    var t = c[e];
                    "function" == typeof t ? i.push(t) : Array.isArray(t) && (i = i.concat(t));
                }), i;
            }
            var S = "~", E = "^";
            function O(e, t) {
                return e === t || "regionchange" === t && ("begin" === e || "end" === e);
            }
            var I = function() {
                function e(t) {
                    u(this, e), this.vueVM = t;
                }
                return c(e, [ {
                    key: "getHandle",
                    value: function(e) {
                        var t = e.type, n = e.target;
                        void 0 === n && (n = {});
                        var i = (e.currentTarget || n).dataset;
                        void 0 === i && (i = {});
                        var r = i.comkey;
                        void 0 === r && (r = "");
                        var o = i.eventid, a = -1 !== r.indexOf("_") ? "_" : ",", s = P(this.vueVM, r.split(a), a);
                        if (s) {
                            var u = C(s._vnode, o, w[t] || [ t ]);
                            if (u.length) {
                                var c = u[0];
                                if (c.isProxied) return c.proxiedName;
                                try {
                                    var l = ("" + c).replace("\n", "");
                                    if (l.match(_)) {
                                        var g = _.exec(l);
                                        if (g && g.length > 1) return g[1];
                                    }
                                } catch (e) {}
                                return c.name;
                            }
                        }
                    }
                }, {
                    key: "handleEvent",
                    value: function(e) {
                        var t, n = e.type, i = (e.currentTarget || e.target).dataset;
                        return (i.eventOpts || i["event-opts"]).forEach(function(e) {
                            var i = e[0], r = e[1];
                            i = (i = i.charAt(0) === E ? i.slice(1) : i).charAt(0) === S ? i.slice(1) : i, r && O(n, i) && r.forEach(function(e) {
                                t = e[0];
                            });
                        }), t;
                    }
                } ]), e;
            }();
            function T() {}
            var A = T.prototype, j = t.EventEmitter;
            function G(e, t) {
                for (var n = e.length; n--; ) if (e[n].listener === t) return n;
                return -1;
            }
            function V(e) {
                return function() {
                    return this[e].apply(this, arguments);
                };
            }
            function L(e) {
                return "function" == typeof e || e instanceof RegExp || !(!e || "object" != l(e)) && L(e.listener);
            }
            A.getListeners = function(e) {
                var t, n, i = this._getEvents();
                if (e instanceof RegExp) for (n in t = {}, i) i.hasOwnProperty(n) && e.test(n) && (t[n] = i[n]); else t = i[e] || (i[e] = []);
                return t;
            }, A.flattenListeners = function(e) {
                var t, n = [];
                for (t = 0; e.length > t; t += 1) n.push(e[t].listener);
                return n;
            }, A.getListenersAsObject = function(e) {
                var t, n = this.getListeners(e);
                return n instanceof Array && ((t = {})[e] = n), t || n;
            }, A.addListener = function(e, t) {
                if (!L(t)) throw new TypeError("listener must be a function");
                var n, i = this.getListenersAsObject(e), r = "object" == l(t);
                for (n in i) i.hasOwnProperty(n) && -1 === G(i[n], t) && i[n].push(r ? t : {
                    listener: t,
                    once: !1
                });
                return this;
            }, A.on = V("addListener"), A.addOnceListener = function(e, t) {
                return this.addListener(e, {
                    listener: t,
                    once: !0
                });
            }, A.once = V("addOnceListener"), A.defineEvent = function(e) {
                return this.getListeners(e), this;
            }, A.defineEvents = function(e) {
                for (var t = 0; e.length > t; t += 1) this.defineEvent(e[t]);
                return this;
            }, A.removeListener = function(e, t) {
                var n, i, r = this.getListenersAsObject(e);
                for (i in r) r.hasOwnProperty(i) && -1 !== (n = G(r[i], t)) && r[i].splice(n, 1);
                return this;
            }, A.off = V("removeListener"), A.addListeners = function(e, t) {
                return this.manipulateListeners(!1, e, t);
            }, A.removeListeners = function(e, t) {
                return this.manipulateListeners(!0, e, t);
            }, A.manipulateListeners = function(e, t, n) {
                var i, r, o = e ? this.removeListener : this.addListener, a = e ? this.removeListeners : this.addListeners;
                if ("object" != l(t) || t instanceof RegExp) for (i = n.length; i--; ) o.call(this, t, n[i]); else for (i in t) t.hasOwnProperty(i) && (r = t[i]) && ("function" == typeof r ? o.call(this, i, r) : a.call(this, i, r));
                return this;
            }, A.removeEvent = function(e) {
                var t, n = l(e), i = this._getEvents();
                if ("string" === n) delete i[e]; else if (e instanceof RegExp) for (t in i) i.hasOwnProperty(t) && e.test(t) && delete i[t]; else delete this._events;
                return this;
            }, A.removeAllListeners = V("removeEvent"), A.emitEvent = function(e, t) {
                var n, i, r, o, a = this.getListenersAsObject(e);
                for (o in a) if (a.hasOwnProperty(o)) for (n = a[o].slice(0), r = 0; n.length > r; r++) !0 === (i = n[r]).once && this.removeListener(e, i.listener), 
                i.listener.apply(this, t || []) === this._getOnceReturnValue() && this.removeListener(e, i.listener);
                return this;
            }, A.trigger = V("emitEvent"), A.emit = function(e) {
                var t = Array.prototype.slice.call(arguments, 1);
                return this.emitEvent(e, t);
            }, A.setOnceReturnValue = function(e) {
                return this._onceReturnValue = e, this;
            }, A._getOnceReturnValue = function() {
                return !this.hasOwnProperty("_onceReturnValue") || this._onceReturnValue;
            }, A._getEvents = function() {
                return this._events || (this._events = {});
            }, T.noConflict = function() {
                return t.EventEmitter = j, T;
            };
            var q = new T();
            function M(e) {
                return null !== e && "[object Object]" === Object.prototype.toString.call(e) && Object.keys(e).length > 0;
            }
            var R = function() {
                function e(t) {
                    u(this, e), this.growingio = t, this.esid = 0, this.info = t.info;
                }
                return c(e, [ {
                    key: "setUserAttributes",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "setUserId",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "clearUserId",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "sendVisitEvent",
                    value: function(e, t) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "track",
                    value: function(e, t) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "_sendEvent",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                } ]), e;
            }(), D = {
                tap: "clck",
                longpress: "lngprss",
                longtap: "lngprss"
            }, H = function(e) {
                a(n, e);
                var t = s(n);
                function n(e) {
                    var i;
                    return u(this, n), i = t.call(this, e), i.growingio = e, i.info = e.info, i.currentPage = new b(), 
                    i.scene = null, i._sessionId = null, i.cs1 = null, i.lastPageEvent = null, i.lastVstArgs = void 0, 
                    i.lastCloseTime = null, i.lastScene = void 0, i.keepAlive = e.vdsConfig.keepAlive, 
                    i.isPauseSession = !1, i.isGettingUid = !1, i.esid = 0 === i.info.esid ? 1 : i.info.esid, 
                    i.uploadingMessages = [], i;
                }
                return c(n, [ {
                    key: "sessionId",
                    get: function() {
                        return null === this._sessionId && (this._sessionId = p.guid()), this._sessionId;
                    }
                }, {
                    key: "resetSessionId",
                    value: function() {
                        this._sessionId = null;
                    }
                }, {
                    key: "pauseSession",
                    value: function() {
                        this.isPauseSession = !0;
                    }
                }, {
                    key: "getVisitorId",
                    value: function() {
                        return this.info.uid;
                    }
                }, {
                    key: "getUserId",
                    value: function() {
                        return this.cs1;
                    }
                }, {
                    key: "getGioInfo",
                    value: function() {
                        return "giou=".concat(this.getVisitorId(), "&giocs1=").concat(this.getUserId(), "&gios=").concat(this.sessionId, "&gioprojectid=").concat(this.growingio.vdsConfig.projectId, "&gioappid=").concat(this.growingio.vdsConfig.appId, "&gioplatform=").concat(gioGlobal.platformConfig.platform);
                    }
                }, {
                    key: "setUserId",
                    value: function(e) {
                        var t = e + "";
                        t && 100 > t.length && (this.cs1 = t, q.emitEvent("setCs1", [ t ]), this.lastPageEvent && this._sendEvent(this.lastPageEvent));
                    }
                }, {
                    key: "clearUserId",
                    value: function() {
                        this.cs1 = null, q.emitEvent("clearCs1");
                    }
                }, {
                    key: "appListener",
                    value: function(e, t, n) {
                        var i = gioGlobal.platformConfig.lisiteners.app;
                        this.isPauseSession || (this.growingio.vdsConfig.debug && console.log("App.", t, Date.now()), 
                        t == i.appShow ? (q.emitEvent("appShow"), this._parseScene(n), !this.lastCloseTime || Date.now() - this.lastCloseTime > this.keepAlive || this.lastScene && this.scene !== this.lastScene ? (this.resetSessionId(), 
                        this.sendVisitEvent(n, this.growingio.vdsConfig.getLocation.type), this.lastVstArgs = n, 
                        this.useLastPageTime = !1, this.lastPageEvent = void 0) : this.lastPageEvent && (this.useLastPageTime = !0)) : t == i.appClose ? (this.lastScene = this.scene, 
                        this.growingio.forceFlush(), this.info.syncStorage(), this.isPauseSession || (this.lastCloseTime = Date.now(), 
                        this.sendVisitCloseEvent())) : t == i.appError && this.sendErrorEvent(n));
                    }
                }, {
                    key: "pageListener",
                    value: function(e, t, n) {
                        var i = gioGlobal.platformConfig.lisiteners.page;
                        if (this.growingio.vdsConfig.wepy && (e.route = e.$is), e.route || (e.route = this.info.getPagePath(e)), 
                        this.growingio.vdsConfig.debug && console.log("Page.", e.route, "#", t, Date.now()), 
                        t === i.pageShow) {
                            var r = h(e, "$page.query");
                            p.isEmpty(r) || "quickApp" !== gioGlobal.gio__platform || this.currentPage.addQuery(e, r), 
                            this.isPauseSession ? this.isPauseSession = !1 : (this.currentPage.touch(e), this.useLastPageTime && (this.currentPage.time = this.lastPageEvent.tm, 
                            this.useLastPageTime = !1), this.sendPage(e));
                        } else if (t === i.pageLoad) {
                            var o = n[0];
                            p.isEmpty(o) || "quickApp" === gioGlobal.gio__platform || this.currentPage.addQuery(e, o);
                        } else if (t === i.pageHide) this.growingio._observer && this.growingio._observer.disconnect(); else if (t === i.pageClose) this.currentPage.pvar["".concat(this.currentPage.path, "?").concat(this.currentPage.query)] = void 0; else if (t === i.shareApp) {
                            var a = null, s = null;
                            2 > n.length ? 1 === n.length && (n[0].from ? a = n[0] : n[0].title && (s = n[0])) : (a = n[0], 
                            s = n[1]), this.pauseSession(), this.sendPageShare(e, a, s);
                        } else "onTabItemTap" === t && this.sendTabClick(n[0]);
                    }
                }, {
                    key: "actionListener",
                    value: function(e, t) {
                        if (!h(e, "currentTarget.dataset.growingIgnore") && !h(e, "target.dataset.growingIgnore")) {
                            var n = gioGlobal.platformConfig.lisiteners.actions;
                            if ("_cmlEventProxy" !== t) {
                                if ("handleProxy" === t && this.growingio.vueRootVMs && this.growingio.vueRootVMs[this.currentPage.path]) {
                                    var i = new I(this.growingio.vueRootVMs[this.currentPage.path]).getHandle(e);
                                    i && (t = i);
                                }
                                if ("__e" === t && this.growingio.vueRootVMs && this.growingio.vueRootVMs[this.currentPage.path]) {
                                    var r = new I(this.growingio.vueRootVMs[this.currentPage.path]).handleEvent(e);
                                    r && (t = r);
                                }
                                if ("_proxy" === t && this.growingio.wepyRootVMs) {
                                    var o = e.currentTarget.dataset.wpyEvt, a = e.type;
                                    h(this, "growingio.wepyRootVMs.".concat(o, ".").concat(a)) && (t = this.growingio.wepyRootVMs[o][a]);
                                }
                                h(this, "growingio.taroRootVMs.".concat(t)) && (t = this.growingio.taroRootVMs[t]), 
                                this.growingio.vdsConfig.debug && console.log("Click on ", t, Date.now()), -1 !== n.click.indexOf(e.type) ? (this.sendClick(e, t), 
                                "getuserinfo" === e.type && h(e, "detail.userInfo") && this.setVisitor(e.detail.userInfo)) : -1 !== n.change.indexOf(e.type) ? this.sendChange(e, t) : -1 !== n.submit.indexOf(e.type) && this.sendSubmit(e, t);
                            }
                        }
                    }
                }, {
                    key: "sendVideoCstm",
                    value: function(e) {
                        this.track("video-".concat(e.type), e.var);
                    }
                }, {
                    key: "track",
                    value: function(e, t) {
                        if ("string" != typeof e || null === e || void 0 === e || 0 === e.length || !e.match(/^\w+$/) || 10 > parseInt(e[0])) console.warn("埋点格式不正确, 事件名只能包含数字，字母和下划线，且不以数字开头, 请参考文档"); else {
                            var n = {
                                t: "cstm",
                                ptm: this.currentPage.time,
                                p: this.currentPage.path,
                                q: this.currentPage.query,
                                n: e
                            };
                            M(t) && (n.var = t), this._sendEvent(n);
                        }
                    }
                }, {
                    key: "identify",
                    value: function(e, t) {
                        void 0 !== e && 0 !== e.length && (this.growingio.login(e), this._sendEvent({
                            t: "vstr",
                            var: {
                                openid: e,
                                unionid: t
                            }
                        }));
                    }
                }, {
                    key: "setVisitor",
                    value: function(e) {
                        M(e) && this._sendEvent({
                            t: "vstr",
                            var: e
                        });
                    }
                }, {
                    key: "setUser",
                    value: function(e) {
                        this.cs1 && M(e) && this._sendEvent({
                            t: "ppl",
                            var: e
                        });
                    }
                }, {
                    key: "setPage",
                    value: function(e) {
                        if (M(e)) {
                            var t = {
                                t: "pvar",
                                ptm: this.currentPage.time,
                                p: this.currentPage.path,
                                q: this.currentPage.query,
                                var: e
                            };
                            this.currentPage.touchRelatedPvarData(t), this._sendEvent(t);
                        }
                    }
                }, {
                    key: "setEvar",
                    value: function(e) {
                        M(e) && this._sendEvent({
                            t: "evar",
                            var: e
                        });
                    }
                }, {
                    key: "getLocation",
                    value: function(e) {
                        this.growingio.vdsConfig.getLocation.autoGet = !0, this.sendVisitEvent(this.lastVstArgs, e);
                    }
                }, {
                    key: "sendVisitEvent",
                    value: function(e, t) {
                        var n = this;
                        this.info.getSystemInfo().then(function(i) {
                            var r = i || {}, o = {
                                t: "vst",
                                tm: Date.now(),
                                av: n.info.sdkVer,
                                db: r.brand,
                                dm: r.model && r.model.replace(/<.*>/, ""),
                                sh: p.getScreenHeight(r),
                                sw: p.getScreenWidth(r),
                                os: p.getOS(r.platform),
                                osv: p.getOSV(r.version),
                                l: r.language
                            };
                            if (n.growingio.vdsConfig.appVer && (o.cv = n.growingio.vdsConfig.appVer + ""), 
                            e.length > 0) {
                                var a = e[0];
                                o.p = a.path || n.info.getPagePath(), p.isEmpty(a.query) || (o.q = n.currentPage._getQuery(a.query)), 
                                o.ch = "scn:".concat(n.info.scnPrefix).concat(n.scene), "quickapp" === n.info.platform ? o.rf = n.info.appSource.packageName : a.referrerInfo && a.referrerInfo.appId && h(a, "referrerInfo.appId") && (o.rf = a.referrerInfo.appId), 
                                n.info.getNetworkType().then(function(e) {
                                    if (e && (o.nt = e.networkType, n._sendEvent(o), n.growingio.vdsConfig.getLocation.autoGet)) {
                                        var i = JSON.parse(JSON.stringify(o));
                                        t && -1 !== [ "wgs84", "gcj02", 0, 1, 2 ].indexOf(t) || (t = "my" === gioGlobal.gio__platform ? 0 : "wgs84"), 
                                        n.info.getLocation(t).then(function(e) {
                                            e && (i.lat = e.latitude, i.lng = e.longitude, n._sendEvent(i));
                                        });
                                    }
                                });
                            }
                        });
                    }
                }, {
                    key: "sendVisitCloseEvent",
                    value: function() {
                        this._sendEvent({
                            t: "cls",
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        });
                    }
                }, {
                    key: "sendErrorEvent",
                    value: function(e) {
                        if (e && e.length > 0) {
                            var t = e[0];
                            if ("string" != typeof t) return;
                            var n, i = t.split("\n");
                            if (i && i.length > 1) {
                                var r = i[1].split(";");
                                if (r && r.length > 1) {
                                    var o = r[1].match(/at ([^ ]+) page (.*) function/);
                                    n = {
                                        key: i[0],
                                        error: r[0]
                                    }, o && o.length > 2 && (n.page = o[1], n.function = o[2]);
                                }
                            } else n = {
                                error: i && i[0]
                            };
                            this._sendEvent({
                                t: "cstm",
                                ptm: this.currentPage.time,
                                p: this.currentPage.path,
                                q: this.currentPage.query,
                                n: "onError",
                                var: n
                            });
                        }
                    }
                }, {
                    key: "sendPage",
                    value: function(e) {
                        var t = this, n = {
                            t: "page",
                            tm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        };
                        n.rp = this.lastPageEvent ? this.lastPageEvent.p : this.scene ? "scn:".concat(this.info.scnPrefix).concat(this.scene) : null;
                        var i = this.info.getPageTitle(e);
                        i && i.length > 0 && (n.tl = i), this._sendEvent(n), this.lastPageEvent = n;
                        var r = this.currentPage.pvar["".concat(this.currentPage.path, "?").concat(this.currentPage.query)];
                        r && r.length > 0 && r.map(function(e) {
                            e.ptm = t.currentPage.time, t._sendEvent(e);
                        });
                    }
                }, {
                    key: "sendPageShare",
                    value: function(e, t, n) {
                        this._sendEvent({
                            t: "cstm",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query,
                            n: "onShareAppMessage",
                            var: {
                                from: t ? t.from : void 0,
                                target: t && t.target ? t.target.id : void 0,
                                title: n ? n.title : void 0,
                                path: n ? decodeURI(n.path) : void 0
                            }
                        });
                    }
                }, {
                    key: "sendClick",
                    value: function(e, t) {
                        var n = {
                            t: D[e.type] || "clck",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        }, i = e.currentTarget || e.target, r = i.id;
                        (!r || "swan" === gioGlobal.gio__platform && /^_[0-9a-f]+/.test(r)) && (r = "");
                        var o = {
                            x: "".concat(r, "#").concat(t)
                        };
                        i.dataset.title && (o.v = i.dataset.title), i.dataset.src && (o.h = i.dataset.src), 
                        void 0 !== i.dataset.index && (o.idx = /^[\d]+$/.test(i.dataset.index) ? parseInt(i.dataset.index) : -1), 
                        n.e = [ o ], this._sendEvent(n);
                    }
                }, {
                    key: "sendSubmit",
                    value: function(e, t) {
                        var n = {
                            t: "sbmt",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        }, i = (e.currentTarget || e.target).id;
                        (!i || "swan" === gioGlobal.gio__platform && /^_[0-9a-f]+/.test(i)) && (i = ""), 
                        n.e = [ {
                            x: "".concat(i, "#").concat(t)
                        } ], this._sendEvent(n);
                    }
                }, {
                    key: "sendChange",
                    value: function(e, t) {
                        var n = {
                            t: "chng",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        }, i = e.currentTarget || e.target, r = i.id;
                        (!r || "swan" === gioGlobal.gio__platform && /^_[0-9a-f]+/.test(r)) && (r = "");
                        var o = {
                            x: "".concat(r, "#").concat(t)
                        }, a = h(e, "detail.value") || h(e, "target.attr.value");
                        (i.dataset.growingTrack || i.dataset.growingtrack) && ("boolean" == typeof a || a && 0 !== a.length) && ("[object Array]" === Object.prototype.toString.call(a) ? (a = a.join(",")) && (o.v = a) : o.v = a), 
                        "change" === e.type && "autoplay" === h(e, "detail.source") || (n.e = [ o ], this._sendEvent(n));
                    }
                }, {
                    key: "sendTabClick",
                    value: function(e) {
                        var t = {
                            t: "clck",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query,
                            e: [ {
                                x: "#onTabItemTap",
                                v: e.text,
                                idx: e.index,
                                h: "string" == typeof e.pagePath ? e.pagePath : JSON.stringify(e.pagePath)
                            } ]
                        };
                        this._sendEvent(t);
                    }
                }, {
                    key: "_sendEvent",
                    value: function(e) {
                        var t = this;
                        if (this.info.uid && this.esid) {
                            var n = this._buildEvent(e, this.info);
                            this.growingio.upload(n);
                        } else if (this.isGettingUid) this.uploadingMessages.push(e); else {
                            this.isGettingUid = !0;
                            var i = this.info.getStorage(this.info.uidKey), r = this.info.getStorage(this.info.esidKey);
                            Promise.all([ i, r ]).then(function(n) {
                                var i = o(n, 2), r = i[0], a = i[1];
                                r || (r = p.guid()), a || (a = 1), t.info.uid = r, t.info.esid = a, t.isGettingUid = !1;
                                var s = t._buildEvent(e, t.info);
                                for (t.growingio.upload(s); 0 !== t.uploadingMessages.length; ) {
                                    var u = t.uploadingMessages.shift();
                                    u = t._buildEvent(u, t.info), t.growingio.upload(u);
                                }
                            });
                        }
                    }
                }, {
                    key: "_buildEvent",
                    value: function(e, t) {
                        if (e.u = t.uid, e.s = this.sessionId, e.tm = e.tm || Date.now(), e.d = this.growingio.vdsConfig.appId, 
                        e.b = t.platform, null !== this.cs1 && (e.cs1 = this.cs1), e.var) {
                            var n = e.var;
                            Object.keys(n).forEach(function(t) {
                                "string" != typeof n[t] && (e.var[t] = JSON.stringify(n[t]));
                            });
                        }
                        return e.esid = this.esid++, e;
                    }
                }, {
                    key: "_parseScene",
                    value: function(e) {
                        if ("quickapp" === this.info.platform) {
                            var t = this.info.getAppSource(), n = t.extra || {}, i = t.type || "";
                            this.scene = i, this.setVisitor({
                                extra: JSON.stringify(n)
                            });
                        } else if (e.length > 0) {
                            var r = e[0];
                            this.scene = r.query && r.query.wxShoppingListScene ? r.query.wxShoppingListScene : r.scene ? r.scene : "NA";
                        }
                    }
                } ]), n;
            }(R), B = function() {
                function e(t) {
                    u(this, e), this.growing = t, this._uid = void 0, this._esid = void 0, this._gioId = void 0, 
                    this._userId = void 0, this._systemInfo = null, this.uidKey = "_growing_uid_", this.esidKey = "_growing_esid_", 
                    this.gioIdKey = "_growing_gioId_", this.userIdKey = "_growing_userId_", this.platform = gioGlobal.platformConfig.platform, 
                    this.sdkVer = gioGlobal.platformConfig.sdkVer, this.scnPrefix = gioGlobal.platformConfig.scnPrefix, 
                    "quickapp" !== gioGlobal.platformConfig.platform && this.initUserInfo();
                }
                return c(e, [ {
                    key: "esid",
                    get: function() {
                        return this._esid;
                    },
                    set: function(e) {
                        this._esid = e, this.setStorage(this.esidKey, this._esid);
                    }
                }, {
                    key: "uid",
                    get: function() {
                        return this._uid;
                    },
                    set: function(e) {
                        this._uid = e, this.setStorage(this.uidKey, this._uid);
                    }
                }, {
                    key: "gioId",
                    get: function() {
                        return this._gioId;
                    },
                    set: function(e) {
                        this._gioId = e, this.setStorage(this.gioIdKey, this._gioId);
                    }
                }, {
                    key: "userId",
                    get: function() {
                        return this._userId;
                    },
                    set: function(e) {
                        this._userId = e, this.setStorage(this.userIdKey, this._userId);
                    }
                }, {
                    key: "systemInfo",
                    get: function() {
                        return this._systemInfo;
                    }
                }, {
                    key: "initUserInfo",
                    value: function() {
                        this.uid = this.getStorageSync(this.uidKey), this.esid = +this.getStorageSync(this.esidKey);
                    }
                }, {
                    key: "syncStorage",
                    value: function() {
                        var e = this;
                        this.getStorage(this.uidKey).then(function(t) {
                            t || e.setStorage(e.uidKey, e._uid);
                        });
                    }
                }, {
                    key: "getAppId",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getAppSource",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getPageTitle",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getPagePath",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getStorage",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getStorageSync",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "setStorage",
                    value: function(e, t) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getSystemInfo",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getNetworkType",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getLocation",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "request",
                    value: function(e) {
                        e.url, e.header, e.method, e.data, e.success, e.fail;
                        throw Error("this a interface function");
                    }
                }, {
                    key: "collectImp",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "initShareAppMessage",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getCurrentPage",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getQuery",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getReferrer",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getInitPath",
                    value: function() {
                        throw Error("this a interface function");
                    }
                } ]), e;
            }(), U = function(e) {
                a(n, e);
                var t = s(n);
                function n(e) {
                    var i;
                    return u(this, n), i = t.call(this, e), i.growingio = e, i;
                }
                return c(n, [ {
                    key: "getAppId",
                    value: function() {
                        this._systemInfo || (this._systemInfo = wx.getSystemInfoSync());
                        var e = void 0;
                        return 0 > p.compareVersion(this._systemInfo.SDKVersion, "2.2.2") || (e = wx.getAccountInfoSync().miniProgram.appId), 
                        e;
                    }
                }, {
                    key: "getPagePath",
                    value: function() {
                        return this.getCurrentPage().route;
                    }
                }, {
                    key: "getCurrentPage",
                    value: function() {
                        var e = getCurrentPages();
                        return e[e.length - 1];
                    }
                }, {
                    key: "getPageTitle",
                    value: function(e) {
                        var t = "";
                        try {
                            if (e.data.title && e.data.title.length > 0 && (t = Array.isArray(e.data.title) ? e.data.title.join(" ") : e.data.title), 
                            0 === t.length && __wxConfig) {
                                if (__wxConfig.tabBar) {
                                    var n = __wxConfig.tabBar.list.find(function(t) {
                                        return t.pathPath == e.route || t.pagePath == "".concat(e.route, ".html");
                                    });
                                    n && n.text && (t = n.text);
                                }
                                if (0 == t.length) {
                                    var i = __wxConfig.page[e.route] || __wxConfig.page["".concat(e.route, ".html")];
                                    t = i ? i.window.navigationBarTitleText : __wxConfig.global.window.navigationBarTitleText;
                                }
                            }
                        } catch (e) {
                            return "";
                        }
                        return t;
                    }
                }, {
                    key: "getStorage",
                    value: function(e) {
                        return new Promise(function(t) {
                            wx.getStorage({
                                key: e,
                                success: function(e) {
                                    return t(e.data);
                                },
                                fail: function() {
                                    return t("");
                                }
                            });
                        });
                    }
                }, {
                    key: "getStorageSync",
                    value: function(e) {
                        return wx.getStorageSync(e);
                    }
                }, {
                    key: "setStorage",
                    value: function(e, t) {
                        wx.setStorage({
                            key: e,
                            data: t
                        });
                    }
                }, {
                    key: "getSystemInfo",
                    value: function() {
                        var e = this;
                        return new Promise(function(t) {
                            wx.getSystemInfo({
                                success: function(n) {
                                    e._systemInfo = n, t(n);
                                },
                                fail: function() {
                                    return t(null);
                                }
                            });
                        });
                    }
                }, {
                    key: "getNetworkType",
                    value: function() {
                        return new Promise(function(e) {
                            wx.getNetworkType({
                                success: function(t) {
                                    return e(t);
                                },
                                fail: function() {
                                    return e(null);
                                }
                            });
                        });
                    }
                }, {
                    key: "getSetting",
                    value: function() {
                        return new Promise(function(e) {
                            wx.getSetting({
                                success: e,
                                fail: e
                            });
                        });
                    }
                }, {
                    key: "getLocation",
                    value: function(e) {
                        return new Promise(function(t) {
                            wx.getLocation({
                                type: e,
                                success: function(e) {
                                    return t(e);
                                },
                                fail: function() {
                                    return t(null);
                                }
                            });
                        });
                    }
                }, {
                    key: "request",
                    value: function(e) {
                        var t = e.url, n = e.header, i = e.method, r = e.data, o = e.success, a = e.fail, s = e.complete;
                        return wx.request({
                            url: t,
                            header: n,
                            method: i,
                            data: r,
                            success: o,
                            fail: a,
                            complete: s
                        });
                    }
                }, {
                    key: "collectImp",
                    value: function(e) {
                        var t = this, n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : null;
                        this.growingio.vdsConfig.vue && (e = e.$mp.page), this.growingio.vdsConfig.taro && (e = e.$scope);
                        var i = {};
                        this.growingio._observer && this.growingio._observer.disconnect(), this.growingio._observer = e.isComponent ? e.createIntersectionObserver({
                            observeAll: !0
                        }) : wx.createIntersectionObserver(e, {
                            observeAll: !0
                        }), (n ? this.growingio._observer.relativeTo(n) : this.growingio._observer.relativeToViewport()).observe(".growing_collect_imp", function(e) {
                            if (e.id && !i[e.id]) {
                                var n = d(e.dataset), r = n.eventId, o = n.properties;
                                r && e.id && !i[e.id] && (t.growingio.observer.track(r, o), i[e.id] = !0);
                            }
                        });
                    }
                }, {
                    key: "setStorageSync",
                    value: function(e, t) {
                        wx.setStorageSync(e, JSON.stringify(t));
                    }
                }, {
                    key: "removeStorageSync",
                    value: function(e) {
                        wx.removeStorageSync(e);
                    }
                }, {
                    key: "navigateTo",
                    value: function(e) {
                        wx.navigateTo(e);
                    }
                }, {
                    key: "switchTab",
                    value: function(e) {
                        wx.switchTab(e);
                    }
                } ]), n;
            }(B), $ = function() {
                function e(t) {
                    u(this, e), this.growingio = t, this.messageQueue = [], this.uploadingQueue = [], 
                    this.uploadTimer = null, this.projectId = this.growingio.vdsConfig.projectId, this.appId = this.growingio.vdsConfig.appId, 
                    this.host = this.growingio.vdsConfig.host, this.url = "".concat(this.host, "/projects/").concat(this.projectId, "/apps/").concat(this.appId, "/collect");
                }
                return c(e, [ {
                    key: "upload",
                    value: function(e) {
                        var t = this;
                        this.messageQueue.push(e);
                        var n = this.messageQueue.length;
                        n > 100 && (this.messageQueue = this.messageQueue.slice(n - 100)), this.uploadTimer || (this.uploadTimer = setTimeout(function() {
                            t._flush(), t.uploadTimer = null;
                        }, 1e3));
                    }
                }, {
                    key: "forceFlush",
                    value: function() {
                        this.uploadTimer && (clearTimeout(this.uploadTimer), this.uploadTimer = null), this._flush();
                    }
                }, {
                    key: "_flush",
                    value: function() {
                        var e = this;
                        this.uploadingQueue = this.messageQueue.slice(), this.messageQueue = [], this.uploadingQueue.length > 0 && this.growingio.info.request({
                            url: "".concat(this.url, "?stm=").concat(Date.now()),
                            header: {
                                "content-type": "application/json"
                            },
                            method: "POST",
                            data: this.uploadingQueue,
                            success: function() {
                                e.messageQueue.length > 0 && e._flush();
                            },
                            fail: function(t) {
                                204 !== t.status && (e.messageQueue = e.uploadingQueue.concat(e.messageQueue));
                            }
                        });
                    }
                } ]), e;
            }(), K = {
                wx: {
                    name: "Weixin",
                    path: "./weixin"
                },
                qq: {
                    name: "QQ",
                    path: "./qq"
                },
                my: {
                    name: "Alipay",
                    path: "./alipay"
                },
                swan: {
                    name: "Baidu",
                    path: "./baidu"
                },
                tt: {
                    name: "Bytedance",
                    path: "./bytedance"
                },
                quickApp: {
                    name: "Quickapp",
                    path: "./quickApp"
                },
                frame: {
                    name: "Frame",
                    path: "./multipleFrame"
                }
            }, N = Object.assign({}, K.wx, {
                platform: "MinP",
                scnPrefix: "",
                appHandlers: [ "onShow", "onHide", "onError" ],
                pageHandlers: [ "onLoad", "onShow", "onShareAppMessage", "onTabItemTap", "onHide", "onUnload" ],
                actionEventTypes: [ "onclick", "tap", "longpress", "blur", "change", "submit", "confirm", "getuserinfo", "getphonenumber", "contact" ],
                originalApp: App,
                originalPage: Page,
                originalComponent: Component,
                originalBehavior: Behavior,
                canHook: !0,
                hooks: {
                    App: !0,
                    Page: !0,
                    Component: !0,
                    Behavior: !0
                },
                lisiteners: {
                    app: {
                        appShow: "onShow",
                        appClose: "onHide",
                        appError: "onError"
                    },
                    page: {
                        pageLoad: "onLoad",
                        pageShow: "onShow",
                        pageHide: "onHide",
                        pageClose: "onUnload",
                        tabTap: "onTabItemTap",
                        shareApp: "onShareAppMessage"
                    },
                    actions: {
                        click: [ "onclick", "tap", "longpress", "getuserinfo", "getphonenumber", "contact" ],
                        change: [ "blur", "change", "confirm" ],
                        submit: [ "submit" ]
                    }
                }
            }), F = Object.assign({}, N, {
                sdkVer: "3.4.1"
            }), Q = function() {
                function e(t) {
                    u(this, e), this.growingio = t;
                }
                return c(e, [ {
                    key: "setDataCollect",
                    value: function(e) {
                        this.growingio.vdsConfig.dataCollect = e;
                    }
                }, {
                    key: "enableDebug",
                    value: function(e) {
                        e && console && (this.growingio.vdsConfig.debug = e);
                    }
                }, {
                    key: "setTrackerScheme",
                    value: function(e) {
                        var t = (e + "").toLocaleLowerCase();
                        "http" !== t && "https" !== t || (this.growingio.vdsConfig.scheme = "".concat(e, "://"));
                    }
                }, {
                    key: "setTrackerHost",
                    value: function(e) {
                        v(e) && (this.growingio.vdsConfig.host = e);
                    }
                } ]), e;
            }(), W = 3e5, J = function() {
                function e() {
                    u(this, e), this.uploadingMessages = [], this.start = !1;
                }
                return c(e, [ {
                    key: "init",
                    value: function(e, t, n) {
                        this.start || (t && "string" != typeof t && (n = t, t = ""), t || n || (t = "", 
                        n = {}), "alip" === F.platform && (n.vue || n.taro || n.cml || n.wepy) && (F.canHook = !0), 
                        n.usePlugin && (F.canHook = !1), this.vdsConfig = {
                            projectId: e,
                            appId: t,
                            appVer: n.version || "",
                            debug: n.debug || !1,
                            forceLogin: n.forceLogin || !1,
                            followShare: void 0 === n.followShare || n.followShare,
                            usePlugin: n.usePlugin || !1,
                            getLocation: {
                                autoGet: ("object" == l(n.getLocation) ? n.getLocation.autoGet : n.getLocation) || !1,
                                type: "object" == l(n.getLocation) && n.getLocation.type || "wgs84"
                            },
                            dataCollect: !("boolean" == typeof n.stopTrack && n.stopTrack || "boolean" == typeof n.dataCollect && !n.dataCollect),
                            keepAlive: +n.keepAlive || W,
                            vue: n.vue || !1,
                            taro: n.taro || !1,
                            cml: n.cml || !1,
                            wepy: n.wepy || !1,
                            host: n.host && n.host.indexOf("http") >= 0 ? "https://".concat(n.host.slice(n.host.indexOf("://") + 3)) : "https://wxapi.growingio.com",
                            sdkVer: F.sdkVer
                        }, gioGlobal.vdsConfig = this.vdsConfig, gioGlobal.platformConfig = F, this.info = new U(this), 
                        t || (this.vdsConfig.appId = this.info.getAppId() || e), this.observer = new H(this), 
                        this.uploader = new $(this), this.config = new Q(this), this.start = !0, n.vue && (this.vueRootVMs = {}, 
                        this._proxyVue(n.vue)), n.taro && (this.taroRootVMs = {}, this._proxyTaro(n.taro)), 
                        n.cml && (gioGlobal.platformConfig.hooks.Component = !1, this._proxyCml(n.cml)), 
                        n.wepy && (this.wepyRootVMs = {}, this._proxyWepy(n.wepy)), "quickapp" === gioGlobal.platformConfig.platform && this.info.initShareAppMessage(this), 
                        this._start());
                    }
                }, {
                    key: "setConfig",
                    value: function(e) {
                        this.init(e.projectId, e.appId, e);
                    }
                }, {
                    key: "setVue",
                    value: function(e) {
                        this.vueRootVMs || (this.vueRootVMs = {}), this.vdsConfig.vue = !0, this._proxyVue(e);
                    }
                }, {
                    key: "_proxyVue",
                    value: function(e) {
                        if (void 0 !== e.mixin) {
                            var t = this;
                            e.mixin({
                                created: function() {
                                    if (this.$options.methods) for (var e = Object.keys(this.$options.methods), t = 0, n = Object.keys(this); t < n.length; t++) {
                                        var i = n[t];
                                        0 > e.indexOf(i) || "function" != typeof this[i] || (Object.defineProperty(this[i], "proxiedName", {
                                            value: i
                                        }), Object.defineProperty(this[i], "isProxied", {
                                            value: !0
                                        }));
                                    }
                                },
                                beforeMount: function() {
                                    var e = this.$root;
                                    e.$mp && "page" === e.$mp.mpType ? e.$mp.page && (t.vueRootVMs[e.$mp.page.route] = e) : "page" === e.mpType && "page" === this.mpType && e.$mp.page && (t.vueRootVMs[e.$mp.page.route || e.$mp.page.is] = e, 
                                    -1 !== [ "wx", "qq", "tt" ].indexOf(gioGlobal.gio__platform) && m.instrumentPageComponent(e.$mp.page));
                                }
                            });
                        }
                    }
                }, {
                    key: "_proxyTaro",
                    value: function(e) {
                        var t = this, n = e.createComponent, i = this.vdsConfig.usePlugin;
                        if (e.createComponent = function(e, r) {
                            for (var o = e; o && o.prototype; ) {
                                for (var a = Object.keys(Object.getOwnPropertyDescriptors(o.prototype) || {}), s = 0; a.length > s; s++) if (a[s].startsWith("func__")) {
                                    var u = o.name, c = a[s].slice(6);
                                    t.taroRootVMs[a[s]] = u + "_" + ("" + e.prototype[a[s]]).match(/this\.__triggerPropsFn\("(.+)",/)[1] + "_" + c;
                                }
                                o = Object.getPrototypeOf(o);
                            }
                            var l = n(e, r), g = -1 !== [ "MinP", "qq" ].indexOf(F.platform), p = g ? l && l.methods : l;
                            return i ? (m.instrument(p), r && m.instrumentPageComponent(p)) : r && g && m.instrumentPageComponent(p), 
                            l;
                        }, i) {
                            var r = e.createApp;
                            e.createApp = function(e) {
                                var t = r(e);
                                return t._growing_app_ = !0, m.instrument(t), t;
                            };
                        }
                    }
                }, {
                    key: "_proxyCml",
                    value: function(e) {
                        var t = e.createApp, n = e.createComponent;
                        e.createApp = function(e) {
                            return e._growing_app_ = !0, t(m.instrument(e));
                        }, e.createComponent = function(e) {
                            return n(e.data && e.data.isComponent ? Object.assign({}, e, {
                                methods: m.instrument(e.methods)
                            }) : e);
                        };
                    }
                }, {
                    key: "_proxyWepy",
                    value: function(e) {
                        var t = this, n = e.page, i = function(e) {
                            for (var n = Object.keys(e), i = 0; n.length > i; i++) for (var r = Object.keys(e[n[i]]), o = 0; r.length > o; o++) if ("function" == typeof e[n[i]][r[o]]) {
                                var a = ("" + e[n[i]][r[o]]).match(/_vm\.(.+)\(.*\)/);
                                a && a[1] && (t.wepyRootVMs[n[i]] || (t.wepyRootVMs[n[i]] = {}), t.wepyRootVMs[n[i]][r[o]] = a[1]), 
                                t.vdsConfig.usePlugin && (e[n[i]][r[o]] = m.hook("_proxy", e[n[i]][r[o]]));
                            }
                        };
                        e.page = function(e, t) {
                            return t.handlers && i(t.handlers), m.instrumentPageComponent(e), n(e, t);
                        };
                        var r = e.component;
                        if (e.component = function(e, t) {
                            return t.handlers && i(t.handlers), r(e, t);
                        }, this.vdsConfig.usePlugin) {
                            var o = e.app;
                            e.app = function(e, t) {
                                return e._growing_app_ = !0, o(m.instrument(e), t);
                            };
                        }
                    }
                }, {
                    key: "_start",
                    value: function() {
                        m.initInstrument(this.observer);
                        try {
                            gioGlobal && F.canHook && (F.hooks.App && (gioGlobal.App = App), F.hooks.Page && (gioGlobal.Page = Page), 
                            F.hooks.Component && (gioGlobal.Component = Component), F.hooks.Behavior && (gioGlobal.Behavior = Behavior));
                        } catch (e) {}
                    }
                }, {
                    key: "setDataCollect",
                    value: function(e) {
                        this.config.setDataCollect(e);
                    }
                }, {
                    key: "login",
                    value: function(e) {
                        if (this.vdsConfig.forceLogin) {
                            this.info.uid = e, this.vdsConfig.forceLogin = !1;
                            var t, n = r(this.uploadingMessages);
                            try {
                                for (n.s(); !(t = n.n()).done; ) {
                                    var i = t.value;
                                    i.u = e, this.upload(i);
                                }
                            } catch (e) {
                                n.e(e);
                            } finally {
                                n.f();
                            }
                        }
                    }
                }, {
                    key: "upload",
                    value: function(e) {
                        this.vdsConfig.dataCollect && (this.vdsConfig.forceLogin ? this.uploadingMessages.push(e) : (this.vdsConfig.debug && console.info("generate new event", JSON.stringify(e, 0, 2)), 
                        q.emitEvent("upload", [ e ]), this.uploader.upload(e)));
                    }
                }, {
                    key: "forceFlush",
                    value: function() {
                        this.info.esid = this.observer.esid, this.uploader.forceFlush();
                    }
                }, {
                    key: "proxy",
                    value: function(e, t) {
                        try {
                            if ("setVue" === e) this.setVue(t[0]); else if ("setDataCollect" === e) this.setDataCollect(t[0]); else if ("setStopTrack" === e) this.setDataCollect(!t[0]); else if ("collectImp" === e) this.collectImp(t[0], t[1]); else if (this.observer && this.observer[e]) return this.observer[e].apply(this.observer, t);
                        } catch (e) {
                            console.error(e);
                        }
                    }
                }, {
                    key: "collectImp",
                    value: function(e) {
                        var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : null;
                        this.info.collectImp(e, t);
                    }
                } ]), e;
            }();
            function z(e, t) {
                if (l(e) != l(t)) return !1;
                if ("string" == typeof e || "number" == typeof e || "boolean" == typeof e || "function" == typeof e || void 0 == e || void 0 == t) return Object.is(e, t);
                if (Array.isArray(e) && Array.isArray(t)) return e.length === t.length && e.every(function(e, n) {
                    return z(e, t[n]);
                });
                if ("[object Object]" === Object.prototype.toString.call(e) && "[object Object]" === Object.prototype.toString.call(t)) {
                    var n = Object.keys(e), i = Object.keys(t);
                    return !(!n.every(function(n) {
                        return t.hasOwnProperty(n) && z(e[n], t[n]);
                    }) || !i.every(function(n) {
                        return e.hasOwnProperty(n) && z(t[n], e[n]);
                    }));
                }
                return !1;
            }
            var Z = function(e, t) {
                if ("string" == typeof t) {
                    "?" !== t[0] && (t = "?" + t), e = e.replace(/[\[\]]/g, "\\$&");
                    var n = RegExp("[?&]" + e + "(=([^&#]*)|&|#|$)").exec(t);
                    return n ? n[2] ? decodeURIComponent(n[2].replace(/\+/g, " ")) : "" : null;
                }
            }, X = function() {
                function e(t) {
                    u(this, e), this.growingio = t, this.namespace = "push-user-status", this.userTagDuration = 432e7, 
                    this.eventTagDuration = 864e5, this.handleCs1 = this.handleCs1.bind(this), this.handleClearCs1 = this.handleClearCs1.bind(this), 
                    this.handleEvent = this.handleEvent.bind(this), this.addEventListener();
                }
                return c(e, [ {
                    key: "addEventListener",
                    value: function() {
                        q.on("appOpen", this.handleEvent), q.on("upload", this.handleEvent), q.on("setCs1", this.handleCs1), 
                        q.on("clearCs1", this.handleClearCs1);
                    }
                }, {
                    key: "handleCs1",
                    value: function(e) {
                        e !== this.get("cs1") && (this.set("cs1", e), this.set("bcs", void 0), q.emit("cs1Refresh"));
                    }
                }, {
                    key: "handleClearCs1",
                    value: function() {
                        this.set("cs1", void 0), this.set("bcs", void 0);
                    }
                }, {
                    key: "handleEvent",
                    value: function(e) {
                        if (e) switch (e.t) {
                          case "vst":
                          case "vstr":
                          case "ppl":
                            this.storeFilters(e, this.generateEventKey.bind(this, "userAttrs"), this.formatUserFilterVars);
                            break;

                          case "cstm":
                            this.storeFilters(e, this.generateEventKey.bind(this, "triggerAttrs"), this.formatEventFilterVars);

                          case "page":
                            this.setIsPreview(e);
                        }
                    }
                }, {
                    key: "setIsPreview",
                    value: function(e) {
                        if (e.q) {
                            var t = Z("scene", e.q);
                            if (t) {
                                var n = Z("gioMessageId", t);
                                if (n) {
                                    var i = {
                                        s: "splash",
                                        pw: "popupWindow",
                                        p: "push",
                                        b: "banner",
                                        ab: "abTest"
                                    }[Z("mt", t)] || "";
                                    gioGlobal.__growing__.marketingPreview = {
                                        messageId: n,
                                        msgType: i
                                    };
                                }
                            }
                        }
                    }
                }, {
                    key: "storeFilters",
                    value: function(e, t, n) {
                        var r = t(), o = this.get(r, this.eventTagDuration) || [], a = n.call(this, e), s = [].concat(i(o), i(a));
                        this.set(r, s);
                    }
                }, {
                    key: "formatUserFilterVars",
                    value: function(e) {
                        var t = e.var;
                        return t ? Object.keys(t).map(function(e) {
                            return {
                                key: e,
                                value: t[e]
                            };
                        }) : [];
                    }
                }, {
                    key: "formatEventFilterVars",
                    value: function(e) {
                        var t = e.var;
                        return [ {
                            key: e.n,
                            value: "",
                            event_variable: t ? Object.keys(t).map(function(e) {
                                return {
                                    key: e,
                                    value: t[e]
                                };
                            }) : []
                        } ];
                    }
                }, {
                    key: "generateEventKey",
                    value: function(e) {
                        return "".concat(e, "#").concat(this.get("cs1") || "");
                    }
                }, {
                    key: "_get",
                    value: function(e) {
                        return this.growingio.info.getStorageSync("".concat(this.namespace, "#").concat(e));
                    }
                }, {
                    key: "getUserAttrs",
                    value: function() {
                        var e = this.generateEventKey("userAttrs");
                        return this.get(e) || [];
                    }
                }, {
                    key: "getTriggerAttrs",
                    value: function() {
                        var e = this.generateEventKey("triggerAttrs");
                        return this.get(e) || [];
                    }
                }, {
                    key: "set",
                    value: function(e, t) {
                        var n = this._get(e), i = new Date();
                        i.setHours(0), i.setMinutes(0), i.setSeconds(0);
                        var r = {
                            startAt: i.getTime(),
                            value: t
                        };
                        n && z(r.value, JSON.parse(n).value) || this.growingio.info.setStorageSync("".concat(this.namespace, "#").concat(e), r);
                    }
                }, {
                    key: "get",
                    value: function(e) {
                        var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : this.userTagDuration, n = this._get(e);
                        if (n) {
                            var i = JSON.parse(n);
                            return Date.now() > i.startAt + t ? void 0 : i.value;
                        }
                    }
                } ]), e;
            }();
            try {
                var Y = "wx";
                f(Y), "frame" !== Y && (gioGlobal.gio__platform = Y);
            } catch (g) {}
            var ee = new J(), te = function() {
                var e = arguments[0];
                if (e) {
                    var t = 2 > arguments.length ? [] : [].slice.call(arguments, 1);
                    if ("init" === e) {
                        if (gioGlobal.vdsConfig) return void console.warn("SDK已经初始化成功，请检查是否加载过其他平台sdk");
                        if (1 > t.length) return void console.log('初始化 GrowingIO SDK 失败。请使用 gio("init", "你的GrowingIO项目ID", "你的应用APP_ID", options);');
                        ee.init(t[0], t[1], t[2]);
                    } else {
                        if ("setConfig" !== e) return ee.proxy(e, t);
                        if (!t[0]) return void console.log("初始化 GrowingIO SDK 失败。请检查你的config文件是否引入正确");
                        if (!t[0].projectId) return void console.log("初始化 GrowingIO SDK 失败。请检查你的 GrowingIO项目ID, 你的应用APP_ID 是否填写正确");
                        ee.setConfig(t[0]);
                    }
                }
            };
            console.log("init growingio...");
            var ne = m.GrowingPage, ie = m.GrowingApp, re = m.GrowingComponent, oe = m.GrowingBehavior, ae = q, se = new X(ee);
            gioGlobal.__growing__ = {
                gioEmitter: ae,
                gio: te,
                growingio: ee,
                userStorage: se,
                marketingPreview: void 0
            }, gioGlobal.gio = te, t.GioApp = ie, t.GioBehavior = oe, t.GioComponent = re, t.GioPage = ne, 
            t.default = te, t.gioEmitter = ae, t.growingio = ee;
        }).call(this, n(45));
    },
    294: function(e, t, n) {
        var i = n(112);
        function r(e) {
            if (Array.isArray(e)) return i(e);
        }
        e.exports = r, e.exports["default"] = e.exports, e.exports.__esModule = !0;
    },
    295: function(e, t) {
        function n(e) {
            if ("undefined" !== typeof Symbol && null != e[Symbol.iterator] || null != e["@@iterator"]) return Array.from(e);
        }
        e.exports = n, e.exports["default"] = e.exports, e.exports.__esModule = !0;
    },
    296: function(e, t) {
        function n() {
            throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
        }
        e.exports = n, e.exports["default"] = e.exports, e.exports.__esModule = !0;
    },
    297: function(e, t) {
        function n(e) {
            if (Array.isArray(e)) return e;
        }
        e.exports = n, e.exports["default"] = e.exports, e.exports.__esModule = !0;
    },
    298: function(e, t) {
        function n(e, t) {
            var n = e && ("undefined" !== typeof Symbol && e[Symbol.iterator] || e["@@iterator"]);
            if (null != n) {
                var i, r, o = [], a = !0, s = !1;
                try {
                    for (n = n.call(e); !(a = (i = n.next()).done); a = !0) if (o.push(i.value), t && o.length === t) break;
                } catch (e) {
                    s = !0, r = e;
                } finally {
                    try {
                        a || null == n["return"] || n["return"]();
                    } finally {
                        if (s) throw r;
                    }
                }
                return o;
            }
        }
        e.exports = n, e.exports["default"] = e.exports, e.exports.__esModule = !0;
    },
    299: function(e, t) {
        function n() {
            throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
        }
        e.exports = n, e.exports["default"] = e.exports, e.exports.__esModule = !0;
    },
    305: function(e, t, n) {
        "use strict";
        (function(e) {
            var i = n(99), r = n(101), o = n(102), a = n(67), s = n(68), u = n(59), c = n(60), l = n(52);
            Object.defineProperty(t, "__esModule", {
                value: !0
            });
            var g, p = {
                devVer: 1,
                guid: function() {
                    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(e) {
                        var t = 16 * Math.random() | 0;
                        return ("x" == e ? t : 3 & t | 8).toString(16);
                    });
                },
                getScreenHeight: function(e) {
                    return e.pixelRatio ? Math.round(e.screenHeight * e.pixelRatio) : e.screenHeight;
                },
                getScreenWidth: function(e) {
                    return e.pixelRatio ? Math.round(e.screenWidth * e.pixelRatio) : e.screenWidth;
                },
                getOS: function(e) {
                    if (e) {
                        var t = e.toLowerCase();
                        return -1 != t.indexOf("android") ? "".concat(gioGlobal.platformConfig.name, "-Android") : -1 != t.indexOf("ios") ? "".concat(gioGlobal.platformConfig.name, "-iOS") : e;
                    }
                },
                getOSV: function(e) {
                    return "".concat(gioGlobal.platformConfig.name, " ").concat(e);
                },
                isEmpty: function(e) {
                    for (var t in e) if (Object.prototype.hasOwnProperty.call(e, t)) return !1;
                    return !0;
                },
                compareVersion: function(e, t) {
                    e = e.split("."), t = t.split(".");
                    for (var n = Math.max(e.length, t.length); n > e.length; ) e.push("0");
                    for (;n > t.length; ) t.push("0");
                    for (var i = 0; n > i; i++) {
                        var r = parseInt(e[i]), o = parseInt(t[i]);
                        if (r > o) return 1;
                        if (o > r) return -1;
                    }
                    return 0;
                }
            }, f = function(t) {
                Object.defineProperty(Object.prototype, "gioGlobal", {
                    get: function() {
                        return "quickApp" === t ? e.__proto__ : "my" === t ? $global : e;
                    },
                    configurable: !1,
                    enumerable: !1
                });
            }, h = function(e, t) {
                if (!e) return e;
                for (var n = t.split("."), i = e[n.shift()], r = 0, o = n.length; o > r; r++) {
                    var a = n.shift();
                    if (!i) return i;
                    i = i[a];
                }
                return i;
            }, d = function(e) {
                var t = {
                    eventId: void 0,
                    properties: {}
                };
                try {
                    if (e.hasOwnProperty("gioTrack") && "object" == l(e.gioTrack)) return t.eventId = e.gioTrack.name, 
                    t.properties = e.gioTrack.properties, t;
                    if (!e.gioImpTrack) return t;
                    t.eventId = e.gioImpTrack;
                    var n = /^gioTrack(.+)/, i = /^\w+$/;
                    for (var r in e) {
                        var o = void 0, a = r.match(n);
                        if (a && ("track" === (o = a[1].toLowerCase()) ? t.eventId = e[r] : t.properties[o] = e[r]), 
                        !i.test(t.eventId) || 10 > parseInt(t.eventId[0])) throw t.eventId = null, Error();
                    }
                } catch (e) {
                    console.warn("半打点IMP格式不正确, 事件名只能包含数字，字母和下划线，且不以数字开头, 请参考文档");
                }
                return t;
            }, v = function(e) {
                return e && "string" == typeof e && e.constructor === String;
            };
            Object.hasOwnProperty("getOwnPropertyDescriptors") || (g = "object" == ("undefined" === typeof Reflect ? "undefined" : l(Reflect)) && "function" == typeof Reflect.ownKeys ? Reflect.ownKeys : "function" == typeof Object.getOwnPropertySymbols ? function(e) {
                return Object.getOwnPropertyNames(e).concat(Object.getOwnPropertySymbols(e));
            } : Object.getOwnPropertyNames, Object.defineProperty(Object, "getOwnPropertyDescriptors", {
                configurable: !0,
                writable: !0,
                value: function(e) {
                    return g(e).reduce(function(t, n) {
                        return Object.defineProperty(t, n, {
                            configurable: !0,
                            enumerable: !0,
                            writable: !0,
                            value: Object.getOwnPropertyDescriptor(e, n)
                        });
                    }, {});
                }
            }));
            var y = function(e) {
                var t = m.observer.growingio;
                t && t.vdsConfig.followShare && e && e.path && (e.path = -1 === e.path.indexOf("?") ? e.path + "?suid=" + t.info.uid : e.path + "&suid=" + t.info.uid);
            }, m = {
                defaultPageCallbacks: {},
                defaultAppCallbacks: {},
                appHandlers: null,
                pageHandlers: null,
                actionEventTypes: null,
                originalPage: null,
                originalApp: null,
                originalComponent: null,
                originalBehavior: null,
                observer: null,
                hook: function(e, t) {
                    return function() {
                        var n, i = arguments ? arguments[0] : void 0;
                        if (i && (i.currentTarget || i.target) && -1 != m.actionEventTypes.indexOf(i.type)) try {
                            m.observer.actionListener(i, e);
                        } catch (e) {
                            console.error(e);
                        }
                        var r = gioGlobal.platformConfig.lisiteners.app, o = gioGlobal.platformConfig.lisiteners.page;
                        if (this._growing_app_ && e !== r.appShow || this._growing_page_ && -1 === [ o.pageShow, o.pageClose, o.pageLoad, o.pageHide, o.tabTap ].indexOf(e) ? n = t.apply(this, arguments) : this._growing_app_ || this._growing_page_ || (n = t.apply(this, arguments)), 
                        this._growing_app_ && -1 !== m.appHandlers.indexOf(e)) {
                            try {
                                m.defaultAppCallbacks[e].apply(this, arguments);
                            } catch (e) {
                                console.error(e);
                            }
                            e === r.appShow && (n = t.apply(this, arguments));
                        }
                        if (this._growing_page_ && -1 !== m.pageHandlers.indexOf(e)) {
                            var a = Array.prototype.slice.call(arguments);
                            n && a.push(n);
                            try {
                                m.defaultPageCallbacks[e].apply(this, a);
                            } catch (e) {
                                console.error(e);
                            }
                            -1 !== [ o.pageShow, o.pageClose, o.pageLoad, o.pageHide, o.tabTap ].indexOf(e) ? n = t.apply(this, arguments) : y(n);
                        }
                        return n;
                    };
                },
                hookComponent: function(e, t) {
                    return function() {
                        var n = arguments ? arguments[0] : void 0;
                        if (n && (n.currentTarget || n.target) && -1 != m.actionEventTypes.indexOf(n.type)) try {
                            m.observer.actionListener(n, e);
                        } catch (e) {
                            console.error(e);
                        }
                        return t.apply(this, arguments);
                    };
                },
                instrument: function(e) {
                    for (var t in e) "function" == typeof e[t] && (e[t] = this.hook(t, e[t]));
                    return e._growing_app_ && m.appHandlers.map(function(t) {
                        e[t] || (e[t] = m.defaultAppCallbacks[t]);
                    }), e._growing_page_ && m.pageHandlers.map(function(t) {
                        e[t] || t === gioGlobal.platformConfig.lisiteners.page.shareApp || (e[t] = m.defaultPageCallbacks[t]);
                    }), e;
                },
                instrumentPageComponent: function(e) {
                    if (e) return m.pageHandlers.map(function(t) {
                        if ("function" == typeof e[t]) {
                            var n = e[t];
                            e[t] = function() {
                                var e = n.apply(this, arguments), i = Array.prototype.slice.call(arguments);
                                return e && i.push(e), m.observer.pageListener(this, t, i), t === gioGlobal.platformConfig.lisiteners.page.shareApp && y(e), 
                                e;
                            };
                        } else t !== gioGlobal.platformConfig.lisiteners.page.shareApp && (e[t] = function() {
                            m.observer.pageListener(this, t, arguments);
                        });
                    }), e;
                },
                instrumentComponent: function(e) {
                    if (e.methods) {
                        var t = e.methods;
                        for (var n in t) "function" == typeof t[n] && (e.methods[n] = this.hookComponent(n, t[n]));
                    }
                    return e;
                },
                GrowingPage: function(e) {
                    return e._growing_page_ = !0, m.originalPage(m.instrument(e));
                },
                GrowingComponent: function(e) {
                    return m.originalComponent(m.instrumentComponent(e));
                },
                GrowingBehavior: function(e) {
                    return m.originalBehavior(m.instrumentComponent(e));
                },
                GrowingApp: function(e) {
                    return e._growing_app_ = !0, m.originalApp(m.instrument(e));
                },
                initPlatformInfo: function(e) {
                    m.appHandlers = e.appHandlers, m.pageHandlers = e.pageHandlers, m.actionEventTypes = e.actionEventTypes, 
                    m.originalApp = e.originalApp, m.originalPage = e.originalPage, m.originalComponent = e.originalComponent, 
                    m.originalBehavior = e.originalBehavior;
                },
                initInstrument: function(e) {
                    if (m.initPlatformInfo(gioGlobal.platformConfig), m.observer = e, m.pageHandlers.forEach(function(e) {
                        m.defaultPageCallbacks[e] = function() {
                            m.observer.pageListener(this, e, arguments);
                        };
                    }), m.appHandlers.forEach(function(e) {
                        m.defaultAppCallbacks[e] = function() {
                            m.observer.appListener(this, e, arguments);
                        };
                    }), gioGlobal.platformConfig.canHook) {
                        var t = gioGlobal.platformConfig.hooks;
                        t.App && !gioGlobal.growingAppInited && (App = function() {
                            return m.GrowingApp(arguments[0]);
                        }, gioGlobal.growingAppInited = !0), t.Page && !gioGlobal.growingPageInited && (Page = function() {
                            return m.GrowingPage(arguments[0]);
                        }, gioGlobal.growingPageInited = !0), t.Component && !gioGlobal.growingComponentInited && (Component = function() {
                            return m.GrowingComponent(arguments[0]);
                        }, gioGlobal.growingComponentInited = !0), t.Behavior && !gioGlobal.growingBehaviorInited && (Behavior = function() {
                            return m.GrowingBehavior(arguments[0]);
                        }, gioGlobal.growingBehaviorInited = !0);
                    }
                    gioGlobal.GioPage = m.GrowingPage, gioGlobal.GioApp = m.GrowingApp, gioGlobal.GioComponent = m.GrowingComponent, 
                    gioGlobal.GioBehavior = m.GrowingBehavior, gioGlobal.trackApp = function() {
                        var e = arguments[0];
                        return e._growing_app_ = !0, m.instrument(e);
                    }, gioGlobal.trackPage = function() {
                        var e = arguments[0];
                        return e._growing_page_ = !0, m.instrument(e);
                    }, gioGlobal.trackComponent = function() {
                        return m.instrument(arguments[0]);
                    }, gioGlobal.trackBehavior = function() {
                        return m.instrument(arguments[0]);
                    };
                }
            }, b = function() {
                function e() {
                    u(this, e), this.queries = {}, this.pvar = {};
                }
                return c(e, [ {
                    key: "touch",
                    value: function(e) {
                        this.path = e.route, this.time = Date.now(), this.query = this.queries[e.route] ? this.queries[e.route] : void 0;
                    }
                }, {
                    key: "addQuery",
                    value: function(e, t) {
                        this.queries[e.route] = t ? this._getQuery(t) : null;
                    }
                }, {
                    key: "_getQuery",
                    value: function(e) {
                        return Object.keys(e).filter(function(e) {
                            return "wxShoppingListScene" !== e;
                        }).map(function(t) {
                            return "".concat(t, "=").concat(e[t]);
                        }).join("&");
                    }
                }, {
                    key: "touchRelatedPvarData",
                    value: function(e) {
                        var t = "".concat(e.p, "?").concat(e.q);
                        this.pvar[t] ? this.pvar[t].push(e) : this.pvar[t] = [ e ];
                    }
                } ]), e;
            }(), w = {
                tap: [ "tap", "click" ],
                longtap: [ "longtap" ],
                input: [ "input" ],
                blur: [ "change", "blur" ],
                submit: [ "submit" ],
                focus: [ "focus" ]
            }, _ = /^function[^\(]*\([^\)]+\).*[^\.]+\.([^\(]+)\(.*/;
            function k(e) {
                return e && e.$attrs ? e.$attrs.mpcomid : "0";
            }
            function x(e, t, n) {
                return !(!e || !t) && (t === e || 0 === t.indexOf(e + n));
            }
            function P(e, t, n) {
                void 0 === t && (t = []);
                var i = t.slice(1);
                if (!i.length) return e;
                var r = i.join(n), o = "";
                return i.reduce(function(e, t) {
                    for (var i = e.$children.length, a = 0; i > a; a++) {
                        var s = e.$children[a], u = k(s);
                        if (o && (u = o + n + u), x(u, r, n)) return o = u, s;
                    }
                    return e;
                }, e);
            }
            function C(e, t, n) {
                void 0 === n && (n = []);
                var i = [];
                if (!e || !e.tag) return i;
                var r = e || {}, o = r.data;
                void 0 === o && (o = {});
                var a = r.children;
                void 0 === a && (a = []);
                var s = r.componentInstance;
                s ? Object.keys(s.$slots).forEach(function(e) {
                    var r = s.$slots[e];
                    (Array.isArray(r) ? r : [ r ]).forEach(function(e) {
                        i = i.concat(C(e, t, n));
                    });
                }) : a.forEach(function(e) {
                    i = i.concat(C(e, t, n));
                });
                var u = o.attrs, c = o.on;
                return u && c && u.eventid === t && n.forEach(function(e) {
                    var t = c[e];
                    "function" == typeof t ? i.push(t) : Array.isArray(t) && (i = i.concat(t));
                }), i;
            }
            var S = "~", E = "^";
            function O(e, t) {
                return e === t || "regionchange" === t && ("begin" === e || "end" === e);
            }
            var I = function() {
                function e(t) {
                    u(this, e), this.vueVM = t;
                }
                return c(e, [ {
                    key: "getHandle",
                    value: function(e) {
                        var t = e.type, n = e.target;
                        void 0 === n && (n = {});
                        var i = (e.currentTarget || n).dataset;
                        void 0 === i && (i = {});
                        var r = i.comkey;
                        void 0 === r && (r = "");
                        var o = i.eventid, a = -1 !== r.indexOf("_") ? "_" : ",", s = P(this.vueVM, r.split(a), a);
                        if (s) {
                            var u = C(s._vnode, o, w[t] || [ t ]);
                            if (u.length) {
                                var c = u[0];
                                if (c.isProxied) return c.proxiedName;
                                try {
                                    var l = ("" + c).replace("\n", "");
                                    if (l.match(_)) {
                                        var g = _.exec(l);
                                        if (g && g.length > 1) return g[1];
                                    }
                                } catch (e) {}
                                return c.name;
                            }
                        }
                    }
                }, {
                    key: "handleEvent",
                    value: function(e) {
                        var t, n = e.type, i = (e.currentTarget || e.target).dataset;
                        return (i.eventOpts || i["event-opts"]).forEach(function(e) {
                            var i = e[0], r = e[1];
                            i = (i = i.charAt(0) === E ? i.slice(1) : i).charAt(0) === S ? i.slice(1) : i, r && O(n, i) && r.forEach(function(e) {
                                t = e[0];
                            });
                        }), t;
                    }
                } ]), e;
            }();
            function T() {}
            var A = T.prototype;
            A.emit = function() {}, A.on = function() {}, A.emitEvent = function(e) {};
            var j = new T();
            function G(e) {
                return null !== e && "[object Object]" === Object.prototype.toString.call(e) && Object.keys(e).length > 0;
            }
            var V = function() {
                function e(t) {
                    u(this, e), this.growingio = t, this.esid = 0, this.info = t.info;
                }
                return c(e, [ {
                    key: "setUserAttributes",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "setUserId",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "clearUserId",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "sendVisitEvent",
                    value: function(e, t) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "track",
                    value: function(e, t) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "_sendEvent",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                } ]), e;
            }(), L = {
                tap: "clck",
                longpress: "lngprss",
                longtap: "lngprss"
            }, q = function(e) {
                a(n, e);
                var t = s(n);
                function n(e) {
                    var i;
                    return u(this, n), i = t.call(this, e), i.growingio = e, i.info = e.info, i.currentPage = new b(), 
                    i.scene = null, i._sessionId = null, i.cs1 = null, i.lastPageEvent = null, i.lastVstArgs = void 0, 
                    i.lastCloseTime = null, i.lastScene = void 0, i.keepAlive = e.vdsConfig.keepAlive, 
                    i.isPauseSession = !1, i.isGettingUid = !1, i.esid = 0 === i.info.esid ? 1 : i.info.esid, 
                    i.uploadingMessages = [], i;
                }
                return c(n, [ {
                    key: "sessionId",
                    get: function() {
                        return null === this._sessionId && (this._sessionId = p.guid()), this._sessionId;
                    }
                }, {
                    key: "resetSessionId",
                    value: function() {
                        this._sessionId = null;
                    }
                }, {
                    key: "pauseSession",
                    value: function() {
                        this.isPauseSession = !0;
                    }
                }, {
                    key: "getVisitorId",
                    value: function() {
                        return this.info.uid;
                    }
                }, {
                    key: "getUserId",
                    value: function() {
                        return this.cs1;
                    }
                }, {
                    key: "getGioInfo",
                    value: function() {
                        return "giou=".concat(this.getVisitorId(), "&giocs1=").concat(this.getUserId(), "&gios=").concat(this.sessionId, "&gioprojectid=").concat(this.growingio.vdsConfig.projectId, "&gioappid=").concat(this.growingio.vdsConfig.appId, "&gioplatform=").concat(gioGlobal.platformConfig.platform);
                    }
                }, {
                    key: "setUserId",
                    value: function(e) {
                        var t = e + "";
                        t && 100 > t.length && (this.cs1 = t, j.emitEvent("setCs1", [ t ]), this.lastPageEvent && this._sendEvent(this.lastPageEvent));
                    }
                }, {
                    key: "clearUserId",
                    value: function() {
                        this.cs1 = null, j.emitEvent("clearCs1");
                    }
                }, {
                    key: "appListener",
                    value: function(e, t, n) {
                        var i = gioGlobal.platformConfig.lisiteners.app;
                        this.isPauseSession || (this.growingio.vdsConfig.debug && console.log("App.", t, Date.now()), 
                        t == i.appShow ? (j.emitEvent("appShow"), this._parseScene(n), !this.lastCloseTime || Date.now() - this.lastCloseTime > this.keepAlive || this.lastScene && this.scene !== this.lastScene ? (this.resetSessionId(), 
                        this.sendVisitEvent(n, this.growingio.vdsConfig.getLocation.type), this.lastVstArgs = n, 
                        this.useLastPageTime = !1, this.lastPageEvent = void 0) : this.lastPageEvent && (this.useLastPageTime = !0)) : t == i.appClose ? (this.lastScene = this.scene, 
                        this.growingio.forceFlush(), this.info.syncStorage(), this.isPauseSession || (this.lastCloseTime = Date.now(), 
                        this.sendVisitCloseEvent())) : t == i.appError && this.sendErrorEvent(n));
                    }
                }, {
                    key: "pageListener",
                    value: function(e, t, n) {
                        var i = gioGlobal.platformConfig.lisiteners.page;
                        if (this.growingio.vdsConfig.wepy && (e.route = e.$is), e.route || (e.route = this.info.getPagePath(e)), 
                        this.growingio.vdsConfig.debug && console.log("Page.", e.route, "#", t, Date.now()), 
                        t === i.pageShow) {
                            var r = h(e, "$page.query");
                            p.isEmpty(r) || "quickApp" !== gioGlobal.gio__platform || this.currentPage.addQuery(e, r), 
                            this.isPauseSession ? this.isPauseSession = !1 : (this.currentPage.touch(e), this.useLastPageTime && (this.currentPage.time = this.lastPageEvent.tm, 
                            this.useLastPageTime = !1), this.sendPage(e));
                        } else if (t === i.pageLoad) {
                            var o = n[0];
                            p.isEmpty(o) || "quickApp" === gioGlobal.gio__platform || this.currentPage.addQuery(e, o);
                        } else if (t === i.pageHide) this.growingio._observer && this.growingio._observer.disconnect(); else if (t === i.pageClose) this.currentPage.pvar["".concat(this.currentPage.path, "?").concat(this.currentPage.query)] = void 0; else if (t === i.shareApp) {
                            var a = null, s = null;
                            2 > n.length ? 1 === n.length && (n[0].from ? a = n[0] : n[0].title && (s = n[0])) : (a = n[0], 
                            s = n[1]), this.pauseSession(), this.sendPageShare(e, a, s);
                        } else "onTabItemTap" === t && this.sendTabClick(n[0]);
                    }
                }, {
                    key: "actionListener",
                    value: function(e, t) {
                        if (!h(e, "currentTarget.dataset.growingIgnore") && !h(e, "target.dataset.growingIgnore")) {
                            var n = gioGlobal.platformConfig.lisiteners.actions;
                            if ("_cmlEventProxy" !== t) {
                                if ("handleProxy" === t && this.growingio.vueRootVMs && this.growingio.vueRootVMs[this.currentPage.path]) {
                                    var i = new I(this.growingio.vueRootVMs[this.currentPage.path]).getHandle(e);
                                    i && (t = i);
                                }
                                if ("__e" === t && this.growingio.vueRootVMs && this.growingio.vueRootVMs[this.currentPage.path]) {
                                    var r = new I(this.growingio.vueRootVMs[this.currentPage.path]).handleEvent(e);
                                    r && (t = r);
                                }
                                if ("_proxy" === t && this.growingio.wepyRootVMs) {
                                    var o = e.currentTarget.dataset.wpyEvt, a = e.type;
                                    h(this, "growingio.wepyRootVMs.".concat(o, ".").concat(a)) && (t = this.growingio.wepyRootVMs[o][a]);
                                }
                                h(this, "growingio.taroRootVMs.".concat(t)) && (t = this.growingio.taroRootVMs[t]), 
                                this.growingio.vdsConfig.debug && console.log("Click on ", t, Date.now()), -1 !== n.click.indexOf(e.type) ? (this.sendClick(e, t), 
                                "getuserinfo" === e.type && h(e, "detail.userInfo") && this.setVisitor(e.detail.userInfo)) : -1 !== n.change.indexOf(e.type) ? this.sendChange(e, t) : -1 !== n.submit.indexOf(e.type) && this.sendSubmit(e, t);
                            }
                        }
                    }
                }, {
                    key: "sendVideoCstm",
                    value: function(e) {
                        this.track("video-".concat(e.type), e.var);
                    }
                }, {
                    key: "track",
                    value: function(e, t) {
                        if ("string" != typeof e || null === e || void 0 === e || 0 === e.length || !e.match(/^\w+$/) || 10 > parseInt(e[0])) console.warn("埋点格式不正确, 事件名只能包含数字，字母和下划线，且不以数字开头, 请参考文档"); else {
                            var n = {
                                t: "cstm",
                                ptm: this.currentPage.time,
                                p: this.currentPage.path,
                                q: this.currentPage.query,
                                n: e
                            };
                            G(t) && (n.var = t), this._sendEvent(n);
                        }
                    }
                }, {
                    key: "identify",
                    value: function(e, t) {
                        void 0 !== e && 0 !== e.length && (this.growingio.login(e), this._sendEvent({
                            t: "vstr",
                            var: {
                                openid: e,
                                unionid: t
                            }
                        }));
                    }
                }, {
                    key: "setVisitor",
                    value: function(e) {
                        G(e) && this._sendEvent({
                            t: "vstr",
                            var: e
                        });
                    }
                }, {
                    key: "setUser",
                    value: function(e) {
                        this.cs1 && G(e) && this._sendEvent({
                            t: "ppl",
                            var: e
                        });
                    }
                }, {
                    key: "setPage",
                    value: function(e) {
                        if (G(e)) {
                            var t = {
                                t: "pvar",
                                ptm: this.currentPage.time,
                                p: this.currentPage.path,
                                q: this.currentPage.query,
                                var: e
                            };
                            this.currentPage.touchRelatedPvarData(t), this._sendEvent(t);
                        }
                    }
                }, {
                    key: "setEvar",
                    value: function(e) {
                        G(e) && this._sendEvent({
                            t: "evar",
                            var: e
                        });
                    }
                }, {
                    key: "getLocation",
                    value: function(e) {
                        this.growingio.vdsConfig.getLocation.autoGet = !0, this.sendVisitEvent(this.lastVstArgs, e);
                    }
                }, {
                    key: "sendVisitEvent",
                    value: function(e, t) {
                        var n = this;
                        this.info.getSystemInfo().then(function(i) {
                            var r = i || {}, o = {
                                t: "vst",
                                tm: Date.now(),
                                av: n.info.sdkVer,
                                db: r.brand,
                                dm: r.model && r.model.replace(/<.*>/, ""),
                                sh: p.getScreenHeight(r),
                                sw: p.getScreenWidth(r),
                                os: p.getOS(r.platform),
                                osv: p.getOSV(r.version),
                                l: r.language
                            };
                            if (n.growingio.vdsConfig.appVer && (o.cv = n.growingio.vdsConfig.appVer + ""), 
                            e.length > 0) {
                                var a = e[0];
                                o.p = a.path || n.info.getPagePath(), p.isEmpty(a.query) || (o.q = n.currentPage._getQuery(a.query)), 
                                o.ch = "scn:".concat(n.info.scnPrefix).concat(n.scene), "quickapp" === n.info.platform ? o.rf = n.info.appSource.packageName : a.referrerInfo && a.referrerInfo.appId && h(a, "referrerInfo.appId") && (o.rf = a.referrerInfo.appId), 
                                n.info.getNetworkType().then(function(e) {
                                    if (e && (o.nt = e.networkType, n._sendEvent(o), n.growingio.vdsConfig.getLocation.autoGet)) {
                                        var i = JSON.parse(JSON.stringify(o));
                                        t && -1 !== [ "wgs84", "gcj02", 0, 1, 2 ].indexOf(t) || (t = "my" === gioGlobal.gio__platform ? 0 : "wgs84"), 
                                        n.info.getLocation(t).then(function(e) {
                                            e && (i.lat = e.latitude, i.lng = e.longitude, n._sendEvent(i));
                                        });
                                    }
                                });
                            }
                        });
                    }
                }, {
                    key: "sendVisitCloseEvent",
                    value: function() {
                        this._sendEvent({
                            t: "cls",
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        });
                    }
                }, {
                    key: "sendErrorEvent",
                    value: function(e) {
                        if (e && e.length > 0) {
                            var t = e[0];
                            if ("string" != typeof t) return;
                            var n, i = t.split("\n");
                            if (i && i.length > 1) {
                                var r = i[1].split(";");
                                if (r && r.length > 1) {
                                    var o = r[1].match(/at ([^ ]+) page (.*) function/);
                                    n = {
                                        key: i[0],
                                        error: r[0]
                                    }, o && o.length > 2 && (n.page = o[1], n.function = o[2]);
                                }
                            } else n = {
                                error: i && i[0]
                            };
                            this._sendEvent({
                                t: "cstm",
                                ptm: this.currentPage.time,
                                p: this.currentPage.path,
                                q: this.currentPage.query,
                                n: "onError",
                                var: n
                            });
                        }
                    }
                }, {
                    key: "sendPage",
                    value: function(e) {
                        var t = this, n = {
                            t: "page",
                            tm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        };
                        n.rp = this.lastPageEvent ? this.lastPageEvent.p : this.scene ? "scn:".concat(this.info.scnPrefix).concat(this.scene) : null;
                        var i = this.info.getPageTitle(e);
                        i && i.length > 0 && (n.tl = i), this._sendEvent(n), this.lastPageEvent = n;
                        var r = this.currentPage.pvar["".concat(this.currentPage.path, "?").concat(this.currentPage.query)];
                        r && r.length > 0 && r.map(function(e) {
                            e.ptm = t.currentPage.time, t._sendEvent(e);
                        });
                    }
                }, {
                    key: "sendPageShare",
                    value: function(e, t, n) {
                        this._sendEvent({
                            t: "cstm",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query,
                            n: "onShareAppMessage",
                            var: {
                                from: t ? t.from : void 0,
                                target: t && t.target ? t.target.id : void 0,
                                title: n ? n.title : void 0,
                                path: n ? decodeURI(n.path) : void 0
                            }
                        });
                    }
                }, {
                    key: "sendClick",
                    value: function(e, t) {
                        var n = {
                            t: L[e.type] || "clck",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        }, i = e.currentTarget || e.target, r = i.id;
                        (!r || "swan" === gioGlobal.gio__platform && /^_[0-9a-f]+/.test(r)) && (r = "");
                        var o = {
                            x: "".concat(r, "#").concat(t)
                        };
                        i.dataset.title && (o.v = i.dataset.title), i.dataset.src && (o.h = i.dataset.src), 
                        void 0 !== i.dataset.index && (o.idx = /^[\d]+$/.test(i.dataset.index) ? parseInt(i.dataset.index) : -1), 
                        n.e = [ o ], this._sendEvent(n);
                    }
                }, {
                    key: "sendSubmit",
                    value: function(e, t) {
                        var n = {
                            t: "sbmt",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        }, i = (e.currentTarget || e.target).id;
                        (!i || "swan" === gioGlobal.gio__platform && /^_[0-9a-f]+/.test(i)) && (i = ""), 
                        n.e = [ {
                            x: "".concat(i, "#").concat(t)
                        } ], this._sendEvent(n);
                    }
                }, {
                    key: "sendChange",
                    value: function(e, t) {
                        var n = {
                            t: "chng",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        }, i = e.currentTarget || e.target, r = i.id;
                        (!r || "swan" === gioGlobal.gio__platform && /^_[0-9a-f]+/.test(r)) && (r = "");
                        var o = {
                            x: "".concat(r, "#").concat(t)
                        }, a = h(e, "detail.value") || h(e, "target.attr.value");
                        (i.dataset.growingTrack || i.dataset.growingtrack) && ("boolean" == typeof a || a && 0 !== a.length) && ("[object Array]" === Object.prototype.toString.call(a) ? (a = a.join(",")) && (o.v = a) : o.v = a), 
                        "change" === e.type && "autoplay" === h(e, "detail.source") || (n.e = [ o ], this._sendEvent(n));
                    }
                }, {
                    key: "sendTabClick",
                    value: function(e) {
                        var t = {
                            t: "clck",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query,
                            e: [ {
                                x: "#onTabItemTap",
                                v: e.text,
                                idx: e.index,
                                h: "string" == typeof e.pagePath ? e.pagePath : JSON.stringify(e.pagePath)
                            } ]
                        };
                        this._sendEvent(t);
                    }
                }, {
                    key: "_sendEvent",
                    value: function(e) {
                        var t = this;
                        if (this.info.uid && this.esid) {
                            var n = this._buildEvent(e, this.info);
                            this.growingio.upload(n);
                        } else if (this.isGettingUid) this.uploadingMessages.push(e); else {
                            this.isGettingUid = !0;
                            var i = this.info.getStorage(this.info.uidKey), r = this.info.getStorage(this.info.esidKey);
                            Promise.all([ i, r ]).then(function(n) {
                                var i = o(n, 2), r = i[0], a = i[1];
                                r || (r = p.guid()), a || (a = 1), t.info.uid = r, t.info.esid = a, t.isGettingUid = !1;
                                var s = t._buildEvent(e, t.info);
                                for (t.growingio.upload(s); 0 !== t.uploadingMessages.length; ) {
                                    var u = t.uploadingMessages.shift();
                                    u = t._buildEvent(u, t.info), t.growingio.upload(u);
                                }
                            });
                        }
                    }
                }, {
                    key: "_buildEvent",
                    value: function(e, t) {
                        if (e.u = t.uid, e.s = this.sessionId, e.tm = e.tm || Date.now(), e.d = this.growingio.vdsConfig.appId, 
                        e.b = t.platform, null !== this.cs1 && (e.cs1 = this.cs1), e.var) {
                            var n = e.var;
                            Object.keys(n).forEach(function(t) {
                                "string" != typeof n[t] && (e.var[t] = JSON.stringify(n[t]));
                            });
                        }
                        return e.esid = this.esid++, e;
                    }
                }, {
                    key: "_parseScene",
                    value: function(e) {
                        if ("quickapp" === this.info.platform) {
                            var t = this.info.getAppSource(), n = t.extra || {}, i = t.type || "";
                            this.scene = i, this.setVisitor({
                                extra: JSON.stringify(n)
                            });
                        } else if (e.length > 0) {
                            var r = e[0];
                            this.scene = r.query && r.query.wxShoppingListScene ? r.query.wxShoppingListScene : r.scene ? r.scene : "NA";
                        }
                    }
                } ]), n;
            }(V), M = function() {
                function e(t) {
                    u(this, e), this.growing = t, this._uid = void 0, this._esid = void 0, this._gioId = void 0, 
                    this._userId = void 0, this._systemInfo = null, this.uidKey = "_growing_uid_", this.esidKey = "_growing_esid_", 
                    this.gioIdKey = "_growing_gioId_", this.userIdKey = "_growing_userId_", this.platform = gioGlobal.platformConfig.platform, 
                    this.sdkVer = gioGlobal.platformConfig.sdkVer, this.scnPrefix = gioGlobal.platformConfig.scnPrefix, 
                    "quickapp" !== gioGlobal.platformConfig.platform && this.initUserInfo();
                }
                return c(e, [ {
                    key: "esid",
                    get: function() {
                        return this._esid;
                    },
                    set: function(e) {
                        this._esid = e, this.setStorage(this.esidKey, this._esid);
                    }
                }, {
                    key: "uid",
                    get: function() {
                        return this._uid;
                    },
                    set: function(e) {
                        this._uid = e, this.setStorage(this.uidKey, this._uid);
                    }
                }, {
                    key: "gioId",
                    get: function() {
                        return this._gioId;
                    },
                    set: function(e) {
                        this._gioId = e, this.setStorage(this.gioIdKey, this._gioId);
                    }
                }, {
                    key: "userId",
                    get: function() {
                        return this._userId;
                    },
                    set: function(e) {
                        this._userId = e, this.setStorage(this.userIdKey, this._userId);
                    }
                }, {
                    key: "systemInfo",
                    get: function() {
                        return this._systemInfo;
                    }
                }, {
                    key: "initUserInfo",
                    value: function() {
                        this.uid = this.getStorageSync(this.uidKey), this.esid = +this.getStorageSync(this.esidKey);
                    }
                }, {
                    key: "syncStorage",
                    value: function() {
                        var e = this;
                        this.getStorage(this.uidKey).then(function(t) {
                            t || e.setStorage(e.uidKey, e._uid);
                        });
                    }
                }, {
                    key: "getAppId",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getAppSource",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getPageTitle",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getPagePath",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getStorage",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getStorageSync",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "setStorage",
                    value: function(e, t) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getSystemInfo",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getNetworkType",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getLocation",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "request",
                    value: function(e) {
                        e.url, e.header, e.method, e.data, e.success, e.fail;
                        throw Error("this a interface function");
                    }
                }, {
                    key: "collectImp",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "initShareAppMessage",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getCurrentPage",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getQuery",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getReferrer",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getInitPath",
                    value: function() {
                        throw Error("this a interface function");
                    }
                } ]), e;
            }(), R = function(e) {
                a(n, e);
                var t = s(n);
                function n(e) {
                    var i;
                    return u(this, n), i = t.call(this, e), i.growingio = e, i;
                }
                return c(n, [ {
                    key: "getAppId",
                    value: function() {
                        return "";
                    }
                }, {
                    key: "getPagePath",
                    value: function(e) {
                        var t = getCurrentPages(), n = t[t.length - 1];
                        return n && n.__route__;
                    }
                }, {
                    key: "getPageTitle",
                    value: function(e) {
                        var t = "";
                        try {
                            e.data.title && e.data.title.length > 0 && (t = Array.isArray(e.data.title) ? e.data.title.join(" ") : e.data.title);
                        } catch (e) {
                            return "";
                        }
                        return t;
                    }
                }, {
                    key: "getStorage",
                    value: function(e) {
                        return new Promise(function(t) {
                            tt.getStorage({
                                key: e,
                                success: function(e) {
                                    return t(e.data);
                                },
                                fail: function() {
                                    return t("");
                                }
                            });
                        });
                    }
                }, {
                    key: "getStorageSync",
                    value: function(e) {
                        return tt.getStorageSync(e);
                    }
                }, {
                    key: "setStorage",
                    value: function(e, t) {
                        tt.setStorage({
                            key: e,
                            data: t
                        });
                    }
                }, {
                    key: "getSystemInfo",
                    value: function() {
                        var e = this;
                        return new Promise(function(t) {
                            tt.getSystemInfo({
                                success: function(n) {
                                    e._systemInfo = n, t(n);
                                },
                                fail: function() {
                                    return t(null);
                                }
                            });
                        });
                    }
                }, {
                    key: "getNetworkType",
                    value: function() {
                        return new Promise(function(e) {
                            tt.getNetworkType({
                                success: function(t) {
                                    return e(t);
                                },
                                fail: function() {
                                    return e(null);
                                }
                            });
                        });
                    }
                }, {
                    key: "getSetting",
                    value: function() {
                        return new Promise(function(e) {
                            tt.getSetting({
                                success: e,
                                fail: e
                            });
                        });
                    }
                }, {
                    key: "getLocation",
                    value: function() {
                        return new Promise(function(e) {
                            tt.getLocation({
                                success: function(t) {
                                    return e(t);
                                },
                                fail: function() {
                                    return e(null);
                                }
                            });
                        });
                    }
                }, {
                    key: "request",
                    value: function(e) {
                        var t = e.url, n = e.header, i = e.method, r = e.data, o = e.success, a = e.fail;
                        return tt.request({
                            url: t,
                            header: n,
                            method: i,
                            data: r,
                            success: o,
                            fail: a
                        });
                    }
                }, {
                    key: "collectImp",
                    value: function(e) {
                        var t = this, n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : null;
                        this.growingio.vdsConfig.vue && (e = e.$mp.page), this.growingio.vdsConfig.taro && (e = e.$scope);
                        var i = {};
                        this.growingio._observer && this.growingio._observer.disconnect(), this.growingio._observer = e.isComponent ? e.createIntersectionObserver({
                            observeAll: !0
                        }) : tt.createIntersectionObserver(e, {
                            observeAll: !0
                        }), (n ? this.growingio._observer.relativeTo(n) : this.growingio._observer.relativeToViewport()).observe(".growing_collect_imp", function(e) {
                            if (e.id && !i[e.id]) {
                                var n = d(e.dataset), r = n.eventId, o = n.properties;
                                r && e.id && !i[e.id] && (t.growingio.observer.track(r, o), i[e.id] = !0);
                            }
                        });
                    }
                }, {
                    key: "setStorageSync",
                    value: function(e, t) {
                        tt.setStorageSync(e, JSON.stringify(t));
                    }
                }, {
                    key: "removeStorageSync",
                    value: function(e) {
                        tt.removeStorageSync(e);
                    }
                }, {
                    key: "navigateTo",
                    value: function(e) {
                        tt.navigateTo(e);
                    }
                }, {
                    key: "switchTab",
                    value: function(e) {
                        tt.switchTab(e);
                    }
                } ]), n;
            }(M), D = function() {
                function e(t) {
                    u(this, e), this.growingio = t, this.messageQueue = [], this.uploadingQueue = [], 
                    this.uploadTimer = null, this.projectId = this.growingio.vdsConfig.projectId, this.appId = this.growingio.vdsConfig.appId, 
                    this.host = this.growingio.vdsConfig.host, this.url = "".concat(this.host, "/projects/").concat(this.projectId, "/apps/").concat(this.appId, "/collect");
                }
                return c(e, [ {
                    key: "upload",
                    value: function(e) {
                        var t = this;
                        this.messageQueue.push(e);
                        var n = this.messageQueue.length;
                        n > 100 && (this.messageQueue = this.messageQueue.slice(n - 100)), this.uploadTimer || (this.uploadTimer = setTimeout(function() {
                            t._flush(), t.uploadTimer = null;
                        }, 1e3));
                    }
                }, {
                    key: "forceFlush",
                    value: function() {
                        this.uploadTimer && (clearTimeout(this.uploadTimer), this.uploadTimer = null), this._flush();
                    }
                }, {
                    key: "_flush",
                    value: function() {
                        var e = this;
                        this.uploadingQueue = this.messageQueue.slice(), this.messageQueue = [], this.uploadingQueue.length > 0 && this.growingio.info.request({
                            url: "".concat(this.url, "?stm=").concat(Date.now()),
                            header: {
                                "content-type": "application/json"
                            },
                            method: "POST",
                            data: this.uploadingQueue,
                            success: function() {
                                e.messageQueue.length > 0 && e._flush();
                            },
                            fail: function(t) {
                                204 !== t.status && (e.messageQueue = e.uploadingQueue.concat(e.messageQueue));
                            }
                        });
                    }
                } ]), e;
            }(), H = {
                wx: {
                    name: "Weixin",
                    path: "./weixin"
                },
                qq: {
                    name: "QQ",
                    path: "./qq"
                },
                my: {
                    name: "Alipay",
                    path: "./alipay"
                },
                swan: {
                    name: "Baidu",
                    path: "./baidu"
                },
                tt: {
                    name: "Bytedance",
                    path: "./bytedance"
                },
                quickApp: {
                    name: "Quickapp",
                    path: "./quickApp"
                },
                frame: {
                    name: "Frame",
                    path: "./multipleFrame"
                }
            }, B = Object.assign({}, H.tt, {
                platform: "bytedance",
                scnPrefix: "bytedance_",
                appHandlers: [ "onShow", "onHide", "onError" ],
                pageHandlers: [ "onLoad", "onShow", "onShareAppMessage", "onTabItemTap", "onHide", "onUnload" ],
                actionEventTypes: [ "onclick", "tap", "longpress", "blur", "change", "submit", "confirm", "getuserinfo", "getphonenumber", "contact" ],
                originalApp: App,
                originalPage: Page,
                originalComponent: Component,
                originalBehavior: Behavior,
                canHook: !0,
                hooks: {
                    App: !0,
                    Page: !0,
                    Component: !0,
                    Behavior: !0
                },
                lisiteners: {
                    app: {
                        appShow: "onShow",
                        appClose: "onHide",
                        appError: "onError"
                    },
                    page: {
                        pageLoad: "onLoad",
                        pageShow: "onShow",
                        pageHide: "onHide",
                        pageClose: "onUnload",
                        tabTap: "onTabItemTap",
                        shareApp: "onShareAppMessage"
                    },
                    actions: {
                        click: [ "onclick", "tap", "longpress", "getuserinfo", "getphonenumber", "contact" ],
                        change: [ "blur", "change", "confirm" ],
                        submit: [ "submit" ]
                    }
                }
            }), U = Object.assign({}, B, {
                sdkVer: "3.4.1"
            }), $ = function() {
                function e(t) {
                    u(this, e), this.growingio = t;
                }
                return c(e, [ {
                    key: "setDataCollect",
                    value: function(e) {
                        this.growingio.vdsConfig.dataCollect = e;
                    }
                }, {
                    key: "enableDebug",
                    value: function(e) {
                        e && console && (this.growingio.vdsConfig.debug = e);
                    }
                }, {
                    key: "setTrackerScheme",
                    value: function(e) {
                        var t = (e + "").toLocaleLowerCase();
                        "http" !== t && "https" !== t || (this.growingio.vdsConfig.scheme = "".concat(e, "://"));
                    }
                }, {
                    key: "setTrackerHost",
                    value: function(e) {
                        v(e) && (this.growingio.vdsConfig.host = e);
                    }
                } ]), e;
            }(), K = 3e5, N = function() {
                function e() {
                    u(this, e), this.uploadingMessages = [], this.start = !1;
                }
                return c(e, [ {
                    key: "init",
                    value: function(e, t, n) {
                        this.start || (t && "string" != typeof t && (n = t, t = ""), t || n || (t = "", 
                        n = {}), "alip" === U.platform && (n.vue || n.taro || n.cml || n.wepy) && (U.canHook = !0), 
                        n.usePlugin && (U.canHook = !1), this.vdsConfig = {
                            projectId: e,
                            appId: t,
                            appVer: n.version || "",
                            debug: n.debug || !1,
                            forceLogin: n.forceLogin || !1,
                            followShare: void 0 === n.followShare || n.followShare,
                            usePlugin: n.usePlugin || !1,
                            getLocation: {
                                autoGet: ("object" == l(n.getLocation) ? n.getLocation.autoGet : n.getLocation) || !1,
                                type: "object" == l(n.getLocation) && n.getLocation.type || "wgs84"
                            },
                            dataCollect: !("boolean" == typeof n.stopTrack && n.stopTrack || "boolean" == typeof n.dataCollect && !n.dataCollect),
                            keepAlive: +n.keepAlive || K,
                            vue: n.vue || !1,
                            taro: n.taro || !1,
                            cml: n.cml || !1,
                            wepy: n.wepy || !1,
                            host: n.host && n.host.indexOf("http") >= 0 ? "https://".concat(n.host.slice(n.host.indexOf("://") + 3)) : "https://wxapi.growingio.com",
                            sdkVer: U.sdkVer
                        }, gioGlobal.vdsConfig = this.vdsConfig, gioGlobal.platformConfig = U, this.info = new R(this), 
                        t || (this.vdsConfig.appId = this.info.getAppId() || e), this.observer = new q(this), 
                        this.uploader = new D(this), this.config = new $(this), this.start = !0, n.vue && (this.vueRootVMs = {}, 
                        this._proxyVue(n.vue)), n.taro && (this.taroRootVMs = {}, this._proxyTaro(n.taro)), 
                        n.cml && (gioGlobal.platformConfig.hooks.Component = !1, this._proxyCml(n.cml)), 
                        n.wepy && (this.wepyRootVMs = {}, this._proxyWepy(n.wepy)), "quickapp" === gioGlobal.platformConfig.platform && this.info.initShareAppMessage(this), 
                        this._start());
                    }
                }, {
                    key: "setConfig",
                    value: function(e) {
                        this.init(e.projectId, e.appId, e);
                    }
                }, {
                    key: "setVue",
                    value: function(e) {
                        this.vueRootVMs || (this.vueRootVMs = {}), this.vdsConfig.vue = !0, this._proxyVue(e);
                    }
                }, {
                    key: "_proxyVue",
                    value: function(e) {
                        if (void 0 !== e.mixin) {
                            var t = this;
                            e.mixin({
                                created: function() {
                                    if (this.$options.methods) for (var e = Object.keys(this.$options.methods), t = 0, n = Object.keys(this); t < n.length; t++) {
                                        var i = n[t];
                                        0 > e.indexOf(i) || "function" != typeof this[i] || (Object.defineProperty(this[i], "proxiedName", {
                                            value: i
                                        }), Object.defineProperty(this[i], "isProxied", {
                                            value: !0
                                        }));
                                    }
                                },
                                beforeMount: function() {
                                    var e = this.$root;
                                    e.$mp && "page" === e.$mp.mpType ? e.$mp.page && (t.vueRootVMs[e.$mp.page.route] = e) : "page" === e.mpType && "page" === this.mpType && e.$mp.page && (t.vueRootVMs[e.$mp.page.route || e.$mp.page.is] = e, 
                                    -1 !== [ "wx", "qq", "tt" ].indexOf(gioGlobal.gio__platform) && m.instrumentPageComponent(e.$mp.page));
                                }
                            });
                        }
                    }
                }, {
                    key: "_proxyTaro",
                    value: function(e) {
                        var t = this, n = e.createComponent, i = this.vdsConfig.usePlugin;
                        if (e.createComponent = function(e, r) {
                            for (var o = e; o && o.prototype; ) {
                                for (var a = Object.keys(Object.getOwnPropertyDescriptors(o.prototype) || {}), s = 0; a.length > s; s++) if (a[s].startsWith("func__")) {
                                    var u = o.name, c = a[s].slice(6);
                                    t.taroRootVMs[a[s]] = u + "_" + ("" + e.prototype[a[s]]).match(/this\.__triggerPropsFn\("(.+)",/)[1] + "_" + c;
                                }
                                o = Object.getPrototypeOf(o);
                            }
                            var l = n(e, r), g = -1 !== [ "MinP", "qq" ].indexOf(U.platform), p = g ? l && l.methods : l;
                            return i ? (m.instrument(p), r && m.instrumentPageComponent(p)) : r && g && m.instrumentPageComponent(p), 
                            l;
                        }, i) {
                            var r = e.createApp;
                            e.createApp = function(e) {
                                var t = r(e);
                                return t._growing_app_ = !0, m.instrument(t), t;
                            };
                        }
                    }
                }, {
                    key: "_proxyCml",
                    value: function(e) {
                        var t = e.createApp, n = e.createComponent;
                        e.createApp = function(e) {
                            return e._growing_app_ = !0, t(m.instrument(e));
                        }, e.createComponent = function(e) {
                            return n(e.data && e.data.isComponent ? Object.assign({}, e, {
                                methods: m.instrument(e.methods)
                            }) : e);
                        };
                    }
                }, {
                    key: "_proxyWepy",
                    value: function(e) {
                        var t = this, n = e.page, i = function(e) {
                            for (var n = Object.keys(e), i = 0; n.length > i; i++) for (var r = Object.keys(e[n[i]]), o = 0; r.length > o; o++) if ("function" == typeof e[n[i]][r[o]]) {
                                var a = ("" + e[n[i]][r[o]]).match(/_vm\.(.+)\(.*\)/);
                                a && a[1] && (t.wepyRootVMs[n[i]] || (t.wepyRootVMs[n[i]] = {}), t.wepyRootVMs[n[i]][r[o]] = a[1]), 
                                t.vdsConfig.usePlugin && (e[n[i]][r[o]] = m.hook("_proxy", e[n[i]][r[o]]));
                            }
                        };
                        e.page = function(e, t) {
                            return t.handlers && i(t.handlers), m.instrumentPageComponent(e), n(e, t);
                        };
                        var r = e.component;
                        if (e.component = function(e, t) {
                            return t.handlers && i(t.handlers), r(e, t);
                        }, this.vdsConfig.usePlugin) {
                            var o = e.app;
                            e.app = function(e, t) {
                                return e._growing_app_ = !0, o(m.instrument(e), t);
                            };
                        }
                    }
                }, {
                    key: "_start",
                    value: function() {
                        m.initInstrument(this.observer);
                        try {
                            gioGlobal && U.canHook && (U.hooks.App && (gioGlobal.App = App), U.hooks.Page && (gioGlobal.Page = Page), 
                            U.hooks.Component && (gioGlobal.Component = Component), U.hooks.Behavior && (gioGlobal.Behavior = Behavior));
                        } catch (e) {}
                    }
                }, {
                    key: "setDataCollect",
                    value: function(e) {
                        this.config.setDataCollect(e);
                    }
                }, {
                    key: "login",
                    value: function(e) {
                        if (this.vdsConfig.forceLogin) {
                            this.info.uid = e, this.vdsConfig.forceLogin = !1;
                            var t, n = r(this.uploadingMessages);
                            try {
                                for (n.s(); !(t = n.n()).done; ) {
                                    var i = t.value;
                                    i.u = e, this.upload(i);
                                }
                            } catch (e) {
                                n.e(e);
                            } finally {
                                n.f();
                            }
                        }
                    }
                }, {
                    key: "upload",
                    value: function(e) {
                        this.vdsConfig.dataCollect && (this.vdsConfig.forceLogin ? this.uploadingMessages.push(e) : (this.vdsConfig.debug && console.info("generate new event", JSON.stringify(e, 0, 2)), 
                        j.emitEvent("upload", [ e ]), this.uploader.upload(e)));
                    }
                }, {
                    key: "forceFlush",
                    value: function() {
                        this.info.esid = this.observer.esid, this.uploader.forceFlush();
                    }
                }, {
                    key: "proxy",
                    value: function(e, t) {
                        try {
                            if ("setVue" === e) this.setVue(t[0]); else if ("setDataCollect" === e) this.setDataCollect(t[0]); else if ("setStopTrack" === e) this.setDataCollect(!t[0]); else if ("collectImp" === e) this.collectImp(t[0], t[1]); else if (this.observer && this.observer[e]) return this.observer[e].apply(this.observer, t);
                        } catch (e) {
                            console.error(e);
                        }
                    }
                }, {
                    key: "collectImp",
                    value: function(e) {
                        var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : null;
                        this.info.collectImp(e, t);
                    }
                } ]), e;
            }();
            function F(e, t) {
                if (l(e) != l(t)) return !1;
                if ("string" == typeof e || "number" == typeof e || "boolean" == typeof e || "function" == typeof e || void 0 == e || void 0 == t) return Object.is(e, t);
                if (Array.isArray(e) && Array.isArray(t)) return e.length === t.length && e.every(function(e, n) {
                    return F(e, t[n]);
                });
                if ("[object Object]" === Object.prototype.toString.call(e) && "[object Object]" === Object.prototype.toString.call(t)) {
                    var n = Object.keys(e), i = Object.keys(t);
                    return !(!n.every(function(n) {
                        return t.hasOwnProperty(n) && F(e[n], t[n]);
                    }) || !i.every(function(n) {
                        return e.hasOwnProperty(n) && F(t[n], e[n]);
                    }));
                }
                return !1;
            }
            var Q = function(e, t) {
                if ("string" == typeof t) {
                    "?" !== t[0] && (t = "?" + t), e = e.replace(/[\[\]]/g, "\\$&");
                    var n = RegExp("[?&]" + e + "(=([^&#]*)|&|#|$)").exec(t);
                    return n ? n[2] ? decodeURIComponent(n[2].replace(/\+/g, " ")) : "" : null;
                }
            }, W = function() {
                function e(t) {
                    u(this, e), this.growingio = t, this.namespace = "push-user-status", this.userTagDuration = 432e7, 
                    this.eventTagDuration = 864e5, this.handleCs1 = this.handleCs1.bind(this), this.handleClearCs1 = this.handleClearCs1.bind(this), 
                    this.handleEvent = this.handleEvent.bind(this), this.addEventListener();
                }
                return c(e, [ {
                    key: "addEventListener",
                    value: function() {
                        j.on("appOpen", this.handleEvent), j.on("upload", this.handleEvent), j.on("setCs1", this.handleCs1), 
                        j.on("clearCs1", this.handleClearCs1);
                    }
                }, {
                    key: "handleCs1",
                    value: function(e) {
                        e !== this.get("cs1") && (this.set("cs1", e), this.set("bcs", void 0), j.emit("cs1Refresh"));
                    }
                }, {
                    key: "handleClearCs1",
                    value: function() {
                        this.set("cs1", void 0), this.set("bcs", void 0);
                    }
                }, {
                    key: "handleEvent",
                    value: function(e) {
                        if (e) switch (e.t) {
                          case "vst":
                          case "vstr":
                          case "ppl":
                            this.storeFilters(e, this.generateEventKey.bind(this, "userAttrs"), this.formatUserFilterVars);
                            break;

                          case "cstm":
                            this.storeFilters(e, this.generateEventKey.bind(this, "triggerAttrs"), this.formatEventFilterVars);

                          case "page":
                            this.setIsPreview(e);
                        }
                    }
                }, {
                    key: "setIsPreview",
                    value: function(e) {
                        if (e.q) {
                            var t = Q("scene", e.q);
                            if (t) {
                                var n = Q("gioMessageId", t);
                                if (n) {
                                    var i = {
                                        s: "splash",
                                        pw: "popupWindow",
                                        p: "push",
                                        b: "banner",
                                        ab: "abTest"
                                    }[Q("mt", t)] || "";
                                    gioGlobal.__growing__.marketingPreview = {
                                        messageId: n,
                                        msgType: i
                                    };
                                }
                            }
                        }
                    }
                }, {
                    key: "storeFilters",
                    value: function(e, t, n) {
                        var r = t(), o = this.get(r, this.eventTagDuration) || [], a = n.call(this, e), s = [].concat(i(o), i(a));
                        this.set(r, s);
                    }
                }, {
                    key: "formatUserFilterVars",
                    value: function(e) {
                        var t = e.var;
                        return t ? Object.keys(t).map(function(e) {
                            return {
                                key: e,
                                value: t[e]
                            };
                        }) : [];
                    }
                }, {
                    key: "formatEventFilterVars",
                    value: function(e) {
                        var t = e.var;
                        return [ {
                            key: e.n,
                            value: "",
                            event_variable: t ? Object.keys(t).map(function(e) {
                                return {
                                    key: e,
                                    value: t[e]
                                };
                            }) : []
                        } ];
                    }
                }, {
                    key: "generateEventKey",
                    value: function(e) {
                        return "".concat(e, "#").concat(this.get("cs1") || "");
                    }
                }, {
                    key: "_get",
                    value: function(e) {
                        return this.growingio.info.getStorageSync("".concat(this.namespace, "#").concat(e));
                    }
                }, {
                    key: "getUserAttrs",
                    value: function() {
                        var e = this.generateEventKey("userAttrs");
                        return this.get(e) || [];
                    }
                }, {
                    key: "getTriggerAttrs",
                    value: function() {
                        var e = this.generateEventKey("triggerAttrs");
                        return this.get(e) || [];
                    }
                }, {
                    key: "set",
                    value: function(e, t) {
                        var n = this._get(e), i = new Date();
                        i.setHours(0), i.setMinutes(0), i.setSeconds(0);
                        var r = {
                            startAt: i.getTime(),
                            value: t
                        };
                        n && F(r.value, JSON.parse(n).value) || this.growingio.info.setStorageSync("".concat(this.namespace, "#").concat(e), r);
                    }
                }, {
                    key: "get",
                    value: function(e) {
                        var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : this.userTagDuration, n = this._get(e);
                        if (n) {
                            var i = JSON.parse(n);
                            return Date.now() > i.startAt + t ? void 0 : i.value;
                        }
                    }
                } ]), e;
            }();
            try {
                var J = "tt";
                f(J), "frame" !== J && (gioGlobal.gio__platform = J);
            } catch (g) {}
            var z = new N(), Z = function() {
                var e = arguments[0];
                if (e) {
                    var t = 2 > arguments.length ? [] : [].slice.call(arguments, 1);
                    if ("init" === e) {
                        if (gioGlobal.vdsConfig) return void console.warn("SDK已经初始化成功，请检查是否加载过其他平台sdk");
                        if (1 > t.length) return void console.log('初始化 GrowingIO SDK 失败。请使用 gio("init", "你的GrowingIO项目ID", "你的应用APP_ID", options);');
                        z.init(t[0], t[1], t[2]);
                    } else {
                        if ("setConfig" !== e) return z.proxy(e, t);
                        if (!t[0]) return void console.log("初始化 GrowingIO SDK 失败。请检查你的config文件是否引入正确");
                        if (!t[0].projectId) return void console.log("初始化 GrowingIO SDK 失败。请检查你的 GrowingIO项目ID, 你的应用APP_ID 是否填写正确");
                        z.setConfig(t[0]);
                    }
                }
            };
            console.log("init growingio...");
            var X = m.GrowingPage, Y = m.GrowingApp, ee = m.GrowingComponent, te = m.GrowingBehavior, ne = j, ie = new W(z);
            gioGlobal.__growing__ = {
                gioEmitter: ne,
                gio: Z,
                growingio: z,
                userStorage: ie,
                marketingPreview: void 0
            }, gioGlobal.gio = Z, t.GioApp = Y, t.GioBehavior = te, t.GioComponent = ee, t.GioPage = X, 
            t.default = Z, t.gioEmitter = ne, t.growingio = z;
        }).call(this, n(45));
    },
    306: function(e, t, n) {
        "use strict";
        (function(e) {
            var i = n(99), r = n(101), o = n(102), a = n(67), s = n(68), u = n(59), c = n(60), l = n(52);
            Object.defineProperty(t, "__esModule", {
                value: !0
            });
            var g, p = {
                devVer: 1,
                guid: function() {
                    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(e) {
                        var t = 16 * Math.random() | 0;
                        return ("x" == e ? t : 3 & t | 8).toString(16);
                    });
                },
                getScreenHeight: function(e) {
                    return e.pixelRatio ? Math.round(e.screenHeight * e.pixelRatio) : e.screenHeight;
                },
                getScreenWidth: function(e) {
                    return e.pixelRatio ? Math.round(e.screenWidth * e.pixelRatio) : e.screenWidth;
                },
                getOS: function(e) {
                    if (e) {
                        var t = e.toLowerCase();
                        return -1 != t.indexOf("android") ? "".concat(gioGlobal.platformConfig.name, "-Android") : -1 != t.indexOf("ios") ? "".concat(gioGlobal.platformConfig.name, "-iOS") : e;
                    }
                },
                getOSV: function(e) {
                    return "".concat(gioGlobal.platformConfig.name, " ").concat(e);
                },
                isEmpty: function(e) {
                    for (var t in e) if (Object.prototype.hasOwnProperty.call(e, t)) return !1;
                    return !0;
                },
                compareVersion: function(e, t) {
                    e = e.split("."), t = t.split(".");
                    for (var n = Math.max(e.length, t.length); n > e.length; ) e.push("0");
                    for (;n > t.length; ) t.push("0");
                    for (var i = 0; n > i; i++) {
                        var r = parseInt(e[i]), o = parseInt(t[i]);
                        if (r > o) return 1;
                        if (o > r) return -1;
                    }
                    return 0;
                }
            }, f = function(t) {
                Object.defineProperty(Object.prototype, "gioGlobal", {
                    get: function() {
                        return "quickApp" === t ? e.__proto__ : "my" === t ? $global : e;
                    },
                    configurable: !1,
                    enumerable: !1
                });
            }, h = function(e, t) {
                if (!e) return e;
                for (var n = t.split("."), i = e[n.shift()], r = 0, o = n.length; o > r; r++) {
                    var a = n.shift();
                    if (!i) return i;
                    i = i[a];
                }
                return i;
            }, d = function(e) {
                var t = {
                    eventId: void 0,
                    properties: {}
                };
                try {
                    if (e.hasOwnProperty("gioTrack") && "object" == l(e.gioTrack)) return t.eventId = e.gioTrack.name, 
                    t.properties = e.gioTrack.properties, t;
                    if (!e.gioImpTrack) return t;
                    t.eventId = e.gioImpTrack;
                    var n = /^gioTrack(.+)/, i = /^\w+$/;
                    for (var r in e) {
                        var o = void 0, a = r.match(n);
                        if (a && ("track" === (o = a[1].toLowerCase()) ? t.eventId = e[r] : t.properties[o] = e[r]), 
                        !i.test(t.eventId) || 10 > parseInt(t.eventId[0])) throw t.eventId = null, Error();
                    }
                } catch (e) {
                    console.warn("半打点IMP格式不正确, 事件名只能包含数字，字母和下划线，且不以数字开头, 请参考文档");
                }
                return t;
            }, v = function(e) {
                return e && "string" == typeof e && e.constructor === String;
            };
            Object.hasOwnProperty("getOwnPropertyDescriptors") || (g = "object" == ("undefined" === typeof Reflect ? "undefined" : l(Reflect)) && "function" == typeof Reflect.ownKeys ? Reflect.ownKeys : "function" == typeof Object.getOwnPropertySymbols ? function(e) {
                return Object.getOwnPropertyNames(e).concat(Object.getOwnPropertySymbols(e));
            } : Object.getOwnPropertyNames, Object.defineProperty(Object, "getOwnPropertyDescriptors", {
                configurable: !0,
                writable: !0,
                value: function(e) {
                    return g(e).reduce(function(t, n) {
                        return Object.defineProperty(t, n, {
                            configurable: !0,
                            enumerable: !0,
                            writable: !0,
                            value: Object.getOwnPropertyDescriptor(e, n)
                        });
                    }, {});
                }
            }));
            var y = function(e) {
                var t = m.observer.growingio;
                t && t.vdsConfig.followShare && e && e.path && (e.path = -1 === e.path.indexOf("?") ? e.path + "?suid=" + t.info.uid : e.path + "&suid=" + t.info.uid);
            }, m = {
                defaultPageCallbacks: {},
                defaultAppCallbacks: {},
                appHandlers: null,
                pageHandlers: null,
                actionEventTypes: null,
                originalPage: null,
                originalApp: null,
                originalComponent: null,
                originalBehavior: null,
                observer: null,
                hook: function(e, t) {
                    return function() {
                        var n, i = arguments ? arguments[0] : void 0;
                        if (i && (i.currentTarget || i.target) && -1 != m.actionEventTypes.indexOf(i.type)) try {
                            m.observer.actionListener(i, e);
                        } catch (e) {
                            console.error(e);
                        }
                        var r = gioGlobal.platformConfig.lisiteners.app, o = gioGlobal.platformConfig.lisiteners.page;
                        if (this._growing_app_ && e !== r.appShow || this._growing_page_ && -1 === [ o.pageShow, o.pageClose, o.pageLoad, o.pageHide, o.tabTap ].indexOf(e) ? n = t.apply(this, arguments) : this._growing_app_ || this._growing_page_ || (n = t.apply(this, arguments)), 
                        this._growing_app_ && -1 !== m.appHandlers.indexOf(e)) {
                            try {
                                m.defaultAppCallbacks[e].apply(this, arguments);
                            } catch (e) {
                                console.error(e);
                            }
                            e === r.appShow && (n = t.apply(this, arguments));
                        }
                        if (this._growing_page_ && -1 !== m.pageHandlers.indexOf(e)) {
                            var a = Array.prototype.slice.call(arguments);
                            n && a.push(n);
                            try {
                                m.defaultPageCallbacks[e].apply(this, a);
                            } catch (e) {
                                console.error(e);
                            }
                            -1 !== [ o.pageShow, o.pageClose, o.pageLoad, o.pageHide, o.tabTap ].indexOf(e) ? n = t.apply(this, arguments) : y(n);
                        }
                        return n;
                    };
                },
                hookComponent: function(e, t) {
                    return function() {
                        var n = arguments ? arguments[0] : void 0;
                        if (n && (n.currentTarget || n.target) && -1 != m.actionEventTypes.indexOf(n.type)) try {
                            m.observer.actionListener(n, e);
                        } catch (e) {
                            console.error(e);
                        }
                        return t.apply(this, arguments);
                    };
                },
                instrument: function(e) {
                    for (var t in e) "function" == typeof e[t] && (e[t] = this.hook(t, e[t]));
                    return e._growing_app_ && m.appHandlers.map(function(t) {
                        e[t] || (e[t] = m.defaultAppCallbacks[t]);
                    }), e._growing_page_ && m.pageHandlers.map(function(t) {
                        e[t] || t === gioGlobal.platformConfig.lisiteners.page.shareApp || (e[t] = m.defaultPageCallbacks[t]);
                    }), e;
                },
                instrumentPageComponent: function(e) {
                    if (e) return m.pageHandlers.map(function(t) {
                        if ("function" == typeof e[t]) {
                            var n = e[t];
                            e[t] = function() {
                                var e = n.apply(this, arguments), i = Array.prototype.slice.call(arguments);
                                return e && i.push(e), m.observer.pageListener(this, t, i), t === gioGlobal.platformConfig.lisiteners.page.shareApp && y(e), 
                                e;
                            };
                        } else t !== gioGlobal.platformConfig.lisiteners.page.shareApp && (e[t] = function() {
                            m.observer.pageListener(this, t, arguments);
                        });
                    }), e;
                },
                instrumentComponent: function(e) {
                    if (e.methods) {
                        var t = e.methods;
                        for (var n in t) "function" == typeof t[n] && (e.methods[n] = this.hookComponent(n, t[n]));
                    }
                    return e;
                },
                GrowingPage: function(e) {
                    return e._growing_page_ = !0, m.originalPage(m.instrument(e));
                },
                GrowingComponent: function(e) {
                    return m.originalComponent(m.instrumentComponent(e));
                },
                GrowingBehavior: function(e) {
                    return m.originalBehavior(m.instrumentComponent(e));
                },
                GrowingApp: function(e) {
                    return e._growing_app_ = !0, m.originalApp(m.instrument(e));
                },
                initPlatformInfo: function(e) {
                    m.appHandlers = e.appHandlers, m.pageHandlers = e.pageHandlers, m.actionEventTypes = e.actionEventTypes, 
                    m.originalApp = e.originalApp, m.originalPage = e.originalPage, m.originalComponent = e.originalComponent, 
                    m.originalBehavior = e.originalBehavior;
                },
                initInstrument: function(e) {
                    if (m.initPlatformInfo(gioGlobal.platformConfig), m.observer = e, m.pageHandlers.forEach(function(e) {
                        m.defaultPageCallbacks[e] = function() {
                            m.observer.pageListener(this, e, arguments);
                        };
                    }), m.appHandlers.forEach(function(e) {
                        m.defaultAppCallbacks[e] = function() {
                            m.observer.appListener(this, e, arguments);
                        };
                    }), gioGlobal.platformConfig.canHook) {
                        var t = gioGlobal.platformConfig.hooks;
                        t.App && !gioGlobal.growingAppInited && (App = function() {
                            return m.GrowingApp(arguments[0]);
                        }, gioGlobal.growingAppInited = !0), t.Page && !gioGlobal.growingPageInited && (Page = function() {
                            return m.GrowingPage(arguments[0]);
                        }, gioGlobal.growingPageInited = !0), t.Component && !gioGlobal.growingComponentInited && (Component = function() {
                            return m.GrowingComponent(arguments[0]);
                        }, gioGlobal.growingComponentInited = !0), t.Behavior && !gioGlobal.growingBehaviorInited && (Behavior = function() {
                            return m.GrowingBehavior(arguments[0]);
                        }, gioGlobal.growingBehaviorInited = !0);
                    }
                    gioGlobal.GioPage = m.GrowingPage, gioGlobal.GioApp = m.GrowingApp, gioGlobal.GioComponent = m.GrowingComponent, 
                    gioGlobal.GioBehavior = m.GrowingBehavior, gioGlobal.trackApp = function() {
                        var e = arguments[0];
                        return e._growing_app_ = !0, m.instrument(e);
                    }, gioGlobal.trackPage = function() {
                        var e = arguments[0];
                        return e._growing_page_ = !0, m.instrument(e);
                    }, gioGlobal.trackComponent = function() {
                        return m.instrument(arguments[0]);
                    }, gioGlobal.trackBehavior = function() {
                        return m.instrument(arguments[0]);
                    };
                }
            }, b = function() {
                function e() {
                    u(this, e), this.queries = {}, this.pvar = {};
                }
                return c(e, [ {
                    key: "touch",
                    value: function(e) {
                        this.path = e.route, this.time = Date.now(), this.query = this.queries[e.route] ? this.queries[e.route] : void 0;
                    }
                }, {
                    key: "addQuery",
                    value: function(e, t) {
                        this.queries[e.route] = t ? this._getQuery(t) : null;
                    }
                }, {
                    key: "_getQuery",
                    value: function(e) {
                        return Object.keys(e).filter(function(e) {
                            return "wxShoppingListScene" !== e;
                        }).map(function(t) {
                            return "".concat(t, "=").concat(e[t]);
                        }).join("&");
                    }
                }, {
                    key: "touchRelatedPvarData",
                    value: function(e) {
                        var t = "".concat(e.p, "?").concat(e.q);
                        this.pvar[t] ? this.pvar[t].push(e) : this.pvar[t] = [ e ];
                    }
                } ]), e;
            }(), w = {
                tap: [ "tap", "click" ],
                longtap: [ "longtap" ],
                input: [ "input" ],
                blur: [ "change", "blur" ],
                submit: [ "submit" ],
                focus: [ "focus" ]
            }, _ = /^function[^\(]*\([^\)]+\).*[^\.]+\.([^\(]+)\(.*/;
            function k(e) {
                return e && e.$attrs ? e.$attrs.mpcomid : "0";
            }
            function x(e, t, n) {
                return !(!e || !t) && (t === e || 0 === t.indexOf(e + n));
            }
            function P(e, t, n) {
                void 0 === t && (t = []);
                var i = t.slice(1);
                if (!i.length) return e;
                var r = i.join(n), o = "";
                return i.reduce(function(e, t) {
                    for (var i = e.$children.length, a = 0; i > a; a++) {
                        var s = e.$children[a], u = k(s);
                        if (o && (u = o + n + u), x(u, r, n)) return o = u, s;
                    }
                    return e;
                }, e);
            }
            function C(e, t, n) {
                void 0 === n && (n = []);
                var i = [];
                if (!e || !e.tag) return i;
                var r = e || {}, o = r.data;
                void 0 === o && (o = {});
                var a = r.children;
                void 0 === a && (a = []);
                var s = r.componentInstance;
                s ? Object.keys(s.$slots).forEach(function(e) {
                    var r = s.$slots[e];
                    (Array.isArray(r) ? r : [ r ]).forEach(function(e) {
                        i = i.concat(C(e, t, n));
                    });
                }) : a.forEach(function(e) {
                    i = i.concat(C(e, t, n));
                });
                var u = o.attrs, c = o.on;
                return u && c && u.eventid === t && n.forEach(function(e) {
                    var t = c[e];
                    "function" == typeof t ? i.push(t) : Array.isArray(t) && (i = i.concat(t));
                }), i;
            }
            var S = "~", E = "^";
            function O(e, t) {
                return e === t || "regionchange" === t && ("begin" === e || "end" === e);
            }
            var I = function() {
                function e(t) {
                    u(this, e), this.vueVM = t;
                }
                return c(e, [ {
                    key: "getHandle",
                    value: function(e) {
                        var t = e.type, n = e.target;
                        void 0 === n && (n = {});
                        var i = (e.currentTarget || n).dataset;
                        void 0 === i && (i = {});
                        var r = i.comkey;
                        void 0 === r && (r = "");
                        var o = i.eventid, a = -1 !== r.indexOf("_") ? "_" : ",", s = P(this.vueVM, r.split(a), a);
                        if (s) {
                            var u = C(s._vnode, o, w[t] || [ t ]);
                            if (u.length) {
                                var c = u[0];
                                if (c.isProxied) return c.proxiedName;
                                try {
                                    var l = ("" + c).replace("\n", "");
                                    if (l.match(_)) {
                                        var g = _.exec(l);
                                        if (g && g.length > 1) return g[1];
                                    }
                                } catch (e) {}
                                return c.name;
                            }
                        }
                    }
                }, {
                    key: "handleEvent",
                    value: function(e) {
                        var t, n = e.type, i = (e.currentTarget || e.target).dataset;
                        return (i.eventOpts || i["event-opts"]).forEach(function(e) {
                            var i = e[0], r = e[1];
                            i = (i = i.charAt(0) === E ? i.slice(1) : i).charAt(0) === S ? i.slice(1) : i, r && O(n, i) && r.forEach(function(e) {
                                t = e[0];
                            });
                        }), t;
                    }
                } ]), e;
            }();
            function T() {}
            var A = T.prototype;
            A.emit = function() {}, A.on = function() {}, A.emitEvent = function(e) {};
            var j = new T();
            function G(e) {
                return null !== e && "[object Object]" === Object.prototype.toString.call(e) && Object.keys(e).length > 0;
            }
            var V = function() {
                function e(t) {
                    u(this, e), this.growingio = t, this.esid = 0, this.info = t.info;
                }
                return c(e, [ {
                    key: "setUserAttributes",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "setUserId",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "clearUserId",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "sendVisitEvent",
                    value: function(e, t) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "track",
                    value: function(e, t) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "_sendEvent",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                } ]), e;
            }(), L = {
                tap: "clck",
                longpress: "lngprss",
                longtap: "lngprss"
            }, q = function(e) {
                a(n, e);
                var t = s(n);
                function n(e) {
                    var i;
                    return u(this, n), i = t.call(this, e), i.growingio = e, i.info = e.info, i.currentPage = new b(), 
                    i.scene = null, i._sessionId = null, i.cs1 = null, i.lastPageEvent = null, i.lastVstArgs = void 0, 
                    i.lastCloseTime = null, i.lastScene = void 0, i.keepAlive = e.vdsConfig.keepAlive, 
                    i.isPauseSession = !1, i.isGettingUid = !1, i.esid = 0 === i.info.esid ? 1 : i.info.esid, 
                    i.uploadingMessages = [], i;
                }
                return c(n, [ {
                    key: "sessionId",
                    get: function() {
                        return null === this._sessionId && (this._sessionId = p.guid()), this._sessionId;
                    }
                }, {
                    key: "resetSessionId",
                    value: function() {
                        this._sessionId = null;
                    }
                }, {
                    key: "pauseSession",
                    value: function() {
                        this.isPauseSession = !0;
                    }
                }, {
                    key: "getVisitorId",
                    value: function() {
                        return this.info.uid;
                    }
                }, {
                    key: "getUserId",
                    value: function() {
                        return this.cs1;
                    }
                }, {
                    key: "getGioInfo",
                    value: function() {
                        return "giou=".concat(this.getVisitorId(), "&giocs1=").concat(this.getUserId(), "&gios=").concat(this.sessionId, "&gioprojectid=").concat(this.growingio.vdsConfig.projectId, "&gioappid=").concat(this.growingio.vdsConfig.appId, "&gioplatform=").concat(gioGlobal.platformConfig.platform);
                    }
                }, {
                    key: "setUserId",
                    value: function(e) {
                        var t = e + "";
                        t && 100 > t.length && (this.cs1 = t, j.emitEvent("setCs1", [ t ]), this.lastPageEvent && this._sendEvent(this.lastPageEvent));
                    }
                }, {
                    key: "clearUserId",
                    value: function() {
                        this.cs1 = null, j.emitEvent("clearCs1");
                    }
                }, {
                    key: "appListener",
                    value: function(e, t, n) {
                        var i = gioGlobal.platformConfig.lisiteners.app;
                        this.isPauseSession || (this.growingio.vdsConfig.debug && console.log("App.", t, Date.now()), 
                        t == i.appShow ? (j.emitEvent("appShow"), this._parseScene(n), !this.lastCloseTime || Date.now() - this.lastCloseTime > this.keepAlive || this.lastScene && this.scene !== this.lastScene ? (this.resetSessionId(), 
                        this.sendVisitEvent(n, this.growingio.vdsConfig.getLocation.type), this.lastVstArgs = n, 
                        this.useLastPageTime = !1, this.lastPageEvent = void 0) : this.lastPageEvent && (this.useLastPageTime = !0)) : t == i.appClose ? (this.lastScene = this.scene, 
                        this.growingio.forceFlush(), this.info.syncStorage(), this.isPauseSession || (this.lastCloseTime = Date.now(), 
                        this.sendVisitCloseEvent())) : t == i.appError && this.sendErrorEvent(n));
                    }
                }, {
                    key: "pageListener",
                    value: function(e, t, n) {
                        var i = gioGlobal.platformConfig.lisiteners.page;
                        if (this.growingio.vdsConfig.wepy && (e.route = e.$is), e.route || (e.route = this.info.getPagePath(e)), 
                        this.growingio.vdsConfig.debug && console.log("Page.", e.route, "#", t, Date.now()), 
                        t === i.pageShow) {
                            var r = h(e, "$page.query");
                            p.isEmpty(r) || "quickApp" !== gioGlobal.gio__platform || this.currentPage.addQuery(e, r), 
                            this.isPauseSession ? this.isPauseSession = !1 : (this.currentPage.touch(e), this.useLastPageTime && (this.currentPage.time = this.lastPageEvent.tm, 
                            this.useLastPageTime = !1), this.sendPage(e));
                        } else if (t === i.pageLoad) {
                            var o = n[0];
                            p.isEmpty(o) || "quickApp" === gioGlobal.gio__platform || this.currentPage.addQuery(e, o);
                        } else if (t === i.pageHide) this.growingio._observer && this.growingio._observer.disconnect(); else if (t === i.pageClose) this.currentPage.pvar["".concat(this.currentPage.path, "?").concat(this.currentPage.query)] = void 0; else if (t === i.shareApp) {
                            var a = null, s = null;
                            2 > n.length ? 1 === n.length && (n[0].from ? a = n[0] : n[0].title && (s = n[0])) : (a = n[0], 
                            s = n[1]), this.pauseSession(), this.sendPageShare(e, a, s);
                        } else "onTabItemTap" === t && this.sendTabClick(n[0]);
                    }
                }, {
                    key: "actionListener",
                    value: function(e, t) {
                        if (!h(e, "currentTarget.dataset.growingIgnore") && !h(e, "target.dataset.growingIgnore")) {
                            var n = gioGlobal.platformConfig.lisiteners.actions;
                            if ("_cmlEventProxy" !== t) {
                                if ("handleProxy" === t && this.growingio.vueRootVMs && this.growingio.vueRootVMs[this.currentPage.path]) {
                                    var i = new I(this.growingio.vueRootVMs[this.currentPage.path]).getHandle(e);
                                    i && (t = i);
                                }
                                if ("__e" === t && this.growingio.vueRootVMs && this.growingio.vueRootVMs[this.currentPage.path]) {
                                    var r = new I(this.growingio.vueRootVMs[this.currentPage.path]).handleEvent(e);
                                    r && (t = r);
                                }
                                if ("_proxy" === t && this.growingio.wepyRootVMs) {
                                    var o = e.currentTarget.dataset.wpyEvt, a = e.type;
                                    h(this, "growingio.wepyRootVMs.".concat(o, ".").concat(a)) && (t = this.growingio.wepyRootVMs[o][a]);
                                }
                                h(this, "growingio.taroRootVMs.".concat(t)) && (t = this.growingio.taroRootVMs[t]), 
                                this.growingio.vdsConfig.debug && console.log("Click on ", t, Date.now()), -1 !== n.click.indexOf(e.type) ? (this.sendClick(e, t), 
                                "getuserinfo" === e.type && h(e, "detail.userInfo") && this.setVisitor(e.detail.userInfo)) : -1 !== n.change.indexOf(e.type) ? this.sendChange(e, t) : -1 !== n.submit.indexOf(e.type) && this.sendSubmit(e, t);
                            }
                        }
                    }
                }, {
                    key: "sendVideoCstm",
                    value: function(e) {
                        this.track("video-".concat(e.type), e.var);
                    }
                }, {
                    key: "track",
                    value: function(e, t) {
                        if ("string" != typeof e || null === e || void 0 === e || 0 === e.length || !e.match(/^\w+$/) || 10 > parseInt(e[0])) console.warn("埋点格式不正确, 事件名只能包含数字，字母和下划线，且不以数字开头, 请参考文档"); else {
                            var n = {
                                t: "cstm",
                                ptm: this.currentPage.time,
                                p: this.currentPage.path,
                                q: this.currentPage.query,
                                n: e
                            };
                            G(t) && (n.var = t), this._sendEvent(n);
                        }
                    }
                }, {
                    key: "identify",
                    value: function(e, t) {
                        void 0 !== e && 0 !== e.length && (this.growingio.login(e), this._sendEvent({
                            t: "vstr",
                            var: {
                                openid: e,
                                unionid: t
                            }
                        }));
                    }
                }, {
                    key: "setVisitor",
                    value: function(e) {
                        G(e) && this._sendEvent({
                            t: "vstr",
                            var: e
                        });
                    }
                }, {
                    key: "setUser",
                    value: function(e) {
                        this.cs1 && G(e) && this._sendEvent({
                            t: "ppl",
                            var: e
                        });
                    }
                }, {
                    key: "setPage",
                    value: function(e) {
                        if (G(e)) {
                            var t = {
                                t: "pvar",
                                ptm: this.currentPage.time,
                                p: this.currentPage.path,
                                q: this.currentPage.query,
                                var: e
                            };
                            this.currentPage.touchRelatedPvarData(t), this._sendEvent(t);
                        }
                    }
                }, {
                    key: "setEvar",
                    value: function(e) {
                        G(e) && this._sendEvent({
                            t: "evar",
                            var: e
                        });
                    }
                }, {
                    key: "getLocation",
                    value: function(e) {
                        this.growingio.vdsConfig.getLocation.autoGet = !0, this.sendVisitEvent(this.lastVstArgs, e);
                    }
                }, {
                    key: "sendVisitEvent",
                    value: function(e, t) {
                        var n = this;
                        this.info.getSystemInfo().then(function(i) {
                            var r = i || {}, o = {
                                t: "vst",
                                tm: Date.now(),
                                av: n.info.sdkVer,
                                db: r.brand,
                                dm: r.model && r.model.replace(/<.*>/, ""),
                                sh: p.getScreenHeight(r),
                                sw: p.getScreenWidth(r),
                                os: p.getOS(r.platform),
                                osv: p.getOSV(r.version),
                                l: r.language
                            };
                            if (n.growingio.vdsConfig.appVer && (o.cv = n.growingio.vdsConfig.appVer + ""), 
                            e.length > 0) {
                                var a = e[0];
                                o.p = a.path || n.info.getPagePath(), p.isEmpty(a.query) || (o.q = n.currentPage._getQuery(a.query)), 
                                o.ch = "scn:".concat(n.info.scnPrefix).concat(n.scene), "quickapp" === n.info.platform ? o.rf = n.info.appSource.packageName : a.referrerInfo && a.referrerInfo.appId && h(a, "referrerInfo.appId") && (o.rf = a.referrerInfo.appId), 
                                n.info.getNetworkType().then(function(e) {
                                    if (e && (o.nt = e.networkType, n._sendEvent(o), n.growingio.vdsConfig.getLocation.autoGet)) {
                                        var i = JSON.parse(JSON.stringify(o));
                                        t && -1 !== [ "wgs84", "gcj02", 0, 1, 2 ].indexOf(t) || (t = "my" === gioGlobal.gio__platform ? 0 : "wgs84"), 
                                        n.info.getLocation(t).then(function(e) {
                                            e && (i.lat = e.latitude, i.lng = e.longitude, n._sendEvent(i));
                                        });
                                    }
                                });
                            }
                        });
                    }
                }, {
                    key: "sendVisitCloseEvent",
                    value: function() {
                        this._sendEvent({
                            t: "cls",
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        });
                    }
                }, {
                    key: "sendErrorEvent",
                    value: function(e) {
                        if (e && e.length > 0) {
                            var t = e[0];
                            if ("string" != typeof t) return;
                            var n, i = t.split("\n");
                            if (i && i.length > 1) {
                                var r = i[1].split(";");
                                if (r && r.length > 1) {
                                    var o = r[1].match(/at ([^ ]+) page (.*) function/);
                                    n = {
                                        key: i[0],
                                        error: r[0]
                                    }, o && o.length > 2 && (n.page = o[1], n.function = o[2]);
                                }
                            } else n = {
                                error: i && i[0]
                            };
                            this._sendEvent({
                                t: "cstm",
                                ptm: this.currentPage.time,
                                p: this.currentPage.path,
                                q: this.currentPage.query,
                                n: "onError",
                                var: n
                            });
                        }
                    }
                }, {
                    key: "sendPage",
                    value: function(e) {
                        var t = this, n = {
                            t: "page",
                            tm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        };
                        n.rp = this.lastPageEvent ? this.lastPageEvent.p : this.scene ? "scn:".concat(this.info.scnPrefix).concat(this.scene) : null;
                        var i = this.info.getPageTitle(e);
                        i && i.length > 0 && (n.tl = i), this._sendEvent(n), this.lastPageEvent = n;
                        var r = this.currentPage.pvar["".concat(this.currentPage.path, "?").concat(this.currentPage.query)];
                        r && r.length > 0 && r.map(function(e) {
                            e.ptm = t.currentPage.time, t._sendEvent(e);
                        });
                    }
                }, {
                    key: "sendPageShare",
                    value: function(e, t, n) {
                        this._sendEvent({
                            t: "cstm",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query,
                            n: "onShareAppMessage",
                            var: {
                                from: t ? t.from : void 0,
                                target: t && t.target ? t.target.id : void 0,
                                title: n ? n.title : void 0,
                                path: n ? decodeURI(n.path) : void 0
                            }
                        });
                    }
                }, {
                    key: "sendClick",
                    value: function(e, t) {
                        var n = {
                            t: L[e.type] || "clck",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        }, i = e.currentTarget || e.target, r = i.id;
                        (!r || "swan" === gioGlobal.gio__platform && /^_[0-9a-f]+/.test(r)) && (r = "");
                        var o = {
                            x: "".concat(r, "#").concat(t)
                        };
                        i.dataset.title && (o.v = i.dataset.title), i.dataset.src && (o.h = i.dataset.src), 
                        void 0 !== i.dataset.index && (o.idx = /^[\d]+$/.test(i.dataset.index) ? parseInt(i.dataset.index) : -1), 
                        n.e = [ o ], this._sendEvent(n);
                    }
                }, {
                    key: "sendSubmit",
                    value: function(e, t) {
                        var n = {
                            t: "sbmt",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        }, i = (e.currentTarget || e.target).id;
                        (!i || "swan" === gioGlobal.gio__platform && /^_[0-9a-f]+/.test(i)) && (i = ""), 
                        n.e = [ {
                            x: "".concat(i, "#").concat(t)
                        } ], this._sendEvent(n);
                    }
                }, {
                    key: "sendChange",
                    value: function(e, t) {
                        var n = {
                            t: "chng",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query
                        }, i = e.currentTarget || e.target, r = i.id;
                        (!r || "swan" === gioGlobal.gio__platform && /^_[0-9a-f]+/.test(r)) && (r = "");
                        var o = {
                            x: "".concat(r, "#").concat(t)
                        }, a = h(e, "detail.value") || h(e, "target.attr.value");
                        (i.dataset.growingTrack || i.dataset.growingtrack) && ("boolean" == typeof a || a && 0 !== a.length) && ("[object Array]" === Object.prototype.toString.call(a) ? (a = a.join(",")) && (o.v = a) : o.v = a), 
                        "change" === e.type && "autoplay" === h(e, "detail.source") || (n.e = [ o ], this._sendEvent(n));
                    }
                }, {
                    key: "sendTabClick",
                    value: function(e) {
                        var t = {
                            t: "clck",
                            ptm: this.currentPage.time,
                            p: this.currentPage.path,
                            q: this.currentPage.query,
                            e: [ {
                                x: "#onTabItemTap",
                                v: e.text,
                                idx: e.index,
                                h: "string" == typeof e.pagePath ? e.pagePath : JSON.stringify(e.pagePath)
                            } ]
                        };
                        this._sendEvent(t);
                    }
                }, {
                    key: "_sendEvent",
                    value: function(e) {
                        var t = this;
                        if (this.info.uid && this.esid) {
                            var n = this._buildEvent(e, this.info);
                            this.growingio.upload(n);
                        } else if (this.isGettingUid) this.uploadingMessages.push(e); else {
                            this.isGettingUid = !0;
                            var i = this.info.getStorage(this.info.uidKey), r = this.info.getStorage(this.info.esidKey);
                            Promise.all([ i, r ]).then(function(n) {
                                var i = o(n, 2), r = i[0], a = i[1];
                                r || (r = p.guid()), a || (a = 1), t.info.uid = r, t.info.esid = a, t.isGettingUid = !1;
                                var s = t._buildEvent(e, t.info);
                                for (t.growingio.upload(s); 0 !== t.uploadingMessages.length; ) {
                                    var u = t.uploadingMessages.shift();
                                    u = t._buildEvent(u, t.info), t.growingio.upload(u);
                                }
                            });
                        }
                    }
                }, {
                    key: "_buildEvent",
                    value: function(e, t) {
                        if (e.u = t.uid, e.s = this.sessionId, e.tm = e.tm || Date.now(), e.d = this.growingio.vdsConfig.appId, 
                        e.b = t.platform, null !== this.cs1 && (e.cs1 = this.cs1), e.var) {
                            var n = e.var;
                            Object.keys(n).forEach(function(t) {
                                "string" != typeof n[t] && (e.var[t] = JSON.stringify(n[t]));
                            });
                        }
                        return e.esid = this.esid++, e;
                    }
                }, {
                    key: "_parseScene",
                    value: function(e) {
                        if ("quickapp" === this.info.platform) {
                            var t = this.info.getAppSource(), n = t.extra || {}, i = t.type || "";
                            this.scene = i, this.setVisitor({
                                extra: JSON.stringify(n)
                            });
                        } else if (e.length > 0) {
                            var r = e[0];
                            this.scene = r.query && r.query.wxShoppingListScene ? r.query.wxShoppingListScene : r.scene ? r.scene : "NA";
                        }
                    }
                } ]), n;
            }(V), M = function() {
                function e(t) {
                    u(this, e), this.growing = t, this._uid = void 0, this._esid = void 0, this._gioId = void 0, 
                    this._userId = void 0, this._systemInfo = null, this.uidKey = "_growing_uid_", this.esidKey = "_growing_esid_", 
                    this.gioIdKey = "_growing_gioId_", this.userIdKey = "_growing_userId_", this.platform = gioGlobal.platformConfig.platform, 
                    this.sdkVer = gioGlobal.platformConfig.sdkVer, this.scnPrefix = gioGlobal.platformConfig.scnPrefix, 
                    "quickapp" !== gioGlobal.platformConfig.platform && this.initUserInfo();
                }
                return c(e, [ {
                    key: "esid",
                    get: function() {
                        return this._esid;
                    },
                    set: function(e) {
                        this._esid = e, this.setStorage(this.esidKey, this._esid);
                    }
                }, {
                    key: "uid",
                    get: function() {
                        return this._uid;
                    },
                    set: function(e) {
                        this._uid = e, this.setStorage(this.uidKey, this._uid);
                    }
                }, {
                    key: "gioId",
                    get: function() {
                        return this._gioId;
                    },
                    set: function(e) {
                        this._gioId = e, this.setStorage(this.gioIdKey, this._gioId);
                    }
                }, {
                    key: "userId",
                    get: function() {
                        return this._userId;
                    },
                    set: function(e) {
                        this._userId = e, this.setStorage(this.userIdKey, this._userId);
                    }
                }, {
                    key: "systemInfo",
                    get: function() {
                        return this._systemInfo;
                    }
                }, {
                    key: "initUserInfo",
                    value: function() {
                        this.uid = this.getStorageSync(this.uidKey), this.esid = +this.getStorageSync(this.esidKey);
                    }
                }, {
                    key: "syncStorage",
                    value: function() {
                        var e = this;
                        this.getStorage(this.uidKey).then(function(t) {
                            t || e.setStorage(e.uidKey, e._uid);
                        });
                    }
                }, {
                    key: "getAppId",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getAppSource",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getPageTitle",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getPagePath",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getStorage",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getStorageSync",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "setStorage",
                    value: function(e, t) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getSystemInfo",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getNetworkType",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getLocation",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "request",
                    value: function(e) {
                        e.url, e.header, e.method, e.data, e.success, e.fail;
                        throw Error("this a interface function");
                    }
                }, {
                    key: "collectImp",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "initShareAppMessage",
                    value: function(e) {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getCurrentPage",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getQuery",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getReferrer",
                    value: function() {
                        throw Error("this a interface function");
                    }
                }, {
                    key: "getInitPath",
                    value: function() {
                        throw Error("this a interface function");
                    }
                } ]), e;
            }(), R = function(e) {
                a(n, e);
                var t = s(n);
                function n(e) {
                    var i;
                    return u(this, n), i = t.call(this, e), i.growingio = e, i;
                }
                return c(n, [ {
                    key: "getAppId",
                    value: function() {
                        return "";
                    }
                }, {
                    key: "getPageTitle",
                    value: function(e) {
                        var t = "";
                        try {
                            e.data.title && e.data.title.length > 0 && (t = Array.isArray(e.data.title) ? e.data.title.join(" ") : e.data.title);
                        } catch (e) {
                            return "";
                        }
                        return t;
                    }
                }, {
                    key: "getStorage",
                    value: function(e) {
                        return new Promise(function(t) {
                            swan.getStorage({
                                key: e,
                                success: function(e) {
                                    return t(e.data);
                                },
                                fail: function() {
                                    return t(null);
                                }
                            });
                        });
                    }
                }, {
                    key: "getStorageSync",
                    value: function(e) {
                        return swan.getStorageSync(e);
                    }
                }, {
                    key: "setStorage",
                    value: function(e, t) {
                        swan.setStorage({
                            key: e,
                            data: t
                        });
                    }
                }, {
                    key: "getSystemInfo",
                    value: function() {
                        var e = this;
                        return new Promise(function(t) {
                            swan.getSystemInfo({
                                success: function(n) {
                                    e._systemInfo = n, t(n);
                                },
                                fail: function() {
                                    return t(null);
                                }
                            });
                        });
                    }
                }, {
                    key: "getNetworkType",
                    value: function() {
                        return new Promise(function(e) {
                            swan.getNetworkType({
                                success: function(t) {
                                    return e(t);
                                },
                                fail: function() {
                                    return e(null);
                                }
                            });
                        });
                    }
                }, {
                    key: "getSetting",
                    value: function() {
                        return new Promise(function(e) {
                            swan.getSetting({
                                success: e,
                                fail: function() {
                                    return e(null);
                                }
                            });
                        });
                    }
                }, {
                    key: "getLocation",
                    value: function(e) {
                        return new Promise(function(t) {
                            swan.getLocation({
                                type: e,
                                success: function(e) {
                                    return t(e);
                                },
                                fail: function() {
                                    return t(null);
                                }
                            });
                        });
                    }
                }, {
                    key: "request",
                    value: function(e) {
                        var t = e.url, n = e.header, i = e.method, r = e.data, o = e.success, a = e.fail;
                        return swan.request({
                            url: t,
                            header: n,
                            method: i,
                            data: r,
                            success: o,
                            fail: a
                        });
                    }
                }, {
                    key: "collectImp",
                    value: function(e) {
                        var t = this, n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : null;
                        this.growingio.vdsConfig.vue && (e = e.$mp.page), this.growingio.vdsConfig.taro && (e = e.$scope);
                        var i = {};
                        this.growingio._observer && this.growingio._observer.disconnect(), this.growingio._observer = e.isComponent ? e.createIntersectionObserver({
                            selectAll: !0
                        }) : swan.createIntersectionObserver(e, {
                            selectAll: !0
                        }), (n ? this.growingio._observer.relativeTo(n) : this.growingio._observer.relativeToViewport()).observe(".growing_collect_imp", function(e) {
                            if (e.id && !i[e.id]) {
                                var n = d(e.dataset), r = n.eventId, o = n.properties;
                                r && e.id && !i[e.id] && (t.growingio.observer.track(r, o), i[e.id] = !0);
                            }
                        });
                    }
                }, {
                    key: "getPagePath",
                    value: function(e) {
                        var t = getCurrentPages();
                        return t[0] && t[0].uri;
                    }
                }, {
                    key: "setStorageSync",
                    value: function(e, t) {
                        swan.setStorageSync(e, JSON.stringify(t));
                    }
                }, {
                    key: "removeStorageSync",
                    value: function(e) {
                        swan.removeStorageSync(e);
                    }
                }, {
                    key: "navigateTo",
                    value: function(e) {
                        swan.navigateTo(e);
                    }
                }, {
                    key: "switchTab",
                    value: function(e) {
                        swan.switchTab(e);
                    }
                } ]), n;
            }(M), D = function() {
                function e(t) {
                    u(this, e), this.growingio = t, this.messageQueue = [], this.uploadingQueue = [], 
                    this.uploadTimer = null, this.projectId = this.growingio.vdsConfig.projectId, this.appId = this.growingio.vdsConfig.appId, 
                    this.host = this.growingio.vdsConfig.host, this.url = "".concat(this.host, "/projects/").concat(this.projectId, "/apps/").concat(this.appId, "/collect");
                }
                return c(e, [ {
                    key: "upload",
                    value: function(e) {
                        var t = this;
                        this.messageQueue.push(e);
                        var n = this.messageQueue.length;
                        n > 100 && (this.messageQueue = this.messageQueue.slice(n - 100)), this.uploadTimer || (this.uploadTimer = setTimeout(function() {
                            t._flush(), t.uploadTimer = null;
                        }, 1e3));
                    }
                }, {
                    key: "forceFlush",
                    value: function() {
                        this.uploadTimer && (clearTimeout(this.uploadTimer), this.uploadTimer = null), this._flush();
                    }
                }, {
                    key: "_flush",
                    value: function() {
                        var e = this;
                        this.uploadingQueue = this.messageQueue.slice(), this.messageQueue = [], this.uploadingQueue.length > 0 && this.growingio.info.request({
                            url: "".concat(this.url, "?stm=").concat(Date.now()),
                            header: {
                                "content-type": "application/json"
                            },
                            method: "POST",
                            data: this.uploadingQueue,
                            success: function() {
                                e.messageQueue.length > 0 && e._flush();
                            },
                            fail: function(t) {
                                204 !== t.status && (e.messageQueue = e.uploadingQueue.concat(e.messageQueue));
                            }
                        });
                    }
                } ]), e;
            }(), H = {
                wx: {
                    name: "Weixin",
                    path: "./weixin"
                },
                qq: {
                    name: "QQ",
                    path: "./qq"
                },
                my: {
                    name: "Alipay",
                    path: "./alipay"
                },
                swan: {
                    name: "Baidu",
                    path: "./baidu"
                },
                tt: {
                    name: "Bytedance",
                    path: "./bytedance"
                },
                quickApp: {
                    name: "Quickapp",
                    path: "./quickApp"
                },
                frame: {
                    name: "Frame",
                    path: "./multipleFrame"
                }
            }, B = Object.assign({}, H.swan, {
                platform: "baidup",
                scnPrefix: "baidup_",
                appHandlers: [ "onShow", "onHide", "onError" ],
                pageHandlers: [ "onLoad", "onShow", "onShareAppMessage", "onTabItemTap", "onHide", "onUnload" ],
                actionEventTypes: [ "onclick", "tap", "longpress", "blur", "change", "submit", "confirm", "getuserinfo", "getphonenumber", "contact" ],
                originalApp: App,
                originalPage: Page,
                originalComponent: Component,
                originalBehavior: Behavior,
                canHook: !0,
                hooks: {
                    App: !0,
                    Page: !0,
                    Component: !0,
                    Behavior: !0
                },
                lisiteners: {
                    app: {
                        appShow: "onShow",
                        appClose: "onHide",
                        appError: "onError"
                    },
                    page: {
                        pageLoad: "onLoad",
                        pageShow: "onShow",
                        pageHide: "onHide",
                        pageClose: "onUnload",
                        tabTap: "onTabItemTap",
                        shareApp: "onShareAppMessage"
                    },
                    actions: {
                        click: [ "tap", "longpress", "getuserinfo", "getphonenumber", "contact" ],
                        change: [ "blur", "change", "confirm" ],
                        submit: [ "submit" ]
                    }
                }
            }), U = Object.assign({}, B, {
                sdkVer: "3.4.1"
            }), $ = function() {
                function e(t) {
                    u(this, e), this.growingio = t;
                }
                return c(e, [ {
                    key: "setDataCollect",
                    value: function(e) {
                        this.growingio.vdsConfig.dataCollect = e;
                    }
                }, {
                    key: "enableDebug",
                    value: function(e) {
                        e && console && (this.growingio.vdsConfig.debug = e);
                    }
                }, {
                    key: "setTrackerScheme",
                    value: function(e) {
                        var t = (e + "").toLocaleLowerCase();
                        "http" !== t && "https" !== t || (this.growingio.vdsConfig.scheme = "".concat(e, "://"));
                    }
                }, {
                    key: "setTrackerHost",
                    value: function(e) {
                        v(e) && (this.growingio.vdsConfig.host = e);
                    }
                } ]), e;
            }(), K = 3e5, N = function() {
                function e() {
                    u(this, e), this.uploadingMessages = [], this.start = !1;
                }
                return c(e, [ {
                    key: "init",
                    value: function(e, t, n) {
                        this.start || (t && "string" != typeof t && (n = t, t = ""), t || n || (t = "", 
                        n = {}), "alip" === U.platform && (n.vue || n.taro || n.cml || n.wepy) && (U.canHook = !0), 
                        n.usePlugin && (U.canHook = !1), this.vdsConfig = {
                            projectId: e,
                            appId: t,
                            appVer: n.version || "",
                            debug: n.debug || !1,
                            forceLogin: n.forceLogin || !1,
                            followShare: void 0 === n.followShare || n.followShare,
                            usePlugin: n.usePlugin || !1,
                            getLocation: {
                                autoGet: ("object" == l(n.getLocation) ? n.getLocation.autoGet : n.getLocation) || !1,
                                type: "object" == l(n.getLocation) && n.getLocation.type || "wgs84"
                            },
                            dataCollect: !("boolean" == typeof n.stopTrack && n.stopTrack || "boolean" == typeof n.dataCollect && !n.dataCollect),
                            keepAlive: +n.keepAlive || K,
                            vue: n.vue || !1,
                            taro: n.taro || !1,
                            cml: n.cml || !1,
                            wepy: n.wepy || !1,
                            host: n.host && n.host.indexOf("http") >= 0 ? "https://".concat(n.host.slice(n.host.indexOf("://") + 3)) : "https://wxapi.growingio.com",
                            sdkVer: U.sdkVer
                        }, gioGlobal.vdsConfig = this.vdsConfig, gioGlobal.platformConfig = U, this.info = new R(this), 
                        t || (this.vdsConfig.appId = this.info.getAppId() || e), this.observer = new q(this), 
                        this.uploader = new D(this), this.config = new $(this), this.start = !0, n.vue && (this.vueRootVMs = {}, 
                        this._proxyVue(n.vue)), n.taro && (this.taroRootVMs = {}, this._proxyTaro(n.taro)), 
                        n.cml && (gioGlobal.platformConfig.hooks.Component = !1, this._proxyCml(n.cml)), 
                        n.wepy && (this.wepyRootVMs = {}, this._proxyWepy(n.wepy)), "quickapp" === gioGlobal.platformConfig.platform && this.info.initShareAppMessage(this), 
                        this._start());
                    }
                }, {
                    key: "setConfig",
                    value: function(e) {
                        this.init(e.projectId, e.appId, e);
                    }
                }, {
                    key: "setVue",
                    value: function(e) {
                        this.vueRootVMs || (this.vueRootVMs = {}), this.vdsConfig.vue = !0, this._proxyVue(e);
                    }
                }, {
                    key: "_proxyVue",
                    value: function(e) {
                        if (void 0 !== e.mixin) {
                            var t = this;
                            e.mixin({
                                created: function() {
                                    if (this.$options.methods) for (var e = Object.keys(this.$options.methods), t = 0, n = Object.keys(this); t < n.length; t++) {
                                        var i = n[t];
                                        0 > e.indexOf(i) || "function" != typeof this[i] || (Object.defineProperty(this[i], "proxiedName", {
                                            value: i
                                        }), Object.defineProperty(this[i], "isProxied", {
                                            value: !0
                                        }));
                                    }
                                },
                                beforeMount: function() {
                                    var e = this.$root;
                                    e.$mp && "page" === e.$mp.mpType ? e.$mp.page && (t.vueRootVMs[e.$mp.page.route] = e) : "page" === e.mpType && "page" === this.mpType && e.$mp.page && (t.vueRootVMs[e.$mp.page.route || e.$mp.page.is] = e, 
                                    -1 !== [ "wx", "qq", "tt" ].indexOf(gioGlobal.gio__platform) && m.instrumentPageComponent(e.$mp.page));
                                }
                            });
                        }
                    }
                }, {
                    key: "_proxyTaro",
                    value: function(e) {
                        var t = this, n = e.createComponent, i = this.vdsConfig.usePlugin;
                        if (e.createComponent = function(e, r) {
                            for (var o = e; o && o.prototype; ) {
                                for (var a = Object.keys(Object.getOwnPropertyDescriptors(o.prototype) || {}), s = 0; a.length > s; s++) if (a[s].startsWith("func__")) {
                                    var u = o.name, c = a[s].slice(6);
                                    t.taroRootVMs[a[s]] = u + "_" + ("" + e.prototype[a[s]]).match(/this\.__triggerPropsFn\("(.+)",/)[1] + "_" + c;
                                }
                                o = Object.getPrototypeOf(o);
                            }
                            var l = n(e, r), g = -1 !== [ "MinP", "qq" ].indexOf(U.platform), p = g ? l && l.methods : l;
                            return i ? (m.instrument(p), r && m.instrumentPageComponent(p)) : r && g && m.instrumentPageComponent(p), 
                            l;
                        }, i) {
                            var r = e.createApp;
                            e.createApp = function(e) {
                                var t = r(e);
                                return t._growing_app_ = !0, m.instrument(t), t;
                            };
                        }
                    }
                }, {
                    key: "_proxyCml",
                    value: function(e) {
                        var t = e.createApp, n = e.createComponent;
                        e.createApp = function(e) {
                            return e._growing_app_ = !0, t(m.instrument(e));
                        }, e.createComponent = function(e) {
                            return n(e.data && e.data.isComponent ? Object.assign({}, e, {
                                methods: m.instrument(e.methods)
                            }) : e);
                        };
                    }
                }, {
                    key: "_proxyWepy",
                    value: function(e) {
                        var t = this, n = e.page, i = function(e) {
                            for (var n = Object.keys(e), i = 0; n.length > i; i++) for (var r = Object.keys(e[n[i]]), o = 0; r.length > o; o++) if ("function" == typeof e[n[i]][r[o]]) {
                                var a = ("" + e[n[i]][r[o]]).match(/_vm\.(.+)\(.*\)/);
                                a && a[1] && (t.wepyRootVMs[n[i]] || (t.wepyRootVMs[n[i]] = {}), t.wepyRootVMs[n[i]][r[o]] = a[1]), 
                                t.vdsConfig.usePlugin && (e[n[i]][r[o]] = m.hook("_proxy", e[n[i]][r[o]]));
                            }
                        };
                        e.page = function(e, t) {
                            return t.handlers && i(t.handlers), m.instrumentPageComponent(e), n(e, t);
                        };
                        var r = e.component;
                        if (e.component = function(e, t) {
                            return t.handlers && i(t.handlers), r(e, t);
                        }, this.vdsConfig.usePlugin) {
                            var o = e.app;
                            e.app = function(e, t) {
                                return e._growing_app_ = !0, o(m.instrument(e), t);
                            };
                        }
                    }
                }, {
                    key: "_start",
                    value: function() {
                        m.initInstrument(this.observer);
                        try {
                            gioGlobal && U.canHook && (U.hooks.App && (gioGlobal.App = App), U.hooks.Page && (gioGlobal.Page = Page), 
                            U.hooks.Component && (gioGlobal.Component = Component), U.hooks.Behavior && (gioGlobal.Behavior = Behavior));
                        } catch (e) {}
                    }
                }, {
                    key: "setDataCollect",
                    value: function(e) {
                        this.config.setDataCollect(e);
                    }
                }, {
                    key: "login",
                    value: function(e) {
                        if (this.vdsConfig.forceLogin) {
                            this.info.uid = e, this.vdsConfig.forceLogin = !1;
                            var t, n = r(this.uploadingMessages);
                            try {
                                for (n.s(); !(t = n.n()).done; ) {
                                    var i = t.value;
                                    i.u = e, this.upload(i);
                                }
                            } catch (e) {
                                n.e(e);
                            } finally {
                                n.f();
                            }
                        }
                    }
                }, {
                    key: "upload",
                    value: function(e) {
                        this.vdsConfig.dataCollect && (this.vdsConfig.forceLogin ? this.uploadingMessages.push(e) : (this.vdsConfig.debug && console.info("generate new event", JSON.stringify(e, 0, 2)), 
                        j.emitEvent("upload", [ e ]), this.uploader.upload(e)));
                    }
                }, {
                    key: "forceFlush",
                    value: function() {
                        this.info.esid = this.observer.esid, this.uploader.forceFlush();
                    }
                }, {
                    key: "proxy",
                    value: function(e, t) {
                        try {
                            if ("setVue" === e) this.setVue(t[0]); else if ("setDataCollect" === e) this.setDataCollect(t[0]); else if ("setStopTrack" === e) this.setDataCollect(!t[0]); else if ("collectImp" === e) this.collectImp(t[0], t[1]); else if (this.observer && this.observer[e]) return this.observer[e].apply(this.observer, t);
                        } catch (e) {
                            console.error(e);
                        }
                    }
                }, {
                    key: "collectImp",
                    value: function(e) {
                        var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : null;
                        this.info.collectImp(e, t);
                    }
                } ]), e;
            }();
            function F(e, t) {
                if (l(e) != l(t)) return !1;
                if ("string" == typeof e || "number" == typeof e || "boolean" == typeof e || "function" == typeof e || void 0 == e || void 0 == t) return Object.is(e, t);
                if (Array.isArray(e) && Array.isArray(t)) return e.length === t.length && e.every(function(e, n) {
                    return F(e, t[n]);
                });
                if ("[object Object]" === Object.prototype.toString.call(e) && "[object Object]" === Object.prototype.toString.call(t)) {
                    var n = Object.keys(e), i = Object.keys(t);
                    return !(!n.every(function(n) {
                        return t.hasOwnProperty(n) && F(e[n], t[n]);
                    }) || !i.every(function(n) {
                        return e.hasOwnProperty(n) && F(t[n], e[n]);
                    }));
                }
                return !1;
            }
            var Q = function(e, t) {
                if ("string" == typeof t) {
                    "?" !== t[0] && (t = "?" + t), e = e.replace(/[\[\]]/g, "\\$&");
                    var n = RegExp("[?&]" + e + "(=([^&#]*)|&|#|$)").exec(t);
                    return n ? n[2] ? decodeURIComponent(n[2].replace(/\+/g, " ")) : "" : null;
                }
            }, W = function() {
                function e(t) {
                    u(this, e), this.growingio = t, this.namespace = "push-user-status", this.userTagDuration = 432e7, 
                    this.eventTagDuration = 864e5, this.handleCs1 = this.handleCs1.bind(this), this.handleClearCs1 = this.handleClearCs1.bind(this), 
                    this.handleEvent = this.handleEvent.bind(this), this.addEventListener();
                }
                return c(e, [ {
                    key: "addEventListener",
                    value: function() {
                        j.on("appOpen", this.handleEvent), j.on("upload", this.handleEvent), j.on("setCs1", this.handleCs1), 
                        j.on("clearCs1", this.handleClearCs1);
                    }
                }, {
                    key: "handleCs1",
                    value: function(e) {
                        e !== this.get("cs1") && (this.set("cs1", e), this.set("bcs", void 0), j.emit("cs1Refresh"));
                    }
                }, {
                    key: "handleClearCs1",
                    value: function() {
                        this.set("cs1", void 0), this.set("bcs", void 0);
                    }
                }, {
                    key: "handleEvent",
                    value: function(e) {
                        if (e) switch (e.t) {
                          case "vst":
                          case "vstr":
                          case "ppl":
                            this.storeFilters(e, this.generateEventKey.bind(this, "userAttrs"), this.formatUserFilterVars);
                            break;

                          case "cstm":
                            this.storeFilters(e, this.generateEventKey.bind(this, "triggerAttrs"), this.formatEventFilterVars);

                          case "page":
                            this.setIsPreview(e);
                        }
                    }
                }, {
                    key: "setIsPreview",
                    value: function(e) {
                        if (e.q) {
                            var t = Q("scene", e.q);
                            if (t) {
                                var n = Q("gioMessageId", t);
                                if (n) {
                                    var i = {
                                        s: "splash",
                                        pw: "popupWindow",
                                        p: "push",
                                        b: "banner",
                                        ab: "abTest"
                                    }[Q("mt", t)] || "";
                                    gioGlobal.__growing__.marketingPreview = {
                                        messageId: n,
                                        msgType: i
                                    };
                                }
                            }
                        }
                    }
                }, {
                    key: "storeFilters",
                    value: function(e, t, n) {
                        var r = t(), o = this.get(r, this.eventTagDuration) || [], a = n.call(this, e), s = [].concat(i(o), i(a));
                        this.set(r, s);
                    }
                }, {
                    key: "formatUserFilterVars",
                    value: function(e) {
                        var t = e.var;
                        return t ? Object.keys(t).map(function(e) {
                            return {
                                key: e,
                                value: t[e]
                            };
                        }) : [];
                    }
                }, {
                    key: "formatEventFilterVars",
                    value: function(e) {
                        var t = e.var;
                        return [ {
                            key: e.n,
                            value: "",
                            event_variable: t ? Object.keys(t).map(function(e) {
                                return {
                                    key: e,
                                    value: t[e]
                                };
                            }) : []
                        } ];
                    }
                }, {
                    key: "generateEventKey",
                    value: function(e) {
                        return "".concat(e, "#").concat(this.get("cs1") || "");
                    }
                }, {
                    key: "_get",
                    value: function(e) {
                        return this.growingio.info.getStorageSync("".concat(this.namespace, "#").concat(e));
                    }
                }, {
                    key: "getUserAttrs",
                    value: function() {
                        var e = this.generateEventKey("userAttrs");
                        return this.get(e) || [];
                    }
                }, {
                    key: "getTriggerAttrs",
                    value: function() {
                        var e = this.generateEventKey("triggerAttrs");
                        return this.get(e) || [];
                    }
                }, {
                    key: "set",
                    value: function(e, t) {
                        var n = this._get(e), i = new Date();
                        i.setHours(0), i.setMinutes(0), i.setSeconds(0);
                        var r = {
                            startAt: i.getTime(),
                            value: t
                        };
                        n && F(r.value, JSON.parse(n).value) || this.growingio.info.setStorageSync("".concat(this.namespace, "#").concat(e), r);
                    }
                }, {
                    key: "get",
                    value: function(e) {
                        var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : this.userTagDuration, n = this._get(e);
                        if (n) {
                            var i = JSON.parse(n);
                            return Date.now() > i.startAt + t ? void 0 : i.value;
                        }
                    }
                } ]), e;
            }();
            try {
                var J = "swan";
                f(J), "frame" !== J && (gioGlobal.gio__platform = J);
            } catch (g) {}
            var z = new N(), Z = function() {
                var e = arguments[0];
                if (e) {
                    var t = 2 > arguments.length ? [] : [].slice.call(arguments, 1);
                    if ("init" === e) {
                        if (gioGlobal.vdsConfig) return void console.warn("SDK已经初始化成功，请检查是否加载过其他平台sdk");
                        if (1 > t.length) return void console.log('初始化 GrowingIO SDK 失败。请使用 gio("init", "你的GrowingIO项目ID", "你的应用APP_ID", options);');
                        z.init(t[0], t[1], t[2]);
                    } else {
                        if ("setConfig" !== e) return z.proxy(e, t);
                        if (!t[0]) return void console.log("初始化 GrowingIO SDK 失败。请检查你的config文件是否引入正确");
                        if (!t[0].projectId) return void console.log("初始化 GrowingIO SDK 失败。请检查你的 GrowingIO项目ID, 你的应用APP_ID 是否填写正确");
                        z.setConfig(t[0]);
                    }
                }
            };
            console.log("init growingio...");
            var X = m.GrowingPage, Y = m.GrowingApp, ee = m.GrowingComponent, te = m.GrowingBehavior, ne = j, ie = new W(z);
            gioGlobal.__growing__ = {
                gioEmitter: ne,
                gio: Z,
                growingio: z,
                userStorage: ie,
                marketingPreview: void 0
            }, gioGlobal.gio = Z, t.GioApp = Y, t.GioBehavior = te, t.GioComponent = ee, t.GioPage = X, 
            t.default = Z, t.gioEmitter = ne, t.growingio = z;
        }).call(this, n(45));
    },
    308: function(e, t, n) {
        !function(t, n) {
            e.exports = n();
        }("undefined" != typeof self && self, function() {
            return function(e) {
                function t(i) {
                    if (n[i]) return n[i].exports;
                    var r = n[i] = {
                        i: i,
                        l: !1,
                        exports: {}
                    };
                    return e[i].call(r.exports, r, r.exports, t), r.l = !0, r.exports;
                }
                var n = {};
                return t.m = e, t.c = n, t.d = function(e, n, i) {
                    t.o(e, n) || Object.defineProperty(e, n, {
                        configurable: !1,
                        enumerable: !0,
                        get: i
                    });
                }, t.n = function(e) {
                    var n = e && e.__esModule ? function() {
                        return e.default;
                    } : function() {
                        return e;
                    };
                    return t.d(n, "a", n), n;
                }, t.o = function(e, t) {
                    return Object.prototype.hasOwnProperty.call(e, t);
                }, t.p = "", t(t.s = 3);
            }([ function(e, t, n) {
                "use strict";
                function i(e, t) {
                    if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
                }
                Object.defineProperty(t, "__esModule", {
                    value: !0
                });
                var r = function() {
                    function e(e, t) {
                        for (var n = 0; n < t.length; n++) {
                            var i = t[n];
                            i.enumerable = i.enumerable || !1, i.configurable = !0, "value" in i && (i.writable = !0), 
                            Object.defineProperty(e, i.key, i);
                        }
                    }
                    return function(t, n, i) {
                        return n && e(t.prototype, n), i && e(t, i), t;
                    };
                }(), o = n(2), a = function(e) {
                    return e && e.__esModule ? e : {
                        default: e
                    };
                }(o), s = function() {
                    function e() {
                        i(this, e), this.actions = [], this.logger = a.default.getLogger();
                    }
                    return r(e, [ {
                        key: "__addSectionToSwan",
                        value: function() {}
                    }, {
                        key: "__addAction",
                        value: function(e) {
                            var t = this;
                            "[object Array]" === Object.prototype.toString.call(e) && e.forEach(function(e) {
                                return t.__addAction(e);
                            }), this.actions.push(e);
                        }
                    }, {
                        key: "callback",
                        value: function(e) {
                            var t = this, n = [];
                            return this.after(e.replace(/^on/g, ""), function(e) {
                                n.forEach(function(t) {
                                    return t(e);
                                });
                            }), {
                                convert: function(e) {
                                    n.push(function() {
                                        return t.logger.send(e);
                                    });
                                }
                            };
                        }
                    }, {
                        key: "after",
                        value: function(e, t) {
                            return this.__addSectionToSwan(this.actions, e, t), this;
                        }
                    } ]), e;
                }();
                t.default = s;
            }, function(e, t, n) {
                "use strict";
                function i(e, t) {
                    if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
                }
                function r(e, t) {
                    if (!e) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
                    return !t || "object" != typeof t && "function" != typeof t ? e : t;
                }
                function o(e, t) {
                    if ("function" != typeof t && null !== t) throw new TypeError("Super expression must either be null or a function, not " + typeof t);
                    e.prototype = Object.create(t && t.prototype, {
                        constructor: {
                            value: e,
                            enumerable: !1,
                            writable: !0,
                            configurable: !0
                        }
                    }), t && (Object.setPrototypeOf ? Object.setPrototypeOf(e, t) : e.__proto__ = t);
                }
                Object.defineProperty(t, "__esModule", {
                    value: !0
                });
                var a = function() {
                    function e(e, t) {
                        for (var n = 0; n < t.length; n++) {
                            var i = t[n];
                            i.enumerable = i.enumerable || !1, i.configurable = !0, "value" in i && (i.writable = !0), 
                            Object.defineProperty(e, i.key, i);
                        }
                    }
                    return function(t, n, i) {
                        return n && e(t.prototype, n), i && e(t, i), t;
                    };
                }(), s = n(0), u = function(e) {
                    return e && e.__esModule ? e : {
                        default: e
                    };
                }(s), c = function(e) {
                    function t(e, n) {
                        i(this, t);
                        var o = r(this, (t.__proto__ || Object.getPrototypeOf(t)).call(this));
                        return o.pagePath = e, o.rule = n, o;
                    }
                    return o(t, e), a(t, [ {
                        key: "event",
                        value: function(e) {
                            return this.__addAction(e), this;
                        }
                    }, {
                        key: "__addSectionToSwan",
                        value: function(e, t, n) {
                            var i = this;
                            Page.after && Page.after({
                                events: e.reduce(function(e, t) {
                                    return e[i.rule + ":" + t] = n, e;
                                }, {})
                            });
                        }
                    } ]), t;
                }(u.default);
                t.default = c;
            }, function(e, t, n) {
                "use strict";
                function i(e, t) {
                    if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
                }
                Object.defineProperty(t, "__esModule", {
                    value: !0
                });
                var r = Object.assign || function(e) {
                    for (var t = 1; t < arguments.length; t++) {
                        var n = arguments[t];
                        for (var i in n) Object.prototype.hasOwnProperty.call(n, i) && (e[i] = n[i]);
                    }
                    return e;
                }, o = function() {
                    function e(e, t) {
                        for (var n = 0; n < t.length; n++) {
                            var i = t[n];
                            i.enumerable = i.enumerable || !1, i.configurable = !0, "value" in i && (i.writable = !0), 
                            Object.defineProperty(e, i.key, i);
                        }
                    }
                    return function(t, n, i) {
                        return n && e(t.prototype, n), i && e(t, i), t;
                    };
                }(), a = function() {
                    function e() {
                        i(this, e), this.defaultParams = {
                            bdVid: ""
                        };
                    }
                    return o(e, [ {
                        key: "setDefaultParams",
                        value: function(e) {
                            r(this.defaultParams, e);
                        }
                    }, {
                        key: "send",
                        value: function(e, t) {
                            var n = e.convertType;
                            swan.sendFrameWorkLog(r({}, this.defaultParams, {
                                convertType: n,
                                bizId: "10001",
                                eventName: "ocpc@event",
                                groupId: "10001"
                            }), t);
                        }
                    } ]), e;
                }();
                a.getLogger = function() {
                    return new a();
                }, t.default = a;
            }, function(e, t, n) {
                "use strict";
                function i(e) {
                    return e && e.__esModule ? e : {
                        default: e
                    };
                }
                function r(e, t) {
                    if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
                }
                Object.defineProperty(t, "__esModule", {
                    value: !0
                });
                var o = Object.assign || function(e) {
                    for (var t = 1; t < arguments.length; t++) {
                        var n = arguments[t];
                        for (var i in n) Object.prototype.hasOwnProperty.call(n, i) && (e[i] = n[i]);
                    }
                    return e;
                }, a = function() {
                    function e(e, t) {
                        for (var n = 0; n < t.length; n++) {
                            var i = t[n];
                            i.enumerable = i.enumerable || !1, i.configurable = !0, "value" in i && (i.writable = !0), 
                            Object.defineProperty(e, i.key, i);
                        }
                    }
                    return function(t, n, i) {
                        return n && e(t.prototype, n), i && e(t, i), t;
                    };
                }(), s = n(2), u = i(s), c = n(4), l = i(c), g = n(5), p = i(g), f = n(6), h = i(f), d = n(1), v = (i(d), 
                function() {
                    function e() {
                        r(this, e), this.logger = u.default.getLogger();
                    }
                    return a(e, [ {
                        key: "init",
                        value: function() {
                            var e = this, t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : {}, n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : [];
                            this.app().method("onShow").after("success", function(i) {
                                var r = i.args.query || {};
                                try {
                                    e.setDefaultParams({
                                        path: i.args.path,
                                        scene: i.args.scene,
                                        query: r,
                                        entryType: i.args.entryType,
                                        shareTicket: i.args.shareTicket,
                                        appLaunchScheme: i.args.appLaunchScheme,
                                        appURL: i.args.appURL,
                                        clkid: i.args.clkid,
                                        extraData: i.args.extraData,
                                        referrerInfo: i.args.referrerInfo
                                    });
                                } catch (e) {}
                                e.setDefaultParams(o({
                                    bdVid: r.bd_vid
                                }, t)), e.log({
                                    convertType: 255
                                }, n);
                            }), this.page().component("[data-agl-cvt]").event([ "tap", "submit" ]).after("success", function(t) {
                                var i = t.args.currentTarget.dataset.aglCvt;
                                e.log({
                                    convertType: i
                                }, n);
                            });
                            var i = {
                                "swan.makePhoneCall": 30,
                                "swan.navigateTo": 20
                            };
                            for (var r in i) !function(t) {
                                e.api(t).after("onsuccess", function(r) {
                                    e.log({
                                        convertType: i[t]
                                    }, n);
                                });
                            }(r);
                        }
                    }, {
                        key: "setDefaultParams",
                        value: function(e) {
                            return this.logger.setDefaultParams(e), this;
                        }
                    }, {
                        key: "page",
                        value: function(e) {
                            return new h.default(e);
                        }
                    }, {
                        key: "component",
                        value: function(e) {
                            return new h.default().component(e);
                        }
                    }, {
                        key: "log",
                        value: function(e) {
                            var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : [];
                            return this.logger.send(e, t), this;
                        }
                    }, {
                        key: "api",
                        value: function(e) {
                            return new l.default(e);
                        }
                    }, {
                        key: "app",
                        value: function() {
                            return new p.default();
                        }
                    } ]), e;
                }()), y = new v();
                e.exports = y, t.default = y;
            }, function(e, t, n) {
                "use strict";
                function i(e, t) {
                    if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
                }
                function r(e, t) {
                    if (!e) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
                    return !t || "object" != typeof t && "function" != typeof t ? e : t;
                }
                function o(e, t) {
                    if ("function" != typeof t && null !== t) throw new TypeError("Super expression must either be null or a function, not " + typeof t);
                    e.prototype = Object.create(t && t.prototype, {
                        constructor: {
                            value: e,
                            enumerable: !1,
                            writable: !0,
                            configurable: !0
                        }
                    }), t && (Object.setPrototypeOf ? Object.setPrototypeOf(e, t) : e.__proto__ = t);
                }
                Object.defineProperty(t, "__esModule", {
                    value: !0
                });
                var a = function() {
                    function e(e, t) {
                        for (var n = 0; n < t.length; n++) {
                            var i = t[n];
                            i.enumerable = i.enumerable || !1, i.configurable = !0, "value" in i && (i.writable = !0), 
                            Object.defineProperty(e, i.key, i);
                        }
                    }
                    return function(t, n, i) {
                        return n && e(t.prototype, n), i && e(t, i), t;
                    };
                }(), s = n(0), u = function(e) {
                    return e && e.__esModule ? e : {
                        default: e
                    };
                }(s), c = function(e) {
                    function t(e) {
                        i(this, t);
                        var n = r(this, (t.__proto__ || Object.getPrototypeOf(t)).call(this));
                        return n.__addAction(e), n;
                    }
                    return o(t, e), a(t, [ {
                        key: "__addSectionToSwan",
                        value: function(e, t, n) {
                            var i = e.reduce(function(e, i) {
                                return e[i.replace(/^swan\./, "")] = [].concat(t).reduce(function(e, t) {
                                    return e[t] = n, e;
                                }, {}), e;
                            }, {});
                            swan.after && swan.after(i);
                        }
                    } ]), t;
                }(u.default);
                t.default = c;
            }, function(e, t, n) {
                "use strict";
                function i(e) {
                    return e && e.__esModule ? e : {
                        default: e
                    };
                }
                function r(e, t) {
                    if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
                }
                function o(e, t) {
                    if (!e) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
                    return !t || "object" != typeof t && "function" != typeof t ? e : t;
                }
                function a(e, t) {
                    if ("function" != typeof t && null !== t) throw new TypeError("Super expression must either be null or a function, not " + typeof t);
                    e.prototype = Object.create(t && t.prototype, {
                        constructor: {
                            value: e,
                            enumerable: !1,
                            writable: !0,
                            configurable: !0
                        }
                    }), t && (Object.setPrototypeOf ? Object.setPrototypeOf(e, t) : e.__proto__ = t);
                }
                Object.defineProperty(t, "__esModule", {
                    value: !0
                });
                var s = function() {
                    function e(e, t) {
                        for (var n = 0; n < t.length; n++) {
                            var i = t[n];
                            i.enumerable = i.enumerable || !1, i.configurable = !0, "value" in i && (i.writable = !0), 
                            Object.defineProperty(e, i.key, i);
                        }
                    }
                    return function(t, n, i) {
                        return n && e(t.prototype, n), i && e(t, i), t;
                    };
                }(), u = n(0), c = i(u), l = n(1), g = (i(l), function(e) {
                    function t() {
                        return r(this, t), o(this, (t.__proto__ || Object.getPrototypeOf(t)).call(this));
                    }
                    return a(t, e), s(t, [ {
                        key: "method",
                        value: function(e) {
                            return this.__addAction(e), this;
                        }
                    }, {
                        key: "__addSectionToSwan",
                        value: function(e, t, n) {
                            var i = {
                                methods: e.reduce(function(e, t) {
                                    return e[t] = n, e;
                                }, {})
                            };
                            App.after && App.after(i);
                        }
                    } ]), t;
                }(c.default));
                t.default = g;
            }, function(e, t, n) {
                "use strict";
                function i(e) {
                    return e && e.__esModule ? e : {
                        default: e
                    };
                }
                function r(e, t) {
                    if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
                }
                function o(e, t) {
                    if (!e) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
                    return !t || "object" != typeof t && "function" != typeof t ? e : t;
                }
                function a(e, t) {
                    if ("function" != typeof t && null !== t) throw new TypeError("Super expression must either be null or a function, not " + typeof t);
                    e.prototype = Object.create(t && t.prototype, {
                        constructor: {
                            value: e,
                            enumerable: !1,
                            writable: !0,
                            configurable: !0
                        }
                    }), t && (Object.setPrototypeOf ? Object.setPrototypeOf(e, t) : e.__proto__ = t);
                }
                Object.defineProperty(t, "__esModule", {
                    value: !0
                });
                var s = function() {
                    function e(e, t) {
                        for (var n = 0; n < t.length; n++) {
                            var i = t[n];
                            i.enumerable = i.enumerable || !1, i.configurable = !0, "value" in i && (i.writable = !0), 
                            Object.defineProperty(e, i.key, i);
                        }
                    }
                    return function(t, n, i) {
                        return n && e(t.prototype, n), i && e(t, i), t;
                    };
                }(), u = n(0), c = i(u), l = n(1), g = i(l), p = function(e) {
                    function t(e) {
                        r(this, t);
                        var n = o(this, (t.__proto__ || Object.getPrototypeOf(t)).call(this));
                        return n.path = e, n;
                    }
                    return a(t, e), s(t, [ {
                        key: "method",
                        value: function(e) {
                            return this.__addAction(e), this;
                        }
                    }, {
                        key: "component",
                        value: function(e) {
                            return new g.default(this.path, e);
                        }
                    }, {
                        key: "__addSectionToSwan",
                        value: function(e, t, n) {
                            var i = {
                                methods: e.reduce(function(e, t) {
                                    return e[t] = n, e;
                                }, {})
                            };
                            this.path && (i.url = this.path), Page.after && Page.after(i);
                        }
                    } ]), t;
                }(c.default);
                t.default = p;
            } ]);
        });
    },
    503: function(e, t, n) {
        "use strict";
        n.r(t);
        n(271);
        var i, r = n(8), o = n(2), a = n.n(o), s = n(16), u = n.n(s), c = n(20), l = n(10), g = n(11), p = n(12), f = n(13), h = n(3), d = n(14), v = n(106), y = n.n(v), m = n(57), b = (n(292), 
        n(80)), w = function(e) {
            return {
                type: b["a"],
                platform: e
            };
        }, _ = n(82), k = function(e) {
            return {
                type: _["a"],
                data: e
            };
        }, x = n(7), P = n(293).default, C = n(305).default, S = n(306).default, E = {
            weappGio: P,
            ttGio: C,
            swanGio: S
        }, O = n(34), I = n(0), T = !1;
        i = E.weappGio, i("init", "8be7ac6fe455b8e6", "wx1f7b9a5ba245f136", {
            version: "2.9.5",
            taro: a.a
        }), Object(O["b"])("gio", i);
        var A = function(e) {
            Object(p["a"])(r, e);
            var t = Object(f["a"])(r);
            function r() {
                return Object(l["a"])(this, r), t.apply(this, arguments);
            }
            return Object(g["a"])(r, [ {
                key: "componentWillMount",
                value: function() {
                    console.log("======环境", "weapp", "production");
                }
            }, {
                key: "componentDidMount",
                value: function() {
                    var e = Object(c["a"])(u.a.mark(function e() {
                        var t;
                        return u.a.wrap(function(e) {
                            while (1) switch (e.prev = e.next) {
                              case 0:
                                n(308), setTimeout(Object(c["a"])(u.a.mark(function e() {
                                    var t;
                                    return u.a.wrap(function(e) {
                                        while (1) switch (e.prev = e.next) {
                                          case 0:
                                            return e.next = 2, x["a"].getDynamicShow();

                                          case 2:
                                            t = e.sent, t.data.success && m["a"].dispatch(k({
                                                weappShow: t.data.weappShow,
                                                isShow: t.data.isShow,
                                                swanShow: t.data.swanShow
                                            }));

                                          case 4:
                                          case "end":
                                            return e.stop();
                                        }
                                    }, e);
                                })), 3e3), a.a.getSystemInfo().then(function(e) {
                                    var t = a.a.getMenuButtonBoundingClientRect(), n = {
                                        isIphonex: !1,
                                        isIos: "ios" == e.platform,
                                        navbarHeight: e.statusBarHeight + t.height + 12
                                    };
                                    n.isIphonex = e.safeArea.top > 20, m["a"].dispatch(w(n));
                                }), t = {
                                    environment: "production",
                                    sampleRate: 1,
                                    debug: !0
                                }, y.a.config("https://8e5cea2b7c224ce5b25b8b5f0caa692a@sentry.kaoputou.com/51", t).install(), 
                                a.a.Logger = y.a;

                              case 4:
                              case "end":
                                return e.stop();
                            }
                        }, e);
                    }));
                    function t() {
                        return e.apply(this, arguments);
                    }
                    return t;
                }()
            }, {
                key: "componentDidShow",
                value: function(e) {
                    if (!T) {
                        console.log("接收参数", e);
                        var t = e.scene, n = (e.path, e.query, this.getInviterSlug());
                        n && x["a"].setInviter(n), 1010 != t || a.a.getStorageSync("showCollectHint") || a.a.setStorageSync("showCollectHint", !0), 
                        1129 != t && "web" != t || x["a"].setIdentity(), 1065 == t && i("track", "clickUrlschemeEntrance"), 
                        T = !0;
                    }
                }
            }, {
                key: "componentDidHide",
                value: function() {}
            }, {
                key: "componentDidCatchError",
                value: function() {}
            }, {
                key: "getInviterSlug",
                value: function() {
                    var e = a.a.getLaunchOptionsSync(), t = e.query;
                    if (t.scene) {
                        var n = decodeURIComponent(t.scene);
                        if (n.indexOf("inviter") > -1) {
                            var i = n.replace("inviter=", "");
                            if (i) return i;
                        }
                    }
                    return t.inviter ? t.inviter : "";
                }
            }, {
                key: "render",
                value: function() {
                    return Object(I["jsx"])(d["a"], {
                        store: m["a"],
                        children: this.props.children
                    });
                }
            } ]), r;
        }(h["Component"]), j = A, G = n(74), V = {
            pages: [ "pages/index/index", "pages/dashboard/index", "pages/login/index", "pages/category-list/index", "pages/information/index", "pages/zhaimen/index", "pages/vip/index" ],
            subPackages: [ {
                root: "pages-extend",
                pages: [ "about/index", "activity/cate-ranking/index", "activity/cate-ranking/detail", "article/index", "article/content", "association/index", "attention/index", "brand/index", "brand/suppliers", "brand-score-ranking/index", "brand-shop-detail/index", "brand-shop-detail/city", "brand-shop-open/index", "brand-shop-open/all", "brands/index", "category/index", "city-distribution/index", "company/index", "compare/index", "compare/brand", "compare/search", "explain/index", "feedback/index", "finance-event/index", "food/index", "food/detail", "food/price", "food/market", "food/marketDetail", "hot-product/index", "invite/index", "invite/poster", "invite/record", "invite/withdraw-record", "landing/index", "meeting-apply/index", "meeting-apply/detail", "meeting-apply/apply", "meeting-apply/edit-demand", "meeting-apply/apply-create-brand", "meeting-apply/vip-benefits", "meeting-apply/public-pay-information", "meeting-apply/edit-company", "message-center/index", "my-brand/index", "my-brand/edit", "poster/index", "poster/save", "premium-brands/index", "premium-brands/detail", "public-page/search", "questionnaire/index", "region/main", "region/city-rank", "region/data-spec", "report/index", "shopping/index", "shopping/detail", "shopping/merchants", "supplier/all", "supplier/customer", "supplier/detail", "supplier/index", "trademark-list/index", "user/index", "waimai/detail", "waimai/ranking", "waimai/shopDetail" ]
            }, {
                root: "pages-extend2",
                pages: [ "home/index", "member-center/index", "member-center/member-info/index", "member-center/member-invite/index", "member-center/member-coupon/index", "member-center/member-order/index", "member-center/member-course/index", "member-center/publish-comment/index", "member-center/member-key/index", "member-center/member-team/index", "member-center/member-team-list/index", "course/course-item/index", "course/course-members/index", "course/course-review/index", "course/course-review-list/index", "course/course-comment-list/index", "course/course-moment-list/index", "apply/combo-detail/index", "apply/apply-deposit-step/index", "apply/apply-complete-step/index", "apply/apply-wait-audit-step/index", "apply/apply-final-pay-step/index", "apply/apply-public-transfer/index", "apply/apply-second-complete/index", "friend/member-list/index", "friend/search-friend/index", "friend/member-profile/index", "signing/join-team/index", "signing/join-success/index", "signing/join-exhibition/index", "signing/join-exhibition-result/index", "invoice/invoice-list/index", "invoice/invoice-detail/index", "invoice/invoice-form/index" ]
            } ],
            preloadRule: {
                "pages/index/index": {
                    network: "all",
                    packages: [ "pages-extend" ]
                }
            },
            tabBar: {
                color: "#989BA8",
                selectedColor: "#7B7E8E",
                backgroundColor: "#FBFBFB",
                borderStyle: "white",
                list: [ {
                    pagePath: "pages/index/index",
                    text: "首页",
                    iconPath: "./asset/images/home-default.png",
                    selectedIconPath: "./asset/images/home-active.png"
                }, {
                    pagePath: "pages/information/index",
                    text: "资讯",
                    iconPath: "./asset/images/icon-article-default.png",
                    selectedIconPath: "./asset/images/icon-article-active.png"
                }, {
                    pagePath: "pages/category-list/index",
                    text: "品类",
                    iconPath: "./asset/images/icon-category-default.png",
                    selectedIconPath: "./asset/images/icon-category-active.png"
                }, {
                    pagePath: "pages/dashboard/index",
                    text: "我",
                    iconPath: "./asset/images/user-default.png",
                    selectedIconPath: "./asset/images/user-active.png"
                } ]
            },
            window: {
                backgroundTextStyle: "light",
                navigationBarBackgroundColor: "#fff",
                navigationBarTextStyle: "black"
            },
            sitemapLocation: "sitemap.json"
        };
        r["window"].__taroAppConfig = V;
        App(Object(r["createReactApp"])(j, h, G["a"], V));
        Object(o["initPxTransform"])({
            designWidth: 750,
            deviceRatio: {
                640: 1.17,
                750: 1,
                828: .905
            }
        });
    },
    99: function(e, t, n) {
        var i = n(294), r = n(295), o = n(100), a = n(296);
        function s(e) {
            return i(e) || r(e) || o(e) || a();
        }
        e.exports = s, e.exports["default"] = e.exports, e.exports.__esModule = !0;
    }
}, [ [ 503, 0, 1, 2, 3 ] ] ]);