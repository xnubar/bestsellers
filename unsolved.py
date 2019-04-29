import inquirer

def menu():
    questions = [
    inquirer.List('option',
                  message="The menu options are",
                  choices=['1: Look up year range', '2: Look up month/year', '3: Search for author', '4: Search for title','Q: Quit'],
              ),
    ]
    answer = inquirer.prompt(questions)
    return answer['option']




def read():
    with open("bestsellers.txt","r") as f:
        return f.read()

def search_by_year_range():
    from_year = int(input("Enter beginning year: "))
    to_year = int(input(" Enter ending year: "))
    print(f"All Titles between {from_year} and {to_year} :")
    for i in read().split("\n"):
        year = int(i.split("\t")[3].split("/")[2])
        if year>=from_year and year<=to_year:
            print(i)
            print("____________________________________________________________________\n")

        
def search_by_specific_month_year():
    searched_year = int(input("Enter year: "))
    searched_month = int(input("Enter month (as a number, 1-12): "))
    print(f"All Titles in month {searched_month} of {searched_year} :")
    for i in read().split("\n"):
        year = int(i.split("\t")[3].split("/")[2])
        month = int(i.split("\t")[3].split("/")[0])
        if year == searched_year and month == searched_month:
            print(i)
            print("____________________________________________________________________\n")


def search_by_author_name():
    searched_author = input(" Enter an author's name (or part of a name): ").capitalize()
    for i in read().split("\n"):
        author = i.split("\t")[1]
        if  searched_author in author:
            print(i)
            print("____________________________________________________________________\n")

def search_by_book_title():
    searched_title = input("Enter a title (or part of a title): ").capitalize()
    for i in read().split("\n"):
        title = i.split("\t")[0]
        if searched_title in title:
            print(i)
            print("____________________________________________________________________\n")



def main():
    choice = menu()
    while True:
        if choice == "1: Look up year range":
            search_by_year_range()
        elif choice == "2: Look up month/year":
            search_by_specific_month_year()
        elif choice == "3: Search for author":
            search_by_author_name()
        elif choice =="4: Search for title":
            search_by_book_title()
        elif choice == "Q: Quit":
            break
            

main()