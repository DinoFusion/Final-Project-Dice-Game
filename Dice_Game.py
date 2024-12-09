import random
import seaborn as sns
import matplotlib.pyplot as plt

class DiceGame:
    def __init__(self, target_score):
        self.target_score = target_score
        self.players = []
        self.scores = {}

    def add_player(self, player_name):
        """Add a player to the game."""
        self.players.append(player_name)
        self.scores[player_name] = 0

    def roll_dice(self, num_dice=3):
        """Roll a specified number of dice."""
        return [random.randint(1, 6) for _ in range(num_dice)]
        
    def visualize_scores(self):
    """Visualize the current scores using a bar chart."""
    plt.figure(figsize=(8, 5))
    sns.barplot(x=list(self.scores.keys()), y=list(self.scores.values()), palette="viridis")
    plt.title("Player Scores")
    plt.xlabel("Players")
    plt.ylabel("Scores")
    plt.ylim(0, self.target_score)  # Ensure y-axis corresponds to the target score
    plt.show()
   
    def play_turn(self, player):
        """Simulate a single turn for a player."""
        print(f"\n{player}'s turn:")
        dice = self.roll_dice()
        print(f"Initial roll: {dice}")

        while True:
            # Check for "tupled out" condition
            if len(set(dice)) == 1:  # All dice have the same value
                print(f"Tupled out! {player} scores 0 points this turn.")
                return 0

            # Fix dice with the same value
            fixed_dice = [value for value in dice if dice.count(value) > 1]
            num_fixed = len(fixed_dice)
            print(f"Fixed dice: {fixed_dice}")

            # If all dice are fixed, player must stop
            if num_fixed == 3:
                print(f"{player} scores {sum(dice)} points.")
                return sum(dice)

            # Allow player to reroll unfixed dice
            reroll_choice = input("Reroll unfixed dice? (y/n): ").lower()
            if reroll_choice == 'y':
                num_reroll = 3 - num_fixed
                new_roll = self.roll_dice(num_reroll)
                print(f"Rerolled dice: {new_roll}")
                dice = fixed_dice + new_roll
                print(f"New dice: {dice}")
            else:
                print(f"{player} decides to stop and scores {sum(dice)} points.")
                return sum(dice)

    def play_game(self):
        """Run the game until a player reaches the target score."""
        while True:
            for player in self.players:
                score = self.play_turn(player)
                self.scores[player] += score
                print(f"{player}'s total score: {self.scores[player]}")

                # Check for a winner
                if self.scores[player] >= self.target_score:
                    print(f"\n{player} wins the game with {self.scores[player]} points!")
                    return

# Game setup
target_score = int(input("Enter the target score to win: "))
game = DiceGame(target_score)

num_players = int(input("Enter the number of players: "))
for i in range(num_players):
    player_name = input(f"Enter the name of player {i + 1}: ")
    game.add_player(player_name)

game.play_game()
