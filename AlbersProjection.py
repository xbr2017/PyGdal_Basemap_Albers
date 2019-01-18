# _*_ coding: utf-8 _*_
__author__ = 'xbr'
__date__ = '2019/1/9 11:40'

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 中文字体设置,防止中文乱码
# 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# width为投影坐标中所需地图域的宽度(米)
# height投影坐标中所需地图域的高度(米)
# l:low低分辨率; aea:Albers Equal Area
# lat_1为第一标准线
# lat_2为第二标准线
# lon_0,lat_0为地图中心点
mp = Basemap(width=8000000, height=7000000,
            resolution='l', projection='aea',
            lat_1=40., lat_2=60., lon_0=100, lat_0=35)
mp.drawcoastlines()
mp.drawcountries()
# 内陆湖泊采用蓝色
mp.fillcontinents(color='red', lake_color='b')

# [1, 1, 0, 0]左右纬度显示, [0, 0, 0, 1]只显示下方经度
mp.drawparallels(np.arange(-80., 81, 20.), labels=[1, 1, 0, 0], fontsize=12)
mp.drawmeridians(np.arange(-180., 181., 20.), labels=[0, 0, 0, 1], fontsize=12)
# 海洋采用水青色
mp.drawmapboundary(fill_color='aqua')

# 获取当前坐标轴对象
ax = plt.gca()
# 添加地图标题
plt.title(u"Albers等面积投影")
# 将文本叠加到地图上,但是Basemap没有annotate方法,所以使用pyplot接口
# xy=(0.42, 0.47)表示本文在图中位置
# xycoords:坐标轴比例
# color:字体颜色
# fontsize:字体大小
plt.annotate(u"中华人民共和国", xy=(0.42, 0.47), xycoords='axes fraction',
             color='k', fontsize=12)
plt.show()
