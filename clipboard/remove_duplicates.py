# ===============================
# Beschreibung: 
# Nimmt alle Daten aus der Zwischenablage, welche druch "\n" (new line) getrennt sind und entfernt aus dieser Liste die Duplikate.
# ===============================

import pyperclip as pc
import string

clipboard = pc.paste()

# Tab durch new line erstzen, Zwischenablage aus Excel (Spalten)
clipboard = clipboard.replace("\t", "\n")

# Komma durch new line erstzen
clipboard = clipboard.replace(",", "\n")

# An Wortende ("\n") trennen
clip_list = clipboard.split("\n")

# Duplikate entfernen und Liste alphabetisch sortieren (asc)
clip_list_removed = sorted(list(dict.fromkeys(clip_list)))

new_list = ""

for item in clip_list_removed:
    new_list = new_list + "\n" + item

pc.copy(new_list)
