# centos7系统

## 创建新用户并授权

### 创建新用户

* 创建用户

  ``` bash
  [root@localhost ~]# adduser oychao
  ```

* 设置用户初始密码

  ``` bash
  [root@localhost ~]# passwd oychao
  ```

### 授权

* 查找sudoers

  ```bash
  [root@localhost ~]# whereis sudoers
  sudoers: /etc/sudoers /etc/sudoers.d ..
  [root@localhost ~]# ls -l /etc/sudoers
  -r--r----- 1 root root 4251 9月  25 15:08 /etc/sudoers
  ```

* 给sudoers添加w权限

  ``` bash
  [root@localhost ~]# chmod -v u+w /etc/sudoers
  mode of "/etc/sudoers" changed from 0440 (r--r-----) to 0640 (rw-r-----)
  ```

* 进入suduers新增用户

  ``` bash
  [root@localhost ~]# vim /etc/sudoers
  ...
  ## Allow root to run any commands anywher  
  root    ALL=(ALL)       ALL  
  oychao  ALL=(ALL)       ALL  #这个是新增的用户
  ```

* 保存退出，并收回w权限

  ``` bash
  [root@localhost ~]# chmod -v u-w /etc/sudoers
  mode of "/etc/sudoers" changed from 0640 (rw-r-----) to 0440 (r--r-----)
  ```

## 生产环境配置

### 安装docker

#### 安装步骤

* 查看你当前的内核版本

  Docker 要求 CentOS 系统的内核版本高于 3.10 

  ``` bash
  $ uname -r
  ```

* yum 包更新到最新

  ``` bash
  $ sudo yum update
  ```

* 卸载旧版本(如果安装过旧版本的话)

  ``` bash
  $ sudo yum remove docker  docker-common docker-selinux docker-engine
  ```

* 安装需要的软件包

  ``` bash
  $ sudo yum install -y yum-utils device-mapper-persistent-data lvm2
  ```

* 设置yum源

  ``` bash
  $ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
  ```

* 查看所有仓库中所有docker版本，并选择特定版本安装

  ``` bash
  $ yum list docker-ce --showduplicates | sort -r
  ```

* 安装docker

  ``` bash
  $ sudo yum install docker-ce-18.03.1.ce-1.el7.centos
  ```

* 启动并加入开机启动

  ``` bash
  $ sudo systemctl start docker
  $ sudo systemctl enable docker
  ```

* 验证安装是否成功

  ``` bash
  $ docker version
  ```

* 设置用户的docker权限，免输sudo

  ``` bash
  sudo usermod -a -G docker $USER
  ```

#### 拉取相关镜像

##### mysql

###### 安装与启动

* 拉取mysql镜像

  ``` bash
  $ sudo docker pull mysql:8.0
  ```

* 启动容器

  ``` bash
  docker run -p 3306:3306 --name mySiteSQL -v $(pwd)/conf:/etc/mysql/conf.d -v $(pwd)/data:/var/lib/mysql -v $(pwd)/logs:/logs -e MYSQL_ROOT_PASSWORD=mysql -d mysql:8.0
  ```

  参数说明

  * -p 3306:3306 端口映射
  * --name mySiteSQL 容器名称
  * -v $(pwd)/conf:/etc/mysql/conf.d 将主机当前目录下的 conf/my.cnf 挂载到容器的 /etc/mysql/my.cnf
  * -v $(pwd)/data:/var/lib/mysql 将主机当前目录下的data目录挂载到容器的 /var/lib/mysql
  * -v $(pwd)/logs:/logs 将主机当前目录下的 logs 目录挂载到容器的 /logs
  * -e MYSQL_ROOT_PASSWORD=mysql 初始化 root 用户的密码
  * -d 后台运行容器，并返回容器ID

###### 常见问题


##### redis

``` bash
sudo docker pull redis:3.2
```

##### mongodb

* 拉取mongo镜像

  ``` bash
  docker pull mongo
  ```

* 启动需要权限认证的容器

  ``` bash
  docker run --name myMongoDB -p 27017:27017 -v $PWD/db:/data/db -d mongo --auth
  ```

  参数说明：

  * --name myMongoDB 容器名称
  * -p 27017:27017 端口映射
  * -v $PWD/db:/data/db 将主机中当前目录下的db挂载到容器的/data/db，作为mongo数据存储目录
  * -d 后台运行容器，并返回容器ID
  * --auth 开启权限认证

* 创建管理员

  * 创建admin用户

    ``` bash
    # 进入容器
    docker exec -it myMongoDB /bin/bash
    # 进入mongo数据库
    mongo
    # 使用admin数据库
    use admin
    # 创建管理员账户
    db.createUser({ user: "admin", pwd: "Oychao@1988", roles: [{ role: "userAdminAnyDatabase", db: "admin" }] })
    # 验证是否添加成功
    db.auth("admin", "Oychao@1988") 
    ```

    参数说明：

    * user 用户名
    * pwd 用户密码
    * roles 身份
    * userAdminAnyDatabase 
      * userAdmin代表用户管理身份
      * AnyDatabase代表可以管理任何数据库。

  * 使用admin用户创建其他数据库管理员账户

    ``` bash
    use admin
    db.auth("admin", "Oychao@1988")
    use scrapydb
    # 创建所有者用户
    db.createUser({user:'oychao',pwd:'Oychao1988',roles:[{role:'dbOwner', db:'scrapydb'}]})
    # 验证用户
    db.auth('oychao', 'Oychao1988')
    ```

    参数说明：

    * dbOwner 代表数据库所有者角色，拥有最高该数据库最高权限

  * 创建读写账户

    ``` bash
    # 登录数据库
    mongo scrapydb -u oychao -pOychao@1988
    # 创建读写用户
    db.createUser({user:'cino',pwd:'cino',roles:[{role:'readWrite', db:'scrapydb'}]})
    ```

    参数说明 ：

    - readWrite 允许用户读写指定数据库

  * 容器中验证登录

    ``` bash
    # 进入容器
    docker exec -it myMongoDB /bin/bash
    # 登录scrapydb
    mongo scrapydb -u cino -p cino
    # 登录验证
    db.auth("cino", "cino")
    ```

  * 修改用户密码

    ``` mongo
    # 需要先验证原用户密码
    db.changeUserPassword('oychao','Oychao1988');
    ```


##### elasticsearch

##### FastDFS

#### 其他操作

* 查看日志

  ``` bash
  docker logs 容器ID
  ```

### 安装mysql

#### 安装步骤

* 卸载mariadb

  ``` bash
  # 列出所有被安装的mariadb rpm包
  rpm -qa | grep mariadb
  # 逐个将所有列出的mariadb rpm包给卸载掉
  sudo rpm -e --nodeps mariadb-libs-5.5.60-1.el7_5.x86_64
  ```

* 添加源

  ``` bash
  # 下载
  wget https://dev.mysql.com/get/mysql80-community-release-el7-1.noarch.rpm
  # 本地安装
  sudo yum localinstall mysql80-community-release-el7-1.noarch.rpm
  # 验证是否成功
  sudo yum repolist enabled | grep "mysql.*-community.*"
  ```

* 安装

  ``` bash
  # 将希望下载的mysql-community的版本的enabled选项置为1
  vim /etc/yum.repos.d/mysql-community.repo
  # 直接安装
  sudo yum install mysql-community-server
  ```

  安装包下载地址：

  * https://dev.mysql.com/downloads/mysql/

* 启动mysql服务

  ``` bash
  sudo service mysqld start
  # /bin/systemctl start mysqld.service
  ```

  * 查看mysql运行状态

    ``` bash
    service mysqld status
    ```

  * 停止mysql服务

    ``` bash
    sudo service mysqld stop
    ```

* 报错解决

  ``` bash
  ** 发现 2 个已存在的 RPM 数据库问题， 'yum check' 输出如下：
  2:postfix-2.10.1-6.el7.x86_64 有缺少的需求 libmysqlclient.so.18()(64bit)
  2:postfix-2.10.1-6.el7.x86_64 有缺少的需求 libmysqlclient.so.18(libmysqlclient_18)(64bit)
  ```

  ``` bash
  # 查看本机libmysqlclient.so版本
  find / -name libmysqlclient.so*
  # 下载mysql-community-libs-compat兼容
  wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-community-libs-compat-8.0.12-1.el7.x86_64.rpm
  # 安装
  sudo yum localinstall MySQL-8.0/mysql-community-libs-compat-8.0.12-1.el7.x86_64.rpm
  ```

* 重置密码

  ``` bash
  # 查看原始密码
  sudo cat /var/log/mysqld.log | grep password
  # 重置密码
  mysql -u root -p
  ```

  ``` mysql
  ALTER USER 'root'@'localhost' IDENTIFIED BY '8Tony&Cino8';
  ```


#### 卸载步骤

* 查看安装的包

  ``` bash
  rpm -qa |grep -i mysql
  ```

* 卸载所有mysql包

  ``` bash
  sudo yum remove mysql*
  # 查看卸载状态
  rpm -qa |grep -i mysql
  ```

* 清理文件

  ``` bash
  sudo find / -name mysql
  sudo find / -name mysqld
  sudo rm -rf 所有mysql文件
  ```

### 安装redis

### 安装python3.6

#### 安装步骤

* 准备编译环境

  ``` bash
  sudo yum groupinstall 'Development Tools'
  sudo yum install zlib-devel bzip2-devel  openssl-devel ncurses-devel
  ```

* 下载python3.6.5

  ``` bash
  wget --no-check-certificate https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
  ```

* 创建安装目录

  ``` bash
  sudo mkdir /usr/local/python3
  ```

* 解压

  ``` bash
  tar -zxvf Python-3.6.5.tgz
  # 切换到解压后的根目录
  cd Python-3.6.5/
  ```

* 编译安装

  ``` bash
  sudo ./configure --prefix=/usr/local/python3 --enable-optimizations
  sudo make
  sudo make install
  ```

  --enable-optimizations配置项用于提高Python安装后的性能

* 创建Python3链接

  ``` bash
  sudo ln -s /usr/local/python3/bin/python3.6 /usr/bin/python3
  ```

* 创建Pip3链接

  ``` bash
  sudo ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
  # 升级pip3版本
  sudo pip3 install --upgrade pip
  ```

#### 修改系统的默认Python版本

* 查看python的替换版本信息

  ``` bash
  sudo alternatives --list python
  ```

* 更新python的替换列表

  ``` bash
  sudo alternatives --install /usr/bin/python python /usr/bin/python2 1
  sudo alternatives --install /usr/bin/python python /usr/bin/python3 2
  ```

* 查看更新后的python版本

  ``` bash
  python --version
  ```

* 切换默认python版本

  ``` bash
  sudo alternatives --config python
  ```

* 移除替换版本

  ``` bash
  sudo alternatives --remove python /usr/bin/python2
  ```

### 安装虚拟环境

* 安装虚拟环境

  ``` bash
  sudo pip3 install virtualenv
  sudo pip3 install virtualenvwrapper
  ```

* 创建虚拟环境目录

  ``` bash
  sudo mkdir $HOME/.virtualenvs
  ```

* 编辑~/.bashrc文件

  ``` 
  export WORKON_HOME=$HOME/.virtualenvs
  export
  PROJECT_HOME=$HOME/workspace
  VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
  source 
  /usr/bin/virtualenvwrapper.sh
  ```

* 在/usr/bin中添加环境变量

  ``` bash
  sudo ln -s /usr/local/python3/bin/virtualenv /usr/bin/virtualenv
  sudo ln -s /usr/local/python3/bin/virtualenvwrapper.sh /usr/bin/virtualenvwrapper.sh
  ```

* 运行~/.bashrc

  ``` bash
  source ~/.bashrc
  ```

### 安装GIt

* 自带GIt，若需要自己安装

  ``` bash
  sudo yum -y install git
  ```

  注意：需要在python2环境下安装。

### 安装screen

``` bash
sudo yum install screen -y
```

### 安装Nginx

* 安装

  ``` bash
  sudo yum install nginx
  ```

* 启动Nginx

  ``` bash
  sudo systemctl start nginx
  ```

* 跟随系统启动

  ``` bash
  sudo systemctl enable nginx
  ```

## 运行项目

### proxy_pool

* github拉取项目

  ``` bash
  git clone https://github.com/oychao1988/proxy_pool.git 
  ```

* 修改Config.ini配置信息

  ``` 
  vim Config.ini
  # 配置host
  host = 127.0.0.1
  ```

* 创建虚拟环境

  ``` bash
  mkvirtualenv -p python3 ProxyPool
  ```

* 安装依赖包

  ``` bash
  workon ProxyPool
  pip install -r requirements.txt
  ```

* 启动

  ``` bash
  cd Run/
  python main.py
  ```

* nginx部署配置

  ``` 
  $ cd /etc/nginx/nginx.conf
  server {
          listen       5050;
          listen       [::]:5050;
          server_name  ProxyPoolServer;
          # root         /usr/share/nginx/html;
  
          # Load configuration files for the default server block.
          include /etc/nginx/default.d/*.conf;
  
          location / {
              proxy_pass http://127.0.0.1:5010;
              proxy_set_header Host $host;
              proxy_set_header X-Real-IP $remote_addr;
          }
  ```

* 访问地址

  * http://182.61.60.153:5010

### MongoDBDataServer

* github拉取项目

  ``` bash
  git clone https://github.com/oychao1988/MongoBDDataServer.git
  ```

* 创建虚拟环境

  ``` bash
  mkvirtualenv -p python MongoDBDataServer
  ```

* 安装依赖包

  ``` bash
  workon MongoDBDataServer
  pip install -r requirements.txt
  ```

* gunicorn启动

  ``` bash
  gunicorn -w 2 -b 127.0.0.1:5021 manage:app
  ```

* 创建数据库

  ``` js
  # 创建数据库
  use scrapydb
  # 创建用户
  db.createUser({user:'cino',pwd:'cino',roles:[{role:'readWrite', db:'scrapydb'}]})
  # 创建唯一联合索引
  db.fingerPrint.ensureIndex({number:1,source:1}, {unique:true})
  ```

* 数据接口

  * 数据去重

    http://182.61.60.153:5020/recruits/duplicateChecking/<fp>

  * 拉勾招聘

    http://182.61.60.153:5020/recruits/lagou?page=1&per_page=10

### mongoDB可视化工具

- 把git仓库克隆到本地: adminMongo

  ```
  git clone https://github.com/mrvautin/adminMongo
  ```

- 进入仓库

  ```bash
  cd adminMongo
  ```

- 安装node.js

  ``` bash
  sudo curl -sL -o /etc/yum.repos.d/khara-nodejs.repo \ https://copr.fedoraproject.org/coprs/khara/nodejs/repo/epel-7/khara-nodejs-epel-7.repo
  sudo yum install -y nodejs nodejs-npm
  ```

- 安装adminMongo

  ```bash
  npm install
  ```

- 启动

  ```bash
  npm start
  ```

- 访问地址 [http://127.0.0.1:1234](http://127.0.0.1:1234/) 

- 建立数据库链接

  ```
  mongodb://cino:cino@182.61.60.153:27017/scrapydb
  ```

### 新经资讯

* github拉取项目

  ``` bash
  git clone https://github.com/oychao1988/information.git
  ```

* 创建虚拟环境

  ``` bash
  mkvirtualenv -p python3 Information
  ```

* 安装依赖包

  ``` bash
  workon Information
  pip install -r requirements.py
  ```

* 安装时报错：mysqlclient==1.3.13

  ``` bash
  # 报错信息
  Complete output from command python setup.py egg_info:
      ...
  	raise EnvironmentError("%s not found" % (mysql_config.path,))
      OSError: mysql_config not found
  # 解决方法
  sudo yum install mysql-devel
  ```

* 创建数据库

  ``` sql
  mysql -u root -pmysql
  # 创建数据库
  create database Information charset utf8mb4;
  # 创建远程登录用户
  create user 'oychao' identified with mysql_native_password by 'Oychao@1988'
  # 授权用户指定数据库
  grant all on Information.* to 'oychao'@'%';
  # 刷新权限
  flush privileges;
  ```

  ``` mysql
  # 第三方数据库
  Host:39.105.124.116:3306
  Database:Information
  User:oychao
  Password:oychao
  ```

* 修改config.py

  ``` python
  SQLALCHEMY_DATABASE_URI = 'mysql://oychao:8Tony&Cino8@127.0.0.1:3306/information'
  ```

* 修改manage.py

  ``` python
  app = create_app('production')
  ```

* 数据库迁移

  ``` bash
  $ python manage.py db init
  $ python manage.py db migrate -m"initial"
  $ python manage.py db upgrade
  ```

* 远程导入数据

  ``` bash
  $ mysql -h182.61.60.153 -uoychao -p information < information_info_category.sql
  $ mysql -h182.61.60.153 -uoychao -p information < information_info_news.sql
  $ Enter password:8Tony&Cino8
  ```

* 配置Nginx

  ``` bash
  $ sudo vim /etc/nginx/nginx.conf
  ```

  ``` python
  server {
          listen       5500;
          listen       [::]:5500;
          server_name  InformationServer;
          root         /var/www/html;
  
          # Load configuration files for the default server block.
          include /etc/nginx/default.d/*.conf;
          index index.html index.htm index.nginx-debian.html;
          location / {
              proxy_pass http://127.0.0.1:5000;
              proxy_set_header Host $host;
              proxy_set_header X-Real-IP $remote_addr;
          }
  
  ```

  ``` bash
  # 检查nginx.conf配置是否正确
  $ sudo nginx -t
  $ sudo service nginx restart
  ```

* 安装gunicorn

  ``` python
  pip install gunicorn
  ```

* 运行

  ``` python
  gunicorn -w 2 -b 127.0.0.1:5000 manage:app
  ```


### 美多商城

* github拉取项目

  ``` bash
  git clone -b 11_01 https://gitee.com/oytonic/meiduo_mall.git
  ```

* 创建虚拟环境

  ``` bash
  mkvirtualenv -p python3 MeiduoMall
  ```

* 安装依赖包

  ``` bash
  workon MeiduoMall
  pip install -r DRF_requirements.txt
  ```

* 创建数据库

  ``` bash
  mysql -u root -pmysql
  create database MeiduoMall charset utf8mb4;
  grant all on MeiduoMall.* to 'oychao'@'%';
  ```

* 收集静态文件

  * 创建目录

    ``` bash
    cd front_end_pc
    mkdir static
    ```

  * 在配置文件中添加目录

    ``` bash
    cd meiduo_mall/meiduo_mall/setting
    vim prod.py
    ```

  * 执行收集命令

    ``` bash
    python manage.py collectstatic
    ```

* 修改配置文件prod.py

  ``` bash
  vim prod.py
  ```

  * 修改数据库

    ``` python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': 3306,
            'USER': 'oychao',
            'PASSWORD': '8Tony&Cino8',
            'NAME': 'MeiduoMall',
        }
    }
    ```

  * 配置动态接口

    ``` python
    DEBUG = False
    CORS_ORIGIN_WHITELIST = (
        '127.0.0.1:8080',
        'localhost:8080',
        'www.meiduo.site:8080',
        'api.meiduo.site:8000',
        '182.61.60.153')
    ```

* 配置nginx.conf

  ``` shell
  	server {
          listen       8080;
          listen       [::]:8080 ;
          server_name  MeiduoMall;
  #        root         /home/oychao/Documents/Projects/MeiduoMall/meiduo_mall/front_end_pc;
  
          # Load configuration files for the default server block.
          include /etc/nginx/default.d/*.conf;
  
          location / {
              root    /home/oychao/Documents/Projects/MeiduoMall/meiduo_mall/front_end_pc;
              index index.html index.htm;
              include uwsgi_params;
              uwsgi_pass 182.61.60.153:8001;
          }
  
          error_page 404 /404.html;
              location = /40x.html {
          }
  
          error_page 500 502 503 504 /50x.html;
              location = /50x.html {
          }
      }
      server {
          listen       80;
          server_naem  www.meiduo.site;
  
          location /admin {
              include uwsgi_params;
              uwsgi_pass 182.61.60.153:8001;
          }
  
          location /ckeditor {
              include uwsgi_params;
              uwsgi_pass 182.61.60.153:8001;
          }
  
          error_page 404 /404.html;
              location = /40x.html {
          }
  
          error_page 500 502 503 504 /50x.html;
              location = /50x.html {
          }
  
      }
  ```

* 修改manage.py文件

  ``` python
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo_mall.settings.prod")
  ```

* 配置 wsgi.py文件

  ``` python
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meiduo_mall.settings.prod")
  ```

* 安装uwsgi

  ``` bash
  pip install uwsgi
  ```

* 在项目目录/meiduo_mall 下创建uwsgi配置文件 uwsgi.ini

  ``` bash
  touch uwsgi.ini
  ```

  ``` python
  [uwsgi]
  #使用nginx连接时使用，Django程序所在服务器地址
  socket=182.61.60.153:8001
  #直接做web服务器使用，Django程序所在服务器地址
  #http=182.61.60.153:8001
  #项目目录
  chdir=/home/oychao/Documents/Projects/MeiduoMall/meiduo_mall
  #项目中wsgi.py文件的目录，相对于项目目录
  wsgi-file=meiduo_mall/meiduo_mall/wsgi.py
  # 进程数
  processes=4
  # 线程数
  threads=2
  # uwsgi服务器的角色
  master=True
  # 存放进程编号的文件
  pidfile=uwsgi.pid
  # 日志文件，因为uwsgi可以脱离终端在后台运行，日志看不见。我们以前的runserver是依赖终端的
  daemonize=uwsgi.log
  # 指定依赖的虚拟环境
  virtualenv=/home/oychao/.virtualenvs/MeiduoMall
  ```

* 启动uwsgi服务器

  ``` bash
  uwsgi --ini uwsgi.ini
  ```

  * 停止服务器

    ``` bash
    uwsgi --stop uwsgi.pid
    ```

* 重启nginx

  ``` bash
  sudo service nginx restart
  ```

### 爬虫

* 创建mongodb数据库

  ``` bash
  # 进入容器
  docker exec -it myMongoDB /bin/bash
  # 登录mongodb
  mongo scrapydb -u oychao -p Oychao@1988
  ```

  * 创建用户

    ``` bash
    # 创建用户
    db.auth('admin', 'Oychao@1988')
    # 创建集合
    db.createCollection('lagouRecruit')
    db.createCollection('tencentRecruit')
    ```


