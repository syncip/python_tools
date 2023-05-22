# ===============================
# Beschreibung: 
# alles groß schreiben
# ===============================

import pyperclip as pc

clipboard = pc.paste()

clipboard = clipboard.upper()

pc.copy(clipboard)
print(clipboard)