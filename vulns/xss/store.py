"""
XSS 模块数据存储
"""

# 存储型XSS数据（内存存储，仅用于演示）
_messages = []


def get_messages():
    """获取所有留言"""
    return _messages


def add_message(author, content):
    """添加留言"""
    _messages.append({'author': author, 'content': content})


def clear_all_messages():
    """清空所有留言"""
    _messages.clear()
