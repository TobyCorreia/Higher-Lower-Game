import art
import game_data
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def compare_a(name, followers, description, origin):
    print(f"Compare A: {name}, a {description}, from {origin}.")
    return (followers)


def compare_b(name, followers, description, origin):
    print(f"Against B: {name}, a {description}, from {origin}.")
    return (followers)


# score
game_over = False
current_score = 0

instagrammer = random.choice(game_data.data)
print(art.logo)

# repeat this game
while not game_over:
    # compare_a(instagrammer['name'], instagrammer['follower_count'], instagrammer['description'], instagrammer['country'])
    a = compare_a(instagrammer['name'], instagrammer['follower_count'], instagrammer['description'],
                  instagrammer['country'])

    print(art.vs)

    # creat random instagrammer
    instagrammer = random.choice(game_data.data)

    # compare_b(instagrammer['name'], instagrammer['follower_count'], instagrammer['description'], instagrammer['country'])
    b = compare_b(instagrammer['name'], instagrammer['follower_count'], instagrammer['description'],
                  instagrammer['country'])

    user_input = input("Who has more followers? Type 'A' or 'B': ")
    cls()
    print(art.logo)
    if user_input == 'A':
        if a > b:
            current_score += 1
            print(f"You're right! Current score: {current_score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game_over = True
    else:
        if b > a:
            current_score += 1
            print(f"You're right! Current score: {current_score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game_over = True






