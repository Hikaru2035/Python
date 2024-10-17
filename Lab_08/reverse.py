def reverse_string(user_input):
 if user_input == 0:
   return user_input
 elif user_input != 0:
   reverse_user_string = user_input[::-1]
   return reverse_user_string
   

user_input = input("Enter a text: ")
result_after_reverse = reverse_string(user_input)
print(f"Text after reverse: {result_after_reverse}")