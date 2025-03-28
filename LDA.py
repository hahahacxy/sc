import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
# 读取 Excel 文件
file_path = 'LDA.xlsx' # 请根据你的文件路径进行修改
data = pd.read_excel(file_path)
# 简化的文本预处理函数
def preprocess_text_simplified(text):
    text = text.lower() # 转换为小写
    text = re.sub(r'[^\w\s]', '', text) # 移除标点符号
    words = text.split() # 分词
    return ' '.join(words)
# 应用文本预处理
data_subset = data['Review_Text'].iloc[:] # 选取评论 s
preprocessed_texts = data_subset.apply(preprocess_text_simplified)
# 构建文档-词矩阵
vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
dtm = vectorizer.fit_transform(preprocessed_texts)
# 定义和训练 LDA 模型
n_topics =5 # 主题数量
lda_model = LatentDirichletAllocation(n_components=n_topics, random_state=0)
lda_model.fit(dtm)
# 显示每个主题的代表词汇
def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print(f"Topic {topic_idx}:")
        print(" ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]))
display_topics(lda_model, vectorizer.get_feature_names_out(), 10)