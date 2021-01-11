from pyecharts.charts import Line ,Grid
from pyecharts import options as opts
import pandas as pd

file_route = r"C:\Users\User\Desktop\2020大三第一学期\数据新闻\数据集-医保问题\2020年医院预算.xlsx"
render_file = "C:\\Users\\User\\Desktop\\2020大三第一学期\\数据新闻\\可视化-数据图表\\公共医院医疗预算.html"

df = pd.read_excel(file_route)
x_data = df['公立医院'].tolist()
y_data1 = df['2019预算数(万元)'].tolist()
y_data2 = df['2020预算数(万元)'].tolist()

def line(i):
    line = (
        Line()
        .add_xaxis(xaxis_data=['2019预算数(万元)', '2020预算数(万元)'])
        .add_yaxis(
            series_name=x_data[i]+"预算数(万元)",
            y_axis=[y_data1[i],y_data2[i]],
        )
        .set_global_opts(yaxis_opts=opts.AxisOpts(type_="value", is_show=False),)
    )
    return line

line0=line(0)
line1=line(1)
line2=line(2)
line3=line(3)
line4=line(4)
line5=line(5)
line6=line(6)

grid=Grid()

def gridline(graph,postop,posleft):
    grid.add(graph, grid_opts=opts.GridOpts(pos_top=postop,pos_left=posleft,height="10%",width="10%"))

gridline(line0,"7%","7%")
gridline(line1,"37%","7%")
gridline(line2,"57%","7%")
gridline(line3,"77%","7%")
gridline(line4,"7%","37%")
gridline(line5,"37%","37%")
gridline(line6,"57%","57%")

grid.render(render_file)