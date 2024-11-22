from flask import Flask, redirect, request, render_template, jsonify

to_dos = {}

site = Flask(__name__)

@site.route("/")
def index():
    return render_template("index.html")

@site.route("/add", methods=['GET'])
def add():
    name = request.args.get('name')
    desc = request.args.get('desc')
    to_dos[name] = desc
    return redirect("/", code=302)

@site.route("/remove", methods=['GET'])
def remove():
    name = request.args.get('name')
    to_dos.pop(name)
    return redirect("/", code=302)

@site.route('/show', methods=['GET'])
def show_todos():
    return jsonify(to_dos)

if __name__ == "__main__":
    site.run(debug=True)