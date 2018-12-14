"""
python3 setup.py install 安装写好的框架
"""

from os.path import dirname, join
# from pip.req import parse_requirements

from setuptools import (
    find_packages,
    setup,
)


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

# 打开/VERSION.txt文件,读取内容,去除两端空白符,赋值给version
# 用于读取当前框架版本号
with open(join(dirname(__file__), './VERSION.txt'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
    name='scrapy-plus',  # 模块名称
    version=version,  # 当前框架版本号
    description='A mini spider framework, like Scrapy',  # 描述
    packages=find_packages(exclude=['test','chajian','day08_guoke','day08_itcast','day08_tencent','day09_suning','day09_travel','day10_CrawlSpider_douban','day10_CrawlSpider_tencent','day10_dynamic_jingdong_food','day10_learn_middliware','day10_load_github','day11_example-project','day11_jd_book','day12_dangdang_book','day12_example-project']),
    author='itcast',
    author_email='your@email.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='#',
    install_requires=parse_requirements("requirements.txt"),  # 所需的运行环境
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)