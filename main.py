from database import Database
from bookModel import BookModel
from cli import BookCLI

db = Database(database="livraria", collection="livros")
bookModel = BookModel(database=db)

bookCLI = BookCLI(bookModel)
bookCLI.run()
