import os, signal, sys
import ctypes
from service.btc import *
import service.routes.btc as rbtc

import cerver
from cerver.http import *
from cerver.headers import *

api_cerver = None

def end (signum, frame):
    http_cerver_all_stats_print (http_cerver_get (api_cerver))
    cerver.cerver_teardown (api_cerver)
    cerver.cerver_end ()
    sys.exit ("Done!")

def btc_set_routes (http_cerver):
    #route_configuration
    #GET /api/btc
    main_route = http_create_route(REQUEST_METHOD_GET, "api/btc", rbtc.top_level_handler, http_cerver = http_cerver)
    pass

def start ():
    global api_cerver
    api_cerver = cerver_main_http_configuration (PORT, CERVER_CONNECTION_QUEUE)

    http_cerver = http_cerver_get (api_cerver)

    cerver_auth_http_configuration(http_cerver)

    btc_set_routes (http_cerver)

    cerver.cerver_start(api_cerver)