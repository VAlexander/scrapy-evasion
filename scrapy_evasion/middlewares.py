import datetime

from scrapy.conf import settings
from stem import Signal
from stem.control import Controller


class TorMiddleware(object):
    def __init__(self):
        self.node_last_changed = datetime.datetime(year=1970, day=1, month=1)

    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')

    def process_response(self, request, response, spider):
        delta = datetime.datetime.now() - self.node_last_changed

        if (response.status == 503 or response.status == 403) and delta.seconds > settings.get("TOR_TIMEOUT"):
            with Controller.from_port(port=9051) as controller:
                controller.authenticate()
                controller.signal(Signal.NEWNYM)
            self.node_last_changed = datetime.datetime.now()
            print "Changed TOR node"

        return response
