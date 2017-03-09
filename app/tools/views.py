from . import tools
from flask import render_template,redirect,Response

@tools.route('/')
def index():
    return


@tools.route('/wenku')
def wenku():
    return



@tools.route('/hash')
def hash():

    return

@tools.route('/crypt')
def crypt():
    return

@tools.route('/encode')
def encode():
    return render_template('tools/encode.html')
