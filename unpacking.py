listA=[2,3,4]
listB=[7,8,9]

listC=[]
listC.extend(listA)
listC.extend(listB)
listD=listA + listB

listC= [*listA, *listB, 8]

dictA= {"a": 1, "b": 2}
dictB= {"c": 3, "d": 4, "a": 10}

dictC = {**dictA, **dictB, "f": 14}

value=[dictA.values(), *dictB]

print(value)

