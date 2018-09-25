# QAbot_by_base_KG
基于知识图谱的多轮问答机制


思路：
将预先处理好的问答语料集做聚类处理， 用户的短文本问题输入后，做文本分类， 分类到相对聚类语料集中， 进行短文本语义匹配， 得出分值最高的匹配问题， 去除相对应的答案。



原料：
文本聚类： 使用了K_means算法聚类， 并使用baidu开源主题建模算法包Familia进行精细化文本处理。      baidu Familia：https://github.com/baidu/Familia

文本分类：使用Facebook的fasttext和textcnn， 比较具有效率和速度。  fasttext:  https://github.com/facebookresearch/fastText

语义相似度匹配： 提前训练好词向量，使用的google的word2vertor 进行短文本语义的平滑计算
