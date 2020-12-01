#!/usr/local/bin/python3

import tkinter
import os
import sys

def end():
    main.destroy()

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def caesar():
    # Nachricht, welche verschlüsselt werden soll
    message = message0.get().lower()
    print(message)
    # Der Wert, um welchen verschoben wird -> Schlüssel
    encryptionValue = int(encValue.get())

    # Variable für die verschlüsselte Nachricht
    newMessage = ""

    for i in range(len(message)):
        # Falls in der Nachricht ein Sonderzeichen ist, wird es gefiltert und nicht verschlüsselt
        if not ord(message[i]) in [i for i in range(97, 123)]:
            newMessage += message[i]
        else:
            # Der alten Ordnungszahl wird der Schlüssel addiert
            newChar = ord(message[i]) + encryptionValue

            # * siehe unten
            if newChar > 122:
                newChar = newChar - 123 + 97

            # Der verschlüsselten Nachricht wird der neue Buchstabe hinzugefügt
            newMessage += chr(newChar)

    # Die verschlüsselte Nachricht wird ausgegeben
    encryptedMessageLabel["text"] = "encrypted message: " + newMessage
    print(newMessage)

def decrypt():

    message = message1.get().lower()
    print(message)
    decryptionValue = int(decValue.get())
    newMessage = ""

    for i in range(len(message)):
        # Falls in der Nachricht ein Sonderzeichen ist, wird es gefiltert und nicht entschlüsselt
        if not ord(message[i]) in [i for i in range(97, 123)]:
            newMessage += message[i]
        else:
            # Der neuen Ordnungszahl wird der Schlüssel subtrahiert
            newChar = ord(message[i]) - decryptionValue

            # * siehe unten
            if newChar < 97:
                newChar = newChar + 26

            # Der entschlüsselten Nachricht wird der neue Buchstabe hinzugefügt
            newMessage += chr(newChar)

    # Die entschlüsselte Nachricht wird ausgegeben
    decryptedMessageLabel["text"] = "decrypted message: " + newMessage
    print(newMessage)

"""
* -> Das Cäsar Verfahren verwendet nur Kleinbuchstaben (in diesem Fall) des
lateinische Alphabets bei der Verschlüsselung. Dies führt dazu, dass ein
Intervall festgelegt werden muss in welchem das Programm hantiert.
"""

main = tkinter.Tk()
main.title("caesar algorithm")

# encryption

messageLabel = tkinter.Label(main, text="message to encrypt:")
messageLabel.pack()

global message0
message0 = tkinter.Entry(main, width=50)
message0.pack()

encryptionValueLabel = tkinter.Label(main, text="encryption value:")
encryptionValueLabel.pack()

global encValue
encValue = tkinter.Entry(main, width=50)
encValue.pack()

encryptButton = tkinter.Button(main, text="encrypt message", command=caesar)
encryptButton.pack()

encryptedMessageLabel = tkinter.Label(main, text="encrypted message:")
encryptedMessageLabel.pack()

spaceLabel = tkinter.Label(main, text=" ")
spaceLabel.pack()

# decryption

messageLabel = tkinter.Label(main, text="message to decrypt:")
messageLabel.pack()

global message1
message1 = tkinter.Entry(main, width=50)
message1.pack()

decryptionValueLabel = tkinter.Label(main, text="decryption value:")
decryptionValueLabel.pack()

global decValue
decValue = tkinter.Entry(main, width=50)
decValue.pack()

decryptButton = tkinter.Button(main, text="decrypt message", command=decrypt)
decryptButton.pack()

decryptedMessageLabel = tkinter.Label(main, text="decrypted message:")
decryptedMessageLabel.pack()

# other buttons

restart = tkinter.Button(main, text="restart", command=restart_program)
restart.pack(side="left")

end = tkinter.Button(main, text="end", command=end)
end.pack(side="right")

main.mainloop()
