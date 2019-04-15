from flask import Flask,render_template
from serv import content
from serv import get_set_anthing
from serv import users
from serv import devices


app = Flask(__name__)
app.register_blueprint(content.content)
app.register_blueprint(get_set_anthing.gsa)
app.register_blueprint(users.users)
app.register_blueprint(devices.devices)


@app.route("/")
def web_toy():
    return render_template("WebToy.html")


if __name__ == '__main__':
    app.run("0.0.0.0",9527,debug=True)
