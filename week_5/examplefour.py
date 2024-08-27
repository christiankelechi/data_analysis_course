import nameparser
# Example names to parse
name1 = "John Doe"
name2 = "Doe, Jane"
# Parse the names
parsed_name1 = nameparser.HumanName(name1)
parsed_name2 = nameparser.HumanName(name2)
# Extract components of the name
print(parsed_name1.first)
print(parsed_name1.last)
print(parsed_name1.middle)
print(parsed_name2.first)
print(parsed_name2.last)
print(parsed_name2.middle)
if parsed_name1.first and parsed_name1.last:
    print("Name is valid")
else:
    print("Name is invalid")