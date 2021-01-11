import pyecharts.options as opts
from pyecharts.charts import Line, Grid, Bar, Page
import pandas as pd

FileRoute = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\2018年医疗人员构成.xlsx"
df = pd.read_excel(FileRoute)

print(df)


# 先画折线图试探一下
def line(x, seriesname, y, legend):
    line = (
        Line()
            .add_xaxis(x.tolist())
            .add_yaxis(seriesname, y.tolist(), is_smooth=True)
            .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
                is_show=True,
            ),
            yaxis_opts=opts.AxisOpts(
                is_show=False,
            ),
            legend_opts=opts.LegendOpts(
                pos_left=legend
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True, trigger="axis", axis_pointer_type="cross"
            ),
            toolbox_opts=opts.ToolboxOpts(
                is_show=False,
            )
        )
    )
    return line


def line_n(variable, start, end, legend):
    line1 = line(df['分类标准'][start:end], variable, df['执业医师'][start:end], legend)
    line2 = line(df['分类标准'][start:end], variable, df['医院人员'][start:end], legend)
    line3 = line(df['分类标准'][start:end], variable, df['社区卫生服务中心'][start:end], legend)
    line4 = line(df['分类标准'][start:end], variable, df['乡镇卫生院人员'][start:end], legend)
    line5 = line(df['分类标准'][start:end], variable, df['村卫生室人员'][start:end], legend)
    return line1, line2, line3, line4, line5


# 年龄分布情况
age_line1, age_line2, age_line3, age_line4, age_line5 = line_n("年龄", 1, 6, "15%")
# 工作年限分布情况
exp_line1, exp_line2, exp_line3, exp_line4, exp_line5 = line_n("工作年限", 8, 12, "30%")


# 职称和学历是非连续变量，只能用条状图啦
def bar(x, seriesname, y, legend):
    bar = (
        Bar()
            .add_xaxis(x.tolist())
            .add_yaxis(seriesname, y.tolist(), category_gap="0%")
            .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                is_scale=False,
                boundary_gap=False,
                is_show=True,
            ),
            yaxis_opts=opts.AxisOpts(
                is_show=False,
            ),
            legend_opts=opts.LegendOpts(
                pos_left=legend
            ),
        )
    )
    return bar


def bar_n(start, end, variable, legend):
    bar1 = bar(df['分类标准'][start:end], variable, df['执业医师'][start:end], legend)
    bar2 = bar(df['分类标准'][start:end], variable, df['医院人员'][start:end], legend)
    bar3 = bar(df['分类标准'][start:end], variable, df['社区卫生服务中心'][start:end], legend)
    bar4 = bar(df['分类标准'][start:end], variable, df['乡镇卫生院人员'][start:end], legend)
    bar5 = bar(df['分类标准'][start:end], variable, df['村卫生室人员'][start:end], legend)
    return bar1, bar2, bar3, bar4, bar5


# 学历分布
edu_bar1, edu_bar2, edu_bar3, edu_bar4, edu_bar5 = bar_n(14, 18, "学历", "50%")
# 职称分布
pro_bar1, pro_bar2, pro_bar3, pro_bar4, pro_bar5 = bar_n(20, 25, "职称", "65%")

grid = Grid()


def grid_rank(graph, pos_top, pos_left):
    grid.add(graph, grid_opts=opts.GridOpts(pos_top=pos_top, pos_left=pos_left, height="10%", width="10%"))


grid_rank(age_line1, "17%", "17%")
grid_rank(age_line2, "32%", "17%")
grid_rank(age_line3, "47%", "17%")
grid_rank(age_line4, "62%", "17%")
grid_rank(age_line5, "77%", "17%")

grid_rank(exp_line1, "17%", "35%")
grid_rank(exp_line2, "32%", "35%")
grid_rank(exp_line3, "47%", "35%")
grid_rank(exp_line4, "62%", "35%")
grid_rank(exp_line5, "77%", "35%")

grid_rank(edu_bar1, "17%", "52%")
grid_rank(edu_bar2, "32%", "52%")
grid_rank(edu_bar3, "47%", "52%")
grid_rank(edu_bar4, "62%", "52%")
grid_rank(edu_bar5, "77%", "52%")

grid_rank(pro_bar1, "17%", "67%")
grid_rank(pro_bar2, "32%", "67%")
grid_rank(pro_bar3, "47%", "67%")
grid_rank(pro_bar4, "62%", "67%")
grid_rank(pro_bar5, "77%", "67%")


def title(_title,_subtitle, pos_top):
    barless = (Bar()
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title=_title,
            subtitle=_subtitle,
            pos_top=pos_top,
        ),
        xaxis_opts=opts.AxisOpts(
            is_show=False,
        ),
        yaxis_opts=opts.AxisOpts(
            is_show=False,
        )
    )
    )
    return barless


barless1 = title("执业", "", "17%")
barless2 = title("医院", "", "32%")
barless3 = title("社区", "", "47%")
barless4 = title("乡镇", "", "62%")
barless5 = title("村站", "", "77%")

grid_rank(barless1, "17%", "67%")
grid_rank(barless2, "32%", "67%")
grid_rank(barless3, "47%", "67%")
grid_rank(barless4, "62%", "67%")
grid_rank(barless5, "77%", "67%")

grid.render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\04-光明的未来？选择者与被选择者\04-城乡卫生人员构成对比.html")

#从这里开始是简单的折线图
year_range=["1950","1955","1960","1965","1970","1975","1980","1985","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018"]
doctor_num=[611240,1052787,1769205,1872300,6571795,7435212,7355483,5606105,6137711,6278458,6409307,6540522,6630710,6704395,6735097,6833962,6863315,6894985,6910383,6874527,6528674,6216971,6332739,6447246,6681184,6964389,7251803,7781448,8207502,8616040,9115705,9790483,10234213,10693881,11172945,11748972,12300325]
doctor_in_country=[0,0,0,0,4779280,4841695,3820776,1293094,1231510,1253324,1269061,1325106,1323701,1331017,1316095,1317786,1327633,1324937,1319357,1290595,1290595,867778,883075,916532,957459,931761,938313,1050991,1091863,1126443,1094419,1081063,1058182,1031525,1000324,968611,907098]

c = (
    Line()
    .add_xaxis(xaxis_data=year_range)
    .add_yaxis(series_name="卫生人员总数",y_axis=doctor_num,is_smooth=True)
    .add_yaxis(series_name="乡村医生和卫生员数量",y_axis=doctor_in_country,is_smooth=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="卫生人员结构变化趋势", subtitle="数据来源：中国卫生健康统计年鉴"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        toolbox_opts=opts.ToolboxOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    # .render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\04-光明的未来？选择者与被选择者\04-城乡卫生人员构成对比.html")
)

sourcefile = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\医生问题.html"
json = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\医生.json"
refile = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\医生质量组合图表.html"
# page=(Page(layout=Page.DraggablePageLayout)
#       .add(c,grid)
#       .render())
