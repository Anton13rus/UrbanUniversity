my_dict = {"Sergey" : 1993, "Vacia" : 1998, "Pasha" : 2001}
print(my_dict)
print(my_dict["Sergey"])
my_dict["Kolya"] = 2006
my_dict.update({"Petr" : 2000,
                "Ivan" : 2011})
del my_dict["Vacia"]
print(my_dict.get("Vacia"))
print(my_dict)

my_set = {1, 1, 2, 3, 2, 3, 4, 5, "apple", 'cucumber'}
print(my_set)
my_set.add(9)
my_set.add(7)
my_set.discard(1)
print(my_set)
