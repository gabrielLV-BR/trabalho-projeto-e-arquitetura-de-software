from flask import Blueprint

blueprint = Blueprint('index', __name__)

@blueprint.get('/')
def index():
    return blueprint.send_static_file('index.html')
