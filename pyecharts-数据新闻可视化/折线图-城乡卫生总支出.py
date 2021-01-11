import pyecharts.options as opts
from pyecharts.charts import Line, Bar, Grid
import pandas as pd

df=pd.read_excel(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\城乡卫生支出.xlsx")

year=df['年份'][0:29]
city_expenditure=df['城市'][0:29].tolist()
country_expenditure=df['农村'][0:29].tolist()
city_percapita=df['城市人均']
country_percapita=df['农村人均']
total=df['总计'].tolist()

line = (
    Line()
    .add_xaxis(xaxis_data=year)
    .add_yaxis(series_name="城市卫生人均费用",y_axis=city_percapita,is_smooth=True)
    .add_yaxis(series_name="乡村卫生人均费用",y_axis=country_percapita,is_smooth=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="城乡卫生费用支出", subtitle="数据来源：中国卫生健康统计年鉴"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        toolbox_opts=opts.ToolboxOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        legend_opts=opts.LegendOpts(is_show=False)
        )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False),)
)

line.render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\02-撕裂的城乡：强者愈强的游戏\12-16年前城乡卫生费用支出.html")