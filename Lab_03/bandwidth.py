print("Enter current usage in bps (-1 to end)")
total = 0
while True:
    current_usage = int(input("Application:"))
    total += current_usage
    if current_usage == -1:
        break
    
usage = round((1000 - (total *(1/1000000))),2)
print("Capacity:", usage)

new_application = int(input("New application usage in Mbps:"))
usage = usage - new_application
print(round(usage,2))

