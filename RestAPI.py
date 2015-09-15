from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.resource import NoResource

from calendar import calendar

class Calendar(Resource):
    def getChild(self, path, request):
        try:
            year = int(path)
        except ValueError:
            return NoResource()
        else:
            return YearPage(year)

class YearPage(Resource):
    def __init__(self, year):
        Resource.__init__(self)
        self.year = year

    def render_GET(self, request):
        return "<html><body><pre>%s</pre></body></html>" % (calendar(self.year),)

root = Calendar
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()