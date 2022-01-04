import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Button

layout = [ 
            [
            sg.Text("Plain"),
            sg.Input(key = "plain")
            ],
            [    
            sg.Text("Cipher"),
            sg.Input(key = "cipher")
            ],
            [
            sg.Button("Confirm"),
            sg.Button("Done")
            ]
    ]

Window = sg.Window("Vigenere", layout)

while True:
    event, values = Window.read()
    if event == "Confirm":
        count = 0
        new = ""
        plainText = values["plain"].lower()
        cipherText = values["cipher"].lower()
        for x in plainText:
            plain = ord(x) - 97
            cipher = ord(cipherText[count % (len(values["cipher"]))]) - 97
            add = chr(((plain + cipher) % 26) + 97)
            if values["plain"][count].islower():
                new += add
            else:
                new += add.upper()
            count += 1        
    sg.popup(str(new))
    if event == "Done":
        break
Window.close()

