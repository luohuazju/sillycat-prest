from txrestapi.methods import GET, POST, PUT, ALL, DELETE
from txrestapi.resource import APIResource
import json

class BookResource(APIResource):

    @GET('^/book/(?P<id>[^/]+)')
    def getBook(self, request, id):
        return 'Pick up one book with id %s' % id

    @GET('^/book/')
    def books(self,request):
        return "books"

    @PUT('^/book/(?P<id>[^/]+)')
    def updateBook(self,request, id):
        book = json.loads(request.content.read())
        book['id'] = id
        return json.dumps(book)

    @POST('^/book/')
    def saveBook(self, request):
        book = json.loads(request.content.read())
        book['id'] = 1
        return json.dumps(book)

    @DELETE('^/book/(?P<id>[^/]+)')
    def deleteBook(self,request,id):
        return "Delete book with id %s" % id

    @ALL('^/')
    def default_view(self, request):
        return "I fail to match other URLs."
