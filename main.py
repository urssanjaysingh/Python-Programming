# importing the custom module we have created earlier in calculator.py file
import calculator

result1 = calculator.add(2, 3)
print(result1)

result2 = calculator.subtract(6, 3)
print(result2)

result3 = calculator.multiply(10, 3)
print(result3)

result4 = calculator.divide(6, 3)
print(result4)


# game module
import game.characters.player
game.characters.player.get_player_info()

from game.characters import player
player.get_player_info()

from game.characters.boss import get_boss_info
get_boss_info()

