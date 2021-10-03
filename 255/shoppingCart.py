
# 商品列表
goods = [{"name": "888垒球", "price": 15.0, "kuCun": 50},
         {"name": "棒球", "price": 150.0, "kuCun": 150},
         {"name": "DB篮球550", "price": 215.0, "kuCun": 20}]

for s, i in enumerate(goods):
    print("%3d %s,\n        价格是：%7.2f元,剩余库存为：%5d个" % (s, i['name'], i['price'], i['kuCun']))
money = float(input("输入余额："))
# 购买商品
cart = []
while 1:
    i = input("是否继续购买？（y是,n否）")
    if i == "n":
        break
    seq = int(input("请输入商品编号："))
    num = int(input("请输入购买数量"))
    if num > goods[seq]['kuCun']:
        print("库存不足")
    money = money - goods[seq]['price'] * num
    goods[seq]['kuCun'] -= num
    d = {"name": goods[seq]['name'], "price": goods[seq]['price'], "num": num}
    cart.append(d)
    print("你购买%d个%s，一共消费了：%.2f元" % (num, goods[seq]['name'], goods[seq]['price'] * num))
