# 负载启动WSGI服务器，加载application()函数

# 从wsgiref 模块导入
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数：
from hello_1128 import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application
httpd = make_server('',8000, application)
print('Serving HTTP on port 8000...')
# 开始监听http请求：
httpd.serve_forever()

# 启动成功打开浏览器，输入http://localhost:8000/，就可以看到结果了