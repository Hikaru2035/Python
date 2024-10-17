# Prompt user for 5 strings
users = [input(f"Enter string {i + 1}: ") for i in range(5)]

# Sort the list alphabetically
sorted_string = sorted(user)

# Output the sorted strings
print("Strings after sorting:", sorted_string)
