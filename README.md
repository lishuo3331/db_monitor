## 功能简介

- 资源管理
    - 支持资源情况录入，涵盖大部分日常所需信息，形成完整资产库
    - 资源管理中各类设备信息作为采集设备来源，支持动态加入实例监控列表
    
...待补充

## 环境

- Python 3.6
    - Django 2.2
    - Django Rest Framework 3.1
    
- Vue.js 2.9
    - iview 3.4

## 安装部署
#### 安装python3.6(略)

#### 安装mysql5.7(略)

注意字符集：utf-8

create database db_monitor; 

#### 项目配置

##### 下载源代码
git clone https://github.com/lishuo3331/db_monitor

##### 安装依赖包
pip install -r requirements.txt

##### settings配置
MySQL数据库：

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
		'NAME': 'db_monitor',  
		'USER': 'root',  
		'PASSWORD': '123456',  
        'HOST':'127.0.0.1',  
		'PORT': '3306',  
    }
}

发送邮件配置：

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #一般不需要修改

EMAIL_HOST = 'smtp.163.com'

EMAIL_PORT = 25

EMAIL_HOST_USER = '*********'    # 邮箱登录名，如11111111111@163.com

EMAIL_HOST_PASSWORD = '*********'   #此处为客户端授权码，不是邮箱密码，需要在邮箱服务商设置

EMAIL_TO_USER = ['1782365880@qq.com','gumengkai@hotmail.com'] # 发送邮件列表,参考格式设置


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
请参考：[db_monitor_vue](https://github.com/lishuo3331/db_monitor_vue)

原始链接：https://github.com/gumengkai/db_monitor


