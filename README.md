# 在项目根目录的 PowerShell 中安装（使用项目虚拟环境）
.\.venv\Scripts\python.exe -m pip install "fastapi[standard]"
# 启动开发服务器
.\.venv\Scripts\fastapi.exe dev api.py
# 浏览器访问
http://127.0.0.1:8000/docs