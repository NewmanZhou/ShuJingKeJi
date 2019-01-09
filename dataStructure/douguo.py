# -*- coding: utf-8 -*-

# 豆果美食 网站采集 数据结构及字段说明：

'''
数据采集的起始点：
根据菜谱分类 进行扩展采集

字典命名 对应 数据库名字

唯一索引，用联合索引 做去重处理（一级菜单，二级菜单，三级菜单，菜品的ID）
'''

douguoItems = {
    # 第一部分
    'topTitle': '热门',  # 一级分类名称
    'secondTitle': '热门食材',  # 二级分类名称
    'title': '面条',  # 三级分类名称
    'titleUrl': 'https://www.douguo.com/caipu/面条',  # 三级分类的链接
    # 第二部分
    'dishes': '荷包蛋面条',  # 菜品名称
    'dishesImg': 'https://cp1.douguo.com/upload/caiku/9/e/9/400x266_9e2a3a7817ade66010ac1de26adee019.jpg',  # 菜品的展示图链接
    'dishesID': '1054561',  # 菜品ID
    'dishesUrl': '1054561.html',  # 菜品链接
    'browse': '463500',  # 浏览数
    'collect': '10383',  # 收藏数
    'userName': 'lin悠然11',  # 发布者
    'userID':'', # 发布者ID
    'userUrl':'', # 发布者链接
    'userImg': 'https://tx1.douguo.com/upload/photo/e/b/d/70_u153299177777809300935.jpg',  # 发布者头像地址
    # 第三部分
    'abstract':'', # 简介
    'materialList': [
        {'material': '面条', 'number': '400g'},
        {'material': '小葱', 'number': '4根'},
        {'material': '鸡蛋', 'number': '2个'},
        {'material': '酱烧葱花油', 'number': '2勺'},
        {'material': '白醋', 'number': '1勺'},
        {'material': '盐', 'number': ' 1勺'},
    ],  # 食材清单
    'processList': [
        {'process': '所需材料',
         'img': 'https://cp1.douguo.com/upload/caiku/2/9/f/yuan_29388b1a74c2971d2ee481067b41105f.jpg'},
        {'process': '小葱切碎',
         'img': 'https://cp1.douguo.com/upload/caiku/b/7/1/yuan_b7e43a08d3eb83ee35b1cb7c26d944a1.jpg'},
        {'process': '锅里烧水，水开后开最小火，将鸡蛋打入煮荷包蛋，先用最小火，让荷包蛋定型。',
         'img': 'https://cp1.douguo.com/upload/caiku/8/3/7/200_8305652b4dee8c669868a9dd199e7f37.jpg'},
        {'process': '另起一锅烧水，水开后下面条.',
         'img': 'https://cp1.douguo.com/upload/caiku/d/4/4/yuan_d4e3c0737a44e6de7123c21819a61d64.jpg'},
        {'process': '荷包蛋煮好。',
         'img': 'https://cp1.douguo.com/upload/caiku/c/2/9/yuan_c271ce190e7c909fc5d3facce8f43439.jpg'},
        {'process': '将面条捞出，放上葱花和葱花油，调入适量盐和醋，再将荷包蛋舀入，最后将煮荷包蛋的汤过滤倒入即可。',
         'img': 'https://cp1.douguo.com/upload/caiku/a/6/2/yuan_a6fd7f2e35349e63c0be4c1416954822.jpg'},
    ],  # 烹饪流程
    'tips': '酱烧葱花油就是将葱花放入碗中，倒入适量生抽，如果想要颜色深可用老抽，然后将油烧热，浇进去即可。',  # 小贴士
    'classify': ['面条', '主食', '孕妇', '晚餐', '锅具'],  # 分类 + 链接
    'relatedMenu':['ID+链接'], # 相关菜谱ID + 链接
    'crawlTime':'', # 抓取时间
    'content':'菜谱详情原始数据', # 菜谱详情原始数据
    'source':'豆果美食', # 来源 豆果美食
    'type':0, # 状态值
}
