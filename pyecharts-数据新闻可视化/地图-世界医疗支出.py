import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map


file_route=r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\好烦啊我还是手动做数据集吧！！！.xlsx"

df = pd.read_excel(file_route)
country = '''
Algeria
Argentina
Australia
Bangladesh
Bolivia
Brazil
Bulgaria
Burkina Faso
Burundi
Canada
Chile
China
Colombia
Costa Rica
Cote d'Ivoire
Croatia
Czechia
Denmark
Dominican Republic
Ecuador
Egypt
El Salvador
Estonia
Ethiopia
Finland
France
Germany
Ghana
Guatemala
Guinea
Guinea-Bissau
Honduras
Hungary
India
Indonesia
Iran
Israel
Italy
Jordan
Kenya
Laos
Latvia
Lesotho
Lithuania
Madagascar
Malaysia
Mali
Mauritania
Mexico
Mongolia
Morocco
Netherlands
New Zealand
Nicaragua
Niger
Nigeria
Norway
Pakistan
Panama
Paraguay
Philippines
Poland
Portugal
Romania
Russia
Rwanda
Senegal
Slovenia
South Africa
Spain
Sri Lanka
Sweden
Tanzania
Thailand
Tunisia
Turkey
Uganda
Ukraine
United Kingdom
United States
Uruguay
Vietnam
Zambia
'''
health_expenditure='''
1031.16964
1389.840341
4491.629858
88.03535581
445.8226242
1391.52257
1491.868089
96.10067087
63.73553919
4600.088285
1903.118645
762.2437789
852.8121654
1286.462817
189.6011903
1656.426156
2469.851757
5083.20928
873.1177009
980.2299724
495.1650809
578.4609406
1886.814387
65.60194586
3996.436879
4542.307106
5356.811177
249.328504
443.9018463
57.19135929
100.2957262
353.3645701
1912.069053
237.7234161
369.2864404
1261.730503
2819.111414
3350.575515
568.122532
157.1920959
165.8303456
1429.309665
251.1429737
1874.615864
76.74339356
1063.888395
118.4518361
177.0806661
1008.676198
469.563584
435.2900287
5313.243391
3530.096913
405.9922707
68.46968478
215.223799
6221.641638
134.4414606
1542.796273
724.3116252
322.7779997
1704.195989
2661.397049
1090.416516
1414.028282
143.1853392
97.08918675
2733.762624
1086.409415
3182.544019
353.1291505
5298.603868
96.49687717
610.1700037
774.0570073
995.9660375
138.5283968
469.4283772
4144.60079
9535.945335
1747.771686
334.319988
203.0385646
'''

country=country.split('\n')
health_expenditure=health_expenditure.split('\n')

c = (
    Map()
    .add("人均卫生支出", [list(z) for z in zip(country, health_expenditure)], "world", is_map_symbol_show=False,)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="世界人均卫生支出", subtitle="数据来源：Our World in Data"),
        visualmap_opts=opts.VisualMapOpts(max_=5000),
    )
    .render(r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\可视化-数据图表\世界人均卫生支出.html")
)