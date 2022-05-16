'''
TEAM:
1. TIGIST WONDIMNEH...UGR/2538/12....SECTION 1
2. FEVEN TOLLA........UGR/4493/12....SECTION 1
3. TIGIST ZELALEM.....UGR/1852/12....SECTION 1
4. MEKDES KEBEDE......UGR/3127/12....SECTION 1
5. FEVEN BELAY........UGR/3979/12....SECTION 1
6. BETEL TAGESSE......UGR/5409/12....SECTION 1
'''
from tkinter import *
import tkinter as tk
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


class vigenereCipher:
    def __init__(self):
        self.root = Tk()
        self.root.configure(bg="black")
        self.root.title("Vigenere cipher")
        self.root.geometry('600x530')

# introduction text on vignere cipher
        self.Intro = Label(self.root, text="Welcome to vigenere cipher!",
                           fg="white", bg="black", font=("Calibri", 13, "bold"))
        self.Intro.grid(row=0, column=0, padx=15, columnspan=2)
        self.Intro2 = Label(self.root, text="It was first described by Giovan Battista Bellaso in 1553!",
                            fg="white",bg="black", font=("Calibri", 13, "bold"))
        self.Intro2.grid(row=1, column=0, padx=15, columnspan=2)
        self.Intro3 = Label(self.root, text="It resisted all attempts to break it until 1863.",
                            fg="white", bg="black", font=("Calibri", 13, "bold"))
        self.Intro3.grid(row=2, column=0, padx=15, columnspan=2)
        self.Intro4 = Label(self.root, text="Try it! You can only use alphanumerics as well as spaces!",
                            fg="white", bg="black", font=("Calibri", 13, "bold"))
        self.Intro4.grid(row=3, column=0, padx=15, columnspan=2)
# texts and labels
        self.Intro5 = Label(self.root, text="Encrypt",
                            bg="black",fg = "white", font=("Calibri", 15, "bold"))
        self.Intro5.grid(row=4, column=0,pady = 15)

        self.plain = Label(self.root, text="Plaintext",
                           fg="white", bg="black", font=("Calibri", 13))
        self.plain.grid(row=5, column=0)

        self.Intro6 = Label(self.root, text="Decrypt",
                            fg="white", bg="black", font=("Calibri", 15, "bold"))
        self.Intro6.grid(row=4, column=1)

        self.cipher = Label(self.root, text="Ciphertext",
                            fg="white", bg="black", font=("Calibri", 13))
        self.cipher.grid(row=5, column=1)

# entry widget specifications

        self.plaintext = tk.Entry(self.root, width=40, borderwidth=3)
        self.plaintext.grid(row=6, column=0, padx=20, ipady=30)

        self.ciphertext = tk.Entry(self.root, width=40, borderwidth=3)
        self.ciphertext.grid(row=6, column=1, padx=10, ipady=30)

        self.e_key = Label(self.root, text="Key",
                           fg="white", bg="black", font=("Calibri", 13))
        self.e_key.grid(row=7, column=0,columnspan =2)

        self.plain_key = tk.Entry(
            self.root, width=40, borderwidth=3)
        self.plain_key.grid(row=8, column=0, columnspan = 2,padx=10, ipady=10)
#  encrypt and decrypt buttons
        self.encrypt_btn = Button(self.root, text="Encrypt", width=10, font=(
            "Calibri", 14, "bold"), fg="blue", bg="grey", command= self.routing_to_encryption)
        self.encrypt_btn.grid(row=9, column=0, pady=20)
        
        self.decrypt_btn = Button(self.root, text="Decrypt", width=10, font=(
            "Calibri", 14, "bold"), fg="red", bg="grey", command=self.routing_to_decryption)
        self.decrypt_btn.grid(row=9, column=1,pady= 20)

# declaring string vars and sets
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.alphabetset = set(self.alphabet)

# changing into a dictionary
        self.letter_to_index = dict(
            zip(self.alphabet, range(len(self.alphabet))))
        self.index_to_letter = dict(
            zip(range(len(self.alphabet)), self.alphabet))

# exit button
        # self.close_btn = Button(self.root, text="Close", width=14, font=(
        #     "Calibri", 14, "bold"), fg="white", bg="black", command=self.close)
        # self.close_btn.grid(row=13, column=0, columnspan=2, pady=5)

        self.root.mainloop()

    def close(self):
        self.root.destroy()

    def routing_to_encryption(self):
        self.result2 = Label(self.root, text="",width=30)
        self.result2.grid(row=10, column=0)
        self.encrypted = self.encrypt()
        if self.encrypted == '':
            self.error = Label(self.root, text="Please enter a valid plain input",fg="red")
            self.error.grid(row=10, column=0)
        else:
            self.result = Label(self.root, text=self.encrypted,wraplength=200,justify = "left")
            self.result.grid(row=10, column=0)
            # self.encrypted.destroy()

    def routing_to_decryption(self):
        self.result5 = Label(self.root, text="", width=30)
        self.result5.grid(row=10, column=1)
        self.decrypted = self.decrypt()
        if self.decrypted == '':
            self.error = Label(self.root, text="Please enter a valid cipher input",fg="red")
            self.error.grid(row=10, column=1)
        else:
            self.result = Label(self.root, text=self.decrypted,wraplength=200, justify="left")
            self.result.grid(row=10, column=1)
            self.decrypted.destroy()

    def encrypt(self):
        self.message = self.plaintext.get().upper()
        self.message = self.message.replace(" ","")
        self.key = self.plain_key.get().upper()
        self.key = self.key.replace(" ","")

        self.encrypted = ""
        self.split_message = [self.message[i:i + len(self.key)]
                          for i in range(0, len(self.message), len(self.key))]
        # for i in range(0, len(self.message), len(self.key)):
        #     self.split_message = self.message[i:i + len(self.key)]
        for each_split in self.split_message:
            i = 0
            for letter in each_split:
                # if letter not in self.alphabetset:
                #     return ""
                self.number = (
                    self.letter_to_index[letter]+self.letter_to_index[self.key[i]]) % len(self.alphabet)
                self.encrypted += self.index_to_letter[self.number]
                i += 1
        return self.encrypted

    def decrypt(self):
        self.ciphermessage = self.ciphertext.get().upper()
        self.ciphermessage= self.ciphermessage.replace(" ","")
        self.key = self.plain_key.get().upper()
        self.key = self.key.replace(" ","")

        self.decrypted = ""
        # for i in range(0, len(self.ciphermessage), len(self.key)):
        #     splited_cipher = self.ciphermessage[i:i + len(self.key)]

        self.splited_cipher = [self.ciphermessage[i:i + len(self.key)]
                         for i in range(0, len(self.ciphermessage), len(self.key))]
        for each_splited_cipher in self.splited_cipher:
            i = 0
            for letter in each_splited_cipher:
                # if letter not in self.alphabetset:
                #     return ""
                self.number = (
                    self.letter_to_index[letter]-self.letter_to_index[self.key[i]]) % len(self.alphabet)
                self.decrypted += self.index_to_letter[self.number]
                i += 1
        return self.decrypted

display = vigenereCipher()
