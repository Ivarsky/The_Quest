from the_quest import *
from the_quest.game import TheQuest

if __name__ == "__main__":
    print("From main")
    print(f"Screen size {HEIGHT}x{WIDTH}")
    game = TheQuest()
    game.main_loop()
