"""
敏感目录暴露漏洞模块
演示常见的敏感目录和文件暴露问题
"""
from flask import Blueprint

sensitive_bp = Blueprint('sensitive', __name__, url_prefix='/sensitive')

# 导入路由
from . import routes  # noqa: F401, E402

# 模块信息
MODULE_INFO = {
    'name': '敏感目录暴露',
    'icon': '📁',
    'description': '敏感目录和文件暴露是常见的信息泄露漏洞。攻击者可以通过访问未受保护的目录获取源代码、配置文件、备份文件等敏感信息。',
    'scenarios': '目录遍历、备份文件泄露、配置文件泄露',
    'url': '/sensitive',
    'available': True,
    'count': 3,
}

__all__ = ['sensitive_bp', 'MODULE_INFO']
