#PROJECT 1
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
n = int(input("Enter the number up to which you want to play Fizz Buzz: "))
fizz_buzz(n)

#PROJECT 2
def calculate_average_budget(movies):
    total_budget = sum([budget for name, budget in movies])
    average_budget = total_budget / len(movies)
    return average_budget

def find_high_budget_movies(movies, average_budget):
    high_budget_movies = []
    for name, budget in movies:
        if budget > average_budget:
            high_budget_movies.append((name, budget, budget - average_budget))
    return high_budget_movies

def print_high_budget_movies(high_budget_movies, average_budget):
    print(f"\nAverage Budget: ${average_budget:,.2f}")
    print("\nMovies with a budget higher than the average:")
    for name, budget, difference in high_budget_movies:
        print(f"{name}: ${budget:,.2f} (Exceeds by ${difference:,.2f})")
    
    print(f"\nTotal movies exceeding the average budget: {len(high_budget_movies)}")

def add_movies_to_list(movies):
    num = int(input("\nHow many movies would you like to add? "))
    for i in range(num):
        name = input(f"Enter movie {i+1} name: ")
        budget = int(input(f"Enter movie {i+1} budget: "))
        movies.append((name, budget))

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
add_movies_to_list(movies)

average_budget = calculate_average_budget(movies)

high_budget_movies = find_high_budget_movies(movies, average_budget)
print_high_budget_movies(high_budget_movies, average_budget)
