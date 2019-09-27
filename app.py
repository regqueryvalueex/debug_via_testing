from flask import Flask, Blueprint
from restplus import api

from cart import resources


def create_app():
    flask_app = Flask(__name__)

    blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(blueprint)
    api.add_namespace(resources.namespace)

    flask_app.register_blueprint(blueprint)

    return flask_app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
