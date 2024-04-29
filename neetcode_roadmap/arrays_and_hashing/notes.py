from collections import defaultdict
"""
Defaultdict is a sub-class of the dictionary class that returns a 
dictionary-like object. The functionality of both dictionaries and
defaultdict are almost same except for the fact that defaultdict
never raises a KeyError. It provides a default value for the key
that does not exists.
defaultdict() has the first argument must be callable or None, which
will be returned if the key is not found in the dictionary.
"""

a = dict()
a[0] = (["1","2"])
a[1] = (("1","2"))
# ERROR: 'a[["1","2"]] = (["1","2"])'.
a[("1","2")] = (("1","2"))

# b = defaultdict(lambda: "There is no such key in the dictionary.")
b = defaultdict(list)
b[0] = (["1","2"])
b[1] = (("1","2"))
b[("1","2")] = (("1","2"))

print(a)
print(a[1])
#print(a[100])
#ERROR: 'a[key]' when the key does not exist in the dictionary
print(b)
print(b[1])
print(b[100]) # defaultdict() returns an empty list when the key is not found
# but you are allowed to b[new_key].append(new_value), even though the key does
# not exist in the defaultdictionary.

# Multiplication of a list
count = [0, 1, 2, 3] * 3
print(count)

# Unicode point for a one-character string (lower and upper cases have different values)
# ASCII - American Standard Code for Information Interchange
# The unicode from 'a' to 'z' is linear, starting from 97
unicode_point_a = ord('a')
print(unicode_point_a)

unicode_point_z = ord('z')
print(unicode_point_z)
print(unicode_point_z - unicode_point_a)

print("\ndefault dict")
default_dict = defaultdict(list)
default_dict[1].append('2')
default_dict[1].append('3')
values_dict1 = default_dict.values()
print(values_dict1)