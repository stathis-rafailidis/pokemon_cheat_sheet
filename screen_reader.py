import time
import mss
import mss.tools
import easyocr
import tkinter as tk


from api import find_types, find_weakness
class ScreenReader:

    def get_screenshot(self):
        with mss.mss() as sct:
            time.sleep(3)
            # The screen part to capture
            # This is for screenshots
            monitor = {"top": 50, "left": 530, "width": 450, "height": 100}
            # This is for the actual game
            # monitor = {"top": 50, "left": 475, "width": 535, "height": 60}
            output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

            # Grab the data
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
            print(output)
            return output

    def find_pokemon_name(self, screenshot):
        reader = easyocr.Reader(['en'])
        # text = reader.readtext('test_pics/sigilyph_cut.png', detail=0)/
        text = reader.readtext(screenshot, detail=0)
        text = ''.join(e for e in text[0] if e.isalnum())
        return text

class AlwaysOnTopWindow:
    def __init__(self, text):
        self.root = tk.Tk()
        self.root.title("Always On Top")

        # self.root.geometry("300x100")
        # and where it is placed
        self.root.geometry('%dx%d+%d+%d' % (300, 100, 100, 100))

        self.root.attributes('-topmost', True)  # Keep the window on top

        # Add a label to display the text
        self.label = tk.Label(self.root, text=text, font=("Arial", 14))
        self.label.pack(expand=True, fill=tk.BOTH)

        # Creating a button with specified options
        button = tk.Button(self.root, 
            text="Click Me", 
            command=self.run_all,
            activebackground="blue", 
            activeforeground="white",
            anchor="center",
            bd=3,
            bg="lightgray",
            cursor="hand2",
            disabledforeground="gray",
            fg="black",
            font=("Arial", 12),
            height=2,
            highlightbackground="black",
            highlightcolor="green",
            highlightthickness=2,
            justify="center",
            overrelief="raised",
            padx=10,
            pady=5,
            width=15,
            wraplength=100)

        button.pack(padx=20, pady=20)

    def run(self):
        self.root.mainloop()

    def change_text(self, new_text):
        self.label.config(text=new_text)

    def run_all(self):
        screen_reader = ScreenReader()
        screenshot = screen_reader.get_screenshot()
        pokemon_name = screen_reader.find_pokemon_name(screenshot=screenshot)
        types = find_types(pokemon_name)
        weakness = ""
        weakness_ls = []
        resistanse_ls = []
        for type in types:
            weak, weak_ls, res = find_weakness(type)
            weakness = weakness + weak 
            weakness_ls.append(weak_ls)
            resistanse_ls.append(res)
        self.change_text(str(weakness) + " res " + str(resistanse_ls))
        
