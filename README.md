# 豆瓣电影数据分析

通过运行main.py中的各个函数，可以实现不同功能
1.yanzhengma() 生成随机数
2.gettop10() 获取电影详细信息的连接
3. getone(url1)获取电影详细信息
4. insert()将数据插入到excel表格中
5. connect_db将数据插入到数据库中
6. virtual_excel()根据得到的电影信息生成雷达图
7. yun()根据得到的数据生成云图
上面的各个函数除getone(url1)均可单独运行，getone函数需要传入参数url才可运行，在其余函数中均提前调用了gettop10函数以及getone函数


### 运行环境

python3及以上版本均可运行

mysql数据库版本无要求
### 运行方法

1. 安装python3
2. 下载本仓库
3. 在命令行中运行python3 main.py
4. 运行完毕后，在当前目录下会生成一个名为test.xlsx的表格，其中包含电影详细信息，生成render.html和yun.html，其中是数据可视化的展示
5. 运行render.html和yun.html即可

### 数据来源

本程序的数据来源为豆瓣电影，具体数据来源为https://movie.douban.com/chart

### 数据说明

本程序的数据为2024年4月豆瓣电影新片榜前10部电影的详细信息，包括电影名称、电影类型、电影评分、电影评价人数、电影导演、电影主演、电影上映时间、电影时长、电影简介等

