import pandas as pd
# 加载 Excel 文件
df = pd.read_excel('筛选后的 Excel 文件.xlsx') # 请替换为您的文件路径
# 检查缺失值
missing_values = df.isnull().sum()
# 打印每个字段的缺失值数量
print("每个字段的缺失值数量：")
print(missing_values)