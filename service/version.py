import cerver.utils

BTC_VERSION = "0.1"
BTC_VERSION_NAME = "Version 0.1"
BTC_VERSION_DATE = "18/05/2021"
BTC_VERSION_TIME = "19:00 CST"
BTC_VERSION_AUTHOR = "Juan Carlos Lara"

def btc_version_print_full ():
   cerver.utils.cerver_log_both (
   cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
   "Btc PyCerver Version: %s".encode ('utf-8'), BTC_VERSION_NAME.encode ('utf-8')
   )

   cerver.utils.cerver_log_both (
   cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
   "Release Date & time: %s - %s".encode ('utf-8'),
   BTC_VERSION_DATE.encode ('utf-8'), BTC_VERSION_TIME.encode ('utf-8')
   )

   cerver.utils.cerver_log_both (
   cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
   "Author: %s\n".encode ('utf-8'),
   BTC_VERSION_AUTHOR.encode ('utf-8')
   )

def api_version_print_version_id ():
   cerver.utils.cerver_log_both (
   cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
   "\nBtc PyCerver Version ID: %s\n".encode ('utf-8'),
   BTC_VERSION.encode ('utf-8')
   )

def api_version_print_version_name ():
   cerver.utils.cerver_log_both (
   cerver.utils.LOG_TYPE_NONE, cerver.utils.LOG_TYPE_NONE,
   "\nBtc PyCerver Version: %s\n".encode ('utf-8'),
   BTC_VERSION_NAME.encode ('utf-8')
   )