import pandas as pd
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import matplotlib
from pyecharts.charts import Bar,Pie,Grid,Page
import pyecharts.options as opts

#文件地址
FileRoute = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\项目用-各种素材\弹幕分析.txt"
OutcomeRoute = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\项目用-各种素材\词频分析结果-弹幕.txt"

def ReadFile(FileRoute):
    df=pd.read_table(FileRoute)
    return df

def EmotionEvaluate(text):
    s=SnowNLP(text)
    return s.sentiments

def dataAnalysis(sentiment):
    mean="均值 = "+ str(sentiment.mean())
    median="中位数 = "+ str(sentiment.median())
    return mean+"\n"+median

#用matplotlib可以轻轻松松画出频数分布直方图，但是真的太丑了,我选择死亡
def DrawBarPlot(sentiments):
    # 设置matplotlib正常显示中文和负号
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
    matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号
    #尝试采用直方图分析
    plt.hist(sentiments,bins=40,facecolor="orange",edgecolor="black", alpha=0.7)
    plt.xlabel("情感区间")
    plt.ylabel('弹幕数量')
    text=dataAnalysis(sentiments)
    plt.title("弹幕情感分布")
    plt.text(-0.2,260,text)
    plt.show()

#制作频数分布表
def CountFrequence(sentiment):
    #将评论情感分成10个区间
    a = pd.cut(sentiment,
               [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5,
                0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1],
               labels=[u"(0,0.05]", u"(0.05,0.1]", u"(0.1,0.15]", u"(0.15,0.2]", u"(0.2,0.25]", u"(0.25,0.3]",
                       u"(0.3,0.35]", u"(0.35,0.4]", u"(0.4,0.45]", u"(0.45,0.5]", u"(0.5,0.55]", u"(0.55,0.6]",
                       u"(0.6,0.65]", u"(0.65,0.7]", u"(0.7,0.75]", u"(0.75,0.8]", u"(0.8,0.85]", u"(0.85,0.9]",
                       u"(0.9,0.95]", u"(0.95,1.0]"])
    #计算每个区间出现的频率
    b = a.value_counts()
    b = b.sort_index()
    #将series类型的b转换为dataframe类型，便于使用pyecharts绘图
    frequency = {'section': b.index, 'frequency': b.values}
    frequency = pd.DataFrame(frequency)
    return frequency

def DrawEcharts(frequency,frequency_pie):
    bar=(
        Bar()
        .add_xaxis(frequency['section'].tolist())
        .add_yaxis("弹幕情感积极度分布", frequency['frequency'].tolist())
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            legend_opts=opts.LegendOpts(pos_top="10%"),
            toolbox_opts=opts.ToolboxOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(
                name='弹幕情感区间',
                type_='category'),
            yaxis_opts=opts.AxisOpts(
                name='弹幕数量',
                type_='value'),
            title_opts=opts.TitleOpts(
                title="《睡前消息》观众对广东花都“一元钱看病”新闻的情感倾向",
                subtitle="数据来源：bilibili"
            )
        )
        .render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\03-一元开局，通关升级：你是全村的希望\03-弹幕情感分析.html")
    )
    #构造饼图数据
    x_data = frequency_pie['section'].tolist()
    y_data = frequency_pie['frequency'].tolist()
    data_pair = [list(z) for z in zip(x_data, y_data)]
    data_pair.sort(key=lambda x: x[1])
    pie=(
        Pie()
        .add(
            series_name="弹幕情感倾向",
            data_pair=data_pair,
            rosetype='radius',
            radius=["30%", "75%"],
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=True),
        )
        .set_global_opts(
            legend_opts=opts.LegendOpts(pos_bottom="1%"),
            title_opts=opts.TitleOpts(title="《睡前消息》观众对广东花都“一元钱看病”新闻的情感倾向",subtitle="数据来源：bilibili")
        )
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
        )
        .render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\03-一元开局，通关升级：你是全村的希望\02-弹幕情感倾向.html")
    )

    df = pd.read_csv(OutcomeRoute).head(50)
    wordfrequency = (
        Bar()
        .add_xaxis(df['词语'].tolist())
        .add_yaxis("关键词词频", df['词频'].tolist(), label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        title_opts=opts.TitleOpts(title="弹幕关键词词频分析", subtitle="数据来源：bilibili"),
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross")
        )
        .render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\03-一元开局，通关升级：你是全村的希望\04-弹幕词频分析.html")
    )

    # grid=(
    #     Grid()
    #     .add(wordfrequency, grid_opts=opts.GridOpts(height="80%",width="80%"))
    #     .render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\评论情感分析.html")
    # )

    # sourcefile = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\评论情感分析.html"
    # json = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\弹幕.json"
    # page = (
    #     Page(layout=Page.DraggablePageLayout)
    #         .add(grid, pie, wordfrequency)
    #         .render(sourcefile)
    # )
    # refile = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\评论情感分析组合表.html"

    # Page.save_resize_html(sourcefile,cfg_file=json,dest=refile)

#用同样的作案手法再来一发饼图，这次情感区间分得粗略些
def CountFrequency_Pie(sentiment):
    # 将评论情感分成10个区间
    a = pd.cut(sentiment,
               [0, 0.2, 0.4, 0.6, 0.8, 1],
               labels=[u"非常负面", u"比较负面", u"情绪中立", u"比较正面", u"非常正面"])
    # 计算每个区间出现的频率
    b = a.value_counts()
    b = b.sort_index()
    # 将series类型的b转换为dataframe类型，便于使用pyecharts绘图
    frequency_pie = {'section': b.index, 'frequency': b.values}
    frequency_pie = pd.DataFrame(frequency_pie)
    print(frequency_pie)
    return frequency_pie



if __name__ == '__main__':
    df=ReadFile(FileRoute)
    df['评论']=df['评论'].apply(str)
    df['sentiment']=df['评论'].apply(EmotionEvaluate)
    dataAnalysis(df['sentiment'])
    frequency=CountFrequence(df['sentiment'])
    frequency_pie=CountFrequency_Pie(df['sentiment'])
    DrawEcharts(frequency,frequency_pie)
