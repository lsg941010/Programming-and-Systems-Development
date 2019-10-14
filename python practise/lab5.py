# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
#exersice1
import matplotlib.pyplot as plt
X=range(1,30)
Y= [value *2 for value in X]
print(*range(1,50))
print(Y)
plt.plot(X,Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('This is the line graph')
plt.show()


#task2
import matplotlib.pyplot as plt
import pandas as pd
data=[['10-03-16',774.25,776.065002,769.5,772.559998],['10-04-16',776.030029,778.710022,772.890015,776.429993],['10-05-16',779.309998,782.070007,775.650024,776.469971],['10-06-16',779,780.47998,775.539978,776.859985],['10-07-16',779.659973,779.659973,770.75,775.080017]]
frame=pd.DataFrame(data,columns=['Date','Open','High','Low','Close'])
frame.to_csv('fdata.csv')
csvframe=pd.read_csv('fdata.csv',sep=',',parse_dates=True,index_col=0)

print(csvframe)
csvframe.plot()
plt.show()
#question, how to add the date into the columns

#task3
import matplotlib.pyplot as plt
import numpy as np
import math
t=np.arange(0,2,0.1)
print(t)
y1=np.sin(math.pi*t)
y2=np.cos(math.pi*t+math.pi/3)
y3=np.cos(math.pi*t+2)
plt.plot(y1,y2,'r*',linewidth=3,label='line1')
plt.plot(t,y2,'g--',linewidth=7,label='line2')
plt.legend()


#task4
import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
# plotting the line 1 points 
plt.plot(x1, y1,'r:' ,linewidth=3,label = "red-dotted")
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
# plotting the line 2 points 
plt.plot(x2, y2,'g--', linewidth=4,label = "green-dashed")
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title of the current axes.
plt.title('Plot with two or more lines with different styles ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()


#task5
import matplotlib.pyplot as plt
x1 = [20, 30, 50, 60, 80]
y1 = [10, 50, 100, 180, 200]
x2 = [30, 40, 60, 70, 90]
y2 = [20, 60, 110, 200, 220]
plt.axis([0, 100, 0, 300]) 
plt.plot(x1,y1,'b^',x2,y2,'ro')


#task6
import matplotlib.pyplot as plt
fig=plt.figure()
#fig.subplots_adjust(bottom=0.020,left=0.020,top=0.900,right=0.800)
plt.subplot(2,1,1)
plt.xticks(())
plt.yticks(())
plt.subplot(234)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 5)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 6)
plt.xticks(())
plt.yticks(())
plt.show()

#task7
import matplotlib.pyplot as plt
index=[ 'Python', 'Java', 'C', 'C++', 'R', 'JavaScript', 'C#']
values=[100, 96.3, 94.4, 87.5, 81.5, 79.4, 74.5]
plt.bar(index,values)
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Happy coding")
x_pos = [i for i, _ in enumerate(index)]
plt.xticks(x_pos, index)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()



#task8
import matplotlib.pyplot as plt
index=[ 'Python', 'Java', 'C', 'C++', 'R', 'JavaScript', 'C#']
values=[100, 96.3, 94.4, 87.5, 81.5, 79.4, 74.5]
plt.barh(index,values)
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Happy coding")
x_pos = [i for i, _ in enumerate(index)]
plt.yticks(x_pos, index)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

#task9
import matplotlib.pyplot as plt
index=[ 'Python', 'Java', 'C', 'C++', 'R', 'JavaScript', 'C#']
values=[100, 96.3, 94.4, 87.5, 81.5, 79.4, 74.5]
plt.barh(index,values,color=('red', 'black', 'green', 'blue', 'yellow', 'cyan'))
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Happy coding")
x_pos = [i for i, _ in enumerate(index)]
plt.yticks(x_pos, index)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
"""

#task10
import matplotlib.pyplot as plt
index=[ 'Python', 'Java', 'C', 'C++', 'R', 'JavaScript', 'C#']
values=[100, 96.3, 94.4, 87.5, 81.5, 79.4, 74.5]
plt.bar(index,values,color=('red', 'black', 'green', 'blue', 'yellow', 'cyan'))
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Happy coding")
x_pos = [i for i, _ in enumerate(index)]
plt.xticks(x_pos, index)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
for x,y in zip(index,values):
    plt.text("Test",ha='center',va='bottom')     
plt.show()
