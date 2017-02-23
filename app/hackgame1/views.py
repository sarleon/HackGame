from flask import Flask,url_for,render_template,request,Response,session,redirect
from . import hackgame1
from ..models.message import Messages
from ..utils.random_token import random_token
@hackgame1.route('/')
def index():

    if not session.get('token'):
        session['token']=random_token()
    return render_template('hackgame1/index.html')

@hackgame1.route('/add_message',methods=['POST'])
def add_message():
    content=request.form.get('content')
    token=session.get('token')
    Messages.add_message("",content,token)
    redirect_method=request.form.get('redirect')
    return redirect(url_for('hackgame1.'+redirect_method))

@hackgame1.route('/delete_message',methods=['POST'])
def delete_message():


    id = request.form.get('id')
    Messages.delete_message(id)
    redirect_method = request.form.get('redirect')
    return redirect(url_for('hackgame1.' + redirect_method))

#template test
@hackgame1.route('/tt1')
def template_test_board():

    return render_template('hackgame1/board.html')


@hackgame1.route('/stage1')
def stage1():
    current_stage = 'stage1'
    messages=Messages.fetch_messages_by_token(session.get('token') or "")
    return render_template('hackgame1/board.html',messages=messages,current_stage=current_stage)


@hackgame1.route('/stage2')
def stage2():
    return

@hackgame1.route('/stage3')
def stage3():
    return


@hackgame1.route('/stage4')
def stage4():
    return
