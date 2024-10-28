Saul
Resendiz
		WEEK MODULE 7 LAB


	QUESTION 1:

def main():
    store_sales = [] 
    total_sales = 0

    for x in range(1, 8):
        while True:
            try:
                day_sales = float(input(f"Enter sales for day {x} of the week: "))
                store_sales.append(day_sales)  
                break  
            except ValueError:
                print("Invalid input. Enter a float integer value")

    total_sales = sum(store_sales)

    print(f'Total sales for the week: ${total_sales:.2f}')

if __name__ == "__main__":
    main()


	QUESTION 2:

import random

MAX_DIGITS = 7
START = 0
END = 9

def main():
    numbers = [0, 0, 0, 0, 0, 0, 0]     #Creating list of 7 numbs and initlaizing them 
    
    for x in range (MAX_DIGITS) :
        numbers[x] = random.randint(START,END)
    
    print(f'Here are your lottery numbers:')
    for x in range (MAX_DIGITS) :
        print(numbers[x], end ='')
    print()

main()

	QUESTION 3:

def main():
    total_rainfall = 0
    rainfall_counter = []
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    for x in months:
          rain = float(input(f"Enter  rainfall for month {x}: "))
          rainfall_counter.append(rain)

    # CALC TOTAL/AVG RAINFALL
    total_rainfall = sum(rainfall_counter)
    average_rainfall = (total_rainfall / 12)

    # CALC HIGHEST/LOWEST RAINFALLS 
    max_rainfall = max(rainfall_counter)
    min_rainfall = min(rainfall_counter)
    month_high = months[rainfall_counter.index(max_rainfall)]
    month_low = months[rainfall_counter.index(min_rainfall)]

    # print data to console
    print(f"Total rainfall for the year: {total_rainfall:.2f}")
    print(f"Average monthly rainfall: {average_rainfall:.2f}")
    print(f"Highest rainfall month: {month_high}")
    print(f"Lowest rainfall month: {month_low}")


if __name__ == "__main__":
    main()


	QUESTION 4:

def main():
    user_numbers = []
    
    # For loop of range 1-20 for num input
    for x in range(1, 21):
        number_input = float(input(f"Enter number for entry #{x}: "))
        user_numbers.append(number_input)

    # getting stats for numbers list
    lowest_num = min(user_numbers)
    highest_num = max(user_numbers)
    total = sum(user_numbers)
    average = total / len(user_numbers)

    # NUMBERS DATA DISPLAY
    print(f"\nLowest #: {lowest_num}")
    print(f"Highest #: {highest_num}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")

if __name__ == "__main__":
    main()


	QUESTION 5:

def main():
    try:
        with open("charge_accounts.txt", "r") as myfile:
            account_numbers_list = [line.strip() for line in myfile]     #putting the content of every line into a list of account nums
    except FileNotFoundError:
        print("Error: File was not found.")
        return

    # User input for acc charge number
    user_charge_account = input("Enter 7 digit charge account number: ")

    # determine if user input is found in the account nums list
    if (user_charge_account in account_numbers_list) :
        print("Acc number is valid.")
    else:
        print("Acc number is invalid.")

if __name__ == "__main__":
    main()


	QUESTION 6:

def larger_than_n(numbers_list, number n):
    # for loop in range of the numbers_list given as an argument, printing the number in the list if it is greater than the number n. 
    for x in numbers_list :
        if (x > n):
            print(x)

        
	QUESTION 7:

def main():
    #  writing answers in a list with correct order for their number spot
    test_correct_answers = ['A', 'C', 'A', 'A', 'D', 'C', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    
    # Read student's answers from the file
    with open('student_answers.txt', 'r') as myfile:
        student_answers = [line.strip() for line in myfile.readlines()]

    # Check answers and calculate results
    correct_answer_counter = 0
    incorrect_answer_counter = 0
    incorrect_answers = []

    for x in range(20):
        if (student_answers[x] == test_correct_answers[x]) :
            correct_answer_counter += 1
        else:
            incorrect_answer_counter += 1
            incorrect_answers.append(x + 1)  

    if (correct_answer_counter >= 15) :
        print("Congrats, you passed the driving exam!")
    else:
        print("Sorry you failed the driving exam.")

    # Display results
    print(f' Total correct answers: {correct_answer_counter}')
    print(f' Total incorrect answers: {incorrect_answer_counter}')
    print(f' Questions specifically answered wrong: {incorrect_answers}')

# Run the program
if __name__ == "__main__":
    main()


	QUESTION 8:

def main():
    with open('popular_names.txt', 'r') as myfile:
        popular_names_list = [line.strip() for line in myfile.readlines()]    # adding every name from each line to the list


    user_name_input = input("Enter a name: ")

    # checking if the name is in the popular names list
    if (user_name_input in popular_names_list) :
        print(f"{user_name_input} is among the most popular.")
    else:
        print(f"{user_name_input} is not among the most popular.")

if __name__ == "__main__":
    main()

	QUESTION 9:

def main():
    with open('USPopulation.txt', 'r') as file:
        population_data = [int(line.strip()) for line in file.readlines()]   # reading every line containing an integer from the file

    annual_changes = []  # The changes every year

    for x in range(1, len(population_data)):  #looping through the entire list of population data integers, starting from 1 for proper calulations
        year_change = population_data[x] - population_data[x - 1]  # calc the change from the previous year to the current year
        annual_changes.append(year_change)   # Now adding the yearly change into the annual changes list 

    total_annual_changes = sum(annual_changes)
    num_of_changes = len(annual_changes)
    average_annual_change = (total_annual_changes / num_of_changes)

     #Greatest/lowest year population calculations
    greatest_change_year = annual_changes.index(max(annual_changes)) + 1950 + 1  # +1 for proper year
    smallest_change_year = annual_changes.index(min(annual_changes)) + 1950 + 1  

    # Printing data to console
    print(f'The average annual change in population during the time period is: {average_annual_change:.2f}')
    print(f'The year with the greatest increase in population is: {greatest_change_year}')
    print(f'The year with the lowest increase in population is: {smallest_change_year}')

if __name__ == "__main__":
    main()



	QUESTION 10:

def main():
    with open('WorldSeriesWinners.txt', 'r') as myfile:
        team_winners = [line.strip() for line in myfile.readlines()]

    wins_counter = {}
    for x in team_winners:
        if x in wins_counter:
            wins_counter[x] += 1
        else:
            wins_counter[x] = 1

    # get  a team name from the user
    team_name = input("Enter a teams name: ")

    # print num of wins for team
    if team_name in wins_counter:
        print(f"{team_name} has won {wins_counter[team_name]} times.")
    else:
        print("They have not won.")

main()

