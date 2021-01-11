from pyecharts import options as opts
from pyecharts.charts import Map, Grid
import pandas as pd

fileroute = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\2020各地平均寿命.txt"

provinces='''
北京
天津
河北
山西
内蒙古
辽宁
吉林
黑龙江
上海
江苏
浙江
安徽
福建
江西
山东
河南
湖北
湖南
广东
广西
海南
重庆
四川
贵州
云南
西藏
陕西
甘肃
青海
宁夏
新疆
'''

value_city='''
40346.3
30283.6
20600.3
18404
23637.8
25379.4
20051.2
19269.8
42304.3
27726.3
31924.2
20740.2
25980.5
19244.5
23072.1
19422.3
21275.6
23162.6
30197.9
18348.6
20371.9
22759.2
21990.6
20347.8
19559.7
21087.5
20388.2
20659.4
21473
20219.5
22796.9
'''

value_country='''
18810.5
16385.9
10535.9
8424
12184.4
10787.3
10279.4
10523.9
18089.8
15611.5
18093.4
11106.1
14003.4
9870.4
10342.1
9211.5
11632.5
11533.6
13199.6
9436.6
9599.4
10936.1
11396.7
8299
8027.3
6691.5
9305.6
8029.7
9902.7
9982.1
8712.6
'''

df = pd.read_csv(fileroute)
province = df['省份'].tolist()
life_expectancy = df['寿命'].tolist()

provinces=provinces.split('\n')
value_city=value_city.split('\n')
value_country=value_country.split('\n')

c = (
    Map(init_opts=opts.InitOpts())
    .add("各省城人均寿命", [list(z) for z in zip(province, life_expectancy)], "china",is_map_symbol_show=False,)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国各省人均寿命", subtitle="数据来源：中国卫生健康统计年鉴"),
        visualmap_opts=opts.VisualMapOpts(min_=68.1,max_= 80.3),
        legend_opts=opts.LegendOpts(is_show=False)
    )
)

grid=(
    Grid()
    .add(c,grid_opts=opts.GridOpts(width="120%",height="120%"))
    .render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\01-看病的人：他们从哪里来，到哪里去\100-各省人均寿命.html")
)
