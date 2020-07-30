学习笔记

创建Django项目
django-admin startproject MyDjango

MyDjango
├── manage.py                   命令行工具
└── MyDjango
    ├── __init__.py
    ├── settings.py             项目配置
    ├── urls.py
    └── wsgi.py

python manage.py help           查看该工具具体功能

创建Django应用程序
python manage.py startapp index

MyDjango
├── index
│   ├── admin.py                管理后台
│   ├── apps.py                 当前app配置文件
│   ├── __init__.py
│   ├── migrations              数据库迁移文件夹
│   │   └── __init__.py
│   ├── models.py               模型
│   ├── tests.py                自动化测试
│   └── views.py                视图
├── manage.py
└── MyDjango
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-37.pyc
    │   └── settings.cpython-37.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py


