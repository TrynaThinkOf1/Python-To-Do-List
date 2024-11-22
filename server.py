import list

from flask import Flask, redirect, request, render_template

site = Flask(__name__)

@site.route("/")
def index():
    return render_template("index.html")

@site.route("/add", methods=['GET'])
def add():
    name = request.args.get('name')
    desc = request.args.get('desc')
    list.to_dos[name:desc]
    return redirect("/")

if __name__ == "__main__":
    site.run(debug=True)