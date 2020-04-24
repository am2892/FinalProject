import flask

auth_bp = flask.Blueprint('auth', __name__)

@auth_bp.route('/')
def login():
    pass

@auth_bp.route('/')
def signup():
    pass