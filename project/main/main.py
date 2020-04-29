from flask import render_template, Blueprint

main_bp = Blueprint('main', __name__)


@main_bp.route("/")
def index():
    print("test here")
    return render_template("index.html")
