

##### - Python Cookbook中文版：https://www.w3cschool.cn/youshq/j2o8nozt.html

##### - Python Grpc通信：https://grpc.io/docs/languages/python/

##### - Protobuf：https://protobuf.dev/

##### - grpc实例代码：https://github.com/grpc/grpc

- 垃圾回收机制：https://www.niwoxuexi.com/blog/python/article/2011
- __getattribute__、__getattr__、__setattr__：https://www.cnblogs.com/sheshouxin/p/10448056.html
- grpc 实现流式上传下载功能：https://www.cnblogs.com/a00ium/p/16937007.html
- sys._getframe():https://blog.csdn.net/weixin_30920853/article/details/98842243

python:
 Python 中常用的 5 种线程锁:
  https://z.itpub.net/article/detail/DE03B9C2CC0ECD3366C7ADCDE9550CE6
 Python--元类:https://blog.csdn.net/weixin_43988680/article/details/123903473
 print 函数打印函数的原理：https://www.zybuluo.com/wzhang1117/note/803061
 pyenv 配置多版本的python环境:
 一个强大的命令行解析器 Plumbum:https://www.jianshu.com/p/e13fd0c38acf
 psutil库:http://www.360doc.com/content/21/1112/16/51091873_1003876985.shtml
 queue中task_done和join用法：https://www.cnblogs.com/lincappu/p/12890761.html
 for 和迭代器对象、可迭代对象的关系：
  https://blog.csdn.net/qq_42902997/article/details/108124049
 ThreadPoolExecutor的submit和map使用:http://c.biancheng.net/view/2627.html
 python中Base64原理和使用:https://www.jianshu.com/p/b089a7b36d82
 hashlib的使用:进行数据账号加密和完整性验证：
  https://blog.csdn.net/dreaming_coder/article/details/108247249
 asyncio教程:https://www.liujiangblog.com/course/python/83
  api:https://docs.python.org/zh-cn/3.9/library/asyncio-task.html#task-object
  https://www.jianshu.com/p/6d582b07c65a
 抽象基类，six模块的作用，直接继承和虚拟子类：
  https://blog.csdn.net/weixin_40907382/article/details/80277170
 requests post请求data和json数据格式深入：https://zhuanlan.zhihu.com/p/202978890

redis:
 中文官网：https://www.redis.com.cn/redis-stream.html

git：
 官网：https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%8F%98%E5%9F%BA


jenkins
 教程参考：https://www.bilibili.com/video/BV19M4y1c7m4
 官网：https://www.jenkins.io/zh/

grpc:
 grpc| python 实战 grpc:https://www.jianshu.com/p/43fdfeb105ff


java
 java泛型：https://blog.csdn.net/qq_66912832/article/details/125272259

kafka:
 文档：https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html
 使用介绍：https://blog.csdn.net/luanpeng825485697/article/details/81036028

mqtt:
 MQTT协议基础：https://www.51cto.com/article/670429.html
 MQTT深入：https://blog.csdn.net/CM_STC89C52/article/details/122712188
 python调用mqtt:https://blog.csdn.net/weixin_41656968/article/details/80848542#13subscribe

Mysql:
 MySQL为什么要用B+树实现索引:
  https://cloud.tencent.com/developer/article/1543335

docker:
 在用：https://yeasy.gitbook.io/docker_practice/image/build
 参考官网：https://docs.docker.com/engine/reference/commandline/
 中文参考网站：
  https://yeasy.gitbook.io/docker_practice/image/dockerfile
  https://outmanzzq.github.io/2019/10/22/docker-network/#%E4%BA%8C%E9%BB%98%E8%AE%A4%E7%BD%91%E7%BB%9C
 视频教程：https://www.bilibili.com/video/BV1og4y1q7M4?p=2
 https://blog.csdn.net/pushiqiang/article/details/78682323

can 通信：
 https://zhuanlan.zhihu.com/p/538834760
 https://blog.csdn.net/weixin_45403142/article/details/120075619
 https://blog.csdn.net/LiuXF93/article/details/113729294

boost库实现python和C通信：
 教程：https://blog.csdn.net/rangfei/category_11569812.html
 # 官方网站
  https://www.boost.org/
  # 下载地址
  https://www.boost.org/users/download/
  # 预编译版本下载地址
  https://sourceforge.net/projects/boost/files/boost-binaries/
  wget https://boostorg.jfrog.io/artifactory/main/release/1.73.0/source/boost_1_73_0.tar.bz2 --no-check-certificate
  tar xvf boost_1_73_0.tar.bz2
  cd boost_1_73_0
  ./boostrap.sh
  ./b2 --buildtype=complete install

modbus:
 半双工通信：数据可以在一个信号载体的两个方向上传输，但是不能同时传输
 例如，在一个局域网上使用具有半双工传输的技术，一个工作站可以在线上发送数据，然后立即在线上接收数据，
 这些数据来自数据刚刚传输的方向。 
 像全双工传输一样，半双工包含一个双向线路（线路可以在两个方向上传递数据）

 全双工（Full Duplex）是指在发送数据的同时也能够接收数据，两者同步进行，
 这好像我们平时打电话一样，说话的同时也能够听到对方的声音。目前的网卡一般都支持全双工

0505：
 uWSGI服务器：https://blog.csdn.net/Aifore/article/details/86703685
    https://blog.csdn.net/baidu_24752135/article/details/123726280
 uWSGI：
  uWSGI是应用服务器，是一个应用执行的容器。应用服务器往往也会集成 HTTP Server 的功能，但是不如专业的 HTTP Server 那么强大，所以应用服务器往往是运行在 HTTP Server 的背后
 WSGI:
  WSGI 是一种 Web 服务器网关接口。WSGI，全称 Web Server Gateway Interface，或者 Python Web Server Gateway Interface ，是为 Python 语言定义的 Web 服务器 和 Web 应用程序或框架之间的一种简单而通用的接口。自从 WSGI 被开发出来以后，许多其它语言中也出现了类似接口。

  它是一 个 Web 服务器（如 nginx，uWSGI 等服务器）与 web 应用（如用 Flask 框架写的程序）通信的一种 规范。WSGI协议其实是定义了一种server与application解耦的规范，即可以有多个实现WSGI server的服务器，也可以有多个实现WSGI application的框架，那么就可以选择任意的server和application组合实现自己的web应用。例如uWSGI和Gunicorn都是实现了WSGI server协议的服务器，Django，Flask是实现了WSGI application协议的web框架，可以根据项目实际情况搭配使用。
 uwsgi
  同WSGI一样是一种通信协议，uWSGI是实现了uwsgi和WSGI两种协议的Web服务器
  
  
pyenv install [options] 
 -f/--force :强制安装，即使该版本已经安装过了
 -s/--skip-existing :跳过已经安装过的版本
 -v/--verbose:输出安装过程中的详细状态信息

安装pyenv-virtualenv
 git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

pyenv install --list # pyenv的install命令，可以查看pyenv当前支持哪些Python版本
pyenv install -v 3.8.1 # 使用pyenv安装不同的Python版本
v=3.6.9; wget https://npm.taobao.org/mirrors/python/$v/Python-$v.tar.xz -P ~/.pyenv/cache/; pyenv install $v 

pyenv version # 检查 pyenv 的版本
 [root@python ~]# pyenv version
 (set by /root/.pyenv/version)
pyenv versions # 查看当前系统中包含的Python版本
 [root@python ~]# 
 * system (set by /root/.pyenv/version)
  2.7.13
  3.8.1
pyenv global 2.7.13 # 
 使用pyenv以后，可以快速切换Python的版本。切换Python版本以后，与版本相关的依赖也会一起切 换。因此，我们不用担心不同的版本在系统中是否会相互干扰。例如，切换Python版本以后，相应的 pip也会跟着切换，所以不用担心自己使用的pip版本和Python版本不匹配的问题
 [root@python ~]# pyenv global 3.8.1
 [root@python ~]# pip --version
  pip 19.2.3 from /root/.pyenv/versions/3.8.1/lib/python3.8/site-packages/pip (python 3.8)
pyenv rehash # 安装新版本后rehash一下

pyenv global 3.6.5 2.7.14 # 指定多个全局版本, 3版本优先
pyenv uninstall 2.7.10 # 删除Python版本，使用uninstall命令即可。


1、# //关闭can设备；ip link set can1 down
2、# //开启can设备；ip link set can1 up
3、# //显示can设备详细信息；ip -details link show can1
4、#candump canX //接收can总线发来的数据；
5、#ifconfig canX down //关闭can设备，以便配置;
6、#ip link set canX up type can bitrate 250000 //设置can波特率
7、#conconfig canX bitrate + 波特率；
8、#canconfig canX start //启动can设备；
9、#canconfig canX ctrlmode loopback on //回环测试；
10、#canconfig canX restart // 重启can设备；
11、#canconfig canX stop //停止can设备；
12、#canecho canX //查看can设备总线状态；
13、#cansend canX --identifier=ID+数据 //发送数据；
14、#candump canX --filter=ID：mask//使用滤波器接收ID匹配的数据
ifconfig can0 down;
ip link set can0 up type can bitrate 125000 triple-sampling on;
ifconfig can0 up;
candump any
candump can0 //接收can总线发来的数据
cansend can0 --identifier=0x123 0xab //发送数据；
也可以使用 ip 命令直接设定位速率：
ip link set can0 type can bitrate 125000
当设置完成后，可以通过下面的命令查询 can0 设备的参数设置：
ip -details link show can0
当设置完成后，可以使用下面的命令使能 can0 设备：
ifconfig can0 down
ifconfig can0 up
