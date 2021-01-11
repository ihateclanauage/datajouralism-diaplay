import pyecharts.options as opts
from pyecharts.charts import Line

year_range=["1950","1955","1960","1965","1970","1975","1980","1985","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018"]
doctor_num=[611240,1052787,1769205,1872300,6571795,7435212,7355483,5606105,6137711,6278458,6409307,6540522,6630710,6704395,6735097,6833962,6863315,6894985,6910383,6874527,6528674,6216971,6332739,6447246,6681184,6964389,7251803,7781448,8207502,8616040,9115705,9790483,10234213,10693881,11172945,11748972,12300325]
doctor_in_country=[0,0,0,0,4779280,4841695,3820776,1293094,1231510,1253324,1269061,1325106,1323701,1331017,1316095,1317786,1327633,1324937,1319357,1290595,1290595,867778,883075,916532,957459,931761,938313,1050991,1091863,1126443,1094419,1081063,1058182,1031525,1000324,968611,907098]

c = (
    Line()
    .add_xaxis(xaxis_data=year_range)
    .add_yaxis(series_name="卫生人员总数",y_axis=doctor_num,is_smooth=True)
    .add_yaxis(series_name="乡村医生/乡村卫生员数量",y_axis=doctor_in_country,is_smooth=True)
    .set_global_opts(title_opts=opts.TitleOpts(title="卫生人员结构变化趋势", subtitle="数据来源：中国卫生健康统计年鉴"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        toolbox_opts=opts.ToolboxOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        legend_opts=opts.LegendOpts(is_show=False)
        )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\04-光明的未来？选择者与被选择者\03-城乡卫生人员数量对比.html")
)