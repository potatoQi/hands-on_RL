# 这个文件存在的目的, 是为了执行pip install -e .时, 可以将 hands_on_RL 变为包
from setuptools import setup

setup(
    name='hands-on_RL', # 包名
    version='0.1.0',    # 版本号
    packages=['infrastructure', 'policies'],    # 包含的子包
)