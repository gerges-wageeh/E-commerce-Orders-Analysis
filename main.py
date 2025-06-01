#عمل تحليل علي بيانات طلبات في متجر الكتروني
import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("sample_orders.csv")

#Exploratory (EDA)
print(data.head())
print(data.info())

#احسب اجمالي المببيعات
total_sales = data['price'].sum()
print("إجمالي المبيعات:", total_sales)

#اكتر المنتجات مبيعا
most_product = data['product'].value_counts().reset_index()

#اكتر العملاء صرفا
customer_exchange = data.groupby("customer")["price"].sum().sort_values(ascending=False).reset_index()

#مبيعات كل شهر مع رسم بياني
data['date'] = pd.to_datetime(data['date'])
data['month_num'] = data['date'].dt.month
data['month_name'] = data['date'].dt.month_name()

price_all_month = data.groupby(['month_num','month_name'])["price"].sum().sort_index()
plt.figure(figsize=(10,6))
ax = price_all_month.plot(kind='bar')
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.bar_label(ax.containers[0])
plt.xticks(rotation=45)
plt.title("Sales every month")
#plt.tight_layout()


plt.savefig('chart.png',bbox_inches='tight',dpi=300)
plt.show()

#تقرير Excel فيه تحليلات + البيانات الخام
with pd.ExcelWriter('shop_analysis.xlsx') as writer:
    pd.DataFrame({'Total Sales': [total_sales]}).to_excel(writer, sheet_name='total sales', index=False)
    customer_exchange.to_excel(writer,sheet_name='customer_exchange',index=False)
    most_product.to_excel(writer,sheet_name='most_product',index=False)
    data.to_excel(writer,sheet_name='raw_dat',index=False)


