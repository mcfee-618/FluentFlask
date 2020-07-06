## Pipenv

Pipenv是Kenneth Reitz在2017年1月发布的Python依赖管理工具，现在由PyPA维护。你可以把它看做是pip和virtualenv的组合体，而它基于的Pipfile则用来替代旧的依赖记录方式（requirements.txt），暂时不再推荐使用了。

## Flask程序结构

* 初始化：所有Flask程序都必须创建一个程序实例 。Web服务器使用一种名为Web服务器网关接口（Web Server Gateway Interface，WSGI）的协议，把接收自客户端的所有请求都转交给这个对象处理，程序实例是Flask 类的对象。Flask 类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。在大多数程序中，Python的__name__ 变量就是所需的值。

* 路由和视图函数：处理URL和函数之间关系的程序称为路由。index这样的函数称为视图函数（view function）。视图函数返回的响应可以是包含HTML的简单字符串，也可以是复杂的表单。

    * 静态路由
    ```
    @app.route('/')
    def index():
    return '<h1>Hello, World!</h1>'
    ```
    * 动态路由:不仅可以为视图函数绑定多个URL，还可以在URL规则中添加变量部分，使用“<变量名>”的形式表示。
    ```
    @app.route('/greet/<name>')
    def greet(name):
        return '<h1>Hello, %s!</h1>' % name
    ```
     Note:当URL规则中包含变量时，如果用户访问的URL中没有添加变量，比如/greet，那么Flask在匹配失败后会返回一个404错误响应。一个很常见的行为是在app.route（）装饰器里使用defaults参数设置URL变量的默认值，这个参数接收字典作为输入，存储URL变量和默认值的映射。

* 启动服务器：Flask内置了一个简单的开发服务器（由依赖包Werkzeug提供），足够在开发和测试阶段使用。旧的启动开发服务器的方式是使用app.run（）方法，目前已不推荐使用（deprecated）。
    * 自动发现程序实例:从当前目录寻找app.py和wsgi.py模块，并从中寻找名为app或application的程序实例。从环境变量FLASK_APP对应的值寻找名为app或application的程序实例。因为我们的程序主模块命名为app.py，所以flask run命令会自动在其中寻找程序实例。如果你的程序主模块是其他名称，比如hello.py，那么需要设置环境变量FLASK_APP，将包含程序实例的模块名赋值给这个变量。
    * 管理环境变量：Flask的自动发现程序实例机制还有第三条规则：如果安装了python-dotenv，那么在使用flask run或其他命令时会使用它自动从.flaskenv文件和.env文件中加载环境变量。当安装了python-dotenv时，Flask在加载环境变量的优先级是：手动设置的环境变量>.env中设置的环境变量>.flaskenv设置的环境变量。
    ```
    .flaskenv用来存储和Flask相关的公开环境变量，比如FLASK_APP；而.env用来
     存储包含敏感信息的环境变量，比如后面我们会用来配置Email服务器的账户名与密码。
    ```
* 项目配置：在一个项目中，你会用到许多配置：Flask提供的配置，扩展提供的
配置，还有程序特定的配置。和平时使用变量不同，这些配置变量都通
过Flask对象的app.config属性作为统一的接口来设置和获取，它指向的
Config类实际上是字典的子类，所以你可以像操作其他字典一样操作
它。
     ```
    配置的名称必须是全大写形式，小写的变量将不会被读取
     ```
* URL：使用Flask提供的url_for（）函数获取URL，当路由中定义的
URL规则被修改时，这个函数总会返回正确的URL。
    ```
    url_for（）函数生成的URL是相对URL（即内部URL），
    即URL中的path部分，比如“/hello”，不包含根URL。相对URL只能在程
    序内部使用。如果你想要生成供外部使用的绝对URL，可以在使用
    url_for（）函数时，将_external参数设为True，这会生成完整的URL，
    ```
* 模板与静态文件：。默认情
况下，模板文件存放在项目根目录中的templates文件夹中，静态文件存
放在static文件夹下，这两个文件夹需要和包含程序实例的模块处于同一
个目录下。

* MVC架构：在MVC架构中，程序被分为三个组件：数据处理（Model）、用户界面（View）、交互
逻辑（Controller）。粗略归类，如果想要使用Flask来编写一个MVC架构的程序，那么
视图函数可以作为控制器（Controller），视图（View）则是使用Jinja2渲染的HTML模板，而模型（Model）可以使用其
他库来实现。


## 相关链接
* pipenv https://blog.csdn.net/qq_18598403/article/details/85108742

  