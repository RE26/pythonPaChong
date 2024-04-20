import random
import re
import string
import urllib.request

import bs4
import openpyxl
import pymysql
from pyecharts import options as opts
from pyecharts.charts import Radar, WordCloud

top10=[]
excel=['','','','','','','','','','']
# 获取豆瓣电影top10
def yanzhengma():
    length = 4
    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for _ in range(length))
    print("验证码:", captcha)
def gettop10(top10):
    url = 'https://movie.douban.com/chart'
    data = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0) Gecko/20100101 Firefox/124.0',
        'cookie': ' ll="118097"; bid=fUBMHhsLpY8; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1712904062%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DCddkQuVch40tFEKGWtZhjc0HHplKs_HfI7Kg9eJcQSVOh57OZ0oAGVrn-heP0Uxw%26wd%3D%26eqid%3Dba70208000325d50000000036618d775%22%5D; _pk_id.100001.4cf6=c246a070310152ee.1712904062.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.1745228535.1712904062.1712904062.1712904062.1; __utmb=30149280.0.10.1712904062; __utmc=30149280; __utmz=30149280.1712904062.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.31942075.1712904062.1712904062.1712904062.1; __utmb=223695111.0.10.1712904062; __utmc=223695111; __utmz=223695111.1712904062.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=O8Kjn1ybN7bkIvdtfo95HxGUTTBeqHOl; __gads=ID=bec5e601186046e8:T=1712904064:RT=1712904064:S=ALNI_MYyiTrbr3YS1Dd0Dfoc1HT29KhiAg; __gpi=UID=00000de9f39160ea:T=1712904064:RT=1712904064:S=ALNI_MYG_r2YU5YTYkkUrN8orRsP7Z3log; __eoi=ID=af1ef4f17b871fd5:T=1712904064:RT=1712904064:S=AA-AfjZm0If5gpmCppzjFzxccNWM',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    }
    req = urllib.request.Request(url, headers=data)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    # https://movie.douban.com/subject/35875476/
    # urls = re.findall('https://movie.douban.com/subject/.*?"', html)
    # urls=re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',html)
    urls=re.findall(r'<a class="nbg" href="(.*)"  title=',html)

    for url in urls:
        if len(url) <= 43:
            top10.append(url.strip('"'))
    top10 = list(set(top10))
    print(top10)
    # print(html)#
# 获取电影信息
def getone(url1):
    url = url1
    data = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0) Gecko/20100101 Firefox/124.0',
        'cookie': 'll="118097"; bid=fUBMHhsLpY8; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1712991963%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DCddkQuVch40tFEKGWtZhjc0HHplKs_HfI7Kg9eJcQSVOh57OZ0oAGVrn-heP0Uxw%26wd%3D%26eqid%3Dba70208000325d50000000036618d775%22%5D; _pk_id.100001.4cf6=c246a070310152ee.1712904062.; __utma=30149280.1745228535.1712904062.1712904062.1712991964.2; __utmz=30149280.1712904062.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.31942075.1712904062.1712904062.1712991964.2; __utmz=223695111.1712904062.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=O8Kjn1ybN7bkIvdtfo95HxGUTTBeqHOl; __gads=ID=bec5e601186046e8:T=1712904064:RT=1712904064:S=ALNI_MYyiTrbr3YS1Dd0Dfoc1HT29KhiAg; __gpi=UID=00000de9f39160ea:T=1712904064:RT=1712904064:S=ALNI_MYG_r2YU5YTYkkUrN8orRsP7Z3log; __eoi=ID=af1ef4f17b871fd5:T=1712904064:RT=1712904064:S=AA-AfjZm0If5gpmCppzjFzxccNWM; __utmc=30149280; __utmc=223695111; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utmb=30149280.0.10.1712991964; __utmb=223695111.0.10.1712991964',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Referer':'https: // movie.douban.com / chart'
    }
    req = urllib.request.Request(url, headers=data)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')

    soup = bs4.BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

    print('------------------------------------')
    print('正在爬取' + url)

    ImageSrc = re.findall(r'<img.*src="(.*?)"', html)#图片
    Title = re.findall(r'<meta property="og:title" content="(.*) />', html)#电影名字
    Rating = re.findall(r'<strong class="ll rating_num" property="v:average">(.*)</strong>', html)#评分
    Summary=soup.find_all('span',property='v:summary')#剧情简介
    # Summary = re.findall(r'<span property="v:summary" class="">(.*)', html)#剧情简介
    Actor = re.findall(r'<meta property="video:actor" content="(.*)" />', html)#演员表
    daoyan=re.findall(r'<meta property="video:director" content="(.*)" />', html)#导演
    leixing=re.findall(r'<span property="v:genre">(.*)</span>', html)
    diqu=re.findall(r'<span class="pl">制片国家/地区:</span> (.*)<br/>', html)
    yuyan=re.findall(r'<span class="pl">语言:</span> (.*)<br/>', html)
    time=re.findall(r'<span class="pl">片长:</span> <span property="v:runtime" content="112">(.*)</span><br/>', html)
    print(ImageSrc[1])
    print(Title[0].strip('"'))
    print(Rating)
    # print(str(Summary[0]).strip('<span class="" property="v:summary"> </'))
    print(str(re.findall(r'[\u4e00-\u9fa5]+',str(Summary[0]))))
    print(Actor)
    print(daoyan)
    print(re.findall(r'[\u4e00-\u9fa5]+',str(leixing[0])))
    print(diqu)
    print(yuyan)
    print(time)
    try:
        excel[0] = ImageSrc[1]
    except:
        pass
    try:
        excel[1] = Title[0].strip('"')
    except:
        pass
    try:
        excel[2] = Rating[0]
    except:
        pass
    try:
        excel[3] = ''.join(re.findall(r'[\u4e00-\u9fa5]+',str(Summary[0])))
    except:
        pass
    try:
        excel[4] = '、'.join(Actor)
    except:
        pass
    try:
        excel[5] = daoyan[0]
    except:
        pass

    try:
        excel[6] = '/'.join(re.findall(r'[\u4e00-\u9fa5]+',str(leixing[0])))

    except:
        pass
    try:
        excel[7] = diqu[0]
    except:
        pass
    try:
        excel[8] = yuyan[0]
    except:
        pass
    try:
        excel[9] = time[0]
    except:
        pass

    print(excel)
    return excel
#将电影信息放入excel
def insertExcel():
    gettop10(top10)
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title='test'
    sheet.append(['图片','电影名字','评分','剧情简介','演员表','导演','类型','地区','语言','片长'])
    for url in top10:
        excel=['','','','','','','','','','']
        sheet.append(getone(url))  # 给每行的数据为0-9
    wb.save('test.xlsx')
#将电影信息放入数据库
def connect_db():
    gettop10(top10)
    # 连接数据库
    conn = pymysql.connect(host='localhost', user='root', password='548988', db='movie', charset='utf8')
    # 创建游标对象
    cursor = conn.cursor()
    # 执行SQL语句
    sql = "INSERT INTO movie(封面,电影名字,评分,简介,演员,导演,类型,地区,语言,片长) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    for url in top10:
        excel = ['', '', '', '', '', '', '', '', '']

        excel = getone(url)

        cursor.execute(sql, (excel[0], excel[1], excel[2], excel[3], excel[4], excel[5], excel[6], excel[7], excel[8], excel[9]))

    # 提交事务
    conn.commit()
    # 关闭游标和数据库连接
    cursor.close()
    conn.close()
#电影信息可视化
def virtual_excel():
    gettop10(top10)
    f = []
    name = []
    for url in top10:
        excel = ['', '', '', '', '', '', '', '', '']
        excel = getone(url)
        f.append(excel[2])
        name.append(excel[1])
    c = (
        Radar()
        .add_schema(
            schema=[
                opts.RadarIndicatorItem(name=name[0], max_=10),
                opts.RadarIndicatorItem(name=name[1], max_=10),
                opts.RadarIndicatorItem(name=name[2], max_=10),
                opts.RadarIndicatorItem(name=name[3], max_=10),
                opts.RadarIndicatorItem(name=name[4], max_=10),
                opts.RadarIndicatorItem(name=name[5], max_=10),
                opts.RadarIndicatorItem(name=name[6], max_=10),
                opts.RadarIndicatorItem(name=name[7], max_=10),
                opts.RadarIndicatorItem(name=name[8], max_=10),
                opts.RadarIndicatorItem(name=name[9], max_=10),
            ]
        )
        .add("评分",[f])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            legend_opts=opts.LegendOpts(selected_mode="single"),
            title_opts=opts.TitleOpts(title="评分对比图"),
        )
        .render()
    )
    print('雷达图生成完毕，请运行render.html来查看生成的雷达图')
def yun():
    gettop10(top10)
    name = []
    f=[]
    for url in top10:
        excel = ['', '', '', '', '', '', '', '', '']
        excel = getone(url)
        name.append(excel[1])
        f.append(excel[2])
    data=[]
    for i,j in zip(name,f):
        data.append((i,j))
    wordcloud = WordCloud()
    wordcloud.add('',data,word_size_range=[6,20], shape='star',textstyle_opts=opts.TextStyleOpts(font_family="cursive"))
    wordcloud.render('yun.html')
    print('云图生成完毕，请运行yun.html来查看生成的云图')
if __name__ == '__main__':
    #gettop10(top10)
    # insertExcel()
    # connect_db()
    # virtual_excel()
    yun()
    # yanzhengma()