name=" Sagar Khemnar !!!!!!"

upp=name.upper() # make a capital
low=name.lower() # make a small
cap=name.capitalize() # make a first letter capital
count=name.count("a")# make a count of a character
center=name.center(20)# make a center character
stripe= name.strip()# make a white space from front and end
rStripe=name.rstrip('!')# remove the trailing
replac=name.replace('a','b')# replace a word or character with another character
spli=stripe.split(" ") #make a array and add element with spacing between
endwi=name.endswith('!!!') # if ends with that then it will give true otherwise give false
find=name.find('Khemnar')


print(upp, low , cap, count, center)
print(stripe)
print(rStripe)
print(replac)
print(spli)
print(endwi)
print(find)