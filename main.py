import signal 
import sys
from service import version as v
from service import btc, conf
from cerver import *

if __name__ == "__main__":
    signal.signal(signal.SIGPIPE, signal.SIG_IGN)

    cerver_initialize(conf.end)
    v.btc_version_print_full()
    btc.btc_config ()

    conf.start()