from fastapi import FastAPI
from .bible import (
    load_bible_from_csv,
    parse_multiple_citations,
    read_book,
    read_citations
)

app = FastAPI()
BIBLE_FLIEPATH = './assets/bible.csv'
bible_data = load_bible_from_csv(BIBLE_FLIEPATH)

@app.get('/')
def get_root():
    return {'author': 'James Lim'}

@app.get('/books')
def get_books():
    return { 'books': list(bible_data.keys()) }

@app.get('/bible/{book_name}')
def get_book(book_name):
    return { book_name: read_book(bible_data, book_name) }

@app.get('/bible/{book_name}/{reference}')
def get_chapter(book_name, reference):
    return {
        book_name: read_citations(
            read_book(bible_data, book_name),
            parse_multiple_citations(reference)
        )
    }
