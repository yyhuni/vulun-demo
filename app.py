"""
Web Security Vulnerability Lab
Modular architecture for easy extension
"""
import os
from flask import Flask, render_template

from config import Config
from vulns.config import CATEGORIES, STATS
from vulns.xss import xss_bp


def create_app():
    """应用工厂函数"""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register vulnerability blueprints
    app.register_blueprint(xss_bp)
    
    @app.route('/')
    def home():
        return render_template('home.html', categories=CATEGORIES, stats=STATS)
    
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
    print("")
    app.run(debug=True, host=host, port=port)
