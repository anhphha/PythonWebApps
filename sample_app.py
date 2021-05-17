from sample_backend import Backend
from flask import g
from build_flask import create_app

app = create_app()


@app.before_request
def before_request():
    backend_instance = Backend(hostname=)
    g.backend_ = backend_instance


# @app.teardown_request
# def teardown_request(request):
#     if g.backend is not None:
#         del g.backend

@app.route('/')
def hello():
    result = g.backend_.get_name()
    return result


@app.route('/time')
def time():
    result = g.backend_.get_time()

    return result


@app.route('/data')
def get_data():
    result = g.backend.result_manger()
    return result

app.run()
