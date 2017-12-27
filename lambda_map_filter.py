#lambda with map and filter
m=[1,2,3,4]
#filter gives the output for condition which is true
new=list(filter(lambda x: (x**2),m))
#map gives the output for all the values in the list i.e for true and false
new_map=list(map(lambda x: (x**2), m))
print(new_map)
print(new)
