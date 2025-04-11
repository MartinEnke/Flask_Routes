from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime


app = Flask(__name__)


users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
}


@app.route("/all_users")
def all_users():
    current_time = datetime.now().strftime("%H:%M:%S  //  %D")
    return render_template("dict_template.html", title="All Users", users=users, time=current_time)


@app.route("/update_country", methods=["GET", "POST"])
def update_country():
    if request.method == "POST":
        name = request.form["name"]
        country = request.form["country"]

        if name in users:
            users[name]["country"] = country
        return redirect(url_for("all_users"))  # Redirect to verify update

    return render_template("update_country.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


@app.errorhandler(500)
def internal_error():
    return render_template("505.html")

@app.route("/") # The home route (@app.route("/")) handles the incoming GET request and uses the value via request.args.get("name").
def home():
    name = request.args.get("name", "Stranger")
    current_time = datetime.now().strftime("%H:%M:%S  //  %D")
    return render_template("index_template.html", title="Home", name=name,  time=current_time)


@app.route("/profile/<username>")
def profile(username):
    return f"Profile page of {username}"


@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')  # Use 'Guest' as default value if no 'name' parameter is provided
    return render_template("form.html", name=name)


@app.route("/update_profile", methods=['GET', 'POST'])
def update_profile():
    if request.method == 'POST':
        user_name = request.form["username"]
        email = request.form["email"]
        return f"Updating profile of {user_name} with email {email}"
    else:
        return "Please submit the form via POST."


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/dict_table")
def dict_table():
    current_time = datetime.now().strftime("%H:%M:%S // %D")
    return render_template("dict_table_template.html", title="Dict_Table", users=users, time=current_time)


@app.route("/user/<username>")
def username(username):
    return username


@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post {post_id}"


@app.route('/path/<path:sub_path>')
def show_sub_path(sub_path):
    # The variable 'subpath' is a string that can include slashes.
    return f"Sub path: {sub_path}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5015, debug=True)