class Solution:
    # A method (DaysOfTheWeek) that takes in input (1-7) from a user
    def DaysofTheWeek(self, day1=None, day2=None, day3=None):
        days = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }

        #Checks the method argument and displays the corresponding day of the week
        try:
            if day1 is not None and day2 is None and day3 is None:
                day_number = day1
                if day_number in days:
                    print(days[day_number])
                else:
                    print("Invalid Number")

            #takes in 2 inputs (1-7) and store the corresponding Day of the week in a dictionary as the key
            # where the value is the number of times the user inputted that number.

            elif day1 is not None and day2 is not None and day3 is None:
                days_list = [int(day1), int(day2)]
                day_count = {}
                for day in days_list:
                    if day in days:
                        if days[day] in day_count:
                            day_count[days[day]] += 1
                        else:
                            day_count[days[day]] = 1
                for day, count in day_count.items():
                    print(f"Dictionary: key - {day}, Value - {count}")

            #takes the 3 inputs (1-7) i.e (the arguments) and store the corresponding Day of the week in a dictionary as the key
            # where the value is the number of times the user inputted that number.
            elif day1 is not None and day2 is not None and day3 is not None:
                days_list = [int(day1), int(day2), int(day3)]
                day_count = {}
                for day in days_list:
                    if day in days:
                        if days[day] in day_count:
                            day_count[days[day]] += 1
                        else:
                            day_count[days[day]] = 1
                for day, count in day_count.items():
                    print(f"Dictionary: key - {day}, Value - {count}")
            else:
                print("No input, please enter 1 or 2 numbers")
        except ValueError:
            return "Invalid Input. Please enter a valid number"


    #Method 1 is called inside this CallMethod to pass in the inputs as the argument
    def CallMethod(self):
        try:
            user_choice = int(input("Enter a number 1 or 2: "))
            if user_choice == 1:
                day_input = int(input("Enter a number (1-7): "))
                self.DaysofTheWeek(day_input)
            elif user_choice == 2:
                day_input = input("Enter 2 or 3 numbers (1-7), separated by space: ").split()
                if 2 <= len(day_input) <= 3:
                    self.DaysofTheWeek(*day_input)
                else:
                    print("Invalid input. Please enter 2 or 3 numbers.")
            else:
                print("Invalid number. Please enter either 1 or 2.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


solution = Solution()
solution.CallMethod()




