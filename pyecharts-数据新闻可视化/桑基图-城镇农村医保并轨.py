from pyecharts import options as opts
from pyecharts.charts import Sankey,Line,Page,Grid
import pandas as pd

colors = [
    "#67001f",
    "#b2182b",
    "#d6604d",
    "#f4a582",
    "#fddbc7",
    "#d1e5f0",
    "#92c5de",
    "#4393c3",
    "#2166ac",
    "#053061",
]
nodes = [
    {"name": "2013：城镇居民医保"},
    {"name": "2013：新农合"},
    {"name": "2014：城镇居民医保"},
    {"name": "2014：新农合"},
    {"name": "2015：城镇居民医保"},
    {"name": "2015：新农合"},
    {"name": "2016：城镇居民医保"},
    {"name": "2016：城乡居民医保"},
    {"name": "2016：新农合"},
    {"name": "2017：城镇居民医保"},
    {"name": "2017：城乡居民医保"},
    {"name": "2017：新农合"},
    {"name": "2018：城镇居民医保"},
    {"name": "2018：城乡居民医保"},
    {"name": "2018：新农合"},
]
links = [
    {"source": "2013：城镇居民医保", "target": "2014：城镇居民医保", "value": 1494.4},
    {"source": "2013：新农合", "target": "2014：新农合", "value": 3074.9},
    {"source": "2014：城镇居民医保", "target": "2015：城镇居民医保", "value": 2085.1},
    {"source": "2014：新农合", "target": "2015：新农合", "value": 3197.5},
    {"source": "2015：城镇居民医保", "target": "2016：城镇居民医保", "value": 696.4},
    {"source": "2015：城镇居民医保", "target": "2016：城乡居民医保", "value": 2220.6},
    {"source": "2015：新农合", "target": "2016：新农合", "value": 3230.6},
    {"source": "2016：新农合", "target": "2017：新农合", "value": 999.8},
    {"source": "2017：新农合", "target": "2018：新农合", "value": 695.4},
    {"source": "2016：城镇居民医保", "target": "2017：城镇居民医保", "value": 282.6},
    {"source": "2016：城乡居民医保", "target": "2017：城乡居民医保", "value": 5472.3},
    {"source": "2017：城镇居民医保", "target": "2018：城镇居民医保", "value": 200.4},
    {"source": "2017：城乡居民医保", "target": "2018：城乡居民医保", "value": 6653.1},
]
c = (
    Sankey()
    .set_colors(colors)
    .add(
        "城乡居民基本医保筹资",
        nodes=nodes,
        links=links,
        pos_bottom="10%",
        focus_node_adjacency="allEdges",
        orient="horizon",
        linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
        label_opts=opts.LabelOpts(position="top"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="城镇医保与新农合改革",subtitle="数据来源：中国卫生健康统计年鉴"),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        legend_opts=opts.LegendOpts(is_show=False,pos_top="20%",pos_left="0%")
    )
    .render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\04-光明的未来？选择者与被选择者\02-医疗保障改革.html")
)

df=pd.read_excel(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\城乡卫生支出.xlsx")

year=df['年份']
city_expenditure=df['城市'].tolist()
country_expenditure=df['农村'].tolist()
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
        legend_opts=opts.LegendOpts(pos_bottom="1%")
        )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False),)
)


sourcefile = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\16年后医疗改革.html"
json = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\医改.json"
refile = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\16年后医疗改革组合表.html"
