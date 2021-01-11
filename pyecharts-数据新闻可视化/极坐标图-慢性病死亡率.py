import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Radar, Page
from pyecharts.commons.utils import JsCode

file_route = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\医保支出、收入与结余.xlsx"
df = pd.read_excel(file_route,sheet_name="死亡原因top10")

c_schema = [
    {"name": "中风", "max": 150},
    {"name": "缺血性心脏疾病", "max": 150},
    {"name": "气管、支气管和肺癌", "max": 150},
    {"name": "慢性阻塞性肺疾病", "max": 150},
    {"name": "肝癌", "max": 150},
    {"name": "交通事故", "max": 150},
    {"name": "胃癌", "max": 150},
    {"name": "痴呆症", "max": 150},
    {"name": "神经性疾病", "max": 150},
    {"name": "高血压心脏病", "max": 150},
]
d_schema = [
    {"name": "中风", "max": 2650},
    {"name": "缺血性心脏疾病", "max": 2650},
    {"name": "气管、支气管和肺癌", "max": 2650},
    {"name": "慢性阻塞性肺疾病", "max": 2650},
    {"name": "肝癌", "max": 2650},
    {"name": "交通事故", "max": 2650},
    {"name": "胃癌", "max": 2650},
    {"name": "痴呆症", "max": 2650},
    {"name": "神经性疾病", "max": 2650},
    {"name": "高血压心脏病", "max": 2650},
]

route1=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\02-撕裂的城乡：强者愈强的游戏\10-死亡原因及比例.html"
route2=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\02-撕裂的城乡：强者愈强的游戏\11-死亡原因及损害寿命.html"

c = (
    Radar()
    .add_schema(schema=c_schema, shape="circle")
    .add("1990年：死亡原因及比例(每十万人)", [df['1990-死亡率'].tolist()], color="#f9713c")
    .add("2017年：死亡原因及比例(每十万人)", [df['2017-死亡率'].tolist()], color="#b3e4a1")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="1990-2017年各类疾病死亡率及原因", subtitle="数据来源：柳叶刀"),
                     legend_opts=opts.LegendOpts(pos_bottom="1%"))
    .render(route1)
)

d = (
    Radar()
    .add_schema(schema=d_schema, shape="circle")
    .add("1990年：死亡原因及损害寿命(年)", [df['1990-YLL'].tolist()], color="#f9713c")
    .add("2017年：死亡原因及损害寿命(年)", [df['2017-YLL'].tolist()], color="#b3e4a1")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="1990-2017年各类疾病死亡损害寿命", subtitle="数据来源：柳叶刀"),
                     legend_opts=opts.LegendOpts(pos_bottom="1%"))
    .render(route2)
)

soursefile=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\各种死亡原因.html"
json=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\死亡.json"
refile=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\各种排好版的死亡原因.html"

# page=Page(layout=Page.DraggablePageLayout)
# page.add(c,d)
# page.render(soursefile)
# Page.save_resize_html(soursefile, cfg_file=json, dest=refile)
