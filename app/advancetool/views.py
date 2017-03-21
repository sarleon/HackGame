from . import advancetools
from flask import render_template,redirect,Response,url_for

@advancetools.route('/')
def index():
    return redirect(url_for('auto_decode_base'))

@advancetools.route('/auto_decode_base')
def auto_decode_base():
    return render_template('advancetool/auto_decode_base.html')


