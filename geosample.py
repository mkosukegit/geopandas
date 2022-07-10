import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import shapely as shapely
from shapely.geometry import Polygon

kyoku_x = 139.79103
kyoku_y = 35.66761

# ポリゴン作成
x = [139.76275, 139.79346, 139.79346, 139.75800]
y = [35.67991, 35.67991, 35.66388, 35.666265]
polygon_geom = Polygon(zip(x, y))
# shapefile 読み込み
path_shp = "./N03-20210101_13_GML/N03-21_13_210101.shp"
gdf = gpd.read_file(path_shp)
gdf.head()

print(gdf.iloc[1].geometry)
# 描画(東京)
plt.figure()
plt.plot(*gdf.iloc[1].geometry.exterior.xy)
plt.plot(*polygon_geom.exterior.xy)
plt.plot(kyoku_x, kyoku_y, marker='.')
# for data in gdf.iloc:
#     plt.plot(*data.geometry.exterior.xy)
plt.show()
plt.close()

# ポリゴン判定
# ポリゴンを取得
poly0 = gdf.iloc[1].geometry
mesh = polygon_geom
# 判定対象の緯度経度
kyoku = shapely.geometry.point.Point(kyoku_x, kyoku_y)
isInPoligon = poly0.contains(kyoku)
isInMesh = mesh.contains(kyoku)
intersection = poly0.intersection(mesh)
plt.figure()
plt.plot(*intersection.exterior.xy)
plt.show()
plt.close()
if isInPoligon & isInMesh:
    print("ポリゴンに入ってます")
elif isInPoligon:
    print("in 千代田")
elif isInMesh:
    print("in メッシュ")
else:
    print("ポリゴンに入ってないです")
