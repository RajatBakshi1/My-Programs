# Q4:-  Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer
#       variable points(your input). points can only take on positive integer values up to 200. 
# If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. If there's no prize,
# the message should state "Sorry! No prize this time."

# Points	Prize
# 1-50	        No Prize
# 51-150	Wooden Dog
# 151-180	Book
# 181-200	Chocolates
points=int(input("Enter your points:"))
if points>=181 and points<=200:
    print("Congratulations! You won chocolates")
elif points>=151 and points<=180:
    print("Congratulations! You won a Book")
elif points>=51 and points<=150:
    print("Congratulations! You won a Wooden Dog")
elif points>=1 and points<=50:
    print("Sorry! No prize this time")
elif points>200:
    print("INVALID POINTS ENTERED BECAUSE POINTS LIMIT EXCEEDS...")
    
