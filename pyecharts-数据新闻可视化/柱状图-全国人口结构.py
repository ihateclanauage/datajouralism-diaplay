import pyecharts.options as opts
from pyecharts.charts import Line, Bar
from pyecharts.faker import Faker
import pandas as pd

FileRoute = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\中国人口结构.xlsx"
df=pd.read_excel(FileRoute)

c = (
    Bar()
    .add_xaxis(df['Year'].tolist())
    .add_yaxis("5岁以下人口", df['under age 5'].tolist(),
               stack='总人口',
               label_opts=opts.LabelOpts(is_show=False),
               )
    .add_yaxis("5~15岁人口", df['under age 15'].tolist(),
               stack='总人口',
               label_opts=opts.LabelOpts(is_show=False),
               )
    .add_yaxis("15~25岁人口", df['under age 25'].tolist(),
               stack='总人口',
               label_opts=opts.LabelOpts(is_show=False),
               )
    .add_yaxis("25~65岁人口", df['aged 25-64'].tolist(),
               stack='总人口',
               label_opts=opts.LabelOpts(is_show=False),
               )
    .add_yaxis("65岁及以上人口", df['aged 65 or over'].tolist(),
               stack='总人口',
               label_opts=opts.LabelOpts(is_show=False),
               )
    .set_global_opts(title_opts=opts.TitleOpts(title="1950-2100年中国人口年龄结构", subtitle="数据来源：Our World in Data"),
                     tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
                     xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False, is_scale=True),
                     yaxis_opts=opts.AxisOpts(
                         type_="value",
                         axistick_opts=opts.AxisTickOpts(is_show=True),
                         splitline_opts=opts.SplitLineOpts(is_show=True),
                     ),
                     legend_opts=opts.LegendOpts(is_show=False,pos_bottom="1%"),
                     )
)

c.render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\02-撕裂的城乡：强者愈强的游戏\09-中国人口结构预测.html")
