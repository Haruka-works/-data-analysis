import pandas as pd

# CSVファイルを読み込む
file_path = "business_sales_2024.csv"
df = pd.read_csv(file_path)

# 日付を適切な型に変換
df["date"] = pd.to_datetime(df["date"])

# 年月ごとに売上を集計
df["year_month"] = df["date"].dt.to_period("M")
monthly_sales = df.groupby("year_month")["sales"].sum().reset_index()

# Excelファイルとして保存
excel_file_path = "business_sales_report.xlsx"
monthly_sales.to_excel(excel_file_path, index=False)

print("Excelレポートを作成しました: business_sales_report.xlsx")
