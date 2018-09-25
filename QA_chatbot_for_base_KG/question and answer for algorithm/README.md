首先配置依赖
pypi安装: windows（anaconda3）: pip install -U synonyms 或 pip install -r Requirements.txt
          linux: pip3 install synonyms 或 pip install -r Requirements.txt

使用的训练数据集是原来小吴给的爬虫的答案数据（.csv文件）

predict.py 预测问题的短文本答案（短文本不得长于30个字符）

描述：output：一个语义匹配相似度最大的回答，元组形式，key为数据集中最相似问题，value为计算出的相似度得分

使用到的工具包

[Word2vec by Google](https://code.google.com/archive/p/word2vec/)

[Wikimedia: 训练语料来源](https://dumps.wikimedia.org/)

[gensim: word2vec.py](https://github.com/RaRe-Technologies/gensim)

[jieba: 中文分词](https://github.com/fxsjy/jieba)

