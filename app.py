import bottle
@bottle.route('/')
def hello_world():
    return '<h1>Hello World</h1>'
