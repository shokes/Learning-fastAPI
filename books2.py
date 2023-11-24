from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI()


# CLASS
class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    
    # CONTRUCTOR
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating 

class BookRequest(BaseModel):    
     id: Optional[int] = None
     title: str = Field(min_length=3)
     author: str = Field(min_length=1)
     description: str = Field(min_length=1, max_length=7)
     rating: int = Field(gt=0, lt=6)
     
     class Config: 
        json_schema_extra = {
            'example': {
               'title': 'A new book',
                'author': 'Oshoke',
                'decription': 'description of a book',
                 'rating': 4,
      }
     }
         
    

BOOKS = [  
 Book(1, 'Computer science pro', 'codingwithroby', 'a very nice book', 5),
 Book(2, 'Computer science pro', 'codingwithroby', 'a very nice book', 4),
 Book(3, 'Computer science pro', 'codingwithroby', 'a very nice book', 3),
 Book(4, 'Computer science pro', 'codingwithroby', 'a very nice book', 2),
 Book(5, 'Computer science pro', 'codingwithroby', 'a very nice book', 1)
         
]


@app.get("/books")
async def read_all_books():
 return BOOKS

@app.get('/books/{book_id}')
async def read_book(book_id: int):
  for book in BOOKS:
     if book.id == book_id:
      return book 

@app.get('/books/')
async def read_book_by_rating(rating: int):
   books_to_return = []
   for book in BOOKS:
     if book.rating == rating: 
      books_to_return.append(book)
      return books_to_return



@app.post('/create-book')
async def create_book(book_request: BookRequest ):
 new_book = Book(**book_request.model_dump())
 BOOKS.append(find_book_id(new_book))
 
 
 
def find_book_id(book: Book):
  if len(BOOKS) > 1:
    book.id = BOOKS[-1].id + 1
  else: 
    book.id = 1
  return book     
 
 
 
@app.put('books/update_book') 
async def update_book(book: BookRequest ):
 new_book = Book(**book.model_dump())
 for i in range(len(BOOKS)):
      if BOOKS[i].id == new_book.id:
         BOOKS[i] = new_book
      
    
      
   
 