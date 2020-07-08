## Web安全防范

* SQL注入攻击：在编写SQL语句时，如果直接将用户传入的数据作为参数使用字符串拼接的方式插入到SQL查询中，那么攻击者可以通过注入其他语句来执行攻击操作。
```
@app.route('/students')
def bobby_table():
    password = request.args.get('password')
    cur = db.execute("SELECT * FROM students WHERE password='%s';" % password)
    results = cur.fetchall()
    return results
```

如果攻击者输入的password参数值为“'or 1=1--”，SQL语句就变成了SELECT * FROM students WHERE password='' or 1=1 --;'

* 主要防范方法：
    * 验证输入类型：比如某个视图函数接收整型id来查询，那么就在URL规则中限制URL变量为整型。
    * 参数化查询：在构造SQL语句时避免使用拼接字符串或字符串格式化（使用百分号或format（）方法）的方式来构建SQL语句。而要使用各类接口库提供的参数化查询方法，以内置的sqlite3库为例： db.execute('SELECT * FROM students WHERE password=?, password)，对于特殊字符，比如引号、分号和横线等。使用参数化查询时，各种接口库会为我们做转义工作。
    
    
* XSS攻击：XSS（Cross-Site Scripting，跨站脚本）攻击历史悠久，最远可以追溯到90年代，但至今仍然是危害范围非常广的攻击方式。
攻击者通过将代码注入被攻击者的网站中，用户一旦访问网页便会执行被注入的恶意脚本。

```
@app.route('/hello')
def hello():
    name = request.args.get('name')
    response = '<h1>Hello, %s!</h1>' % name
    
http://example.com/hello?name=<script>alert('Bingo!');</script>
```


危害：即攻击者通过JavaScript几乎能够做任何事情：窃取用户的cookie和其他敏感数据，重定向到钓鱼网站，发送其他请求，执行诸如转账、发布广告信息、在社交网站关注某个用户等。

防范手段：1.防范XSS攻击最主要的方法是对用户输入的内容进行HTML转义，转义后可以确保用户输入的内容在浏览器中作为文本显示，而不是作为代码解析。2.验证用户输入，利用正则表达式验证。


* CSRF攻击：CSRF（Cross Site Request Forgery，跨站请求伪造）是一种近年来才逐渐被大众了解的网络攻击方式

    * 攻击原理：攻击者利用用户在浏览器中保存的认证信息，向对应的站点发送伪造请求。在发送请求时，只要浏览器中保存了对应的
cookie，服务器端就会认为用户已经处于登录状态，而攻击者正是利用了这一机制。

```
@app.route('/account/delete')
def delete_account():
    if not current_user.authenticated:
    abort(401)
    current_user.delete()
    return 'Deleted!'
    
<img src="http://example.com/account/delete">
```

当用户访问B网站时，浏览器在解析网页时会自动向img标签的src属性中的地址发起请求。此时你在A网站的登录信息保存在cookie中，
因此，仅仅是访问B网站的页面就会让你的账户被删除掉。

* CSRF令牌校验：当处理非GET请求时，要想避免CSRF攻击，关键在于判断请求是否来自自己的网站。在前面我们曾经介绍过使用HTTP referer获取请求来源，理论上说，通过referer可以判断源站点从而避免CSRF攻击，但因为referer很容易被修改和伪造，所以不能作为主要的防御措施。一般的做法是通过在客户端页面中加入伪随机数来防御CSRF攻击，这个伪随机数通常被称为CSRF令牌（token），
把在服务器端创建的伪随机数（CSRF令牌）添加到表单中的隐藏字段里和session变量（即签名cookie）中，当用户提交表单时，这个令牌会和表单数据一起提交。在服务器端处理POST请求时，我们会对表单中的令牌值进行验证，如果表单中的令牌值和session中的令牌值相同，那么就说明请求发自自己的网站。

```
每个页面都有一个令牌，这个令牌有服务器生成，当提交请求时，会用页面的令牌和session中的令牌进行比较，因为攻击者无法生成令牌，所以
令牌校验会失败。
```