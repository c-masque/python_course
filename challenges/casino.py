class Casino():

    # essential variables
    credits = 100
    fingers = 5
    finger_bet = False
    bet_amount = 0

    def __init__(self):
        self.intro()
        self.main_menu()


    def die(self):
        import numpy

        roll = numpy.random.randint(1, 7)
        
        return roll   


    def intro(self):
        input("\nYou step outside of the casino and begin to pass a darkened alley way to head home.\n")
        input("A seedy lookin' feller catches your eye and gestures yer way.\n")
        input("As he motions to you and you get closer, you notice his hand is missin' two fingers.\n")


    def main_menu(self):
        gamble_time = input("\"Sir, would ya be interested in some... high reward gamblin'?\" He flashes a repugnant smile.\n\n  (YEAH)   (NO)   >>> ").lower()

        if gamble_time == "let's cut to the chase" or gamble_time == 'ff':
            input("\n\"Alright, make your bet...\"\n")
            self.place_bets()

        elif gamble_time == 'yes' or gamble_time == 'yeah' or gamble_time == 'y':
            input("\n\"That's what I like to hear. The game is like this:")
            input("\n\"I have a couple dice here... Whichever of us two can roll the highest combo, wins.\"")
            game_accept = input("\n\"What do you say?\"\n\n  (YEAH)   (NO)   >>> ")

            if game_accept == 'yes' or game_accept == 'yeah' or game_accept == 'y' or game_accept == 'ok':
                input("\n\"Alright, make your bet...\"\n")
                self.place_bets()

            elif game_accept == 'no' or game_accept == 'n':
                input("\n\"Oh. Ok. Nevermind then.\"")
                exit()

            else:
                input("\n\"I couldn't quite make that out... Lemme start over...\"\n")
                self.main_menu()

        elif gamble_time == 'no' or gamble_time == 'n':
            input("\n\"Oh. Ok. Nevermind then.\"")
            exit()

        else:
            input("\n\"I couldn't quite make that out... Lemme start over...\"\n")
            self.main_menu()


    def place_bets(self):
        print(f"You currently have {self.credits} credits.\n")

        bet_amount = input("How much would you like to bet? | (5) (10) (50) (custom) >>> ")

        if bet_amount == 'custom':
            special_bet = input("\nWhat would you like to bet? | (1. custom credit amount) (2. credits and finger) >>> ").lower()

            if special_bet == '1' or special_bet == "credits" or special_bet == "custom credit amount":
                print(f"\nYou currently have {self.credits} credits.\n")
                bet_amount = int(input("Wager credit amount: "))
                
                if bet_amount > 0:
                    print(f"\nYou are wagering {bet_amount}.\n")
                    self.credits -= bet_amount
                    self.rolling_rolling()

                else:
                    input("\n\"I couldn't quite make that out... Lemme start over...\"\n")
                    self.place_bets()


            elif special_bet == '2' or special_bet == "credits and finger" or special_bet == "finger":
                special_bet_accept = input("\nWARNING! Wagering a finger is technically free, but the monetary gain/loss is multiplied by ten fold!\nDo you wish to proceed?\n\n  (YEAH)   (NO)   >>> ").lower()

                if special_bet_accept == 'yes' or special_bet_accept == 'yeah' or special_bet_accept == 'y' or special_bet_accept == 'ok':
                    print(f"\nYou currently have {self.credits} credits.\n")

                    special_bet_amount = int(input("How much would you like to bet? >>> "))
                    if special_bet_amount > 0:
                        self.finger_bet = True
                        self.credits -= (special_bet_amount)
                        print(f"\nYou are wagering {special_bet_amount} and a finger.\n")
                        self.rolling_rolling()
                    else:
                        input("\n\"I'm not sure you understand I don't understand what you're saying...\"\n")
                        self.place_bets()

                else:
                    print("It's okay, don't make any hasty decisions...\n")
                    self.place_bets()

            else:
                input("\n\"I couldn't quite make that out... Lemme start over...\"\n")
                self.place_bets()


        elif bet_amount == '5':
            print(f"\nYou currently have {self.credits} credits.")
            bet_amount = 5
            print(f"\nYou are wagering {bet_amount} credits.\n")
            self.credits -= bet_amount
            self.rolling_rolling()

        elif bet_amount == '10':
            print(f"\nYou currently have {self.credits} credits.")
            bet_amount = 10
            print(f"\nYou are wagering {bet_amount} credits.\n")
            self.credits -= bet_amount
            self.rolling_rolling()

        elif bet_amount == '50':
            print(f"\nYou currently have {self.credits} credits.")
            bet_amount = 50
            print(f"\nYou are wagering {bet_amount} credits.\n")
            self.credits -= bet_amount
            self.rolling_rolling()

        else:
            input("\n\"I couldn't quite make that out... Lemme start over...\"\n")
            self.place_bets()


    def rolling_rolling(self):
        input("Alright, let 'er roll...\n")
        input(' . \n')
        input(' . \n')
        input(' . \n')
        player_roll = self.die()
        cp_roll = self.die()

Casino()
        