def get_initials(input_str):
  initials = ""
  input_str_list = list(input_str)
  for char in input_str_list:
    if char.upper() == char:
      initials += char
  initials = initials.replace(' ','.')
  return initials


user_input = input("Enter your name: ")
result_initials = get_initials(user_input) + "."
print(result_initials)