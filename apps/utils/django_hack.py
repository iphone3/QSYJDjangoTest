"""
需求: 模板中需要将 {'颜色': ['梦境紫'], '度数': ['100', '125']} 将对应的数组显示到一个位置中

解决: 自定义过滤器来处理
"""
from django import template

register = template.Library()

@register.filter()
def hash(h, key):
    if key in h:
        return h[key]
    else:
        return None