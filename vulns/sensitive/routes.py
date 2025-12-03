"""
敏感目录暴露模块路由处理
"""
from flask import render_template, send_file, abort
from io import BytesIO
from . import sensitive_bp


@sensitive_bp.route('/')
def index():
    """敏感目录靶场首页"""
    return render_template('sensitive_index.html')


@sensitive_bp.route('/directory')
def directory_listing():
    """目录遍历演示"""
    directories = [
        {
            'name': '.git',
            'description': 'Git 版本控制目录',
            'risk': '高',
            'content': '包含完整的项目历史、提交记录、分支信息等'
        },
        {
            'name': '.env',
            'description': '环境变量配置文件',
            'risk': '严重',
            'content': '数据库密码、API密钥、密钥等敏感信息'
        },
        {
            'name': 'config/',
            'description': '配置文件目录',
            'risk': '高',
            'content': '数据库连接字符串、第三方服务密钥'
        },
        {
            'name': 'admin/',
            'description': '后台管理目录',
            'risk': '高',
            'content': '未授权访问管理界面'
        },
    ]
    return render_template('sensitive_directory.html', directories=directories)


@sensitive_bp.route('/backup')
def backup_files():
    """备份文件泄露演示"""
    backups = [
        {
            'filename': 'database.sql.bak',
            'description': '数据库备份文件',
            'risk': '严重',
            'content': '完整的数据库数据，包括用户信息、密码哈希等'
        },
        {
            'filename': 'config.php.bak',
            'description': 'PHP 配置备份',
            'risk': '高',
            'content': '数据库连接信息、密钥配置'
        },
        {
            'filename': 'app.tar.gz',
            'description': '应用源代码压缩包',
            'risk': '高',
            'content': '完整的源代码，可能包含硬编码的密钥'
        },
        {
            'filename': '.DS_Store',
            'description': 'macOS 目录信息文件',
            'risk': '中',
            'content': '目录结构和文件名信息'
        },
    ]
    return render_template('sensitive_backup.html', backups=backups)


@sensitive_bp.route('/source')
def source_code():
    """源代码泄露演示"""
    files = [
        {
            'filename': 'app.py',
            'description': 'Flask 应用主文件',
            'risk': '高',
            'content': '应用逻辑、数据库查询、业务规则',
            'url': '/sensitive/download/app.py'
        },
        {
            'filename': 'database.py',
            'description': '数据库配置文件',
            'risk': '严重',
            'content': '数据库连接字符串、用户名密码',
            'url': '/sensitive/download/database.py'
        },
        {
            'filename': 'secret_key.txt',
            'description': '应用密钥文件',
            'risk': '严重',
            'content': 'Flask SECRET_KEY、JWT 密钥等',
            'url': '/sensitive/download/secret_key.txt'
        },
        {
            'filename': 'utils/crypto.py',
            'description': '加密工具文件',
            'risk': '中',
            'content': '加密算法实现、密钥管理逻辑',
            'url': '/sensitive/download/crypto.py'
        },
    ]
    return render_template('sensitive_source.html', files=files)


# ============ 敏感文件下载 ============

SENSITIVE_FILES = {
    '.env': '''# Flask 环境配置
FLASK_ENV=production
FLASK_DEBUG=0
SECRET_KEY=sk-1234567890abcdefghijklmnopqrstuvwxyz

# 数据库配置
DATABASE_URL=mysql://admin:password123@db.example.com:3306/app_db
DB_USER=admin
DB_PASSWORD=P@ssw0rd!2024

# API 密钥
STRIPE_API_KEY=sk_live_PLACEHOLDER_EXAMPLE_KEY_12345
GITHUB_TOKEN=ghp_1234567890abcdefghijklmnopqrstuvwxyz
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

# 邮件配置
MAIL_SERVER=smtp.gmail.com
MAIL_USERNAME=admin@example.com
MAIL_PASSWORD=gmailpassword123

# JWT 密钥
JWT_SECRET=jwt_secret_key_12345678901234567890
''',
    'app.py': '''from flask import Flask, render_template
from config import Config
from vulns.xss import xss_bp
from vulns.sensitive import sensitive_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(xss_bp)
    app.register_blueprint(sensitive_bp)
    
    @app.route('/')
    def home():
        return render_template('home.html')
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
''',
    'database.py': '''import os
from sqlalchemy import create_engine

# 数据库连接配置
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_USER = os.environ.get('DB_USER', 'admin')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password123')
DB_NAME = os.environ.get('DB_NAME', 'app_db')

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"

engine = create_engine(DATABASE_URL)

# 硬编码的备用密码
BACKUP_DB_PASSWORD = "backup_db_password_2024"
ADMIN_API_KEY = "admin_api_key_secret_12345"
''',
    'secret_key.txt': '''# Flask 应用密钥
SECRET_KEY=sk-prod-1234567890abcdefghijklmnopqrstuvwxyz

# JWT 密钥
JWT_SECRET_KEY=jwt-secret-key-production-12345

# 加密密钥
ENCRYPTION_KEY=encryption-key-base64-encoded-12345

# API 密钥
INTERNAL_API_KEY=internal-api-key-12345
ADMIN_TOKEN=admin-token-12345
''',
    'crypto.py': '''import hashlib
import hmac
from cryptography.fernet import Fernet

# 硬编码的加密密钥（非常危险！）
ENCRYPTION_KEY = b'hardcoded_key_12345678901234567890'
cipher = Fernet(ENCRYPTION_KEY)

def encrypt_password(password):
    """加密密码"""
    return cipher.encrypt(password.encode()).decode()

def verify_password(password, hashed):
    """验证密码"""
    return cipher.decrypt(hashed.encode()).decode() == password

# 内部 API 密钥
INTERNAL_API_KEYS = {
    'service_a': 'key_service_a_12345',
    'service_b': 'key_service_b_12345',
    'admin': 'admin_key_12345'
}
''',
}


@sensitive_bp.route('/download/<filename>')
def download_file(filename):
    """下载敏感文件"""
    if filename not in SENSITIVE_FILES:
        abort(404)
    
    content = SENSITIVE_FILES[filename]
    return send_file(
        BytesIO(content.encode('utf-8')),
        mimetype='text/plain',
        as_attachment=True,
        download_name=filename
    )
