from httpbin import views


def setup_routes(app):
    app.router.add_get('/', views.index)
    app.add_routes(views.http_method_routes)
