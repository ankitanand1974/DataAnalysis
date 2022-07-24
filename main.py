import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("      ___________________  ")
print("  -->|  Employee Details |<---")
print("     |___________________|     ")
print("                    ------->by Vasu Brother")

dataset = pd.read_csv("vasu.csv")
print("1 for salary frequency plot")
print("2 for department frequency plot")
print("3 to find employees with maximum salary")
print("5 to exit")
j = input("Enter your choice: ")
if (j==1) :
    dataset['SALARY'].value_counts().plot(kind='bar' , figsize=(12,12))
elif (j==2) :
    dataset['DEPARTMENT_10'].value_counts().plot(kind='bar' , figsize=(12,12))
elif (j==3) :
    print(dataset['SALARY'].max())
#elif (j==5) :
    