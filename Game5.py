import random

class BattleCard:
    def __init__(self, pattern, rank):
        self.pattern = pattern # Rock, Paper, or Scissors
        self.rank = rank       # 1 to 10
        
    def __str__(self):
        return f"[{self.pattern} - Level {self.rank}]"

def solve_battle(p_card, c_card):
    # Standard RPS Logic
    wins = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
    
    if p_card.pattern == c_card.pattern:
        # RPS Tie: Check Card Rank
        if p_card.rank > c_card.rank:
            return "Win (Rank Tie-break)"
        elif p_card.rank < c_card.rank:
            return "Loss (Rank Tie-break)"
        return "Complete Draw"
    
    if wins[p_card.pattern] == c_card.pattern:
        return "Win (RPS Advantage)"
    return "Loss (RPS Disadvantage)"

def play_game():
    patterns = ["Rock", "Paper", "Scissors"]
    
    # Generate a random hand for the player
    player_hand = [BattleCard(random.choice(patterns), random.randint(1, 10)) for _ in range(3)]
    computer_card = BattleCard(random.choice(patterns), random.randint(1, 10))

    print(f"Computer draws a mystery card!")
    print("\nYour Hand:")
    for i, card in enumerate(player_hand):
        print(f"{i+1}: {card}")

    choice = int(input("\nPick a card (1-3) to battle: ")) - 1
    p_card = player_hand[choice]
    
    print(f"\nBATTLE: {p_card} vs {computer_card}")
    result = solve_battle(p_card, computer_card)
    print(f"RESULT: {result}")

if __name__ == "__main__":
    play_game()
