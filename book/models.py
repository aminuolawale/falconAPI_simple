from mongoengine import Document, StringField, IntField, DateTimeField, ObjectIdField
from datetime import datetime

class Book(Document):
    title = StringField(max_length=50, required=True)
    genre = StringField(max_length=50, required=True)
    page_count = IntField(min_value=10, required=True)
    author = ObjectIdField(required=True)
    created_at = DateTimeField(default=datetime.utcnow())

    def format(self):
        """ returns the Book instance formated as a dict. Should be called when passing object for json serialization """
        book = {}
        book['id'] = str(self.id)
        book['title'] = self.title
        book['genre'] = self.genre
        book['page_count'] = self.page_count
        author = Author.objects.get(id=self.author)
        book['author'] = author.format()
        book['created_at'] = self.created_at.strftime("%c")
        return book

class Author(Document):
    name = StringField(max_length=50, required=True)
    nationality = StringField(max_length=50, required=True)
    created_at = DateTimeField(default=datetime.utcnow()) 

    def format(self):
        author = {}
        author['id'] = str(self.id)
        author['name'] = self.name
        author['nationality'] = self.nationality
        author['created_at'] = self.created_at.strftime("%c")
        return author