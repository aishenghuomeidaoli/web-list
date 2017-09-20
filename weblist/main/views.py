# _*_ coding: utf-8 _*_
from flask import render_template, redirect, request, session, url_for
from . import main
from .. import db
from .models import User

ENGINES = [
    {'name_zh_cn': u'百度', 'url': 'https://www.baidu.com/s', 'name_en': 'Baidu', 'key': 'wd'},
    {'name_zh_cn': u'搜狗', 'url': 'https://www.sogou.com/web', 'name_en': 'Sougou', 'key': 'query'},
    {'name_zh_cn': u'必应', 'url': 'https://cn.bing.com/search', 'name_en': 'Bing', 'key': 'q'},
]


@main.route('/')
def engines():
    name = session.get('user_name')
    return render_template('index.html', engines=ENGINES, name=name)


@main.route('/search')
def search():
    engines = request.args.getlist('engine')
    if not engines:
        return redirect('/')
    keyword = request.args.get('keyword')
    links = []
    for engine in ENGINES:
        if engine.get('name_en') in engines:
            links.append(engine.get('url') + '?' + engine.get('key') + '=' + keyword)
    width = 12 / len(links)
    name = session.get('user_name')
    return render_template('search.html', links=links, engines=ENGINES, selects=engines, keyword=keyword, width=width,
                           name=name)


@main.route('/register', methods=['POST', 'GET'])
def register():
    if session.get('user_id'):
        return redirect(url_for('main.engines'))
    if request.method == 'GET':
        return render_template('register.html')
    name = request.form.get('name')
    email = request.form.get('email')
    pw = request.form.get('pw')
    pw_confirm = request.form.get('pw_confirm')
    msg = ''
    if not name:
        msg = u'名称不能为空'
    elif not email:
        msg = u'邮箱不能为空'
    elif db.query(User).filter_by(email=email).first():
        msg = u'邮箱已被注册'
    elif not pw:
        msg = u'密码不能为空'
    elif pw_confirm != pw:
        msg = u'确认密码与密码不一致'
    if msg:
        return render_template('register.html', **locals())
    user = User(name=name, email=email, pw=pw)
    db.add(user)
    db.commit()
    msg = u'注册成功，欢迎你，%s' % name
    return render_template('register.html', msg=msg)


@main.route('/login', methods=['POST', 'GET'])
def login():
    if session.get('user_id'):
        return redirect(url_for('main.engines'))
    if request.method == 'GET':
        return render_template('login.html')
    email = request.form.get('email')
    pw = request.form.get('pw')
    msg = ''
    if not email:
        msg = u'邮箱不能为空'
    elif not pw:
        msg = u'密码不能为空'
    else:
        user = db.query(User).filter_by(email=email, pw=pw).first()
        if not user:
            msg = u'邮箱或密码错误'
    if msg:
        return render_template('register.html', **locals())
    session['user_id'] = user.id
    session['user_name'] = user.name
    return redirect(url_for('main.engines'))


@main.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.engines'))
