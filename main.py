import random

def generate_lottery_numbers():
    main_numbers = random.sample(range(1, 91), 6)
    main_numbers.sort()
    
    while True:
        joker = random.randint(1, 90)
        if joker not in main_numbers:
            break
    
    return main_numbers, joker

numbers, joker = generate_lottery_numbers()
print("Ana Numaralar:", numbers)
print("Joker (SuperStar):", joker)
