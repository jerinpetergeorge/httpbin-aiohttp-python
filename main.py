from aiohttp import web
from httpbin.routes import setup_routes

app = web.Application()
setup_routes(app)
web.run_app(app, port=3333)

