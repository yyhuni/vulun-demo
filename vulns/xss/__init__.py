"""
XSS 漏洞模块
包含反射型、存储型、DOM型三种XSS漏洞场景
"""
from flask import Blueprint

xss_bp = Blueprint('xss', __name__, url_prefix='/xss')

# 导入路由（必须在蓝图创建后导入，避免循环导入）
from . import routes  # noqa: F401, E402

# 模块信息
MODULE_INFO = {
    'name': 'XSS 跨站脚本攻击',
    'icon': '💉',
    'description': '跨站脚本攻击是最常见的Web漏洞之一。攻击者通过注入恶意脚本，可以窃取用户Cookie、劫持会话、钓鱼攻击等。',
    'scenarios': '反射型XSS、存储型XSS、DOM型XSS',
    'url': '/xss',
    'available': True,
    'count': 3,
}

__all__ = ['xss_bp', 'MODULE_INFO']
