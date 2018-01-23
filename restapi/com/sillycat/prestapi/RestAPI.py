from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.internet import reactor

from BookAPI import BookResource

bookResource = BookResource()

rootResource = Resource()
rootResource.putChild("book", bookResource)

site = Site(rootResource, timeout=None)
reactor.listenTCP(8888,site)
reactor.run()