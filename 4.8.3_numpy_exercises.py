import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?
a_negative = a < 0

count_negative_in_a = a_negative.sum()

assert count_negative_in_a == 4

# How many positive numbers are there?
a_positive = a > 0

count_positive_in_a = a_positive.sum()

assert count_positive_in_a == 5

# How many even positive numbers are there?
a_even_positive = a[a_positive] % 2 == 0

count_even_positive = a_even_positive.sum()

assert count_even_positive == 3

# If you were to add 3 to each data point, how many positive numbers would there be?
a_add_3_positive = (a + 3) > 0

count_add_3_positive = a_add_3_positive.sum()

assert count_add_3_positive == 10

# If you squared each number, what would the new mean and standard deviation be?
a_squared = a ** 2

print(f"The mean of a^2 is {a_squared.mean()}") # 74.0
print(f"The standard deviation of a^2 is {a_squared.std()}") # 144.0243035046516

# A common statistical operation on a dataset is centering. This means to adjust the data 
# such that the center of the data is at 0. This is done by subtracting the mean from each 
# data point. Center the data set.
a_centered = a - a.mean()
print(f"A centered is {a_centered}")

# Calculate the z-score for each data point.
z_score = (a - a.mean()) / a.std()

print(f"The z score of each data point is {z_score}")
print(f"Check z score accuracy: mean should be 0: {z_score.mean()} and std should be 1: {z_score.std()}")

# Copy the setup and exercise directions from More Numpy Practice into your 
# 4.8.3_numpy_exercises.py and add your solutions.
import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above 
# list
sum_of_a = sum(a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the 
# above list
min_of_a = min(a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in 
# the above list
max_of_a = max(a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in 
# the above list
mean_of_a = sum(a) / len(a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all 
# the numbers in the above list together
product_of_a = []

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared 
# like [1, 4, 9, 16, 25...]
squares_of_a = [x ** 2 for x in a]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [x for x in a if x % 2 == 1]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [x for x in a if x % 2 == 0]

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a 
# chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, 
# and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

b_array = np.array(b)
# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, 
# you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_of_b_array = b_array.sum()
# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b_array = b_array.min()

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b_array = b_array.max()

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b_array = b_array.mean()

# Exercise 5 - refactor the following to use numpy for calculating the product of all 
# numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_of_b_array = b_array.prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b_array = np.square(a)

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b_array = b_array[b_array % 2 == 1]

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

evens_in_b_array = b_array[b_array % 2 == 0]

# Exercise 9 - print out the shape of the array b.
print(np.shape(b_array))

# Exercise 10 - transpose the array b.
trans_b_array = b_array.transpose()
print(trans_b_array)

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
reshape_b_array_1_x_6 = b_array.reshape((1, 6))
print(reshape_b_array_1_x_6)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number 
# (6 x 1)
reshape_b_array_6_x_1 = b_array.reshape((6, 1))
print(reshape_b_array_6_x_1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array(c)
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to 
# using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
min_c = c.min()
print(min_c)

max_c = c.max()
print(max_c)

sum_c = c.sum()
print(sum_c)

product_c = c.prod()
print(product_c)

# Exercise 2 - Determine the standard deviation of c.
std_c = c.std()
print(std_c)

# Exercise 3 - Determine the variance of c.
var_c = c.var()
print(var_c)

# Exercise 4 - Print out the shape of the array c
print(np.shape(c))

# Exercise 5 - Transpose c and print out transposed result.
trans_c = c.transpose()
print(trans_c)

# Exercise 6 - Get the dot product of the array c with c. 
dot_prod_c = c.dot(c)
print(dot_prod_c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. 
# Answer should be 261
sum_of_c_times_trans_c = (c * trans_c).sum()
print(f"c: {c} trans_c: {trans_c}")
print(c * trans_c)
print(sum_of_c_times_trans_c)
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. 
# Answer should be 131681894400.
prod_of_c_times_trans_c = (c * trans_c).prod()
print(prod_of_c_times_trans_c)


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)
# Exercise 1 - Find the sine of all the numbers in d
sine_d = np.sin(d)
print(sine_d)

# Exercise 2 - Find the cosine of all the numbers in d
cos_d = np.cos(d)
print(cos_d)

# Exercise 3 - Find the tangent of all the numbers in d
tan_d = np.tan(d)
print(tan_d)

# Exercise 4 - Find all the negative numbers in d
all_negs_d = d[d < 0]
print(all_negs_d)

# Exercise 5 - Find all the positive numbers in d
all_pos_d = d[d > 0]
print(all_pos_d)

# Exercise 6 - Return an array of only the unique numbers in d.
unique_val_d = np.unique(d)
print(unique_val_d)

# Exercise 7 - Determine how many unique numbers there are in d.
num_unique_d = unique_val_d.size
print(num_unique_d)

# Exercise 8 - Print out the shape of d.
print(d.shape)

# Exercise 9 - Transpose and then print out the shape of d.
print(d.T.shape)
# Exercise 10 - Reshape d into an array of 9 x 2
d_9_x_2 = d.reshape((9,2))
print(d_9_x_2)