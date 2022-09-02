import re
str1="The dictionary is an unordered collection that contains" \
     " key:value pairs separated by commas inside curly brackets. " \
     "Dictionaries are optimized to retrieve values when the key is known." \
     " The following declares a dictionary object. Example: Dictionary."
dict1=re.findall("is",str1)
print(dict1)
dict2=re.search("key",str1)
print(dict2)
dict3=re.split(str1,"optimized")
print(dict3)
dict4=re.match(str1,"declares")
print(dict4)