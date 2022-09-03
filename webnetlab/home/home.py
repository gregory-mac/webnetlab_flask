from flask import Blueprint, redirect, url_for

home_bp = Blueprint("home_bp", __name__)


@home_bp.get("/")
@home_bp.get("/index")
def home():
    return redirect(url_for("list_labs_view"), 303)

# TODO: make about page
# @home_bp.get("/about")
# def about():
#     return render_template()
