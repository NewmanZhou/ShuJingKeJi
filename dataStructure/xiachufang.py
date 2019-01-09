# -*- coding: utf-8 -*-

# 下厨房 网站采集 数据结构及字段说明：

'''
数据采集的起始点：
http://www.xiachufang.com/category/
根据菜谱分类 进行扩展采集

字典命名 对应 数据库名字

唯一索引，用联合索引 做去重处理（一级菜单，二级菜单，三级菜单，菜品的ID）

http://www.xiachufang.com/category/
'''

douguoItems = {
    # 第一部分
    'topTitle': '热门专题',  # 一级分类名称
    'secondTitle': '菜式',  # 二级分类名称
    'title': '家常菜',  # 三级分类名称
    'titleUrl': 'http://www.xiachufang.com/category/40076/',  # 三级分类的链接
    # 第二部分
    'dishes': '懒人版糖醋排骨',  # 菜品名称
    'dishesImg': 'http://i2.chuimg.com/4daad8ea877a11e6a9a10242ac110002_469w_701h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90',  # 菜品的展示图链接
    'dishesID': '1064357',  # 菜品ID
    'dishesUrl': 'http://www.xiachufang.com/recipe/1064357/',  # 菜品链接

    # 第三部分
    'score': '8.5',  # 综合评分
    'doneNum': '50744',  # 做过的人数
    'bigImg':'http://i2.chuimg.com/4daad8ea877a11e6a9a10242ac110002_469w_701h.jpg?imageView2/1/w/215/h/136/interlace/1/q/90', # 菜品详情页大图
    'userName': '小辞xiaoci',  # 发布者
    'userID':'10047347', # 发布者ID
    'userUrl':'http://www.xiachufang.com/cook/10047347/', # 发布者链接
    'userImg': 'http://i2.chuimg.com/ac6738e025a44c2cabdaa554fd5dc8cc_1124w_1124h.jpg?imageView2/1/w/60/h/60/interlace/1/q/90',  # 发布者头像地址
    'abstract':'国庆在家宴客最大小通吃的菜话说，小辞在家宴客也有了一些经验，总。。。, ',# 简介
    'materialList': [
        {'material': '猪小排', 'number': '1汤勺（1汤勺为15毫升容量的勺)'},
        {'material': '料酒', 'number': '4根'},
        {'material': '盐', 'number': '3克'},
        {'material': '酱油', 'number': '2汤勺（1汤勺为15毫升容量的勺）'},
        {'material': '米醋', 'number': '3汤勺（1汤勺为15毫升容量的勺）'},
        {'material': '白糖', 'number': ' 4汤勺（1汤勺为15毫升容量的勺）'},
        {'material': '姜片', 'number': ' '},
    ],  # 食材清单
    'processList': [
        {'process': '猪小排冼净，晾干水份备用', 'img': 'http://i2.chuimg.com/96cf5bfa8cba11e6a9a10242ac110002_469w_354h.jpg?imageView2/2/w/300/interlace/1/q/90'},
        {'process': '锅内倒少量油，烧热之后，爆香姜片', 'img': ''},
        {'process': '放入排骨，一直煸炒到排骨变色后，表面金黄微焦', 'img': ''},
        {'process': '此时就可以放入黄金比例中的调料了，顺序是：先放一汤勺料酒，接着两汤勺酱油，三汤勺米醋最后四汤勺白糖，炒匀', 'img': ''},
        {'process': '再倒入能没过排骨的开水，调中小火焖20分钟', 'img': ''},
        {'process': '20分钟后调入盐，开大火收汁，收到汁浓色亮时，撒入芝麻点缀即可出锅（锅里剩下的姜片丢掉不用，最后大火收汁时注意多翻动锅内的排骨，避免烧焦哟！）', 'img': ''},
    ],  # 烹饪流程
    'tips': '*做这道菜，请一定选用猪纯小排，最好还带有脆骨的，此部位肉质软嫩，是最适合用来做糖醋排骨的。*排骨在入锅炒之前，尽量晾干水份，用厨房纸擦干也行，这样在炒的时候不会油花四溅，烫到手。*在洒料酒的时候，沿着锅边淋一圈，这样酒香分布更均匀。*黄金比例中的3汤勺米醋和4汤勺糖，可以根据自己的口味来调整，喜欢酸点的可以换成4汤勺米醋、3汤勺白糖。*喜欢颜色深点的童鞋，可以在焖好调入盐的时候，再放少量的老抽来增色。',  # 小贴士
    'classify': [
        {'title':'酸甜','url':'http://www.xiachufang.com/category/51449/'},
        {'title':'家常菜','url':'http://www.xiachufang.com/category/40076/'},
        {'title':'糖醋','url':'http://www.xiachufang.com/category/40066/'},
        {'title':'宴客','url':'http://www.xiachufang.com/category/52385/'},
        {'title':'宿舍','url':'http://www.xiachufang.com/category/52370/'},
        {'title':'......','url':'......'},
    ],  # 分类 + 链接
    'crawlTime':'', # 抓取时间
    'content':'菜谱详情原始数据', # 菜谱详情原始数据
    'source':'下厨房', # 来源 豆果美食
    'type':0, # 状态值
}
