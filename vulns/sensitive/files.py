"""
敏感文件模拟数据
"""

# 模拟的敏感文件内容
SENSITIVE_FILES = {
    '.env': '''FLASK_ENV=production
SECRET_KEY=sk-1234567890abcdefghijklmnopqrstuvwxyz
DATABASE_URL=mysql://admin:password123@db.example.com:3306/app_db
STRIPE_API_KEY=sk_live_PLACEHOLDER_EXAMPLE_KEY_12345
GITHUB_TOKEN=ghp_1234567890abcdefghijklmnopqrstuvwxyz
''',
    'config.php.bak': '''<?php
define('DB_USER', 'admin');
define('DB_PASSWORD', 'password123');
define('ADMIN_PASS', 'admin@123456');
define('JWT_SECRET', 'jwt_secret_key_12345');
?>''',
    'database.sql.bak': '''INSERT INTO users VALUES 
(1, 'admin', 'admin@example.com', '$2b$12$hash', 'sk_admin_12345'),
(2, 'user1', 'user1@example.com', '$2b$12$hash', 'sk_user1_12345');''',
    'app.py.bak': '''SECRET_API_KEY = 'sk_live_PLACEHOLDER_EXAMPLE_KEY_12345'
ADMIN_PASSWORD = 'admin@123456'
DATABASE_PASSWORD = 'password123'
DB_CONNECTION = 'mysql://admin:password123@db.example.com:3306/app_db'
''',
    '.git/config': '''[remote "origin"]
url = https://github.com/admin:ghp_1234567890abcdefghijklmnopqrstuvwxyz@github.com/company/app.git
[user]
name = Developer
email = dev@example.com
''',
    'README_BACKUP.txt': '''管理员账户:
用户名: admin
密码: admin@123456
API密钥: sk_live_PLACEHOLDER_EXAMPLE_KEY_12345

数据库连接:
主机: db.example.com
用户: admin
密码: password123
''',
    '.env.bak': '''# 备份的环境配置文件
FLASK_ENV=production
SECRET_KEY=sk-backup-abcdef123456
DATABASE_URL=mysql://backup:backup123@db-backup.example.com:3306/app_db_backup
''',
}


def get_sensitive_file(filename):
    """获取敏感文件内容"""
    return SENSITIVE_FILES.get(filename)


def get_all_files():
    """获取所有敏感文件列表"""
    return list(SENSITIVE_FILES.keys())
