from list_to_dataframe import df

df.index = ['학생','학생2']

df.columns = ['연령','남녀','소속']
print('행 인덱스, 열 이름 변경하기', df, df.index, df.columns, sep='\n', end='\n\n')

df.rename(columns={'연령':'나이', '남녀':'성별', '소속':'학교'}, inplace=True)
print('열 이름 중, 연령을 나이로, 남녀를 성별로, 소속을 학교로 바꾸기')
print( df, df.index, df.columns, sep='\n', end='\n\n')

df.rename(index={'학생1':'준서', '학생2':'예은'}, inplace=True)
print('행 이름 중, 학생1을 준서로, 학생2를 예은으로 바꾸기')
print( df, df.index, df.columns, sep='\n', end='\n\n')