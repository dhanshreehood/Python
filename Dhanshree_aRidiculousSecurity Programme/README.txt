We are going to create a ridiculous security programme called Dhanshree it's gonna have list of known users and everytime it runs will ask your name.
If your name is in the list it will wlcm you and ask if you want to remove name from the list.
If your name is not in the list it will ask if u like to be added in the list.

learning:
1. To add and remove the data in the list.
2. 'in' keyword

#to take input from user
# strip() for extra security, if user puts space while giving input name.
#capitalize() if i write name starting 1st letter from small letter, it will convert it to capital and then read with capital 1st letter, in this way u can give user flexibility.

"""
you get flexibility to remove the value ,
it depends:
1. del()
if you know the specific value that you want to delete.
ex: 
L = [1,2,3,4]
del L[0] #by indexing
ans-L = [2,3,4,1]

2. remove()
if you don't know the spacific value.
ex.
L = [1,2,3,4]
L.remove(1)
ans- L = [2,3,4,1]
"""