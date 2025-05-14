import requests

def find_types(pokemon_name: str) -> list:

    pokemon = f"pokemon/{pokemon_name}"
    request = f"https://pokeapi.co/api/v2/{pokemon}/"
    response = requests.get(request)
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        height = data["height"]
        weight = data["weight"]
        types = [type_info["type"]["name"] for type_info in data["types"]]
        # abilities = [ability_info["ability"]["name"] for ability_info in data["abilities"]]
        return types

    else:
        print(f"Error: {response.status_code}")
        return 1
    


def find_weakness(types: list) -> list[str]:
    resistanses: list = []
    weaknesses: list = []
    no_dmg: list = []
    for type in types:

        request = f"https://pokeapi.co/api/v2/type/{type}/"
        response = requests.get(request)
        if response.status_code == 200:
            data = response.json()
            dmg_relation = data['damage_relations']
            
            for weakness in dmg_relation['double_damage_from']:
                weaknesses.append(weakness['name'])

            for resistanse in dmg_relation['half_damage_from']:
                resistanses.append(resistanse['name'])
            
            for no_damage in dmg_relation['no_damage_from']:
                no_dmg.append(no_damage['name'])

    weaknesses = list(set(weaknesses) - set(resistanses) - set(no_dmg))

    return weaknesses