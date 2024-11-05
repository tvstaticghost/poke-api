import random

firered_pokemon_types = {
    'Grass': [
        'Oddish/Gloom/Vileplume', 'Paras/Parasect', 
        'Exeggcute/Exeggutor', 'Tangela', 'Chikorita'
    ],
    'Fire': [
        'Growlithe/Arcanine',
        'Ponyta/Rapidash'
    ],
    'Water': [
        'Psyduck/Golduck', 'Poliwag/Poliwhirl/Poliwrath', 
        'Seel/Dewgong',
        'Magikarp/Gyarados', 'Kingler/Krabby',
        'Goldeen/Seaking', 'Tentacool/Tentacruel',
        'Shellder/Cloyster', 'Horsea/Seadra'
    ],
    'Electric': [
        'Pikachu/Raichu', 'Magnemite/Magneton',
        'Voltorb/Electrode', 'Electabuzz'
    ],
    'Normal': [
        'Rattata/Raticate', 'Pidgey/Pidgeotto/Pidgeot',
        'Jigglypuff/Wigglytuff', 'Meowth/Persian', 'Snorlax'
    ],
    'Fighting': [
        'Machop/Machoke/Machamp', 'Hitmonlee', 'Hitmonchan'
    ],
    'Poison': [
        'Ekans/Arbok', 'Nidoran♀/Nidorina/Nidoqueen',
        'Nidoran♂/Nidorino/Nidoking', 'Grimer/Muk',
        'Gastly/Haunter/Gengar'
    ],
    'Ground': [
        'Diglett/Dugtrio',
        'Geodude/Graveler/Golem', 'Onix'
    ],
    'Rock': [
        'Kabuto/Kabutops', 'Aerodactyl', 'Omanyte/Omastar'
    ],
    'Bug': [
        'Caterpie/Metapod/Butterfree', 'Weedle/Kakuna/Beedrill',
        'Pinsir', 'Scyther'
    ],
    'Psychic': [
        'Abra/Kadabra/Alakazam', 'Drowzee/Hypno',
        'Mr. Mime'
    ],
    'Ghost': [
        'Gastly/Haunter/Gengar'
    ],
    'Flying': [
        'Pidgey/Pidgeotto/Pidgeot', 'Spearow/Fearow',
        'Zubat/Golbat'
    ]
}

    # LeafGreen types
leafgreen_pokemon_types = {
    'Grass': [
        'Paras/Parasect', 'Bellsprout/Weepinbell/Victreebel',
        'Exeggcute/Exeggutor', 'Tangela', 'Chikorita'
    ],
    'Fire': [
        'Vulpix/Ninetales',
        'Ponyta/Rapidash', 'Magmar'
    ],
    'Water': [
        'Poliwag/Poliwhirl/Poliwrath', 'Seel/Dewgong',
        'Staryu/Starmie', 'Magikarp/Gyarados', 'Kingler/Krabby',
        'Goldeen/Seaking', 'Tentacool/Tentacruel', 'Horsea/Seadra'
    ],
    'Electric': [
        'Pikachu/Raichu', 'Magnemite/Magneton',
        'Voltorb/Electrode'
    ],
    'Normal': [
        'Rattata/Raticate', 'Pidgey/Pidgeotto/Pidgeot',
        'Jigglypuff/Wigglytuff', 'Meowth/Persian', 'Snorlax'
    ],
    'Fighting': [
        'Machop/Machoke/Machamp', 'Hitmonlee', 'Hitmonchan'
    ],
    'Poison': [
        'Nidoran♀/Nidorina/Nidoqueen',
        'Nidoran♂/Nidorino/Nidoking', 'Grimer/Muk',
        'Gastly/Haunter/Gengar'
    ],
    'Ground': [
        'Sandshrew/Sandslash', 'Diglett/Dugtrio',
        'Geodude/Graveler/Golem', 'Onix'
    ],
    'Rock': [
        'Kabuto/Kabutops', 'Aerodactyl', 'Omanyte/Omastar'
    ],
    'Bug': [
        'Caterpie/Metapod/Butterfree', 'Weedle/Kakuna/Beedrill',
        'Pinsir'
    ],
    'Psychic': [
        'Abra/Kadabra/Alakazam', 'Drowzee/Hypno',
        'Mr. Mime'
    ],
    'Ghost': [
        'Gastly/Haunter/Gengar'
    ],
    'Flying': [
        'Pidgey/Pidgeotto/Pidgeot', 'Spearow/Fearow',
        'Zubat/Golbat'
    ]
}

class PokeLineup:
    #all pokemon borken down by type and game they are available in

    # FireRed types
    

    #types: grass, fire, water, electric, normal, fighting, poison, ground, rock, 
    # bug, psychic, ghost, flying
    #params: string, string, bool, string
    #returns: array of strings
    def __init__(self, game_version, starter, starter_used, challenge_type):
        self.game_version = game_version
        self.starter = starter
        self.starter_used = starter_used
        self.challenge_type = challenge_type

    def balanced(self):
        lineup = []
        #bit map of used types in the lineup
        types_used = {'Grass': False, 'Fire': False, 'Water': False, 
                      'Electric': False, 'Normal': False, 'Fighting': False, 'Poison': False, 'Ground': False,
                      'Rock': False, 'Bug': False, 'Psychic': False, 'Ghost': False, 'Flying': False}
        
        #add more balanced lineup options
        possible_lineup_types = [['Fire', 'Water', 'Grass/Bug', 'Normal/Poison/Flying', 'Psychic/Ghost', 'Ground/Fighting/Rock'], 
                                 ['Fire/Water', 'Psychic/Ghost', 'Normal', 'Grass', 'Ground/Rock/Fighting', 'Electric']]
        
        if self.starter_used:
            if self.starter == 'squirtle':
                lineup.append('Squirtle/Wartortle/Blastoise')
                types_used['Water'] = True
            elif self.starter == 'charmander':
                lineup.append('Charmander/Charmeleon/Charizard')
                types_used['Fire'] = True
            elif self.starter == 'bulbasaur':
                lineup.append('Bulbasaur/Ivysaur/Venusaur')
                types_used['Grass'] = True
        
        selected_lineup = random.choice(possible_lineup_types)
        #check to see what types are already included

        filtered_lineup = []
        for i in range(0, len(selected_lineup)):
            if "/" in selected_lineup[i]:
                splitList = selected_lineup[i].split('/')
                appeared = False
                for j in range(0, len(splitList)):
                    if types_used[splitList[j]] == True:
                        appeared = True
                        break
                if not appeared:
                    filtered_lineup.append(selected_lineup[i])
            else:
                if types_used[selected_lineup[i]] == False:
                    filtered_lineup.append(selected_lineup[i])
        
        #select a random pokemon based on the types selected in the filtered_lineup list
        for i in filtered_lineup:
            possibility_list = []
            if '/' in i:
                split_type = i.split('/')
                for j in split_type: # combine the multiple type possbility arrays for fair rolling odds
                    if self.game_version == 'firered':
                        possibility_list.extend(firered_pokemon_types[j])
                    elif self.game_version == 'leafgreen':
                        possibility_list.extend(leafgreen_pokemon_types[j])
                lineup.append(random.choice(possibility_list))
            else:
                if self.game_version == 'firered':
                    lineup.append(random.choice(firered_pokemon_types[i]))
                elif self.game_version == 'leafgreen':
                    lineup.append(random.choice(leafgreen_pokemon_types[i]))
        
        return lineup