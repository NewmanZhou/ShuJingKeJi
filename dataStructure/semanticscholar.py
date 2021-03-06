# -*- coding: utf-8 -*-

# semanticscholar 网站采集 数据结构：

semanticscholarItme = {
    'paper_id': '源文件自带',# ==》paper_id
    'scholar_id': '源文件自带',# ==》scholar_id
    'search_title': '要搜索的标题',# ==》paper_title
    'authors':['作者数组'],# ==》semantic_scholar_author_list
    'years':'年份',# ==》semantic_scholar_year
    'journal':'发表期刊/会议',# ==》semantic_scholar_journal
    'DOI':'DOI',# ==》semantic_scholar_DOI
    'topics':['topics'],# ==》semantic_scholar_topic
    'contentUrl':'详情页Url',# ==》semantic_url
    'list_title':'列表标题',# ==》
    'con_title':'正文标题',# ==》semantic_scholar_title
    'list_content':'列表摘要',# ==》
    'con_content':'正文摘要',# ==》semantic_scholar_abstract
    'title_similarity':'标题相似度（列表标题和原文标题）',# ==》title_similarity
    'abstract_similarity':'摘要相似度（列表摘要和原文摘要）',# ==》abstract_similarity
    'type': 0,# ==》 0: 未抓取， 1：采集完成，2:获取到url,但详情访问失败 ，3:搜索不到数据 ，5：相似度比较完成，已是一条完整数据。
    'paper_abstract':'源文件自带的 谷歌搜索结果',
    'paper_abstract_text':'清洗源文件的搜索结果'
}


'''《type ： 状态值 详细说明》'''

'''
表 ： hasPaper_abstract //Paper0  的原始google 数据清洗的 结果。 
0： 未清洗，刚入库的初始状态
1： 有内容，并且清洗完成。
2： 没有内容，不需要清洗。
3： 在状态 1 的基础上 已经其结果 合并到表《paper2219521_from_0》 的 'Clean_abstract' 字段上。



'''

'''
['paper_id', 'scholar_id', 'paper_abstract_text']
['paper_id', 'scholar_id', 'paper_title', 'semantic_scholar_author_list', 'semantic_scholar_year', 'semantic_scholar_journal', 'semantic_scholar_DOI', 'semantic_scholar_topic', 'semantic_url', 'semantic_scholar_title', 'semantic_scholar_abstract']
>>> df = pd.read_csv('paper_part0_rmEnter.csv')
>>> dd = pd.read_csv('semanticScholarClean.csv')
>>> data = pd.merge(df, dd, on=['paper_id','scholar_id'], how='left')
>>> data.to_csv('paper_part0_google_rmEnter.csv',encoding='utf-8',index='false')
'''