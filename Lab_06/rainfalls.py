def print_vertical_histogram(rainfall_data, column_width):
    max_rainfall = max(rainfall_data.values())

    for level in range(int(max_rainfall), 0, -1):
        for month in rainfall_data:
            print(('x' if rainfall_data[month] >= level else ' ').center(column_width), end='')
        print() 
    
    for month in rainfall_data:
        print(f'{month}'.center(column_width), end='')

def main():
    rainfall_data = {}
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    column_width = max(len(month) for month in months) + 3

    for month in months:
        rainfall = float(input(f"Enter rainfall for {month}: "))
        rainfall_data[month] = rainfall

    print("\nRainfall Histogram")
    print_vertical_histogram(rainfall_data, column_width)

    print("\nProcess finished with exit code 0")

main()