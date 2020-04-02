## 特性
- **构建**: 前后端分离架构，Python+Django+restframework提供后台API，celery定制数据采集策略，Iview作为前端展示
- **UI**: 开箱即用的高质量前端设计，提供丰富的图表、指标展示，核心数据形成趋势图分析
- **深度定制**: 提供完整可用的数据监控方案，告别冗长的SQL脚本、常用手册，复杂数据通过web页面即可轻易浏览

## 功能简介

- 资源管理
    - 支持资源情况录入，涵盖大部分日常所需信息，形成完整资产库
    - 资源管理中各类设备信息作为采集设备来源，支持动态加入实例监控列表
    
...待补

## 环境

- Python 3.6
    - Django 2.2
    - Django Rest Framework 3.1
    
- Vue.js 2.9
    - iview 3.4
  
用户名：admin 
密码：111111

## 安装部署
#### 1. 安装python3.6(略)

#### 2. 安装mysql5.7(略)

注意字符集：utf-8

create database db_monitor; 

#### 3. 安装redis3.2(略)

#### 4. 安装oracle instant client(略)

#### 5. 项目配置

##### 下载源代码
git clone https://github.com/gumengkai/db_monitor

##### 安装依赖包
pip install -r requirements.txt

##### setting配置
MySQL数据库：

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
		'NAME': 'db_monitor',  
		'USER': 'root',  
		'PASSWORD': 'mysqld',  
        'HOST':'127.0.0.1',  
		'PORT': '3306',  
    }
}

Redis：

CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

CELERY_BROKER_URL = 'redis://localhost:6379/2'

##### 创建数据库
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser(创建登录用户)

##### 执行数据库脚本

@install/initdata.sql

#### 6. 启动
python manage.py runserver

celery –A db_monitor worker –l info

celery –A db_monitor beat –l info

#### 7. 前端配置
请参考：[db_monitor_vue](https://github.com/gumengkai/db_monitor_vue)

grant.sql & table.sql & procedure.sql

