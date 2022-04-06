from flask import Flask, render_template, url_for
from forms import Hypervisor, Servers, RegistrationForm ,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '7b6dcdbbef6bb266b3dc2b191a3b2356'


@app.route("/")
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form = form)


@app.route("/hyper")
def hyper():
    form = Hypervisor()
    return render_template('hypervisor.html', title='Hypervisor', form=form)


@app.route("/servers")
def servers():
    form = Servers()
    return render_template('servers.html', title='Servers', form=form)


@app.route("/register")
def register():
    form = RegistrationForm()
    return   render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=80)
