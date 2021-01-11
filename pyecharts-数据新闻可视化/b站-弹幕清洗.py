from lxml import etree

path = r"C:\Users\User\Desktop\弹幕.txt"

# 读取txt文件
def getfile(path):
    f = open(path, encoding='utf-8')
    line = f.readline()
    f.close()
    return line

#处理txt文件
def parsefile(line):
    #用etree将字符串解析成为特殊的html对象
    html = etree.HTML(line.encode('utf=8'))
    #将html对象转成字符串
    result=etree.tostring(html,encoding='utf-8').decode()
    #获取p标签里的内容
    text=html.xpath('//d')
    return text

#获得弹幕文本文件
def writefile(text):
    fileroute=r'C:\Users\User\Desktop\弹幕分析.txt'
    f=open(fileroute,'w',encoding='utf-8')
    for i in text:
        f.write(i.text+'\n')
    f.close()

line=getfile(path)
text=parsefile(line)
writefile(text)

