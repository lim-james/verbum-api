from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_root():
    return {'Hello': 'World'}

@app.get('/bible/{book}')
def get_book(book):
    return {'book': book}

def parse_possible_range(text):
    if '-' in text:
        return tuple(int(i) for i in text.split('-'))
    else:
        return int(text)

def parse_verses(text):
    return [parse_possible_range(t) for t in text.split(',')]

def parse_citation(citation):
    components = citation.split(':')
    if len(components) == 1:
        return {"chapters": parse_possible_range(components[0])}
    else:
        return {
            "chapters": int(components[0]),
            "verses": parse_verses(components[1])
        }

def parse_multiple_citations(citation):
    return [parse_citation(book) for book in citation.split(';')]

@app.get('/bible/{book}/{reference}')
def get_chapter(book, reference):
    return {
        'book': book,
        'citation': parse_multiple_citations(reference)
    }
