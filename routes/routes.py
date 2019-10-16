from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/check")
def check():
    return "Congratulations! Your app works. :)"

@router.route("/check")
def hello():
    return "Hacktober fest is cool"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return
