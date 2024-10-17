user = int(input("Choose a number from 1 to 7:"))

output = [[1,"One for sorrow"],
          [2,"Two for joy"],
          [3,"Three for a girl"],
          [4,"Four for a boy"],
          [5,"Five for silver"],
          [6,"Six for gold"],
          [7,"Seven for a secret never to be told"]]

for use, title in output:
    if user == use:
        print(title)
    elif user != use:
        pass
else:
    print("Not a permitted number")