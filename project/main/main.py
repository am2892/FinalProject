import flask

main_bp = flask.Blueprint('main', __name__, template_folder='templates')


@main_bp.route('/')
def index():
    pass