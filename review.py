my_var = 2
my_var_2 = 2


print(type(my_var))
print(type(my_var_2))



colors = ["rojo", "azul", "verde", "amarillo", "naranja"]

print(type(colors))


print(len(colors))


print(colors[2])

colors.append('Púrpura')


print('verde' in colors)


# Loops

print('--------------------')
for i in range(0,len(colors)):
    print(i)

for i in colors:
    print(i)


# 

def return_something():
    """This function will return any value"""
    a = 2
    # return 50

print(return_something())
