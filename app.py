from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from forms import CadastroUsuarioForm, LoginUsuarioForm
from flask_login import LoginManager, login_user, logout_user

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///abrigo.db'
app.config['SECRET_KEY'] = 'akjcnncshdna' 

db = SQLAlchemy(app)
login_manager = LoginManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(12), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymou(self):
        return False
      
    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % self.usuario

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/cadastro', methods = ['GET', 'POST'])
def cadastro():
    form = CadastroUsuarioForm()
    if request.method == 'POST':
        user = User()
        user.usuario = request.form['usuario']
        user.email = request.form['email']
        user.senha = request.form['senha']
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("cadastro.html", form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginUsuarioForm()
    if form.validate_on_submit():
        user = User.query.filter_by(usuario=form.usuario.data).first()
        if user and user.senha == form.senha.data:
            login_user(user)
            return redirect(url_for("home"))
    
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)