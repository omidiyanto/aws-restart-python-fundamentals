# Define the absolute path for the result file
ABSOLUTE_PATH_RESULT_FILE = './results.txt' 
# clear old file content before writing new results
with open(ABSOLUTE_PATH_RESULT_FILE, 'w') as file:
    file.write("")
    
# Print prime numbers from 1 to 250
for num in range(1, 251):
    if num > 1:  # prime numbers must be greater than 1
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
            
            with open(ABSOLUTE_PATH_RESULT_FILE, 'a') as file:
                file.write(f"{num}\n")
