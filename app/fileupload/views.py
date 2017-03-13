from  . import fileupload
from flask import render_template,redirect




@fileupload.route('/stage')
def stage():
    return render_template('')