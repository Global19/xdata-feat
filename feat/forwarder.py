from __future__ import print_function
from os.path import join, dirname, abspath
import time

from bokeh.server.settings import settings as server_settings
from bokeh.server.forwarder import Forwarder

if __name__ == "__main__":
    config_file = abspath(join(dirname(__file__), 'config.py'))
    print (config_file)
    server_settings.from_file(config_file)
    forwarder = Forwarder(server_settings.ctx,
                          server_settings.pub_zmqaddr,
                          server_settings.sub_zmqaddr)
    try:
        forwarder.start()
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        forwarder.stop()
