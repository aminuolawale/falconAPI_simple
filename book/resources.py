from .models import  Book, Author
import falcon
import json

class HomeResource(object):
    def on_get(self, req, resp):
        resp.body = json.dumps({'status': True, 'message': 'welcome to the books api'})
        resp.status = falcon.HTTP_200

class AuthorResource(object):
    def on_get(self, req, resp, author_id=None):
        if author_id:
            author = Author.object.get(id=author_id)
            if not author:
                resp.body = json.dumps({'status': False,'message':'invalid author_id'})
                resp.status = falcon.HTTP_404
            resp.body = json.dumps({'status':True,'message':'success','data':author.format()})
            resp.status = falcon.HTTP_200
        else:
            authors = [author.format() for author in Author.objects]
            resp.body = json.dumps({'status':True,'message':'success', 'data':authors})
            resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        author_data = req.media
        author = Author.objects.create(**author_data)
        author.save()
        resp.body = json.dumps({'status': True, 'message': 'successfully added new author', 'data': author.format()})
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp, author_id):
        author = Author.objects.get(id=author_id)
        if not author:
            resp.body = json.dumps({'status': False,'message':'invalid author_id'})
            resp.status = falcon.HTTP_404
        author_data = req.media
        for key in author_data:
            author[key] = author_data[key]
        author.save()
        resp.body = json.dumps({'status':True,'message':'author updated succesfully', 'data':author.format()})
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, author_id):
        author = Author.objects.get(id=author_id)
        if not author:
            resp.body = json.dumps({'status': False,'message':'invalid author_id'})
            resp.status = falcon.HTTP_404
        author.delete()
        resp.body = json.dumps({'status':True, 'message': 'author deleted successfully'})
        resp.status = falcon.HTTP_200



class BookResource(object):
    def on_get(self, req, resp, book_id=None):
        if book_id:
            book = Book.objects.get(id=book_id)
            if not book:
                resp.body = json.dumps({'status': False, 'message': 'invalid book_id'})
                resp.status = falcon.HTTP_404
            resp.body = json.dumps({'status':True, 'message': 'success', 'data':book.format()})
        else:
            books = [ book.format() for book in Book.objects ]
            resp.body = json.dumps({'status': True, 'message': 'success', 'data':books})
    def on_post(self, req, resp):
        book_data = req.media
        book = Book.objects.create(**book_data)
        book.save()
        resp.body = json.dumps({'status':True, 'message': 'book added successfully','data':book.format()})
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp, book_id):
        book = Book.objects.get(id=book_id)
        if not book:
            resp.body = json.dumps({'status': False, 'message': 'invalid book_id'})
            resp.status = falcon.HTTP_404
        book_data = req.media
        for key in book_data:
            book[key]= book_data[key]
        book.save()
        resp.body = json.dumps({'status':True, 'message': 'book updated successfully','data':book.format()})
        resp.status = falcon.HTTP_200
    def on_delete(self, req, resp, book_id):
        book = Book.objects.get(id=book_id)
        if not book:
            resp.body = json.dumps({'status': False, 'message': 'invalid book_id'})
            resp.status = falcon.HTTP_404
        book.delete()
        resp.body = json.dumps({'status':True, 'message': 'book deleted successfully'})
        resp.status = falcon.HTTP_200

