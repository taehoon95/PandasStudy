import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns',15)
pd.set_option('display.width',600)

titanic = sns.load_dataset('titanic')
print('titanic', pd.DataFrame(titanic).head(),titanic.shape ,sep='\n', end='\n\n')

print('#titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기')
df = titanic.loc[:,['age','fare']]
print(df.head(), end='\n\n')

print('#df 에서 ten 열을 추가')
df['ten'] = 10
print(df.head())
print()

def add_10(n):
    return n + 10

def add_two_obj(a,b):
    return a + b

print('#사용자 함수 정의')
print('add_10(10) : ', add_10(10))
print('add_two_obj(10,10) : ', add_two_obj(10,10),end='\n\n')

print('#시리즈 객체에 적용')
sr1 = df['age'].apply(add_10)
print(sr1.head(), end='\n\n')

print('#시리즈 객체와 숫자에 적용: 2개의 인수(시리즈 + 숫자)')
sr2 = df['age'].apply(add_two_obj, b = 10)
print(sr2.head())
print('\n')

print('#람다 함수 활용 : 시리즈 객체에 적용1')
sr3 = df['age'].apply(lambda x:add_10(x))
print(sr3.head(), end='\n\n')

print('# 람다 함수 활용: 시리즈 객체에 적용2')
sr4 = df['age'].apply(lambda x:x + 40)
print(sr4.head())