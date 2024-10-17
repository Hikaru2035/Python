import json
 
file_path = "char_classes.json"
 
with open('Lab_10/char_classes.json', 'r') as file:
    data = json.load(file)
 
table_headers = ["Class", "Strength", "Intelligence", "Wisdom", "Dexterity", "Constitution"]
table_rows = []
 
for class_name, attributes in data.items():
    row = [class_name.capitalize()]
    for attr in ["str", "int", "wis", "dex", "con"]:
        row.append(str(attributes.get(attr, "-")))
    table_rows.append(row)
 
max_lengths = [len(header) for header in table_headers]
for row in table_rows:
    for i, value in enumerate(row):
        max_lengths[i] = max(max_lengths[i], len(value))
 
separator = "+".join("-" * (length + 2) for length in max_lengths)
header_row = "| " + " | ".join(f"{header.center(max_lengths[i])}" for i, header in enumerate(table_headers)) + " |"
separator_row = f"+{separator}+"
 
print(separator_row)
print(header_row)
print(separator_row)
 
for row in table_rows:
    formatted_row = "| " + " | ".join(f"{value.center(max_lengths[i])}" for i, value in enumerate(row)) + " |"
    print(formatted_row)
 
print(separator_row)