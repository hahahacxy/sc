import pandas as pd
# 加载 Excel 文件
df = pd.read_excel('C:/Users/29760/Desktop/原始数据(1).xlsx')
# 使用一个函数来检查每个文本中单词的数量
def count_words(text):
    return len(str(text).split())
# 筛选出'Review_Text'列中单词数量大于等于 3 的行
filtered_df = df[df['Review_Text'].apply(count_words) >= 2]
# 将筛选后的数据保存到新的 Excel 文件
filtered_df.to_excel('筛选后的 Excel 文件.xlsx', index=False)