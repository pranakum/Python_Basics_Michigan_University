#rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"

rainfall_mi = rainfall_mi.split(',')
rainfall_mi = list(map(float, rainfall_mi))

count = 0
for i in rainfall_mi:
    if i > 3:
        count += 1


num_rainy_months = count
print(num_rainy_months)