enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
#print(potion_strength)

# Global scope

players_health = 10

def drink_potion():
    potion_strength = 2
    print(players_health)

drink_potion()
print(players_health)




