import falcon
from book.resources import BookResource, HomeResource, AuthorResource
from mongoengine import connect
connect('bookdb1',host='mongodb+srv://wawindaji:wawindaji@cluster0-e0miz.mongodb.net/test?retryWrites=true&w=majority',port=27017)

app = falcon.API()
app.add_route('/', HomeResource())
app.add_route('/books', BookResource())
app.add_route('/books/{book_id}', BookResource())
app.add_route('/authors',AuthorResource())
app.add_route('/authors/{author_id}', AuthorResource())
