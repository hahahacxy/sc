import pandas as pd
from senticnet.senticnet import SenticNet
sn = SenticNet()
'''
Blouses Pants
Casual bottoms Shorts
Chemises Skirts
Dresses Sleep
Fine gauge Sweaters
Intimates Swim
Jackets Trend
Jeans
Knits
Layering
Legwear
Lounge
Outerwear
'''
data = pd.read_excel('副本评论分类(1).xlsx',sheet_name="total")
features = {
'topic1': ['love', 'sweater', 'great', 'wear', 'I', 'color', 'perfect', 'This', 'skirt', 'look', 'soft',
'top', 'dress', 'comfortable', 'nice', 'will', 'fit', 'well', 'fabric', 'flattering', 'little', 'jeans', 'really',
'pants', 'one', 'length', 'bought', 'long', 'beautiful', 'colors'],
'topic2': ['size', 'small', 'im', 'fit', 'I', 'top', 'medium', 'large', 'ordered', 'wear', 'waist',
'love', 'look', 'really', 'usually', 'little', 'big', 'bit', 'short', 'petite', 'xs', 'runs', 'way', 'This', 'long',
'think', 'fabric', 'much', 'great', 'tried'],
'topic3': ['size', 'fit', 'soft', 'small', 'I', 'fabric', 'im', 'quality', 'love', 'price', 'This', 'well',
'ordered', 'got', 'wear', 'shirt', 'tee', 'fits', 'one', 'beautiful', 'These', 'comfortable', 'great', 'sale',
'really', 'bought', 'cute', 'wool', 'sweater', 'true'],
'topic4': ['I', 'color', 'size', 'fit', 'top', 'one', 'love', 'store', 'ordered', 'online', 'back',
'wear', 'looks', 'will', 'im', 'tried', 'bought', 'much', 'fabric', 'colors', 'didnt', 'really', 'little', 'see',
'person', 'dont', 'even', 'sleeves', 'pretty', 'soft']
}
# 初始化一个空的 DataFrame 来存储结果
results = pd.DataFrame(columns=['Comment'] + list(features.keys()))
# 遍历每条评论
for index, row in data.iterrows():
    comment = row['text']
    sentiment_scores = {'Comment': comment}
    # 计算每个主题的情感得分
    for feature, keywords in features.items():
        feature_sentiment_score = 0
        keyword_count = 0
        for word in comment.split():
            if word.lower() in keywords:
                try:
                    polarity_value = float(sn.polarity_value(word))
                    feature_sentiment_score += polarity_value
                    keyword_count += 1
                except:
                    pass
        if keyword_count > 0:
            feature_sentiment_score /= keyword_count
        sentiment_scores[feature] = feature_sentiment_score
    # 将当前评论的得分添加到结果 DataFrame 中
    results = results.append(sentiment_scores, ignore_index=True)
# 导出结果到 Excel 文件
results.to_excel('total.xlsx', index=False)