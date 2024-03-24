#Data manipulation using lists and dictionaries

#Display welcome message to the screen
print ("Welcome to Achro's Ice Cream Shop!")

#Print a blank line for readibility
print()

#Creates a list to hold the flavors of ice cream to choose from
flavorsList = ["Vanilla", "Chocolate", "Strawberry", "Pistachio", "Butter Pecan", "Cookie Dough", "Neapolitan"]

#Change the name of one flavor in the list
flavorsList[5] = "Very Berry Strawberry"
print()
print (flavorsList)
print()

#Append a flavor to the end of the list
flavorsList.append("Blackberry Cheesecake")
print()
print (flavorsList)
print()

#Sorting the list
flavorsList.sort()

#Storing the number of items in the list in a variable
numFlavors = len(flavorsList)

#Display the number of items in the list
print ("These are the ", numFlavors, " flavors we have available today: ")

#Using a for loop to display the number and name of each item in the Ice Cream shopping list
for flavor in flavorsList:
    #Add one to the index value to show the item number to customers from one rather than from zero
    print ("Flavor #: ", (flavorsList.index(flavor)+1), " ", flavor)

#Printing a blank line for readability
print()

#Create dictionaries to hold the price and descriptions of the sizes
conePrices = {"S":"$1.50", "M":"$2.50", "L":"$3.50"}
coneSizes = {"S":"Small Enough", "M":"Maybe Enough", "L":"Large Enough"}

#Prompt the user to enter a size
customerSize = input("Please select a cone size: S, M, or L: ")

#Check that a valid size value has been entered
if (customerSize != "S") and (customerSize != "M") and (customerSize != "L"):
    print ("We're sorry, but that is not a cone size we serve here. Please choose between S, M, or L.")
else:
    #If a valid size was enetered, prompt the user to enter a flavor number from the list shared
    customerFlavor = int(input("Please enter the number of which flavor you would like to get today: "))

    #Check that a valid flavor number has been entered
    if (customerFlavor < 1 or customerFlavor > 8):
        print ("We're sorry, but there is no flavor associated with that menu number. We currently have", numFlavors, "flavors of ice cream today.")
    else:
        #Printing a blank line for readability
        print()

        #Display the price for the size entered
        print ("Your total today is ringing up at:", conePrices[customerSize])

        #Display the size and flavor
        print ("Your", coneSizes[customerSize], "cone from Zach's Ice Cream Shop with the flavor", flavorsList[customerFlavor-1], "will be yours to enjoy in just a moment!")

        #Print another blank line for readability
        print()

#Display closing greeting to the screen upon exit
print("Thank you for coming to see us at Achro's Ice Cream Shop today!")