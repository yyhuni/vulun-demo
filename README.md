# Web安全漏洞靶场

模块化漏洞靶场，方便扩展新漏洞类型。

## 快速启动

### 1. 创建虚拟环境
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 运行应用
```bash
python3 app.py

# 指定端口启动
PORT=8900 python app.py

```

访问 http://localhost:80

### 环境变量配置
复制 `.env.example` 为 `.env` 并修改配置：
```bash
cp .env.example .env
```

## 项目结构

```
vulun-demo-1/
├── app.py                  # Flask 应用入口
├── config.py               # 应用配置
├── wsgi.py                 # WSGI 入口（生产部署）
├── requirements.txt        # 依赖列表
├── pyproject.toml          # 项目元数据
├── .env.example            # 环境变量示例
├── .gitignore              # Git 忽略规则
├── README.md               # 项目说明
├── static/                 # 静态资源目录
├── templates/              # Jinja2 模板
│   ├── base.html           # 基础模板
│   └── home.html           # 主页模板
├── vulns/                  # 漏洞模块包
│   ├── __init__.py         # 包初始化
│   ├── config.py           # 漏洞配置
│   └── xss/                # XSS 漏洞模块
│       └── __init__.py
└── tests/                  # 测试目录
    ├── __init__.py
    └── test_app.py
```

## 添加新漏洞模块

### 1. 创建模块目录

```bash
mkdir vulns/sqli
touch vulns/sqli/__init__.py
```

### 2. 编写模块代码 (vulns/sqli/__init__.py)

```python
from flask import Blueprint, request, render_template_string

sqli_bp = Blueprint('sqli', __name__, url_prefix='/sqli')

# 模板和路由...

@sqli_bp.route('/')
def index():
    return render_template_string(INDEX_HTML)

# 更多路由...
```

### 3. 注册蓝图 (app.py)

```python
from vulns.sqli import sqli_bp
app.register_blueprint(sqli_bp)
```

### 4. 更新配置 (vulns/config.py)

在 `CATEGORIES` 中将对应模块的 `available` 改为 `True`，更新 `STATS` 统计数据。

## 已有模块

- **XSS** (`/xss`) - 反射型、存储型、DOM型XSS
