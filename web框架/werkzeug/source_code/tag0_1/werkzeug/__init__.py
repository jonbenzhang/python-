# -*- coding: utf-8 -*-
"""
    werkzeug
    ~~~~~~~~

    Werkzeug is the Swiss Army® knife of Python web development.

    It provides useful classes and functions for any WSGI application take
    make life much easier.  All of the provided classes are independed from
    each other so you can mix it with any other library.


    Builtin blades^Wfeatures
    ~~~~~~~~~~~~~~~~~~~~~~~~

    **Request / Response objects**

        These objects wrap the WSGI `environ` and `start_response` objects.
        They handle unicode conversion, form data parsing, cookie management
        and much more in a django like manner.

        Just subclass them and hook your own features in.

    **Reporter stream**

        A class that can wrap a `wsgi.input` stream so that it reports it's
        progress into the active session, a file on the filesystem etc.  This
        is very useful if you want to give your users a visual feedback for
        file uploads using AJAX.

    **Application debugger middleware**

        If you want to debug your WSGI application you can hook in the
        `DebuggedApplication` middleware that allows you to inspect the frames
        of tracebacks either by looking at the current locals and sourcecode
        or starting an interactive shell in one of the frames.

    **Shared data middleware**

        In production environments static data is usually served by a
        lightweight webserver like lighttpd or nginx.  But during development
        it makes no sense to install another service on the computer so the
        `SharedDataMiddleware` can serve static files in your WSGI
        application.

    **Unicode aware data processing**

        The utils package contains functions that work like their counterparts
        in the builtin `urllib` or `cgi` module but are unicode aware.  Per
        default they expect utf-8 strings like the request/response objects
        but you can pass an encoding to the too.

    **Mini template engine**

        For small projects you often face the problem that a real template
        engine means another requirement but the builtin string formattings
        (or string template) operations are not enough for the application.
        Werkzeug provides a minimal template engine that looks and behaves
        like the e-ruby template engine.

    **Context Locals**

        The `Local` object works pretty much like a normal thread local but
        it has support for py.magic greenlets too.  Additionally there is a
        `LocalManager` that allows you to clean up all the context locals you
        have instanciated.

    **Test utilities**

        Werkzeug provides a `Client` class that can be used to test
        applications.  Just instanciate it with the app and fire virtual
        requests.


    :copyright: 2007 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from types import ModuleType
import sys


all_by_module = {
    'werkzeug':             ['exceptions', 'routing', 'script'],
    'werkzeug.debug':       ['DebuggedApplication'],
    'werkzeug.local':       ['Local', 'LocalManager', 'LocalProxy'],
    'werkzeug.templates':   ['Template'],
    'werkzeug.serving':     ['run_simple'],
    'werkzeug.test':        ['Client'],
    'werkzeug.testapp':     ['test_app'],
    'werkzeug.utils':       ['escape', 'create_environ', 'url_quote',
                             'environ_property', 'cookie_date', 'http_date',
                             'url_encode', 'url_quote_plus', 'Headers',
                             'EnvironHeaders', 'CombinedMultiDict',
                             'run_wsgi_app', 'get_host',
                             'SharedDataMiddleware', 'ClosingIterator',
                             'FileStorage', 'url_unquote_plus',
                             'url_unquote', 'get_current_url', 'redirect',
                             'lazy_property', 'MultiDict', 'url_decode'],
    'werkzeug.http':        ['Accept', 'CacheControl', 'parse_accept_header',
                             'parse_cache_control_header',
                             'HTTP_STATUS_CODES'],
    'werkzeug.wrappers':    ['BaseResponse', 'BaseRequest',
                             'BaseReporterStream']
}


from .debug import DebuggedApplication
from .local import  Local,LocalManager,LocalProxy
from .templates import  Template
from .serving import  run_simple
from .test import  Client
from .testapp import  test_app
from .utils import escape,SharedDataMiddleware,ClosingIterator,CombinedMultiDict,MultiDict,EnvironHeaders,create_environ,
from .wrappers import BaseReporterStream ,BaseRequest as Request,BaseResponse as Response
