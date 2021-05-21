import os

import cerver

from service.runtime import * 
from service.errors import btc_errors_init, btc_errors_end

RUNTIME = runtime_from_string (os.environ.get("RUNTIME"))

PORT = int (os.environ.get("PORT"))

CERVER_RECEIVE_BUFFER_SIZE = int (os.environ.get("CERVER_RECEIVE_BUFFER_SIZE"))
CERVER_TH_THREADS = int (os.environ.get("CERVER_TH_THREADS"))
CERVER_CONNECTION_QUEUE = int (os.environ.get("CERVER_CONNECTION_QUEUE"))

PRIV_KEY = os.environ.get("PRIV_KEY")
PUB_KEY = os.environ.get("PUB_KEY")

def btc_config ():
   print ("RUNTIME: ", runtime_to_string (RUNTIME))

   print ("PORT: ", PORT)

   print ("CERVER_RECEIVE_BUFFER_SIZE: ", CERVER_RECEIVE_BUFFER_SIZE)
   print ("CERVER_TH_THREADS: ", CERVER_TH_THREADS)
   print ("CERVER_CONNECTION_QUEUE: ", CERVER_CONNECTION_QUEUE)


   print ("PRIV_KEY: ", PRIV_KEY)
   print ("PUB_KEY: ", PUB_KEY)

   btc_errors_init ()

def btc_end ():
   btc_errors_end ()