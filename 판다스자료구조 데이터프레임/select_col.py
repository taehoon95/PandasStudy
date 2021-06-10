import pandas as pd

exam_data = {
    '이름':['서준','우현','인아'],
    '수학':[90,80,70],
    '영어':[98,89,95],
    '음악':[85,95,100],
    '체육':[100,90,90]
}

df = pd.DataFrame(exam_data)
print('exam_data',type(df) ,df,sep='\n', end='\n\n')

math1 = df['수학']
print(type(math1), math1, sep='\n', end='\n\n')

english = df.영어
print(type(english), english, sep='\n', end='\n\n')

music_gym = df[['음악','체육']]
print(type(music_gym), music_gym, sep='\n', end='\n\n')

math2 = df[['수학']]
print(type(math2), math2, sep='\n', end='\n\n')