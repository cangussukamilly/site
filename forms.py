#coding: utf-8
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CadastroUsuarioForm(FlaskForm):
    usuario = StringField('Usuário', validators = [DataRequired(), Length(min = 2, max = 80)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    senha = PasswordField('Senha', validators = [DataRequired(), EqualTo('conf_senha')])
    submit = SubmitField('Cadastrar')

class LoginUsuarioForm(FlaskForm):
    usuario = StringField('Usuário', validators = [DataRequired()])
    senha = PasswordField('Senha', validators = [DataRequired()])
    submit = SubmitField('Entrar')

class AdocoesForm(FlaskForm):
    motivo = TextAreaField('Por que você deseja dotar um cão?', validators = [DataRequired()])
    submit = SubmitField('Adotar')