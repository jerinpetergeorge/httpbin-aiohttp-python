from json.decoder import JSONDecodeError


async def request_has_file(request):
    from aiohttp.web_request import FileField
    multipart_data = await request.post()
    for field, value in multipart_data.items():
        if type(value) == FileField:
            return True
    else:
        return False


async def parse_input_data(request):
    has_file = await request_has_file(request)
    parsed_data = {
        'body': await request.text(),
        'has_file': has_file
    }
    try:
        parsed_data['json'] = await request.json()
    except JSONDecodeError:
        if not has_file:
            parsed_data['form'] = dict(await request.post())
    return parsed_data


async def parse_request(request):
    parsed_data = await parse_input_data(request)
    parsed_request = {
        'origin': request.remote,
        'url': str(request.url),
        'headers': dict(request.headers),
        **parsed_data,

    }
    return parsed_request