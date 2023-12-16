# Django购物平台

基于`python3.9.5`和`Django4.2.8`的购物平台。

 Django是python的Web后端框架   

## 知识运用：

- 使用Mysql数据库连接后端
- 使用了WebAPI RESTfulAPI规范来写API
- 集成后台管理系统admin
- 创建API有产品，购物车，订单，系列，用户
- 创建了Token令牌
- 设置了用户权限，用户只能访问自己的购物车和订单，只有管理员才能查看所有订单
- 购物车的API有时实更新，重写了该序列化器和视图函数
- 在创建订单时把该购物车里面的产品全部放进订单中，然后会自动删除购物车
- 购物车和订单使用了uuid4来加强购物车和订单的URL安全性
- 后台管理系统可以去创建用户，更改用户权限，添加产品等等


## 缺点
只做到了API相关事情

后面的部署，自动化测试的都还没有做



## 运用的软件

VSCode

DataGrip(数据库)

GitKraken(记录历史代码)





## 前提

**需要用到VScode软件**

1.先配置数据库在settings.py文件中配置

```django
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '123456'
    }
}
```

2.下载pipenv(Python包管理器)

```
pip install pipenv
```

3.下载该项目的依赖包

```
pipenv install
```

4.迁移模型到数据库

```
python manage.py migrate
```

5.下载虚拟数据seed.sql文件

6.运行服务器

```
python manage.py runserver
```

7.需要创建超级用户

```
python manage.py createsuperuser
```



## 运行

运行服务器

```
python manage.py runserver
```



查看后台管理系统(Django)

```
#URL
http://127.0.0.1:8000/admin/
```

登录后台管理系统 可以管理后台数据



创建用户

```
http://127.0.0.1:8000/auth/users/
```



获得Token

```
http://127.0.0.1:8000/auth/jwt/create
```



查看store后面的所有API

```
http://127.0.0.1:8000/store/
```



查看产品API

```
http://127.0.0.1:8000/store/products/
```

里面可以进行过滤,排序，查询，操作

但是只有管理员才有创建和删除产品的权限

订单也是相似



