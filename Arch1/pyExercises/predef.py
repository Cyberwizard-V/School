
# Usually companies use a predefined templates in their emails. 
# A company named XYZ would like to have a Python program that collects basic information and generates the content of the email. 
# You are assigned to implement the program with the following criteria:
# - There are only two templates: Job Offer and Rejection.
# - For the Job Offer email, the program asks: first name, last name, job title, annual salary, starting date.
# - For the Rejection email, the program asks: first name, last name, job title, with or without feedback, one feedback statement in case it is with feedback.
# - The program must check valid input formats.
# - First and last names: each minimum two characters and maximum ten characters; cotaining only alphabets, both starting with capital letters.
# - Job title: minimum 10 characters without numbers.
# - Salary: valid floating point number between (and including) 20.000,00 and 80.000,00.
# - Date: only in YYYY-MM-DD format, no negative numbers, days between 1 - 31, month between 1 - 12, year only 2021 and 2022.
# - Feedback: if the email contains a feedback there is an extra line in the text otherwise that line must be removed (check the example below).
# - The program will generate emails until the user answers No to the More Letters? question.
# - In case of invalid input from the user, the program must proper message and then repeats the question again.
# - A sample execution is presented below. Use this sample execution for the templates of the emails. Your program must have only two templates:
# More Letters?(Yes or No)Yes
# Job Offer or Rejection?Job Offer
# First Name? John
# Last Name? Hartman
# Job Title? Junior Python Programmer
# Annual Salary? 30.500,50
# Start Date?(YYYY-MM-DD) 2021-01-01
# Here is the final letter to send:
# Dear John Hartman, 
#  After careful evaluation of your application for the position of Junior Python Programmer, 
#  we are glad to offer you the job. Your salary will be 30.500,50 euro annually. 
# Your start date will be on 2021-01-01. Please do not hesitate to contact us with any questions. 
# Sincerely, 
# HR Department of XYZ 
# More Letters?(Yes or No)Yes
# Job Offer or Rejection?Rejection
# First Name? David
# Last Name? Johanson
# Job Title? Junior C++ Programmer
# Feedback? (Yes or No) No
# Here is the final letter to send:
# Dear David Johanson, 
# After careful evaluation of your application for the position of Junior C++ Programmer, 
# at this moment we have decided to proceed with another candidate. 
# We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions. 
# Sincerely, 
# HR Department of XYZ 
# More Letters?(Yes or No)Yes
# Job Offer or Rejection?Rejection
# First Name? David
# Last Name? Chan
# Job Title? Software Tester
# Feedback? (Yes or No) Yes
# Enter your Feedback (One Statement): You have sufficient testing knowledge but we expected to see more experience in web application testing techniques.
# Here is the final letter to send:
# Dear David Chan, 
# After careful evaluation of your application for the position of Software Tester, 
# at this moment we have decided to proceed with another candidate. 
# Here we would like to provide you our feedback about the interview.
# You have sufficient testing knowledge but we expected to see more experience in web application testing techniques. 
# We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions. 
# Sincerely, 
# HR Department of XYZ 
# More Letters?(Yes or No)No
import re

patt = "/^\d{4}-\d{2}-\d{2}$/"


def job_offer(first_name, last_name, job_title, salary, start_date):
    print("Here is the final letter to send:")
    print("Dear", first_name, last_name + ",")
    print("After careful evaluation of your application for the position of", job_title + ",")
    print("we are glad to offer you the job. Your salary will be", salary + " euro annually.")
    print("Your start date will be on", start_date + ". Please do not hesitate to contact us with any questions.")
    print("Sincerely,")
    print("HR Department of XYZ")

def rejection(first_name, last_name, job_title, feedback, feedback_statement = "none"):
    print("Here is the final letter to send:")
    print("Dear", first_name, last_name + ",")
    print("After careful evaluation of your application for the position of", job_title + ",")
    print("at this moment we have decided to proceed with another candidate.")
    if feedback == "Yes":
        print("Here we would like to provide you our feedback about the interview.")
        print(feedback_statement)
    print("We wish you the best in finding your future desired career. Please do not hesitate to contact us with any questions.")
    print("Sincerely,")
    print("HR Department of XYZ")



# - First and last names: each minimum two characters and maximum ten characters; cotaining only alphabets, both starting with capital letters.
# - Job title: minimum 10 characters without numbers.
# - Salary: valid floating point number between (and including) 20.000,00 and 80.000,00.
# - Date: only in YYYY-MM-DD format, no negative numbers, days between 1 - 31, month between 1 - 12, year only 2021 and 2022.
# - Feedback: if the email contains a feedback there is an extra line in the text otherwise that line must be removed (check the example below).
# - The program will generate emails until the user answers No to the More Letters? question.
# - In case of invalid input from the user, the program must proper message and then repeats the question again.
moreLetters = input("More Letters?(Yes or No) ")
if moreLetters == "Yes":
    while moreLetters == "Yes":
        letter_type = input("Job Offer or Rejection? ")

        first_name = input("First Name? ")
        #check firstname format each minimum two characters and maximum ten characters; cotaining only alphabets, both starting with capital letters.
        if len(first_name) < 2 or len(first_name) > 10:
            print("Input error")
            first_name = input("First Name? ")
        elif first_name.isalpha() == False:
            print("Input error")
            first_name = input("First Name? ")
        elif first_name[0].isupper() == False:
            print("Input error")
            first_name = input("First Name? ")

        last_name = input("Last Name? ")
        #check lastname format each minimum two characters and maximum ten characters; cotaining only alphabets, both starting with capital letters.
        if len(last_name) < 2 or len(last_name) > 10:
            print("Input error")
            last_name = input("Last Name? ")
        elif last_name.isalpha() == False:
            print("Input error")
            last_name = input("Last Name? ")
        elif last_name[0].isupper() == False:
            print("Input error")
            last_name = input("Last Name? ")
        job_title = input("Job Title? ")
        #minimum 10 characters without numbers.
        if len(job_title) < 10:
            print("Input error")
            job_title = input("Job Title? ")

        if letter_type == "Job Offer":
            salary = input("Annual Salary? ")
            
            start_date = input("Start Date?(YYYY-MM-DD) ")
            #regex match pattern
            if re.match(patt, start_date):
                print("Input error")
                start_date = input("Start Date?(YYYY-MM-DD) ")
            elif int(start_date[0:4]) != 2021 and int(start_date[0:4]) != 2022:
                print("Input error")
                start_date = input("Start Date?(YYYY-MM-DD) ")
            elif int(start_date[5:7]) < 1 or int(start_date[5:7]) > 12:
                print("Input error")
                start_date = input("Start Date?(YYYY-MM-DD) ")
            elif int(start_date[8:10]) < 1 or int(start_date[8:10]) > 31:
                print("Input error")
                start_date = input("Start Date?(YYYY-MM-DD) ")
                


            job_offer(first_name, last_name, job_title, salary, start_date)
        elif letter_type == "Rejection":
            feedback = input("Feedback? (Yes or No)")
            if feedback == "Yes":
                feedback_statement = input("Enter your Feedback (One Statement):")
                rejection(first_name, last_name, job_title, feedback, feedback_statement)
            else:
                rejection(first_name, last_name, job_title, feedback)
        moreLetters = input("More Letters?(Yes or No)")
else:
    print("Goodbye")