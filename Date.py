#Program reads string from user containing date in the form mm/dd/yyyy. 
#It should print the date in the format March 12, 2018
#George Curry

#get user input
date = input("Please Enter date in the format mm/dd/yyyy:\n")

#make a dictionary for months (key:Value)
months = {
    "01":"January",
    "02":"Febuary",
    "03":"March",
    "04":"April",
    "05":"May",
    "06":"June",
    "07":"July",
    "08":"August",
    "09":"September",
    "10":"October",
    "11":"November",
    "12":"December"
}
#make a function that searches through dictonary for key inside string, 
#if found return string
def writeDate(date):
    key = date[0:2]#gets the first 2 numbers inside string
    if key in months:
        print(months[key]+" "+date[3:5]+", "+date[6:])
        #proper format using splicing

#call function
writeDate(date)

