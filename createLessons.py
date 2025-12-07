import os

folder_names = [
    "L1_IntroToPython",
    "L2_Variables",
    "L3_InputOutput",
    "L4_Operators",
    "L5_Conditionals",
    "L6_Loops",
    "L7_Strings",
    "L8_Lists",
    "L9_TuplesSets",
    "L10_Dictionaries",
    "L11_Functions",
    "L12_ErrorHandling",
    "L13_FileHandling",
    "L14_Modules",
    "L15_OOPBasics",
    "L16_Packages",
    "L17_Basic_Projects"
]



import os
import json

def create_contentFileInEachFolder(folder_names):
    # Minimal default notebook structure
    empty_notebook = {
        "cells": [],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5
    }

    for folder in folder_names:
        path = os.path.join(folder, "content.ipynb")
        
        # Check if the file already exists
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump(empty_notebook, f, indent=2)
            print(f"Created: {path}")
        else:
            print(f"Already exists: {path}")


create_contentFileInEachFolder(folder_names)

exit
gamma_links = [
    ("L1_IntroToPython", "https://gamma.app/docs/Introduction-to-Python-bx5o6xru1qe2vdq?mode=doc"),
    ("L2_Variables", "https://gamma.app/docs/Variables-and-Data-Types-g3zj6pjz7ha6xl4?mode=doc"),
    ("L3_InputOutput", "https://gamma.app/docs/Lesson-3-Input-and-Output-aj6jz9mcoen9hwv?mode=present#card-xg477tbmrqqgajh"),
    ("L4_Operators", ""),
    ("L5_Conditionals", ""),
    ("L6_Loops", ""),
    ("L7_Strings", ""),
    ("L8_Lists", ""),
    ("L9_TuplesSets", ""),
    ("L10_Dictionaries", ""),
    ("L11_Functions", ""),
    ("L12_ErrorHandling", ""),
    ("L13_FileHandling", ""),
    ("L14_Modules", ""),
    ("L15_OOPBasics", ""),
    ("L16_Packages", "")
]






for folder in folder_names:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

print("All folders created successfully!")
