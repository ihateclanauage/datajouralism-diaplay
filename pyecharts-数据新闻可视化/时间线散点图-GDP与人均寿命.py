import math

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Scatter, Timeline

FileRoute_aging = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\historic-and-un-pop-projections-by-age.csv"
FileRoute_gdp = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\average-real-gdp-per-capita-across-countries-and-regions.csv"
writeRoute=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\好像自己手动做数据集也没那么麻烦.xlsx"

def readFile(FileRoute_aging, FileRoute_gdp):
    df_aging = pd.read_csv(FileRoute_aging)
    df_gdp = pd.read_csv(FileRoute_gdp)
    df=pd.merge(df_aging,df_gdp,on=['Entity','Code','Year'])
    df['Gross GDP']=df['Estimates, 1950 - 2020: Total population by broad age group, both sexes combined (thousands) - Total']*df['Real GDP per capita in 2011US$, multiple benchmarks (Maddison Project Database (2018))']
    df['Aging Ratio']=(df['Estimates, 1950 - 2020: Total population by broad age group, both sexes combined (thousands) - Population aged 65 or over']/df['Estimates, 1950 - 2020: Total population by broad age group, both sexes combined (thousands) - Total'])*100
    return df

df=readFile(FileRoute_aging,FileRoute_gdp)
df.to_excel(writeRoute)
df=pd.read_excel(writeRoute)

ti=Timeline()
ti.add_schema(is_auto_play=True, play_interval=500)
for i in range(1950,2016):
    data=df.loc[df['Year']==i].reset_index(drop=True)
    scatter=Scatter()
    for j in range(len(data.index)):
        scatter.add_xaxis(data['Real GDP per capita in 2011US$, multiple benchmarks (Maddison Project Database (2018))'].loc[df['Entity']==df['Entity'][j]].tolist())
        scatter.add_yaxis(data['Entity'][j],
                          data['Aging Ratio'].loc[df['Entity']==df['Entity'][j]].tolist(),
                          label_opts=opts.LabelOpts(is_show=False),

                          )
        scatter.set_global_opts(
            title_opts=opts.TitleOpts(
                title='各国历年人均GDP与老龄化人口占比变化',
                subtitle='数据来源：Our World in Data',
                pos_right='7%',
            ),
            legend_opts=opts.LegendOpts(
                is_show=False, pos_right='7%', pos_bottom="7%", item_height=5, item_width=5,
            ),
            xaxis_opts=opts.AxisOpts(
                name='人均GDP(亿元)',
                type_="value", splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            yaxis_opts=opts.AxisOpts(
                name='老龄人口占比(%)',
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True, trigger='axis', axis_pointer_type='cross'),
        )
    ti.add(scatter,"{}年".format(i))

ti.render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\各国历年人均GDP与老龄化人口占比变化.html")



