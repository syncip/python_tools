# ===============================
# Beschreibung: 
# alles klein schreiben
# ===============================

import pyperclip as pc

clipboard = pc.paste()

clipboard = clipboard.lower()

pc.copy(clipboard)
print(clipboard)