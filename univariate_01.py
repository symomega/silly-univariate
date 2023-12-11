# -*- coding: utf-8 -*-

import numpy as np

"""
 The Univariate class stores one numeric variable and provides methods
 which calculate univariate summary statistics.
 
 Data should be provided to the class as a numpy array.
"""
class Univariate:
    
    # The initialisation method is used to define an instance of a class.
    # Input data should be a numpy array.
    def __init__(self, data):
        self.data = data
        self.n = len(data)
    
    # Update the data associated with an instance of class Univariate.
    # newdata should be a numpy array.
    def set_data(self, newdata):
        self.data = newdata
    
    def calc_mean(self):
        return sum(self.data) / len(self.data)

    def calc_range(self):
        print("Not implemented")
    
    def calc_median(self):
        print("Not implemented")
      
    def calc_var(self):
        avg = np.array(self.calc_mean())
        n = len(self.data)
        var = sum((self.data - avg)**2) / (n-1)
        return var
    
    def calc_correlation(self, other):
        print("Not implemented")
    
    # Use format strings to print summary statistics.
    def print_summary(self):      
        print(f"Mean: \t\t{self.calc_mean()}")
        print(f"Variance: \t{self.calc_var()}")
         
# Examples and Testing

# Create a numpy array to store our data and use with the Univariate class
mydata = np.array([2,3,5,7,11])
u = Univariate(mydata)

# Try out some methods
print(u)
print(u.calc_mean())
print(u.calc_var())
u.print_summary()

mo_data_mo_problems = np.array([1,2,3,4,5])
u.set_data(mo_data_mo_problems)
u.print_summary()

baba = np.array([1,2,3])
x = Univariate(baba)
y = Univariate(baba)
x == y

