x = 10
y = 'Anthony'

z = x
x = y
y = z

print("x = {} e y = {}".format(x,y))

# Em python fazemos assim :

x,y = y,x
print("\33[32mx = {} e y = {}".format(x,y))

X = 10
Y = "Anthony"
z = True

x,y,z = z,x,y
print("\33[32mx = {}, y = {} e z = {}".format(x,y,z))