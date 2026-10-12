


books = load_books("data/books.json")
for book in filter_by_genre(books,"科幻"):
   print(book["title"])