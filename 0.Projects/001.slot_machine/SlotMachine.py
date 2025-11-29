import random
import time
import os

class SlotMachine:
    def __init__(self):
        # Define the symbols and their payouts
        self.symbols = {
            '🍒': 2,    # Cherry - low payout
            '🍋': 3,    # Lemon - medium payout
            '🍊': 4,    # Orange - medium payout
            '🍇': 5,    # Grape - high payout
            '🔔': 7,    # Bell - very high payout
            '💎': 10,   # Diamond - jackpot symbol
            '7️⃣': 15    # Seven - highest regular payout
        }

        # Player's balance
        self.balance = 100
        # Cost per spin
        self.spin_cost = 5
        # Track game statistics
        self.stats = {
            'spins': 0,
            'wins': 0,
            'total_win': 0,
            'biggest_win': 0
        }

    def clear_screen(self):
        """Clear the console screen for better visual experience"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_welcome(self):
        """Display welcome message and game rules"""
        print("🎰 WELCOME TO PYTHON SLOT MACHINE! 🎰")
        print("=" * 50)
        print(f"Starting Balance: ${self.balance}")
        print(f"Cost per spin: ${self.spin_cost}")
        print("\nSYMBOLS AND PAYOUTS:")
        print("-" * 30)

        for symbol, payout in self.symbols.items():
            print(f"  {symbol} -> {payout}x your bet")

        print("\nSPECIAL COMBINATIONS:")
        print("  Three Diamonds (  💎 💎 💎  ) -> JACKPOT! 100x bet")
        print("  Three 7s ( 7️⃣  7️⃣  7️⃣  ) -> MEGA JACKPOT! 200x bet")
        print("\nControls: 's' to spin, 'q' to quit")
        print("=" * 50)

    def spin_reels(self):
        """Simulate spinning the reels with animation"""
        reels = []
        print("\nSpinning...", end='', flush=True)

        # Create spinning animation
        for i in range(8):
            temp_reels = [random.choice(list(self.symbols.keys())) for _ in range(3)]
            print(f"\nSpinning... {'  '.join(temp_reels)}")
            # print(f"\rSpinning... {' '.join(temp_reels)}", end='', flush=True)
            time.sleep(0.1)

        # Final result
        final_result = [random.choice(list(self.symbols.keys())) for _ in range(3)]
        print(f"\rSpinning... {'  '.join(final_result)}", end='', flush=True)
        time.sleep(0.5)
        print() # New line after spinning

        return final_result
    
    def calculate_payout(self, result, bet):
        """Calculate payout based on the spin result"""
        # Check for special combinations first
        if result == ['💎', '💎', '💎']:
            return bet * 100, "🎉 JACKPOT! THREE DIAMONDS! 🎉"
        elif result == ['7️⃣', '7️⃣', '7️⃣']:
            return bet * 200, "🚀 MEGA JACKPOT! THREE 7s! 🚀"
        
        # Check for three of a kind (regular symbols)
        if result[0] == result[1] == result[2]:
            payout_multiplier = self.symbols[result[0]]
            return bet * payout_multiplier, f"Three {result[0]}s! {payout_multiplier}x payout!"
        
        # Check for two of a kind
        if result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
            # Find which symbol appears twice
            for symbol in set(result):
                if result.count(symbol) == 2:
                    payout_multiplier = max(1, self.symbols[symbol] // 3) # neglect friction ==> 2.5 becomes 2, against 1 and divided result and return max number 
                    return bet * payout_multiplier, f"Two {symbol}s! {payout_multiplier}x payout!"

        # No win
        return 0, "No win this time. Try again!"
    

    
    def display_result(self, result, payout, message):
        """Display the spin result and payout information"""
        print(f"\n🎯 RESULT: {' '.join(result)}")
        print(f"💬 {message}")
        
        if payout > 0:
            print(f"💰 You won: ${payout}!")
        else:
            print("😔 Better luck next spin!") 
        print(f"💵 Current Balance: ${self.balance}")



    def display_stats(self):
        """Display game statistics"""
        print("\n📊 GAME STATISTICS:")
        print(f"   Total Spins: {self.stats['spins']}")
        print(f"   Wins: {self.stats['wins']}")

        if self.stats['spins'] > 0:
            win_rate = (self.stats['wins'] / self.stats['spins']) * 100
            print(f" Win Rate: {win_rate:.1f}%")
        
        print(f" Total Won: ${self.stats['total_win']}")
        print(f" Biggest Win: ${self.stats['biggest_win']}")

    

    def play_game(self):
        """Main game loop"""
        self.clear_screen()
        self.display_welcome()

        while self.balance >= self.spin_cost:
            print(f"\nBalance: ${self.balance} | Spin cost: ${self.spin_cost}")
            choice = input("\nPress 's' to spin, 'q' to quit, 'r' for rules: ").lower()

            if choice == 'q': 
                print("\nThanks for playing! Final balance:", self.balance)
                # self.display_stats()
                break
            elif choice == 'r':
                # self.clear_screen()
                self.display_welcome()
                continue
            elif choice != 's':
                print("Invalid input! Press 's' to spin or 'q' to quit.")
                continue
        
            # Deduct spin cost
            self.balance -= self.spin_cost
            self.stats['spins'] += 1

            # Spin the reels
            result = self.spin_reels()

            # Calculate payout
            payout, message = self.calculate_payout(result, self.spin_cost)

            # Update balance and statistics
            if payout > 0:
                self.balance += payout
                self.stats['wins'] += 1
                self.stats['total_win'] += payout
                self.stats['biggest_win'] = max(self.stats['biggest_win'], payout)

            # Display result
            self.display_result(result, payout, message)

            # Check if player can continue
            if self.balance < self.spin_cost:
                print(f"\n💸 Game Over! You don't have enough balance for another spin.")
                self.display_stats()
                break

            # Small pause before next spin
            time.sleep(1)
                
        

def main():
    """Main function to start to game"""
    try:
        slot_machine = SlotMachine()
        slot_machine.play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
        


    