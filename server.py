import list

from flask import Flask, redirect, request, render_template, jsonify

site = Flask(__name__)

@site.route("/")
def index():
    return render_template("index.html")

@site.route("/add", methods=['GET'])
def add():
    name = request.args.get('name')
    desc = request.args.get('desc')
    print(name, desc)
    list.to_dos[name] = desc
    return redirect("/")

@site.route('/show', methods=['GET'])
def show_todos():
    return jsonify(list.to_dos)

if __name__ == "__main__":
    site.run(debug=True)