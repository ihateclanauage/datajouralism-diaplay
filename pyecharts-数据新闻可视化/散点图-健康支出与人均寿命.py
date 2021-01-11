import pandas as pd
from pyecharts.charts import Scatter, Grid
import pyecharts.options as opts
import math

fileroute=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\好烦啊我还是手动做数据集吧！！！.xlsx"
df=pd.read_excel(fileroute)

item_color_js_2 = """new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                offset: 0,
                color: 'rgb(129, 227, 238)'
            }, {
                offset: 1,
                color: 'rgb(25, 183, 207)'
            }])"""

item_style_2 = {
    'shadowBlur': 10,
    'shadowColor': 'rgba(120, 36, 50, 0.5)',
    'shadowOffsetY': 5,
}


c=Scatter(init_opts=opts.InitOpts())
for i in range(len(df.index)):
    c.add_xaxis(xaxis_data=df["Current health expenditure per capita, PPP (current international $)"].loc[df['Entity']==df['Entity'][i]].tolist())
    c.add_yaxis(df['Entity'][i],
                y_axis=df['Life expectancy'].loc[df['Entity']==df['Entity'][i]].tolist(),
                label_opts=opts.LabelOpts(is_show=False),
                symbol_size=math.sqrt(df['Gross GDP'][i])/5e4,
                itemstyle_opts=item_style_2,
                )
c.set_series_opts()
c.set_global_opts(
    title_opts=opts.TitleOpts(
        title='各国人均卫生费用与人均寿命相关性',
        subtitle='数据来源：Our World in Data',
    ),
    legend_opts=opts.LegendOpts(
        is_show=True, pos_left='90%',pos_bottom="7%", item_height=5, item_width=5,
    ),
    xaxis_opts=opts.AxisOpts(
        name='人均健康支出',
        type_="value", splitline_opts=opts.SplitLineOpts(is_show=True),
    ),
    yaxis_opts=opts.AxisOpts(
        name='基尼指数',
        type_="value",
        axistick_opts=opts.AxisTickOpts(is_show=True),
        is_scale=True,
    ),
    tooltip_opts=opts.TooltipOpts(is_show=True,trigger='axis',axis_pointer_type='cross'),
)



grid=Grid()
grid.add(c, grid_opts=opts.GridOpts(pos_top='15%',pos_left='7%', height="80%", width="80%"))

grid.render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\各国人均卫生费用与人均寿命相关性.html")

print(df)