from book_filter.data_loader import load_books
from book_filter.recommender import filter_by_genre
def main():
   books = load_books("data/books.json")
   genre = input("请输入类别：").strip()
   results = filter_by_genre(books, genre)
   if not results:
      print("没有找到匹配的图书")
      return
   for book in results:
      print(f"{book['title']} - {book['genre']}")
if __name__ == "__main__":
   main()