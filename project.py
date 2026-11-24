STRONG = {"fire": "grass",
          "water": "fire",
          "grass": "water"}

MOVES = {"charmander": ("Ember", "fire", 40),
         "squirtle": ("Water Gun", "water", 50),
         "bulbasaur": ("Vine Whip", "grass", 45)}

def effectiveness(your_type, opponent_type):
    """Calculate the effectiveness of your Pokémon's type against the opponent's type."""
    if your_type == opponent_type:
        return 1
    elif STRONG[your_type] == opponent_type:
        return 2
    elif STRONG[opponent_type] == your_type:
        return 0.5

def best_move(pokemon_name, your_type, opponent_type):
    """Determine the best move for your Pokémon based on type effectiveness."""
    multiplier = effectiveness(your_type, opponent_type)
    if multiplier < 1:
        return ("Tackle", "normal", 40)
    else:
        return MOVES[pokemon_name]
    
def calculate_damage(damage, multiplier):
    """Calculate the total damage dealt based on the base damage and effectiveness multiplier."""
    return damage * multiplier


def main():
    """Main function to run the Pokémon battle simulation."""
    your_type = input("Enter your Pokémon type (fire, water, grass): ").lower()
    your_pokemon = input("Enter your Pokémon name (charmander, squirtle, bulbasaur): ").lower()
    opponent_type = input("Enter your opponent's Pokémon type (fire, water, grass): ").lower()

    effectiveness_value = effectiveness(your_type, opponent_type)
    print(f"Effectiveness of {your_type} against {opponent_type}: {effectiveness_value}")

    move_name, move_type, move_damage = best_move(your_pokemon, your_type, opponent_type) 
    if move_name == "Tackle":
        damage = move_damage
    else:
        damage = calculate_damage(move_damage, effectiveness_value)

    print(f"Best move for {your_pokemon}: {move_name} ({move_type}) with base damage {move_damage}")
    print(f"Total damage dealt to opponent: {damage}")

if __name__ == "__main__":
    main()