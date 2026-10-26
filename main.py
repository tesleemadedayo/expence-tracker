print("==============================")
print("     EXPENSE TRACKER")
print("==============================")

print("1.Add Expense")
print("2.View All Expenses")
print("3.View Total Spending")
print("4.View Spending by Category")
print("5.Exit")



choice = input("Choose and option: ")
print("You select option:", choice)


if choice == "1":
    print ("Add Expense selected")
    exname = input("Enter expense name: ")
    exprice = input("Enter expense amount: ")
    print("Expense added sucecssfully")
    print("expence:",exname)
    print("amount:",exprice)


# elif choice == "2":
#     print ("View all Expense selected")
# elif choice == "3":
#     print("View all Total Spending")
# elif choice == "4":
#     print("View all spending by category")
# elif choice == "5":
#     print("Goodbye")

# else:

print("Invalid Option!")
