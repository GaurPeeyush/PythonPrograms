def remove_and_strip(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()
str1 = "     My name is Peeyush Gaur    "
n = remove_and_strip(str1, "Gaur")
print(n)
