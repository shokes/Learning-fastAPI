from fastapi import Body, FastAPI


app = FastAPI()


BOOKS = [
 {
  'title': 'Title One', 'author': 'Author One', 'category': 'Science'
 },
 {
  'title': 'Title Two', 'author': 'Author Two', 'category': 'Science'
 },
 {
  'title': 'Title Three', 'author': 'Author Three', 'category': 'History'
 },
 {
  'title': 'Title Four', 'author': 'Author Four', 'category': 'Math'
 },
 {
  'title': 'Title Five', 'author': 'Author Five', 'category': 'Math'
 },
 {
  'title': 'Title Six', 'author': 'Author Two', 'category': 'Math'
 }
]


# GET METHOD

@app.get("/books")
async def read_all_books():
    return BOOKS
   
# path parameters
@app.get("/books/{book_title}")   
async def read_book(book_title: str):
   for book in BOOKS:
    if book.get('title').casefold() == book_title.casefold():
     return book  
    
    
 # query parameters
@app.get("/books/")
async def read_book_category_by_query(category: str):
  books_to_return = []
  for book in BOOKS:
   if book.get('category').casefold() == category.casefold():
     books_to_return.append(book) 
  return books_to_return  
 
 
@app.get("/books/books_author")
async def read_book_author_category_by_query(author: str, category):
  books_to_return = []
  for book in BOOKS:
   if book.get('category').casefold() == category.casefold() and book.get('author').casefold() == author.casefold():
     books_to_return.append(book) 
  return books_to_return  
 
 
# POST METHOD
@app.post("/books/create_book")
async def create_book(new_book=Body()):
  BOOKS.append(new_book)
  return {"message" : "Successfully added a book"}
 

# PUT METHOD 
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
   for i in range(len(BOOKS)):
       if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
           BOOKS[i] =  updated_book
           return {"message" : "Successfully added a book"}
          

# DELETE METHOD

@app.delete("/books/delete_book/{book_title}")   
async def delete_book(book_title: str):
   for i in range(len(BOOKS)):
       if BOOKS[i].get('title').casefold() == book_title.casefold():
          BOOKS.pop(i)
          break
          
     
           
          
 
    