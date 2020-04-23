import random

def generate_rps():
    """A function to generate a choice of (r)ock, (p)aper, or (s)cissors."""
    randnum = random.randint(0, 2)
    if randnum == 0:
        computer = 'r'
    elif randnum == 1:
        computer = 'p'
    else:
        computer = 's'
    return computer

def play_rps(p0, p1, score=0):
    """A function to play the game Rock, Paper, Scissors."""
    if p0 == p1:
        print("It's a tie!!\n")
    elif p0 == 'r':
        if p1 == 'p':
            print("Computer beats you with paper. You lose.\n")
        elif p1 == 's':
            score += 1
            print("You beat the computer with rock.")
            print("\nYou Are A Winner!!!\n")
    elif p0 == 'p':
        if p1 == 'r':
            score += 1
            print("You beat the computer with paper.")
            print("\nYou Are A Winner!!\n")
        elif p1 == 's':
            print("Computer beats you with scissors. You lose.\n")
    elif p0 == 's':
        if p1 == 'r':
            print("Computer beats you with rock. You lose.\n")
        elif p1 == 'p':
            score += 1
            print("You beat the computer with scissors.")
            print("\nYou Are A Winner!!\n")
    return score

running = True # A flag to keep the game going.
score = 0
games = 0
while running:
    print("Welcome to Rock, Paper, Scissors.")
    print("Type 'r' for rock.")
    print("Type 'p' for paper.")
    print("Type 's' for scissors.")
    print("Type 'q' to quit the game.\n")
    p0 = input("Please enter your choice: ")
    if p0 == 'q':
        running = False
    else:
        p1 = generate_rps()
        score += play_rps(p0, p1)
        games += 1

print(f"You played {games} games and won {score} of them.")


