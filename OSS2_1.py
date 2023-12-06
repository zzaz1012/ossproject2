import pandas as pd
data = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

datain2015 = data[data['year']==2015]
print('2015년')
print('안타 기준 정렬')
datain2015 = datain2015.sort_values(by='H', ascending=False)
print(datain2015[['batter_name','H']].head(10))
print('\n타율 기준 정렬')
datain2015 = datain2015.sort_values(by='avg', ascending=False)
print(datain2015[['batter_name','avg']].head(10))
print('\n홈런 기준 정렬')
datain2015 = datain2015.sort_values(by='HR', ascending=False)
print(datain2015[['batter_name','HR']].head(10))
print('\n출루율 기준 정렬')
datain2015 = datain2015.sort_values(by='OBP', ascending=False)
print(datain2015[['batter_name','OBP']].head(10))

datain2016 = data[data['year']==2016]
print('\n\n\n2016년')
print('안타 기준 정렬')
datain2016 = datain2016.sort_values(by='H', ascending=False)
print(datain2016[['batter_name','H']].head(10))
print('\n타율 기준 정렬')
datain2016 = datain2016.sort_values(by='avg', ascending=False)
print(datain2016[['batter_name','avg']].head(10))
print('\n홈런 기준 정렬')
datain2016 = datain2016.sort_values(by='HR', ascending=False)
print(datain2016[['batter_name','HR']].head(10))
print('\n출루율 기준 정렬')
datain2016 = datain2016.sort_values(by='OBP', ascending=False)
print(datain2016[['batter_name','OBP']].head(10))

datain2017 = data[data['year']==2017]
print('\n\n\n2017년')
print('안타 기준 정렬')
datain2017 = datain2017.sort_values(by='H', ascending=False)
print(datain2017[['batter_name','H']].head(10))
print('\n타율 기준 정렬')
datain2017 = datain2017.sort_values(by='avg', ascending=False)
print(datain2017[['batter_name','avg']].head(10))
print('\n홈런 기준 정렬')
datain2017 = datain2017.sort_values(by='HR', ascending=False)
print(datain2017[['batter_name','HR']].head(10))
print('\n출루율 기준 정렬')
datain2017 = datain2017.sort_values(by='OBP', ascending=False)
print(datain2017[['batter_name','OBP']].head(10))

datain2018 = data[data['year']==2018]
print('\n\n\n2018년')
print('안타 기준 정렬')
datain2018 = datain2018.sort_values(by='H', ascending=False)
print(datain2018[['batter_name','H']].head(10))
print('\n타율 기준 정렬')
datain2018 = datain2018.sort_values(by='avg', ascending=False)
print(datain2018[['batter_name','avg']].head(10))
print('\n홈런 기준 정렬')
datain2018 = datain2018.sort_values(by='HR', ascending=False)
print(datain2018[['batter_name','HR']].head(10))
print('\n출루율 기준 정렬')
datain2018 = datain2018.sort_values(by='OBP', ascending=False)
print(datain2018[['batter_name','OBP']].head(10))

print('----------------------------------------')
print('2018 highest war')
print('highest war 포수')
posu_list = datain2018[datain2018['cp']=='포수']
print(datain2018.loc[posu_list['war'].idxmax()])
print()

print('highest war 1루수')
firstlu_list = datain2018[datain2018['cp']=='1루수']
print(datain2018.loc[firstlu_list['war'].idxmax()])
print('\n')

print('highest war 2루수')
secondlu_list = datain2018[datain2018['cp']=='2루수']
print(datain2018.loc[secondlu_list['war'].idxmax()])
print('\n')

print('highest war 3루수')
thirdlu_list = datain2018[datain2018['cp']=='3루수']
print(datain2018.loc[thirdlu_list['war'].idxmax()])
print('\n')

print('highest war 유격수')
yousu_list = datain2018[datain2018['cp']=='유격수']
print(datain2018.loc[yousu_list['war'].idxmax()])
print('\n')

print('highest war 좌익수')
leftsu_list = datain2018[datain2018['cp']=='좌익수']
print(datain2018.loc[leftsu_list['war'].idxmax()])
print('\n')

print('highest war 중견수')
midsu_list = datain2018[datain2018['cp']=='중견수']
print(datain2018.loc[midsu_list['war'].idxmax()])
print('\n')

print('highest war 우익수')
rightsu_list = datain2018[datain2018['cp']=='우익수']
print(datain2018.loc[rightsu_list['war'].idxmax()])
print('\n')

print('----------------------------------------')
values_cor = {
    'R': data['R'].corr(data['salary']),
    'H': data['H'].corr(data['salary']),
    'HR': data['HR'].corr(data['salary']),
    'RBI': data['RBI'].corr(data['salary']),
    'SB': data['SB'].corr(data['salary']),
    'war': data['war'].corr(data['salary']),
    'avg': data['avg'].corr(data['salary']),
    'OBP': data['OBP'].corr(data['salary']),
    'SLG': data['SLG'].corr(data['salary'])
}
max_val = max(values_cor,key=values_cor.get)
print(f"{max_val}이 {values_cor[max_val]}로 가장 높은 연관성을 보임")