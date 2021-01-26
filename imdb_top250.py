import imdb
import random


print("Welcome to the imdb top 250\n")
print("MENU\n"
      "1) IMDB top 250\n"
      "2) IMDB top 10\n"
      "3) Random ")
choice = int(input("Enter the choice you would like to make: "))
ia = imdb.IMDb()
search = ia.get_top250_movies()
if choice == 1:  
    for i in range(250):
    	print(search[i])
elif choice == 2:
    for i in range(10):
    	print(search[i])
elif choice == 3:
    random_index = int(250 * random.random())
    print("Your random movie: {0}".format(search[random_index]))
    retry = input("Hit enter to search again ")
    if retry == "" :
    	random_index = int(250 * random.random())
    	print("Your random movie: {0}".format(search[random_index]))
    else: 
    	print("Enjoy")

else:
    print("invalid input")