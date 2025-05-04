from screen_reader import ScreenReader, AlwaysOnTopWindow
import time

from api import find_types, find_weakness
t0 = time.time()
screen_reader = ScreenReader()

screenshot = screen_reader.get_screenshot()
pokemon_name = screen_reader.find_pokemon_name(screenshot=screenshot)
if pokemon_name == "BLISSET":
    pokemon_name = 'BLISSEY'
print(pokemon_name)

types = find_types(pokemon_name)
print(types)
t1 = time.time()
weakness, weakness_ls, resistanse_ls = find_weakness(types[0])
print(weakness_ls)
window = AlwaysOnTopWindow(types)
window.run()
t2 = time.time()


print(f"type took : {round(t1 - t0, 2)}")
print(f"overall took : {round(t2 - t0, 2)}")
