利用django写的一个简单的值班表，以及服务器管理 <br>
因为不懂前端，所以值班表展示页面很简单，实现功能，后面的看我心情吧 <br>

# 后台管理页面：

![image](https://github.com/banqinghong/watchman/blob/master/docs/1.png)

# 站点页面：

![image](https://github.com/banqinghong/watchman/blob/master/docs/2.png)

# 值班表页面：

![image](https://github.com/banqinghong/watchman/blob/master/docs/3.png)

# 部署注意：
1.修改settings.py中的ALLOWED_HOSTS以及DATABASES <br>
2.进入项目目录，初始化数据库 <br>
    python manage.py makemigrations <br>
    python manage.py migrate <br>
3.创建超级用户<br>
    python manage.py createsuperuser <br>
4.修改base.html <br />
    将django\contrib\admin\templates\admin中的base.html替换为templates\static\base.html文件 <br>
5.启动项目 <br>
    python manage.py runserver YOUR_IP:YOUR_PORT  <br>