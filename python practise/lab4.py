# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
#exercise 4 task1
import numpy as np
x=np.array([10,2,30,57])
print(x)
print(np.all(x))
x=np.array([1,0,78,100])
print(x)
print(np.all(x))


#task2
import numpy as np
a=np.array([45,67,23,20])
b=np.array([56,23,89,20])
print(a)
print(b)
print(np.greater(a,b))
print(np.greater_equal(a,b))
print(np.less(a,b))
print(np.less_equal(a,b))



#task3
import numpy as np
array1=np.zeros(8)
print(array1)
array2=np.ones(5)
print(array2)
array3=np.ones(10)*5
print(array3)
whole=np.hstack((array1,array2,array3))
print(whole)



#task4
import numpy as np
m= np.array([[23,45,11],[12,23,54],[29,19,34],[1,23,10]])
v= np.array([2,0,2])
print(m)
print(v)
answer=np.empty_like(m)
for i in range(4):
    #print("this is in answer",i)
    print(answer[i,:])
    answer[i,:]=m[i,:]+v
print(answer)

#task5
import numpy as np
array=np.ones((5,5))
print(array)
array[1:-1,1:-1]=25
print(array)

#task6
import numpy as np
array1=np.array([23,45,11,5])
array2=np.array([23,5,1])
intersection=np.intersect1d(array1,array2)
print(intersection)

#task7
import numpy as np
array1=np.array([[23,45,11],[12,23,54],[1,23,10]])
array2=np.array([[3,5,1],[2,3,4],[9,1,5]])
print(array1,array2)
print(np.vstack((array1,array2)))
print(np.hstack((array1,array2)))
[b,c]=np.hsplit(np.hstack((array1,array2)),2)
print(b)
[b,c]=np.vsplit(np.vstack((array1,array2)),2)
print(c)

#task8
import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
#labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data)
print("First three rows of the data frame:")
print(df.iloc[3:])


#task9
import pandas as pd
import numpy as np
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print(" number of attempts in the examination is greater than 2")
print(df[(df['attempts'] >2)])

#task10
import pandas as pd
import numpy as np
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)

rows=len(df.axes[0])
cols=len(df.axes[1])
print(rows)
print(cols)

#task11
import pandas as pd
import numpy as np
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print(df[(df['score']>=14) & (df['score']<=20)])
'''
#task12
import pandas as pd
import numpy as np
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data , index=labels)
df.loc['c','score']=11.5
print(df.loc['c'])

#task13
import pandas as pd
import numpy as np
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("\nMean score for each different student in data frame:")
print(df['score'].mean())



