"""
需求: 模版中要遍历字典(dict)，但想要获取value(数组)，还需要再次遍历时，常规操作是不行的

解决: 添加以下自定义过滤器即可
"""

from django import template
register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)