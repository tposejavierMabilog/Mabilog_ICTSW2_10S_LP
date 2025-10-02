from pyscript import display 
#resturant order system (python datatypes)

#string 
restaurant_name = "magic brew"
owner_name = "javier Mabilog"


# interger
year_since = 1700,

#float 
tax_rate = 0.08,

#Boolean 
has_devliery = True
is_dine_in = True
is_takeaway = False 

#list 
product_name = ["magic tea", "fire ball delight", "green nature milkshake","frozentea", "fizzy wonder "]


#business
business_hours = ("11:00 am", "11:00 pm")


#dictionary 
menu= {
    "magic tea" : 79.99,
    "fire ball delight" : 50,
    "green nature milkshake" : 150,
    "frozentea" : 30,
    "fizzy wonder": 20, 
}

#set 

common_allergens = {"gluten", "dairy", "nuts"}

display(restaurant_name, target="name1")
display(f"Owner:{owner_name}", target= "owner")
display(f"since{year_since}", target= "since")
display(f"Menu Pricelist", target= "heading1")

display(product_name[0], target="prod1")
display(f"${menu['magic tea']:.2f}", target="price1")

display(product_name[1], target="prod2")
display(f"${menu['fire ball delight']:.2f}", target="price2")

display(product_name[2], target="prod3")
display(f"${menu['green nature milkshake']:.2f}" ,target="price3")

display(product_name[3], target="prod4")
display(f"${menu['frozentea']:.2f}", target="price4")

display(product_name[4], target="prod5")
display(f"${menu['fizzy wonder']:.2f}", target="price5")

#display addition information \

display(f"open: {business_hours[0]} - {business_hours[1]}", target= "openingHours")

display(f"dine-in available", target="orderType")