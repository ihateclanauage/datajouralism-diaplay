import pyecharts.options as opts
from pyecharts.charts import Line, Bar, Page
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
                     legend_opts=opts.LegendOpts(pos_bottom="1%")
                     )
)

FIleRoute = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\医保支出、收入与结余.xlsx"
df = pd.read_excel(FIleRoute)
df['年份']=df['年份'].apply(str)

print(df)

bar=(
    Bar()
    .add_xaxis(df['年份'].tolist())
    .add_yaxis(
        "全国医保基金收入",
        df['收入'].tolist(),
        yaxis_index=0
    )
    .add_yaxis(
        "全国医保基金支出",
        df['支出'].tolist(),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="结余率",
            type_="value",
            min_=0,
            max_=25,
            position="right",
            axislabel_opts=opts.LabelOpts(formatter="{value} %")
        )
    )
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
        is_show=True, trigger='axis', axis_pointer_type="cross",
    ),
        xaxis_opts=opts.AxisOpts(
            type_='category',
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_='shadow'),
        ),
        yaxis_opts=opts.AxisOpts(
            name="亿元",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        title_opts=opts.TitleOpts(
            title="中国历年医保基金收支出及结余",
            subtitle="数据来源：国家统计局官网"
        ),
        legend_opts=opts.LegendOpts(
            pos_bottom="1%"
        )
    )
    )


line=(
    Line()
    .add_xaxis(xaxis_data=df['年份'].tolist())
    .add_yaxis(series_name="全国医保基金结余率", y_axis=df['结余率'].tolist(),yaxis_index=1,z_level=1)
    .set_global_opts(
        toolbox_opts=opts.ToolboxOpts(is_show=True),
    )
)


FileRoute = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\中国人口结构.xlsx"
df=pd.read_excel(FileRoute)

sourcefile=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\老龄化与城市化.html"
json=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\格式.json"
refile=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\老龄化与城市化com.html"

# page=Page(layout=Page.DraggablePageLayout)
# page.add(bar.overlap(line),c)
# page.render(sourcefile)
Page.save_resize_html(sourcefile,cfg_file=json,dest=refile)