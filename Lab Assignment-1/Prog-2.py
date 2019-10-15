def tuple_to_dictionary(tup,dict):
    for m,n in tup:
        dict.setdefault(m,[]).append(n)
    return dict
    
def sorting(dict):
    for idx,list_of_tups in dict.items():
        dict[idx]=sorted(list_of_tups,key=lambda x: x[1]) #sorts on 1st value of list
    return dict
    
tup=[('John',('Physics',80)),('Daniel',('Science',90)),('John',('Science',95)),
     ('Mark',('Maths',100)),('Daniel',('History',75)),('Mark',('Social',95))]

dict={}
dict=tuple_to_dictionary(tup,dict)

print("Tuple to Dictionary")
print(sorting(dict))