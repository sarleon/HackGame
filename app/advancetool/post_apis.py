import base64
from flask import render_template,request
from . import advancetools



def is_printable_string(input_string):


@advancetools.route('/auto_decode_base64_api',methods=['POST'])
def auto_decode_base64_api():
    input_string=request.form.get('input')


