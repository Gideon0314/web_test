# -*- coding: UTF-8 -*-
import os
import yaml
from tools.times import timestamp
from config.config import ELEMENT_PATH, LOCATE_MODE


def inspect_element():
    """审查所有的元素是否正确"""
    start_time = timestamp()
    for i in os.listdir(ELEMENT_PATH):
        _path = os.path.join(ELEMENT_PATH, i)
        if os.path.isfile(_path):
            with open(_path, encoding='utf-8') as f:
                data = yaml.safe_load(f)
                for k in data.values():
                    pattern, value = k.split('==')
                    if pattern not in LOCATE_MODE:
                        raise AttributeError('【%s】路径中【%s]元素没有指定类型' % (i, k))
                    if pattern == 'xpath':
                        assert '//' in value, '【%s】路径中【%s]元素xpath类型与值不配' % (
                            i, k)
                    if pattern == 'css':
                        assert '//' not in value, '【%s】路径中【%s]元素css类型与值不配' % (
                            i, k)
                    if pattern in ('id', 'name', 'class'):
                        assert value, '【%s】路径中【%s]元素类型与值不匹配' % (i, k)
    end_time = timestamp()
    print("校验元素结束！用时%.3f秒！" % (end_time - start_time))


if __name__ == '__main__':
    inspect_element()
