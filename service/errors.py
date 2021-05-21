import cerver
from cerver.headers import *
from cerver.http import *

BTC_ERROR_NONE = 0
BTC_ERROR_BAD_REQUEST = 1
BTC_ERROR_MISSING_VALUES = 2
BTC_ERROR_BAD_USER = 3
BTC_ERROR_EXISTING_USER = 4
BTC_ERROR_SERVER_ERROR = 5
BTC_ERROR_NOT_FOUND = 6

bad_request_error = None
bad_user_error = None
missing_values = None
existing_user_error = None
server_error = None
not_found_error = None

def btc_errors_init ():
    global bad_request_error
    global bad_user_error
    global missing_values
    global existing_user_error
    global server_error
    global not_found_error

    bad_request_error = http_response_json_key_value (
        HTTP_STATUS_BAD_REQUEST,
            "error".encode ("utf-8"),
            "Bad request!".encode ("utf-8")
    )

    bad_user_error = http_response_json_key_value (
        HTTP_STATUS_BAD_REQUEST,
            "error".encode ("utf-8"),
            "Bad user!".encode ("utf-8")
    )

    missing_values = http_response_json_key_value (
        HTTP_STATUS_BAD_REQUEST,
            "error".encode ("utf-8"),
            "Missing values!".encode ("utf-8")
    )

    existing_user_error = http_response_json_key_value (
        HTTP_STATUS_BAD_REQUEST,
            "error".encode ("utf-8"),
            "User already exists!".encode ("utf-8")
    )

    server_error = http_response_json_key_value (
        HTTP_STATUS_INTERNAL_SERVER_ERROR,
            "error".encode ("utf-8"),
            "Server error!".encode ("utf-8")
    )

    not_found_error = http_response_json_key_value (
        HTTP_STATUS_NOT_FOUND,
        "error".encode("utf-8"),
        "Element not found!".encode("utf-8")
    )

def btc_error_send_response (btc_error, http_receive):
    if (btc_error == BTC_ERROR_NONE):
        pass

    if (btc_error == BTC_ERROR_BAD_REQUEST):
        http_response_send (bad_request_error, http_receive)

    if (btc_error == BTC_ERROR_MISSING_VALUES):
        http_response_send (missing_values, http_receive)

    if (btc_error == BTC_ERROR_BAD_USER):
        http_response_send (bad_user_error, http_receive)

    if (btc_error == BTC_ERROR_EXISTING_USER):
        http_response_send (existing_user_error, http_receive)

    if (btc_error == BTC_ERROR_SERVER_ERROR):
        http_response_send (server_error, http_receive)

    if (btc_error == BTC_ERROR_NOT_FOUND):
        http_response_send (not_found_error, http_receive)

def btc_errors_end ():
    global bad_request_error
    global bad_user_error
    global missing_values
    global existing_user_error
    global server_error
    global not_found_error

    http_response_delete (bad_request_error)
    http_response_delete (bad_user_error)
    http_response_delete (missing_values)
    http_response_delete (existing_user_error)
    http_response_delete (server_error)
    http_response_delete (not_found_error)