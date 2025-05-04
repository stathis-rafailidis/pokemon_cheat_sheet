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

    request = f"https://pokeapi.co/api/v2/type/{types}/"
    response = requests.get(request)
    if response.status_code == 200:
        data = response.json()
        dmg_relation = data['damage_relations']
        weak = ''
        weakness_ls = []
        for weakness in dmg_relation['double_damage_from']:
            weak = weak + " " + (weakness['name'])
            weakness_ls.append(weakness)

        resistanse_ls = []
        for resistanse in dmg_relation['half_damage_from']:
            resistanse_ls.append(resistanse['name'])
        
    return weak, weakness, resistanse_ls