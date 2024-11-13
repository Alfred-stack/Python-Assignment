# Assignment Instructions
# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a 
# discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price. 
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
# Print the final price after applying the discount, or if no discount was applied, print the original price.


# Function that calculates the discounted price

def calculate_discount(price, discount_percent):
  # To check if the discount is higher than 20% we will use the if statement
  if discount_percent >= 20:
  # We calculate the final price after discount
    final_price = price * (1-discount_percent / 100) # Using 1 - discount_percent would allow python to calculate the percentage as a whole
    return final_price
  # if the price is less than 20% we return the original price
  else:
      return price

# To prompt the user to provide the values we will use the input function
try:
  price = float(input("Enter the price of an item: $"))
  discount_percent = int(input("Enter the discount price of the item in percentage: "))


# To calculate the final price we will call the discount function

  final_price = calculate_discount(price, discount_percent)


# finally we will use a condition to print the output of the final price and discount to the user

  if final_price < price:
    print(f"the final price after applying the discount is: ${final_price: .2f} ") # Here .2f signifies converting to two decimal places, and the value is returned as a float

  else:
    print(f"there was no discount applied to your price therefor your original price is: ${price: .2f}")

except ValueError:
          print("Invalid Number, kindly enter a valid number to get a price or discount percentage")