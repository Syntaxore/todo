from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "create" in request.form:
            return redirect(url_for("main.create"))
    return render_template("index.html")

@main.route("/create", methods=["GET", "POST"])
def create():
    return render_template("create.html")