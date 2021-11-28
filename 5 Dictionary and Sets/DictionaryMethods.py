mydict = {
    "Name" : "Peeyush Gaur",
    "Sem" : "3rd",
    "College" : "DSCE",
    "List" : [1, 2, 3],
    "anotherdict": {"abc":"xyz", "123":"456"}
}
print(mydict.values())
print(mydict.items())
print(mydict.keys())
print(mydict)
updatedict = {
    "Branch": "AI and ML"
}
mydict.update(updatedict)
print(mydict)
print(mydict.get("School")) #prints null doesn't throw error
#print(mydict["School"]) will throw an error as School isn't present in the Dict