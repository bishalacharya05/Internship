from fastapi import FastAPI,Path,HTTPException,status,Response
from pydantic import BaseModel,Field

app = FastAPI()

class Book(BaseModel):
    id:int
    title:str
    author:str
    price:float
    isbn:int
    available:bool
    number_of_pages:int
    rating: float = Field(1,ge=1, le=5)

    class config():
        extra="forbid"
        orm_mode=True

Books =[]
@app.get("/books")
def get_books():
    return {
        "books":Books
    }

#fetching books by rating
@app.get("/bookrating/{book_rating}")
def get_book_by_rating(book_rating:float):
    matched_books=[]
    for b in Books:
        if b.rating==book_rating:
            matched_books.append(b)
    if matched_books:
     return matched_books
    return {
        "message":"No books found related to that rating"
    }
            
#getting the book details with id and also validating with path parameter gt=0
@app.get("/book/{book_id}")
def get_book_details(book_id:int = Path(..., ge=0, description="The ID of the book")):
    '''the value of book_id should be integer and greater than 0'''
    for b in Books:
        if b.id==book_id:
            return b
        #http exception
    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )
            
        
#Post operation with explicit status code in path 
@app.post("/book",status_code=status.HTTP_201_CREATED)
def create_book(book:Book):
    Books.append(book)
    return {
        "message":"Book added successfully",
        "book":book
    }

@app.put("/book/{book_id}")
def update_book(book_id:int,book:Book):
    for b in Books:
        if b.id==book_id:
            b.title=book.title
            b.author=book.author
            b.isbn=book.isbn
            b.price=book.price
            b.available=book.available
            b.number_of_pages=book.number_of_pages
            return {
                "message":"Book updated successfully",
                "book":b
        }
    return {
        "message":"Book not found"
    }

#Deleting book 
@app.delete("books/{book_id}")
#passing Response status code as parameter
def delete_details(book_id:int,response:Response):
    for b in Books:
        if b.id==book_id:
            deleted_book= Books.pop(b)
            return {
                "message":"book deleted successfully",
                "book":deleted_book
            }
    response.status_code= 404
    return {
        "message":"book not found"
    }



