"""
漏洞模块配置
添加新漏洞时，在此注册模块信息
"""

# 已注册的漏洞模块
VULN_MODULES = []

# 统计信息
STATS = [
    {'count': 3, 'label': 'XSS漏洞场景'},
    {'count': 0, 'label': 'SQL注入场景'},
    {'count': 0, 'label': '文件上传场景'},
    {'count': 0, 'label': '其他漏洞'},
]

# 漏洞分类（用于主页展示）
CATEGORIES = [
    {
        'name': 'XSS 跨站脚本攻击',
        'icon': '💉',
        'description': '跨站脚本攻击是最常见的Web漏洞之一。攻击者通过注入恶意脚本，可以窃取用户Cookie、劫持会话、钓鱼攻击等。',
        'scenarios': '反射型XSS、存储型XSS、DOM型XSS',
        'url': '/xss',
        'available': True,
    },
    {
        'name': 'SQL 注入攻击',
        'icon': '🗄️',
        'description': 'SQL注入是通过将恶意SQL代码插入查询语句，从而操纵数据库的攻击方式。可导致数据泄露、权限提升等。',
        'scenarios': '联合查询、布尔盲注、时间盲注',
        'url': '/sqli',
        'available': False,
    },
    {
        'name': '文件上传漏洞',
        'icon': '📁',
        'description': '文件上传漏洞允许攻击者上传恶意文件到服务器，可能导致远程代码执行、服务器被控制等严重后果。',
        'scenarios': '绕过前端验证、MIME类型绕过、文件头绕过',
        'url': '/upload',
        'available': False,
    },
    {
        'name': 'CSRF 跨站请求伪造',
        'icon': '🔓',
        'description': 'CSRF攻击利用用户已登录的身份，诱使用户执行非预期的操作，如转账、修改密码等。',
        'scenarios': 'GET型CSRF、POST型CSRF、Token绕过',
        'url': '/csrf',
        'available': False,
    },
]


def register_module(module_info):
    """注册漏洞模块"""
    VULN_MODULES.append(module_info)
    # 更新分类中的可用状态
    for cat in CATEGORIES:
        if cat['url'] == module_info.get('url'):
            cat['available'] = True
            break


def update_stats():
    """更新统计信息"""
    # 可根据已注册模块动态更新
    pass
