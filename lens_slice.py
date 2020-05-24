
# We will create pizza list and price list. Then we will do a list by zipping two lists to sort them low to high. 
# We will calcualate the cheapest and expensive pizzas. Then we will count the number of the pizzas which includes specific price.
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas= len(toppings)
print("we sell " + str(num_pizzas) +" different kinds of pizza!")
pizzas = list(zip(prices, toppings))
print(pizzas)
pizzas.sort()
cheapest_pizza = pizzas[0]
priciest_pizzas = pizzas[-1]
three_cheapest = pizzas [:3]
print(three_cheapest)
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
