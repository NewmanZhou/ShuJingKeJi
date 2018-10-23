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