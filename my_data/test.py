import tkinter as tk
from PIL import Image, ImageDraw
import os

class HandwritingDataCollector:
    def __init__(self, root):
        self.root = root
        self.root.title("Sanskrit Vowel and Consonant Data Collector")
        
        self.sanskrit_dict = {
            'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ii', 'उ': 'u', 'ऊ': 'uu', 'ऋ': 'ṛ', 'ॠ': 'ṝ',
            'ऌ': 'ḷ', 'ॡ': 'ḹ', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',
            'क': 'ka', 'ख': 'kha', 'ग': 'ga', 'घ': 'gha', 'ङ': 'ṅa',
            'च': 'ca', 'छ': 'cha', 'ज': 'ja', 'झ': 'jha', 'ञ': 'ña',
            'ट': 'ṭa', 'ठ': 'ṭha', 'ड': 'ḍa', 'ढ': 'ḍha', 'ण': 'ṇa',
            'त': 'ta', 'थ': 'tha', 'द': 'da', 'ध': 'dha', 'न': 'na',
            'प': 'pa', 'फ': 'pha', 'ब': 'ba', 'भ': 'bha', 'म': 'ma',
            'य': 'ya', 'र': 'ra', 'ल': 'la', 'व': 'va', 'श': 'śa',
            'ष': 'ṣa', 'स': 'sa', 'ह': 'ha'
        }

        self.current_char = list(self.sanskrit_dict.values())[0]
        self.save_directory = os.path.dirname(os.path.abspath(__file__))
        self.samples_per_char = 10
        self.current_sample = 1
        
        self.canvas = tk.Canvas(self.root, width=200, height=200, bg="white")
        self.canvas.pack()
        
        self.label = tk.Label(self.root, text=f"Draw the character: {self.current_char}", font=("Helvetica", 16))
        self.label.pack()
        
        self.sample_label = tk.Label(self.root, text=f"Sample {self.current_sample}/{self.samples_per_char}", font=("Helvetica", 12))
        self.sample_label.pack()
        
        self.save_button = tk.Button(self.root, text="Save", command=self.save_character)
        self.save_button.pack()
        
        self.reset_button = tk.Button(self.root, text="Clear", command=self.clear_canvas)
        self.reset_button.pack()
        
        self.next_char_button = tk.Button(self.root, text="Next Character", command=self.next_character)
        self.next_char_button.pack()
        
        self.prev_char_button = tk.Button(self.root, text="Previous Character", command=self.prev_character)
        self.prev_char_button.pack()
        
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)
        
        self.drawing = False
        self.last_x = 0
        self.last_y = 0
        self.image = Image.new("L", (200, 200), "white")
        self.draw = ImageDraw.Draw(self.image)
        
    def start_draw(self, event):
        self.drawing = True
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        if self.drawing:
            x, y = event.x, event.y
            self.canvas.create_line((self.last_x, self.last_y, x, y), width=5, fill="black")
            self.draw.line((self.last_x, self.last_y, x, y), fill="black", width=5)
            self.last_x = x
            self.last_y = y
    
    def stop_draw(self, event):
        self.drawing = False

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (200, 200), "white")
        self.draw = ImageDraw.Draw(self.image)

    def save_character(self):
        char_folder = f"{self.save_directory}/{self.current_char}"
        try:
            os.makedirs(char_folder)
        except FileExistsError:
            pass
        image_path = f"{char_folder}/{len(os.listdir(char_folder)) + 1}.png"
        self.image.save(image_path)
        print(f"Saved character {self.current_char} as {image_path}")
        self.clear_canvas()
        self.current_sample += 1
        self.sample_label.config(text=f"Sample {self.current_sample}/{self.samples_per_char}")
        if self.current_sample > self.samples_per_char:
            self.next_character()

    def next_character(self):
        current_index = list(self.sanskrit_dict.values()).index(self.current_char)
        if current_index < len(self.sanskrit_dict) - 1:
            self.current_char = list(self.sanskrit_dict.values())[current_index + 1]
            self.label.config(text=f"Draw the character: {self.current_char}")
            self.clear_canvas()
            self.current_sample = 1
            self.sample_label.config(text=f"Sample {self.current_sample}/{self.samples_per_char}")
        else:
            self.label.config(text="All characters collected!")

    def prev_character(self):
        current_index = list(self.sanskrit_dict.values()).index(self.current_char)
        if current_index > 0:
            self.current_char = list(self.sanskrit_dict.values())[current_index - 1]
            self.label.config(text=f"Draw the character: {self.current_char}")
            self.clear_canvas()
            self.current_sample = 1
            self.sample_label.config(text=f"Sample {self.current_sample}/{self.samples_per_char}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HandwritingDataCollector(root)
    root.mainloop()
