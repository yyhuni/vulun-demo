"""
应用基础测试
"""
import pytest
from app import create_app


@pytest.fixture
def app():
    """创建应用实例用于测试"""
    app = create_app()
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    """创建测试客户端"""
    return app.test_client()


def test_home_page(client):
    """测试主页"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Web' in response.data


def test_xss_index(client):
    """测试XSS模块首页"""
    response = client.get('/xss/')
    assert response.status_code == 200
