rating = {"Very Poor": 0, "Poor": 0, "Average": 0, "Good": 0, "Very Good": 0}

def rating_input(rating_index):
    match rating_index:
        case 1:
            rating["Very Poor"] += 1
            return True
        case 2:
            rating["Poor"] += 1
            return True
        case 3:
            rating["Average"] += 1
            return True
        case 4:
            rating["Good"] += 1
            return True
        case 5:
            rating["Very Good"] += 1
            return True
        case -1:
            return False
        case _:
            raise ValueError

            

def main():
    try:
        while True:
            print("Welcome to the restaurant rater!")
            print("Enter your rating")
            print("1. Very Poor")
            print("2. Poor")
            print("3. Average")
            print("4. Good")
            print("5. Very Good")
            print("Enter -1 to quit")
            rating_index = int(input("Enter your rating: "))
            if rating_input(rating_index): # if rating_input returns True, continue
                continue
            else: # if rating_input returns False, break
                print("Rating analysis:")
                for key, value in rating.items():
                    print(f"{value} people voted {key}")
                break
    except ValueError:
        print("Please enter a valid rating")
        main()

main()