import json

# Get user input
i = int(input("Enter a number"))


numbers = [i]  # Start the list with the initial number

while i != 1:
    if i % 2 == 0:  
        i = i // 2  # If even, divide by 2
    else:
        i = i * 3 + 1  # If odd, apply 3n + 1 rule

    numbers.append(i)  # Store each step
    print(i)

# Save data as a single JSON object
data = {"Numbers": numbers}

with open("data.json", "w") as file:  # "w" mode overwrites old content
    json.dump(data, file, indent=4)  # Pretty-print JSON
