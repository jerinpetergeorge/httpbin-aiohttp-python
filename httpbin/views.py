from aiohttp import web
from httpbin.function import parse_request


async def index(request):
    return web.Response(text='Hello Aiohttp!')


class HttpMethodHandler:
    def __init__(self):
        pass

    async def all_method_handler(self, request):
        parsed_request = await parse_request(request)
        print(parsed_request)
        return web.json_response(parsed_request)


http_method_names = ['get', 'post', 'put', 'patch', 'delete']
http_method_handler = HttpMethodHandler()
http_method_routes = [getattr(web, method_name)('/%s/' % method_name, http_method_handler.all_method_handler, name='http-%s' % method_name)
                      for method_name in http_method_names]
