import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import time
# importing libraries

print("\t \t \t \t \t Welcome User\n")  # welcome message
print("The data of Gold,Platinum and Silver are given for 23 years from 2000-2023 you can predict the price of the precious metals.")

df=pd.read_excel('data.xlsx') # loading data
time.sleep(1.3) 
ip=input("Enter which item you want to see: ") # asking precious stone
  
def sorter(ip):

    df1=df[df['Item']==ip]  # filtering the data according to input
    global x,y
    x=(df1['Year'])  # create an object x for year as series
    y=(df1['Price'])   # create an object x for year as series

    how=int(input("How can you view the data \n1.Dataframe 2.Line chart:")) # asking how to view the data

    if how==1:
        print(df1) # print dataframe
        
    elif how==2:
        
        plt.plot(x,y,marker='o',color='red',label='Price')
        plt.xlabel('Year',color='blue')
        plt.ylabel('Price',color='blue')

        plt.title(ip + ' Price ',color='blue')  # plot a line chart
        plt.legend()
        plt.show()



def regression(a,b):
    sum_x=sum(a)
    sum_y=sum(b)
    sum_x_sq=sum((np.array(a))*(np.array(a)))
    sum_xy=sum(np.array(a)*np.array(b))

    #print(f"sum_x={sum_x}\nsum_y={sum_y}\nsum_x_sq={sum_x_sq}\nsum_xy={sum_xy}")


    m=(sum_y*sum_x_sq-sum_x*sum_xy)/((len(a))*sum_x_sq-(sum_x*sum_x)) # finding slope as m
    b=(len(a)*sum_xy-sum_x*sum_y)/((len(a))*sum_x_sq-(sum_x*sum_x)) # finding y intercept as b

    #print(f"slope(m)={m}\ny-intercept(b)={b}")
    global finder,Y
    finder=int(input("Which year you want to find price? ")) # asking user to give  which year you want in x axis

    Y=m+b*(finder) # calculating y 

    print(Y) # print y
    
    time.sleep(.5)


    # create a scatter plot to mark the value of finder(x) and Y(y)
def plotter():
    plt.scatter(x, y, marker='o', color='red', label='Actual data')
    plt.scatter(finder, Y, marker='o', color='green', label='New data')
    plt.xlabel("Year", color='blue')
    plt.ylabel("Price", color='blue')
    plt.title(f"Price of Y when X={finder}",color='blue')
    plt.legend()
    plt.show()

  

#------------------------------------------------------------------------------------------------------


time.sleep(1.5)


sorter(ip) # sorter() sort and result the data filtered data

time.sleep(1)
print("----------------------------------------------------------------------------------------------------------------------------------------------------------")

regression(x,y) # regression() calculates the value of y 

plotter() # plot the actual and new data in a scatter plot chart
