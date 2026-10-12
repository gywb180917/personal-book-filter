# 从 FastAPI 中导入 FastAPI 类和 Query 参数验证工具
from fastapi import FastAPI, Query


# 导入自己写的数据加载函数
# 作用：读取 books.json 文件，返回图书列表
from book_filter.data_loader import load_books


# 导入自己写的图书筛选函数
# 作用：根据类别筛选图书
from book_filter.recommender import filter_by_genre


# 创建 FastAPI 应用对象
# title 会显示在接口文档 Swagger 页面中
app = FastAPI(title="个人图书筛选器 API")



# 定义根路径接口
# 访问:
# http://127.0.0.1:8000/
#
# 使用 GET 请求
@app.get("/")
def read_root():

    # 返回 Python 字典
    # FastAPI 会自动转换成 JSON
    return {
        "message": "Book API is running"
    }



# 定义图书查询接口
#
# 访问:
# GET /books
#
# 例如:
# http://127.0.0.1:8000/books
#
# 或:
# http://127.0.0.1:8000/books?genre=科幻
@app.get("/books")
def list_books(
    # 定义一个可选查询参数 genre
    #
    # str | None 表示:
    # 可以是字符串，也可以为空
    #
    # 默认值 None
    genre: str | None = None
):

    # 调用 data_loader.py 中的函数
    # 从 data/books.json 加载所有图书
    books = load_books("data/books.json")


    # 判断用户有没有传 genre 参数
    #
    # 如果:
    # /books?genre=科幻
    #
    # 那么 genre 有值
    if genre:

        # 调用 recommender.py 中的筛选函数
        # 只保留指定类别的图书
        books = filter_by_genre(books, genre)


    # 返回查询结果
    #
    # items:
    # 图书列表
    #
    # count:
    # 图书数量
    return {
        "items": books,
        "count": len(books)
    }




# 定义推荐接口
#
# 访问:
# GET /recommendations
#
# 示例:
# /recommendations?genre=科幻&top_k=3
@app.get("/recommendations")
def recommend_books(

    # 必须提供 genre 参数
    #
    # Query:
    # 用来限制参数规则
    #
    # min_length=1:
    # 类别名称不能为空
    genre: str = Query(min_length=1),


    # top_k 表示返回多少本推荐书
    #
    # 默认返回5本
    #
    # ge=1:
    # 最小值1
    #
    # le=20:
    # 最大值20
    top_k: int = Query(
        default=5,
        ge=1,
        le=20
    ),
):

    # 加载所有图书
    books = load_books("data/books.json")


    # 按类别筛选
    #
    # [:top_k]
    # 只取前 top_k 本
    items = filter_by_genre(
        books,
        genre
    )[:top_k]


    # 返回推荐结果
    return {
        "genre": genre,
        "items": items,
        "count": len(items),
    }