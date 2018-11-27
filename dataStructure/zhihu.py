# -*- coding: utf-8 -*-

# 知乎 网站采集 数据结构及字段说明：

'''
数据采集的起始点：
根据话题标签 进行扩展采集

字典命名 对应 数据库名字
'''
# 知乎 话题标签信息
topicIDItems = {
    "topicID": "话题标签ID",
    "topicName": "话题标签名称",
    "type": '采集状态值',
    "topicIDUrl": "https://www.zhihu.com/topic/19551915",  # 话题标签链接
    "topicCardDescription": "话题标签的简介",
    "topicCardImageUrl": "话题标签的图片地址",
    "boardNum": "关注者 数量",
    "questionNum": "问题数 数量",
    "index": "话题的索引 及其 索引子条目",
    "parent": [
        {
            "topicName": "车辆",
            "topicID": "19562361"
        }
    ]  # 话题的父类 及其 话题标签ID
}

# 知乎 话题关注者
# 话题 关注者 表：  话题topicId + 关注者Id 做联合唯一索引
topicFollower = {
    "topicName": "汽车品牌",  # 话题名称
    "topicID": "19697090",  # 话题ID
    "id": "246e6cf44e94cefbf4b959cb5042bc91",  # 关注者的 ID
    "name": "于欣烈",  # 关注者的id名字
    "headline": "和自己赛跑",  # 关注者的自我描述
    "url_token": "yuxinlie",  # 关注者的 的短链接 https://www.zhihu.com/people/yuxinlie/activities
    "answer_count": 433,  # 关注者的 回答数
    "articles_count": 188,  # 关注者的 文章数
    "follower_count": 282027,  # 关注者的 关注数
    "avatar_url": "https://pic1.zhimg.com/50/3d4085b43_is.jpg",  # 关注者的 头像地址
    "crowlTime": "2018-09-20 15:49:34",  # 数据采集时间 or 数据的更新时间
    "type": 0  # 采集的状态值
}

# 知乎 用户 的个人信息的 详细字段说明（未完待添加）
# 用户表： 用户ID 做唯一索引
peopleTable = {
    "id": "246e6cf44e94cefbf4b959cb5042bc91",  # 用户的ID
    "name": "于欣烈",  # 用户的 名称
    "headline": "和自己赛跑",  # 用户的 自我描述
    "url_token": "yuxinlie",  # 用户的 短链接
    "answer_count": 433,  #  回答数
    "articles_count": 188,  #  文章数
    "follower_count": 282030,  #  被关注数
    "avatar_url": "https://pic1.zhimg.com/50/3d4085b43_is.jpg",  # 关注者的 头像地址
    "gender": "",  # 性别  1 男，0 女， -1 未注明
    "locations": "",  # 居住地 (多条)
    "business": "",  # 行业  待校验
    "employments": "",  # 职业经历（多条）
    "educations": "",  # 教育经历（多条）
    "description": "",  # 个人简介

    # 标签栏： 回答、提问、文章、专栏、想法
    # "answerCount": "",  # 回答数  (上面有 answer_count)
    "questionCount": "",  # 提问数
    # "articlesCount": "",  # 文章数  (上面有 articles_count)
    "columnsCount": "",  # 专栏数
    "pinsCount": "",  # 想法数
    "favoriteCount": "",  # 收藏数
    "followingCount": "",  # 关注数

    # 个人成就 栏
    "badge": "",  # 优秀回答话题，可能是一个话题列表
    "includedAnswersCount": "",  # 收录回答数 （知乎收录 4 个回答 12 篇文章）
    "includedArticlesCount": "",  # 收录文章数
    "voteupCount": "",  # 被点赞数 （赞同数：获得 10,846 次赞同）
    "logsCount": "",  # 编辑数
    "hostedLiveCount": "",  # 主持Live数
    "participatedLiveCount": "",  # 赞助Live数
    "followingTopicCount": "",  # 关注话题数
    "followingColumnsCount": "",  # 关注专栏数
    "followingQuestionCount": "",  # 关注的问题数
    "followingFavlistsCount": "",  # 关注的收藏夹数

    "usersJson": "",  # 用户信息的 待解析的原始Json （从crawlContent 提取的）
    "crawlContent": "",  # 采集到的原始JSON 数据不包含 Html

    "crowlTime": "2018-09-20 16:05:17",  # 数据采集时间 or 数据的更新时间
    # 待完善
    "type": 0  # 采集的状态值0 未采集，1 采集了详细信息，2 解析了详细信息， 4 没有详细内容

}

# 知乎 话题标签下的 问题 及问题的相关信息
# 话题ID  + 问题ID 做唯一索引
topicQuestions = {
    "topicName": "汽车品牌",  # 问题所属的 话题标签名称
    "topicID": "19697090",  # 问题所属的 话题标签ID
    # "labels": ['产品', '汽车品牌'],  # 问题 所属的父类 话题标签 ==> questionTopics
    "title": "13款宝马740中间储物箱的这个是什么？",  # 问题的 标题
    "follower_count": 1,  # 问题 关注者 的数量
    # "browse_count": "",  # 问题 被浏览 的数量  ==> visitCount
    "answer_count": 0,  # 问题  回答数
    "created_tiem": "2018-09-25 17:48:56",  # 问题创建的时间
    "created_user": "debadebade",  # 问题 创建者
    "user_url": "debadebade-82",  # 问题创建者的 短链接 https://www.zhihu.com/people/debadebade-82/activities
    "created_id": "58a93716405637f65f75f30307106b5a",
    # 问题创建者的ID https://www.zhihu.com/people/58a93716405637f65f75f30307106b5a
    "question_id": 296045977,  # 问题的ID、 https://www.zhihu.com/question/296045977
    "crawl_time": "2018-09-25 18:31:50",  # 数据采集的时间
    "content": {  # 原始数据信息
        "author": {
            "avatar_url_template": "https://pic4.zhimg.com/50/da8e974dc_{size}.jpg",
            "type": "people",
            "name": "debadebade",
            "edu_member_tag": {
                "type": "default",
                "member_tag": ""
            },
            "url": "http://www.zhihu.com/api/v4/people/58a93716405637f65f75f30307106b5a",
            "gender": -1,
            "user_type": "people",
            "url_token": "debadebade-82",
            "is_advertiser": False,
            "avatar_url": "https://pic4.zhimg.com/50/da8e974dc_is.jpg",
            "is_org": False,
            "headline": "",
            "badge": [],
            "id": "58a93716405637f65f75f30307106b5a"
        },
        "url": "http://www.zhihu.com/api/v4/questions/296045977",
        "title": "13款宝马740中间储物箱的这个是什么？",
        "answer_count": 0,
        "created": 1537868936,
        "question_type": "normal",
        "follower_count": 1,
        "is_following": False,
        "type": "question",
        "id": 296045977
    },
    "questionJson": "", # 采集问题详情页 所获得的 问题原始数据
    "crawlHtmlContent": "", # 采集问题详情页 所获得的 原始数据
    "visitCount": "", # 问题浏览量 ==》 被浏览的次数
    "questionTopics": [], # 问题所属的话题组
    "type": 0  # 采集的状态值0 未采集，1 采集了详细信息，2 解析了详细信息， 4 没有详细内容
}

# 知乎话题下  活跃回答者 字段说明
# 话题ID  + 用户ID 做唯一索引
bestAnswerersItem = {
    'topicName': '',  # 话题名称
    'topicID': '',  # 话题ID
    'id': '',  # 用户ID
    'name': '',  # 用户昵称
    'headline': '',  # 用户个签
    'url_token': '',  # 用户短链接
    'answer_count': '',  # 用户在问题下的 回答数
    'answer_votes': '',  # 回答后的 赞同数
    'crawlContent': '',  # 采集到的原始数据
    'crowlTime': '',  # 采集时间
    'type': 0,  # 状态值
}
