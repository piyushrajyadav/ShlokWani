import os
import json

def load_shlok(chapter, slok):
    file_name = f"gita_data/bhagavadgita_chapter_{chapter}_slok_{slok}.json"
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    return None
