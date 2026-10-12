def filter_by_genre(books,genre):
   result = []
   for book in books:
      if book["genre"] == genre:
         result.append(book)
   return result