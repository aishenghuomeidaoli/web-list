# _*_ coding: utf-8 _*_
from flask import render_template, redirect, request
from . import main

ENGINES = [
    {'name_zh_cn': u'百度', 'url': 'https://www.baidu.com/s', 'name_en': 'Baidu', 'key': 'wd'},
    {'name_zh_cn': u'搜狗', 'url': 'https://www.sogou.com/web', 'name_en': 'Sougou', 'key': 'query'},
    {'name_zh_cn': u'必应', 'url': 'https://cn.bing.com/search', 'name_en': 'Bing', 'key': 'q'},
]


@main.route('/')
def engines():
    return render_template('index.html', engines=ENGINES)


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
    return render_template('search.html', links=links, engines=ENGINES, selects=engines, keyword=keyword, width=width)
