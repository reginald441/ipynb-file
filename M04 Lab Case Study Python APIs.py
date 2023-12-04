from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {
        'id': 1,
        'book_name': 'War and Peace',
        'author': 'Leo Tolstoy',
        'publisher': 'Russian Publishing House'
    },
    {
        'id': 2,
        'book_name': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'publisher': 'Charles Scribner\'s Sons'
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = [book for book in books if book['id'] == id]
    return jsonify(book)

@app.route('/books', methods=['POST'])
def add_book():
    book = {
        'id': books[-1]['id'] + 1,
        'book_name': request.json['book_name'],
        'author': request.json['author'],
        'publisher': request.json['publisher']
    }
    books.append(book)
    return jsonify(book)

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = [book for book in books if book['id'] == id]
    book[0]['book_name'] = request.json.get('book_name', book[0]['book_name'])
    book[0]['author'] = request.json.get('author', book[0]['author'])
    book[0]['publisher'] = request.json.get('publisher', book[0]['publisher'])
    return jsonify(book[0])

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = [book for book in books if book['id'] == id]
    books.remove(book[0])
    return jsonify({'result': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)
