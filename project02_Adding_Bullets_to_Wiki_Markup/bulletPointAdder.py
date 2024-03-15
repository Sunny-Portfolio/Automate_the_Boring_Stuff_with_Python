#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

copied_text = pyperclip.paste()

# Separate lines and add stars.
lines = copied_text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

copied_text = '\n'.join(lines)

# Copies the modified text to clipboard to paste to Wikipedia
pyperclip.copy(copied_text)
