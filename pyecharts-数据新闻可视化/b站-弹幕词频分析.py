import re
import jieba.posseg
import collections
import numpy
import PIL.Image
import wordcloud
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from pyecharts.charts import Bar,Grid
import pyecharts.options as opts
from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts

#请确认输入的文件路径是txt文档
FileRoute = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\项目用-各种素材\cell研究.txt"
StopWordRoute = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\项目用-各种素材\视频专用停用词表.txt"
ImageRoute = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\项目用-各种素材\cell.jpg"
RenderRoute = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\04-光明的未来？选择者与被选择者\05-cell.JPG"
amuRoute = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\04-光明的未来？选择者与被选择者\06-cell研究分析.html"
En2Cn = {
    'a'    : '形容词',
    'ad'   : '形容词',
    'ag'   : '形容词',
    'al'   : '形容词',
    'an'   : '形容词',
    'b'    : '区别词',
    'bl'   : '区别词',
    'c'    : '连词',
    'cc'   : '连词',
    'd'    : '副词',
    'e'    : '叹词',
    'eng'  : '英文',
    'f'    : '方位词',
    'g'    : '语素',
    'h'    : '前缀',
    'i'    : '成语',
    'j'    : '简称略语',
    'k'    : '后缀',
    'l'    : '习用语',
    'm'    : '数词',
    'mq'   : '数量词',
    'n'    : '名词',
    'ng'   : '名词',
    'nl'   : '名词',
    'nr'   : '名词',
    'nr1'  : '名词',
    'nr2'  : '名词',
    'nrf'  : '名词',
    'nrfg' : '名词',
    'nrj'  : '名词',
    'ns'   : '名词',
    'nsf'  : '名词',
    'nt'   : '名词',
    'nz'   : '名词',
    'o'    : '拟声词',
    'p'    : '介词',
    'pba'  : '介词',
    'pbei' : '介词',
    'q'    : '量词',
    'qt'   : '量词',
    'qv'   : '量词',
    'r'    : '代词',
    'rg'   : '代词',
    'rr'   : '代词',
    'rz'   : '代词',
    'rzs'  : '代词',
    'rzt'  : '代词',
    'rzv'  : '代词',
    'ry'   : '代词',
    'rys'  : '代词',
    'ryt'  : '代词',
    'ryv'  : '代词',
    's'    : '处所词',
    't'    : '时间词',
    'tg'   : '时间词',
    'u'    : '助词',
    'ude1' : '助词',
    'ude2' : '助词',
    'ude3' : '助词',
    'udeng': '助词',
    'udh'  : '助词',
    'uguo' : '助词',
    'ule'  : '助词',
    'ulian': '助词',
    'uls'  : '助词',
    'usuo' : '助词',
    'uyy'  : '助词',
    'uzhe' : '助词',
    'uzhi' : '助词',
    'v'    : '动词',
    'vd'   : '动词',
    'vf'   : '动词',
    'vg'   : '动词',
    'vi'   : '动词',
    'vl'   : '动词',
    'vn'   : '动词',
    'vshi' : '动词',
    'vx'   : '动词',
    'vyou' : '动词',
    'w'    : '标点符号',
    'wb'   : '标点符号',
    'wd'   : '标点符号',
    'wf'   : '标点符号',
    'wj'   : '标点符号',
    'wh'   : '标点符号',
    'wkz'  : '标点符号',
    'wky'  : '标点符号',
    'wm'   : '标点符号',
    'wn'   : '标点符号',
    'wp'   : '标点符号',
    'ws'   : '标点符号',
    'wt'   : '标点符号',
    'ww'   : '标点符号',
    'wyz'  : '标点符号',
    'wyy'  : '标点符号',
    'x'    : '字符串',
    'xu'   : '字符串',
    'xx'   : '字符串',
    'y'    : '语气词',
    'z'    : '状态词',
    'zg'   : '动词',
    'un'   : '未知词',
    'nrt'  : '未知词',
    'ug'   : '未知词',
}
OutcomeRoute="C:\\Users\\User\\Desktop\\词频分析结果.txt"

def ReadFile(FileRoute):
    #读取文件
    fn=open(FileRoute,'r',encoding="utf-8")
    string_data=fn.read()
    fn.close()
    #文本预处理
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')
    string_data=re.sub(pattern,'',string_data)
    return string_data

def RemoveMeaningless(string_data):
    #去除停用词
    seg_list_exact=jieba.cut(string_data,cut_all=False,HMM=True)
    object_list=[]

    with open(StopWordRoute,'r',encoding='UTF-8') as meaninglessFile:
        stopwords=set(meaninglessFile.read().split('\n'))
    stopwords.add('')
    for word in seg_list_exact:
        if word not in stopwords:
            object_list.append(word)
    meaninglessFile.close()

    meaninglessFile.close()

    return object_list

def WordCounts(object_list):
    word_counts=collections.Counter(object_list)
    word_counts_top=word_counts.most_common(100)
    return word_counts_top,word_counts

def WriteTxt(word_counts_top,En2Cn):
    print('\n词语\t词频\t词性')
    print('----------------')
    fileOut=open("C:\\Users\\User\\Desktop\\词频分析结果.txt",'w',encoding='utf-8')
    fileOut.write('词语,词频,词性\n')
    count=0
    for TopWord,Frequency in word_counts_top:
        for POS in jieba.posseg.cut(TopWord):
            if count==100:
                break
            print(TopWord + ',', str(Frequency) + ',', list(En2Cn.values())[list(En2Cn.keys()).index(POS.flag)])  # 逐行输出数据
            fileOut.write(TopWord + ',' + str(Frequency) + ',' + list(En2Cn.values())[list(En2Cn.keys()).index(POS.flag)] + '\n')  # 逐行写入str格式数据
            count += 1
    fileOut.close()

def WordCloud(word_counts):
    #词频展示
    print('\n开始制作词云……')

    mask=numpy.array(PIL.Image.open(ImageRoute))
    wc=wordcloud.WordCloud(
        font_path="C:\\Users\\User\\AppData\\Local\\Microsoft\\Windows\\Fonts\\WenYue-XinQingNianTi-NC-W8-1.otf",
        background_color='white',
        mask=mask,
        max_words=2500,
        max_font_size=50,
        min_font_size=5,
    )

    wc.generate_from_frequencies(word_counts)
    #wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
    plt.figure('词云')
    image_colors = wordcloud.ImageColorGenerator(mask)
    plt.imshow(wc.recolor(color_func=image_colors),interpolation='bilinear')
    plt.axis('off')
    plt.show()

def WordFrequency(OutcomeRoute):
    df = pd.read_csv(OutcomeRoute).head(100)
    bar=(
        Bar()
        .add_xaxis(df['词语'].tolist())
        .add_yaxis("关键词词频", df['词频'].tolist(),label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        title_opts=opts.TitleOpts(title="2017-2020科学杂志《cell》中人工智能医疗领域的研究方向", subtitle="数据来源：cellpress"),
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(trigger="axis",axis_pointer_type="cross")
        )
        .render(amuRoute)
    )

def image():
    image = Image()
    imageroute = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\04-光明的未来？选择者与被选择者\05-cell.JPG"
    img_src = (
        imageroute
    )
    image.add(
        src=img_src,
        style_opts={"width": "200px", "height": "200px", "style": "margin-top: 20px"},
    )
    image.set_global_opts(
        title_opts=ComponentTitleOpts(title="科学杂志《Cell》", subtitle="封面与其词云图")
    )
    image.render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\cell研究分析.html")
    return image

if __name__ == '__main__':
    string_data=ReadFile(FileRoute)
    object_list=RemoveMeaningless(string_data)
    word_counts_top,word_count=WordCounts(object_list)
    WriteTxt(word_counts_top,En2Cn)
    WordCloud(word_count)
    WordFrequency(OutcomeRoute)
    print('制作完成！')
    print('\n作者：|cyt|')
    print('日期：2020.10.04')
