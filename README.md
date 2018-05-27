# Django-starter

Django项目起始配置，根据平时项目经验配置，目前需要自定义的操作比较繁琐，需要修改一堆配置文件，内心是想做一个Web配置页面，可以带来更强的自定义，让django快速配置。

### TODO 
+ 类似[Spring Start](start.spring.io)页面


### Django配置主目录

- neptune/

### Django配置子目录(neptune/conf)
- secret(安全配置)
- base(基础配置)
- debug(开发配置)
- database(数据库配置)
- log(日志配置)
- static(静态文件配置)
- api(API配置)
- customer(自定义配置)
- email(邮件配置)
- celery(异步任务/分布式任务配置)


### Web服务器启动
- [Web Server](http://localhost:8000)
```
Python manage.py runserver 0.0.0.0:8000
```
- [Web Admin](http://localhost:8000/admin)

- [Web API](http://127.0.0.1:8000/api_v1/auth/)

### Celery启动
- Work
```
python manange.py celery worker --loglevel=info
```
- Beat
```
python manange.py celery beat
```

### 日志收集
- 使用[Sentry](https://sentry.io/welcome/)
- 需要配置Sentry DSN