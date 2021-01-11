from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType,SymbolType
from pyecharts.globals import ThemeType

geo=Geo()

#地图类型为中国地图
geo.add_schema(
    maptype='china',
    itemstyle_opts=opts.ItemStyleOpts(color="#323c48", border_color="#111"),
    )

#添加流向
geo.add("各省患者流向",
        [("西藏","上海"),
         ("西藏","北京"),
         ("西藏","江苏"),
         ("西藏","浙江"),
         ("安徽","上海"),
         ("安徽","北京"),
         ("安徽","江苏"),
         ("安徽","浙江"),
         ("内蒙古","上海"),
         ("内蒙古","北京"),
         ("内蒙古","江苏"),
         ("内蒙古","浙江"),
         ("河北","上海"),
         ("河北","北京"),
         ("河北","江苏"),
         ("河北","浙江"),
         ("甘肃", "上海"),
         ("甘肃", "北京"),
         ("甘肃", "江苏"),
         ("甘肃", "浙江")],
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW, symbol_size=6, color="yellow"),
        linestyle_opts=opts.LineStyleOpts(curve=0.3),
        is_large=True)

#添加数据点
geo.add("患者流入/流出百分比(%)",[("上海",18.9),("北京",14.7),("江苏",14.0),("浙江",12.1),
            ("西藏",27.6),("安徽",18.8),("内蒙古",16.0),("河北",14.3),("甘肃",11.8)],
        type_=ChartType.EFFECT_SCATTER)

#标签太难看了！必须去掉
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=10,max_=30),
                    title_opts=opts.TitleOpts(
                        title="各省患者异地就诊流向地图",subtitle="数据来源：2017年国家医疗服务与质量安全报告"),
                    legend_opts=opts.LegendOpts(is_show=False)
                    )

#生成html文件
geo.render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\01-看病的人：他们从哪里来，到哪里去\02-全国患者流向.html")

