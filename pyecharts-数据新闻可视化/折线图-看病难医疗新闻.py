import pandas as pd
from pyecharts.charts import Line,Grid
import pyecharts.options as opts

file_route=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\看病难-新闻报道.xlsx"
df=pd.read_excel(file_route)

year=df['年份']
report=df['报道数量']

line = (
    Line()
    .add_xaxis(xaxis_data=year)
    .add_yaxis(series_name="报道数量",y_axis=report,is_smooth=False)
    .set_global_opts(title_opts=opts.TitleOpts(title="传统媒体对“看病难”问题的历年跟踪报道", subtitle="数据来源：CND中文新闻数据库"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        toolbox_opts=opts.ToolboxOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        legend_opts=opts.LegendOpts(is_show=False)
        )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True),)
    .render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\02-撕裂的城乡：强者愈强的游戏\03-媒体报道.html")
)

