#注释：以下为"购买水果计费.py"的代码，请不要删除①和②以外的任何代码。
#如果购买水果斤数小于10，则每斤按10元/斤计算，否则，全部按每斤8元/斤计算。求购买水果的费用。

x= float(input("请输入购买水果的重量（斤）:"))
if x<10：
    total=10*x
else:
    total=8*x
print("购买水果的费用为：",total)
