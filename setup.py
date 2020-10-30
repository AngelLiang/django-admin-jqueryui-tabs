from os import path
from codecs import open
from setuptools import setup

basedir = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(basedir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-admin-jqueryui-tabs',  # 包名称
    version='0.1.1',  # 版本
    url='https://github.com/AngelLiang/django-admin-jqueryui-tabs',
    license='MIT',
    author='AngelLiang',
    author_email='yannanxiu@126.com',
    description='A plug-in that modifies django admin form fieldset style to jqueryui tabs',
    long_description=long_description,
    long_description_content_type='text/markdown',  # 长描述内容类型
    platforms='any',
    packages=['django_admin_jqueryui_tabs'],  # 包含的包列表
    zip_safe=False,
    include_package_data=True,
    install_requires=[
    ],
    keywords='django jquery jqueryui tabs',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
