from txrestapi.methods import GET, POST, PUT, ALL, DELETE
from txrestapi.resource import APIResource

class BookResource(APIResource):
    @GET('^/book/(?P<id>[^/]+)')
    def getBook(self, request, id):
        return 'Pick up one book with id %s' % id

    @GET('^/book/')
    def books(self,request):
        return "books"

    @PUT('^/book/(?P<id>[^/]+)')
    def updateBook(self,request):
        return "Update book with id %s" % id

    @POST('^/book/(?P<id>[^/]+)')
    def saveBook(self, request, id):
        return "Save book with id %s" % id

    @DELETE('^/book/(?P<id>[^/]+)')
    def deleteBook(self,request,id):
        return "Delete book with id %s" % id

    @ALL('^/')
    def default_view(self, request):
        return "I fail to match other URLs."
