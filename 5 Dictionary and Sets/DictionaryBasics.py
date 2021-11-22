mydict = {
    "Name" : "Peeyush Gaur",
    "Sem" : "3rd",
    "College" : "DSCE",
    "List" : [1, 2, 3],
    "anotherdict": {"abc":"xyz", "123":"456"}
}
print(mydict['Name'])
print(mydict['Sem'])
print(mydict['College'])
print(mydict['List'])
print(mydict['anotherdict'])
#Dictionary is mutable
mydict['Name'] = "Peeyush"
print(mydict['Name'])