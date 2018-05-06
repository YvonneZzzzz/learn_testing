# 实现web应用程序的WSGI处理函数

# 最基本的V1.0
# def application ( environ,  start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [b'<h1>Hello,web!</h1>']

# 最基本的V2.0
# def application ( environ,  start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     body = '<h1>hello, {}! </h1>'.format(environ['PATH_INFO'][1:] or 'web')
#     return [body.encode('utf-8')]

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]