from base64 import b16decode,b32decode,b64decode
from flask import render_template,request
from . import advancetools
import  string
from ..errors.codecerroes import InvalidCharsetError

b16charset=string.digits+"ABCDEF"+"="
b32charset=string.ascii_uppercase+"3456789"+"="
b64charset=string.digits+string.ascii_letters+"+/="

def is_printable_string(input_string):
    return all(string.printable(c) for c in input_string)

def check_is_valid(input_string):
    return is_printable_string(input_string)

def get_decode_function(input_string):
    if all_true(in_charset,input_string,b64charset):
        if all_true(in_charset,input_string,b32charset):
            if all_true(in_charset,input_string,b16charset):
                return b64decode
            else:
                return b32decode
        else:
            return b16decode
    else:
        raise InvalidCharsetError


def in_charset(input_char,charset):
    return input_char in charset

def all_true(function,iterable,*args):
    flag=True
    for item in iterable:
        if not function(item):
            flag=False
    return flag


@advancetools.route('/auto_decode_base64_api',methods=['POST'])
def auto_decode_base64_api():
    input_string=request.form.get('input')


