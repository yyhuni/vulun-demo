"""
Web Security Vulnerability Lab
Modular architecture for easy extension
"""
import os
from flask import Flask, render_template, Response

from config import Config
from vulns.config import CATEGORIES, STATS
from vulns.xss import xss_bp
from vulns.sensitive import sensitive_bp
from vulns.sensitive.files import get_sensitive_file


def create_app():
    """应用工厂函数"""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register vulnerability blueprints
    app.register_blueprint(xss_bp)
    app.register_blueprint(sensitive_bp)
    
    @app.route('/')
    def home():
        return render_template('home.html', categories=CATEGORIES, stats=STATS)
    
    # 敏感文件访问路由
    @app.route('/<path:filepath>')
    def sensitive_file(filepath):
        """处理敏感文件访问"""
        content = get_sensitive_file(filepath)
        if content:
            return Response(content, mimetype='text/plain')
        return 'Not Found', 404
    
    return app


app = create_app()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    host = os.environ.get('HOST', '0.0.0.0')
    
    print("=" * 50)
    print("Web Security Vulnerability Lab Started!")
    print(f"URL: http://127.0.0.1:{port}")
    print("=" * 50)
    print("\nLoaded modules:")
    print("  - XSS (/xss)")
    print("  - Sensitive Directory (/sensitive)")
    print("")
    app.run(debug=True, host=host, port=port)
