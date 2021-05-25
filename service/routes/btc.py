import traceback
import ctypes
import json
import random
import re
from cerver import *
from cerver.http import *
from cerver.headers import *
from service.errors import *
from service import runtime, btc
from service.controllers.btc import *
from service.utils.body_validator import *

#GET /api/btc
@ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
def top_level_handler (http_receive, request):
    try:
        http_send_response(http_receive,HTTP_STATUS_OK, {"msg": "BTC Works!"})
    except:
        btc_error_send_response(BTC_ERROR_SERVER_ERROR, http_receive)

#GET /api/btc/prediction
@ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
def prediction_handler (http_receive, request):
    try:
        prediction = predict_next_day()
        http_send_response(http_receive, HTTP_STATUS_OK, prediction)
    except:
        traceback.print_exc()
        btc_error_send_response(BTC_ERROR_SERVER_ERROR, http_receive)