# Program to manage a list of countries and their capital cities
def manage_countries():
    countries = {}
    while True:
        country = input("Enter the name of a country (or 'exit' to quit): ").strip().lower()
        if country == 'exit':
            print("Goodbye!")
            break
        if country in countries:
            print(f"The capital of {country.capitalize()} is {countries[country]}.")
        else:
            capital = input(f"Enter the capital city of {country.capitalize()}: ").strip()
            countries[country] = capital
            print(f"Added {country.capitalize()} with capital {capital}.")

