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

    return render_template('tools/hash.html')

@tools.route('/crypt')
def crypt():
     return render_template('tools/crypt.html')

@tools.route('/encode')
def encode():
    return render_template('tools/encode.html')

