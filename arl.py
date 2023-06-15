############################################
# ASSOCIATION RULE LEARNING (BİRLİKTELİK KURALI ÖĞRENİMİ)
############################################

# 1. Veri Ön İşleme
# 2. ARL Veri Yapısını Hazırlama (Invoice-Product Matrix)
# 3. Birliktelik Kurallarının Çıkarılması
# 4. Çalışmanın Scriptini Hazırlama
# 5. Sepet Aşamasındaki Kullanıcılara Ürün Önerisinde Bulunmak

############################################
# 1. Veri Ön İşleme
############################################

# !pip install mlxtend
import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
# çıktının tek bir satırda olmasını sağlar.
pd.set_option('display.expand_frame_repr', False)
from mlxtend.frequent_patterns import apriori, association_rules

# https://archive.ics.uci.edu/ml/datasets/Online+Retail+II

df_ = pd.read_excel("/home/firengiz/Belgeler/recommedation/online_retail_II.xlsx", sheet_name="Year 2010-2011")[:4000]

df = df_.copy()
print(df.head())
print(df.describe().T)
print(df.isnull().sum())
print(df.shape)


#aykiri degerleri 
def outlier_thresholds(dataframe, varible):
    quartile1 = dataframe[varible].quantile(0.01)
    quartile3 = dataframe[varible].quantile(0.99)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit

def replace_thresholds(dataframe, varible):
    low_limit, up_limit = outlier_thresholds(dataframe, varible)
    dataframe.loc[(dataframe[varible] < low_limit), varible] = low_limit
    dataframe.loc[(dataframe[varible] > up_limit), varible] = up_limit



def retail_data_prep(dataframe):
    dataframe.dropna(inplace=True)
    dataframe = dataframe[~dataframe['Invoice'].str.contains('C',na=False)]
    dataframe = dataframe[dataframe['Quantity'] > 0]
    dataframe = dataframe[dataframe['Price'] > 0]
    replace_thresholds(dataframe, 'Quantity')
    replace_thresholds(dataframe, 'Price')
    return dataframe
df = retail_data_prep(df)

print(df.describe().T)
print(df.isnull().sum())


############################################
# 2. ARL Veri Yapısını Hazırlama (Invoice-Product Matrix)
############################################

df_fr = df[df['Country']=='France']

df_fr.groupy(['Invoice', 'Description']).agg({'Quantity':'sum'}).head(20)

df_fr.groupy(['Invoice', 'Description']).agg({'Quantity':'sum'}).unstack().iloc[0:5, 0:5]#description'daki isimleri  sutun ismi yapma islmi
df_fr.groupy(['Invoice', 'Description']).agg({'Quantity':'sum'}).unstack().fillna(0).iloc[0:5, 0:5]

df_fr.groupby(['Invoice','StockCode']). \
    agg({'Quantity':'sum'}). \
    unstack(). \
    fillna(0). \
    applymap(lambda x:  1 if x > 0 else 0).iloc[0:5, 0:5]


def create_invoice_product_df(dataframe, id=False):
    if id:
        return dataframe.groupby(['Invoice', 'StockCode'])['Quantity'].sum().unstack().fillna(0).\
            applymap(lambda x: 1 if x > 0 else 0)
    else:
        return dataframe.groupby(['Invoice', 'Description'])['Quantity'].sum().unstack().fillna(0).\
            applymap(lambda x: 1 if x > 0 else 0)
    
fr_inv_pro_df = create_invoice_product_df(df_fr, id=True)

#sorgulamak istedigimiz stok id
#analiz yaptigimda birliktelik kuralini cikartdigimizda  bir id sormak istedigimizde 
def check_id(dataframe, stock_code):
    product_name = dataframe[dataframe['StockCode'] == stock_code][['Description']].values[0].tolist
    print(product_name)

check_id(df_fr,10002)

############################################
# 3. Birliktelik Kurallarının Çıkarılması
############################################

#olasi urun ciftlerinin olasiliklari olucak
frequent_itemsets = apriori(fr_inv_pro_df, 
                            min_support=0.01,
                            use_colnames=True)

frequent_itemsets.sort_values('support', ascending=False)

rules = association_rules(frequent_itemsets, 
                          metric='support',
                          min_threshold=0.01)

rules[(rules['support'] > 0.05) & (rules['confidence'] > 0.1) & (rules['lift'] > 5)].\
    sort_values('confidence',ascending=False)

check_id(df_fr, 21086)



##################################
# Butun sureci fonksiyonlastirmak
#################################
def retail_data_prep(dataframe):
    dataframe.dropna(inplace=True)
    dataframe = dataframe[~dataframe['Invoice'].str.contains('C',na=False)]
    dataframe = dataframe[dataframe['Quantity'] > 0]
    dataframe = dataframe[dataframe['Price'] > 0]
    replace_thresholds(dataframe, 'Quantity')
    replace_thresholds(dataframe, 'Price')
    return dataframe

def create_invoice_product_df(dataframe, id=False):
    if id:
        return dataframe.groupby(['Invoice', 'StockCode'])['Quantity'].sum().unstack().fillna(0).\
            applymap(lambda x: 1 if x > 0 else 0)
    else:
        return dataframe.groupby(['Invoice', 'Description'])['Quantity'].sum().unstack().fillna(0).\
            applymap(lambda x: 1 if x > 0 else 0)

def check_id(dataframe, stock_code):
    product_name = dataframe[dataframe['StockCode'] == stock_code][['Description']].values[0].tolist
    print(product_name)

def creat_rules(dataframe, id=True, country='France'):
    dataframe = dataframe[dataframe['Country'] == country]
    dataframe = create_invoice_product_df(dataframe, id)
    frequent_itemsets = apriori(dataframe, min_support=0.01, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric='support', min_threshold=0.01)
    return rules

df = df_.copy()
df = retail_data_prep(df)
rules = creat_rules(df)


############################################
# 5. Sepet Aşamasındaki Kullanıcılara Ürün Önerisinde Bulunmak
############################################

product_id = 22492
check_id(df, product_id)

sorted_rules = rules.sort_values('lift', ascending=False)

recommendation_list = []

for i, product in enumerate(sorted_rules['antecendents']):
    for j in list(product):
        if j == product_id:
            recommendation_list.append(list(sorted_rules.iloc[i]['consequents'])[0])

recommendation_list[0]
check_id(df, 22326)

# Fonksiyonlastirilmasi
# Parametreler ---- kurallari girip, oneri yaplmasini istedigimiz id giriyoruz(Stockcode) ve recommendation sayisi
def arl_recommender(rules_df, product_id, rec_count=1):
    sorted_rules = rules_df.sort_values('lift', ascending=False)
    recommendation_list = []
    for i, product in enumerate(sorted_rules['antecendents']):
        for j in list(product):
            if j == product_id:
                recommendation_list.append(list(sorted_rules.iloc[i]['consequents'])[0])

    return recommendation_list[0:rec_count]

arl_recommender(rules, 22492, 1)
