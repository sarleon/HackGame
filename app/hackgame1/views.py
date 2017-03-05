# coding:utf-8
from flask import Flask, url_for, render_template, request, Response, session, redirect
from . import hackgame1
from ..models.message import Messages
from ..utils.random_token import random_token
from ..utils.string_filter import script_tag_recursive_filter, script_tag_filter, script_tag_nf_filter

levels_map = [
     lambda x: x,
     script_tag_filter,
     script_tag_nf_filter,
     script_tag_recursive_filter
]
levels_tip_map=[
    "",
    "",
    "",
    ""

]


@DeprecationWarning
def generate_indentity(fn):
    def wrapper():
        print "generate!!!"
        if session.get('token') is None:
            session['token'] = random_token()
        fn()

    return wrapper


@hackgame1.route('/')
def index():
    if not session.get('token'):
        session['token'] = random_token()
    return render_template('hackgame1/index.html')


@hackgame1.route('/add_message', methods=['POST'])
def add_message():
    stage = request.form.get('redirect')
    content = request.form.get('content')
    try:
        print stage+" submit"
        stage = int(stage)

    except ValueError as e:
        print e.message
        return 'invalid request', 400

    try:
        content=levels_map[stage-1](content)
    except:
        return 'invalid request', 400
    token = session.get('token')
    Messages.add_message("", content, token)

    return redirect(url_for('hackgame1.stage', level=stage))


@hackgame1.route('/delete_message', methods=['POST'])
def delete_message():
    id = request.form.get('id')
    Messages.delete_message(id)
    redirect_method = request.form.get('redirect')
    return redirect(url_for('hackgame1.stage', level=redirect_method))


# template test
@hackgame1.route('/delete_my_message', methods=['POST'])
def delete_my_message():
    token = session.get('token')
    if Messages.delete_my_message(token):
        return "success"
    else:
        return "failed"


@hackgame1.route('/tt1')
def template_test_board():
    return render_template('hackgame1/board.html')


@hackgame1.route('/stage')
def stage():
    stage = request.args.get('level')
    try:
        stage = int(stage)
    except ValueError as e:
        print e.message
        return 'invalid request', 400
    if stage > len(levels_map)+1:

        print stage
        print len(levels_map)
        return 'invalid argument', 404



    current_stage = stage
    try:
        tip=levels_tip_map[stage]
    except IndexError as e:
        print e.message

    if stage < len(levels_map):
        next_stage = current_stage + 1
    else:
        next_stage = None

    messages = Messages.fetch_messages_by_token(session.get('token') or "")
    return render_template('hackgame1/board.html', messages=messages, current_stage=current_stage,
                           next_stage=next_stage,tip=tip)


# # 第一关
# @hackgame1.route('/stage1')
# def stage1():
#     current_stage = 'stage1'
#     next_stage = 'stage2'
#     messages = Messages.fetch_messages_by_token(session.get('token') or "")
#     return render_template('hackgame1/board.html', messages=messages, current_stage=current_stage,
#                            next_stage=next_stage)
#
#
# # 第二关
# @hackgame1.route('/stage2')
# def stage2():
#     current_stage = 'stage2'
#     next_stage = 'stage3'
#     messages = Messages.fetch_messages_by_token(session.get('token') or "")
#     return render_template('hackgame1/board.html', messages=messages, current_stage=current_stage,
#                            next_stage=next_stage)
#
#
# @hackgame1.route('/stage3')
# def stage3():
#     return
#
#
# @hackgame1.route('/stage4')
# def stage4():
#     return
