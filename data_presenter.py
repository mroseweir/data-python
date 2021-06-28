#### PART 2####

# Create a new file called data_presenter.py.

# Open the CupcakeInvoices.csv.

# Loop through all the data and print each row.
data = open('CupcakeInvoices.csv')

for row in data:
  print(row)
data.close()

# Loop through all the data and print the type of cupcakes purchased.

data = open('CupcakeInvoices.csv')
for item in data:
  item = item.rstrip('/n').split(',')
  print(item[2])


# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).

data = open('CupcakeInvoices.csv')
for item in data:
  item = item.rstrip('/n').split(',')
  num_cup = float(item[3])
  price_cup = float(item[4])
  print(round(num_cup * price_cup, 0))
data.close()


# Loop through all the data, and print out the total for all invoices combined.
data = open('CupcakeInvoices.csv')
total = 0
for item in data:
  item = item.rstrip('/n').split(',')
  num_cup = float(item[3])
  price_cup = float(item[4])
  total += round(num_cup * price_cup, 0)
print(total)
data.close()

####
# print('____')

data = open('CupcakeInvoices.csv')
total = 0
for item in data:
  item = item.rstrip('/n').split(',')
  num_cup = float(item[3])
  price_cup = float(item[4])
  price = num_cup * price_cup
  total += price
  # print(price)
print(round(total, 0))
data.close()


# Close your open file.