"""
XSS 漏洞模块路由处理
"""
from flask import request, render_template
from . import xss_bp
from .store import get_messages, add_message, clear_all_messages


@xss_bp.route('/')
def index():
    """XSS 靶场首页"""
    return render_template('xss_index.html')


@xss_bp.route('/reflected')
def reflected():
    """反射型 XSS 测试"""
    name = request.args.get('name', '')
    return render_template('xss_reflected.html', name=name)


@xss_bp.route('/stored', methods=['GET', 'POST'])
def stored():
    """存储型 XSS 测试"""
    if request.method == 'POST':
        author = request.form.get('author', '')
        content = request.form.get('content', '')
        if author and content:
            add_message(author, content)
    return render_template('xss_stored.html', messages=get_messages())


@xss_bp.route('/stored/clear', methods=['POST'])
def clear_messages():
    """清空存储的留言"""
    clear_all_messages()
    return render_template('xss_stored.html', messages=get_messages())


@xss_bp.route('/dom')
def dom():
    """DOM型 XSS 测试"""
    return render_template('xss_dom.html')
