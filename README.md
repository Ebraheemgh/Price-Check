Price Check
There is a shop with old-style cash registers. Rather than scanning items and pulling the price from a database, the price of each item is typed in manually. This method sometimes leads to errors. Given a list of items and their correct prices, compare the prices to those entered when each item was sold. Determine the number of errors in selling prices.

Example
products = ['eggs', 'milk', 'cheese']
productPrices = [2.89, 3.29, 5.79]
productSold = ['eggs', 'eggs', 'cheese', 'milk']
soldPrice = [2.89, 2.99, 5.97, 3.29]



Price


Sold Product
Sold Price
Expected Price
Error
eggs
2.89
2.89
no
eggs
2.99
2.89
yes
cheese
5.97
5.79
yes
milk
3.29
3.29
no

The second sale of eggs has a wrong price, as does the sale of cheese. There are 2 errors in pricing.
Function Description 
Write the body of the function priceCheck and the test for this function in one of the recommended languages.
The function should have the following parameters:
string products[n]:  each products[i] is the name of an item for sale
string productPrices[n]:  each productPrices[i] is the price of products[i]
string productSold[m]:  each productSold[j] is the name of a product sold
float soldPrice[m]:  each soldPrice[j] contains the sale price recorded for productSold[j].
and return:
int: the number of sale prices that were entered incorrectly
Constraints
1 ≤ n ≤ 99
1 ≤ m ≤ 99
productPrices[i] ∈ products[n], where 0 ≤ i < m
1.00 ≤ productPrices[i], soldPrice[j] ≤ 100000.00, where 0 ≤ i < n, and 0 ≤ j < m
Example of Function Call
priceCheck(
	products=['rice', 'sugar', 'wheat', 'cheese'],
	productPrices=[16.89, 56.92, 20.89, 345.99],
	productSold=['rice', 'cheese'],
	soldPrice=[18.99, 400.89]
) => 2
The sales of rice and cheese were at the wrong prices. So, the number of sale prices that were entered incorrectly is 2:


Price


Product
Actual
Expected
Error
rice
18.99
16.89
yes
cheese
400.89
345.99
yes

You may use this example and the example in the beginning of the section as test data for your function.
