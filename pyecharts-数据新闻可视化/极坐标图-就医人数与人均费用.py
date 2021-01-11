import pandas as pd
from pyecharts.charts import Polar, Grid, Page
from pyecharts.commons.utils import JsCode
import pyecharts.options as opts

file_route = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\历年诊疗费用.xlsx"

df = pd.read_excel(file_route)

year = df['年份'].tolist()
hospital = df['医院诊疗人次数'].tolist()
country = df['基层医疗卫生机构诊疗人次数'].tolist()
inhospital = df['医院入院人数'].tolist()
incountry = df['基层医疗卫生机构入院人数'].tolist()

df2 = pd.read_excel(file_route, sheet_name="Sheet2")
year2 = df2['年份'].tolist()
mediex =  df2['医院门诊病人次均医药费（元）'].tolist()
hosptex = df2['医院住院病人人均医药费（元）'].tolist()
comm_mediex = df2['社区卫生服务中心门诊病人次均医药费（元）'].tolist()
comm_hosptex = df2['社区卫生服务中心住院病人人均医药费（元）'].tolist()
coun_mediex = df2['乡镇卫生机构门诊病人次均医药费（元）'].tolist()
coun_hosptex = df2['乡镇卫生机构住院病人人均医药费（元）'].tolist()

route1=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\02-撕裂的城乡：强者愈强的游戏\04-历年就医人数.html"
route2=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\02-撕裂的城乡：强者愈强的游戏\05-历年住院人数.html"
route3=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\02-撕裂的城乡：强者愈强的游戏\06-历年人均医药费用.html"
route4=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\02-撕裂的城乡：强者愈强的游戏\07-历年人均住院费用.html"

polar=(
    Polar()
    .add_schema(angleaxis_opts=opts.AngleAxisOpts(data=year, type_="category"))
    .add("医院诊疗人次数", hospital, type_="bar", stack="总诊疗人数")
    .add("基层医疗卫生机构诊疗人次数", country, type_="bar", stack="总诊疗人数")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国历年医疗机构接诊人次数", subtitle="数据来源：中国卫生健康统计年鉴"),
        legend_opts=opts.LegendOpts(pos_bottom="1%"),
        tooltip_opts=opts.TooltipOpts(
        is_show=True, trigger='axis', axis_pointer_type="cross",
    ),
        xaxis_opts=opts.AxisOpts(
            type_='category',
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_='shadow'),
        )
    )
    .render(route1)
)

polar2=(
    Polar()
    .add_schema(angleaxis_opts=opts.AngleAxisOpts(data=year, type_="category"))
    .add("医院入院人数", inhospital, type_="bar", stack="总入院人数")
    .add("基层医疗卫生机构入院人数", incountry, type_="bar", stack="总入院诊疗人数")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国历年医疗机构入院人次数", subtitle="数据来源：中国卫生健康统计年鉴"),
        legend_opts=opts.LegendOpts(pos_bottom="1%"),
        tooltip_opts=opts.TooltipOpts(
        is_show=True, trigger='axis', axis_pointer_type="cross",
    ),
        xaxis_opts=opts.AxisOpts(
            type_='category',
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_='shadow'),
        )
    )
    .render(route2)
)

polar3=(
    Polar()
    .add_schema(radiusaxis_opts=opts.RadiusAxisOpts(data=year2),
                angleaxis_opts=opts.AngleAxisOpts(is_clockwise=True))
    .add("医院门诊病人次均医药费（元）", mediex, type_="bar", stack="总人均医药费用")
    .add("社区卫生服务中心门诊病人次均医药费（元）", comm_mediex, type_="bar", stack="总人均医药费用")
    .add("乡镇卫生机构门诊病人次均医药费（元）", coun_mediex, type_="bar", stack="总人均医药费用")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国各级医疗机构人均医药费用", subtitle="数据来源：中国卫生健康统计年鉴"),
        legend_opts=opts.LegendOpts(pos_bottom="1%"),
        tooltip_opts=opts.TooltipOpts(
        is_show=True, trigger='axis', axis_pointer_type="cross",
    ),
        xaxis_opts=opts.AxisOpts(
            type_='category',
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_='shadow'),
        )
    )
    .render(route3)
)

polar4=(
    Polar()
    .add_schema(radiusaxis_opts=opts.RadiusAxisOpts(data=year2),
                angleaxis_opts=opts.AngleAxisOpts(is_clockwise=False))
    .add("医院住院病人次均医药费（元）", hosptex, type_="bar", stack="总人均住院费用")
    .add("社区卫生服务中心住院病人次均医药费（元）", comm_hosptex, type_="bar", stack="总人均住院费用")
    .add("乡镇卫生机构住院病人次均医药费（元）", coun_hosptex, type_="bar", stack="总人均住院费用")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国各级医疗机构人均住院费用", subtitle="数据来源：中国卫生健康统计年鉴"),
        legend_opts=opts.LegendOpts(pos_bottom="1%"),
        tooltip_opts=opts.TooltipOpts(
        is_show=True, trigger='axis', axis_pointer_type="cross",
    ),
        xaxis_opts=opts.AxisOpts(
            type_='category',
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_='shadow'),
        )
    )
    .render(route4)
)

soursefile=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\各种极坐标图.html"
json=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\chart_config(1).json"
refile=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\各种排好版的极坐标图.html"

# page=Page(layout=Page.DraggablePageLayout)
# page.add(polar,polar2,polar3,polar4)
# page.render(soursefile)
# Page.save_resize_html(soursefile, cfg_file=json, dest=refile)


