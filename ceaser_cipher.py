import tkinter as tk
from tkinter import messagebox


##developed by Mr. Suryakanti Ghosh##
def encrypt():
    window2 = tk.Tk()
    window2.geometry("500x400")
    window2.configure(bg = "red")
    window2.title("Encryption Page")
    label1 = tk.Label(window2, text="Text to be encrypted ->")
    label1.grid(row=0, column=0, padx=10, pady=10)
    entry1 = tk.Entry(window2, width=40)
    entry1.grid(row=0, column=1, padx=10, pady=10)
    label2 = tk.Label(window2, text="Set The Shift Value ->")
    label2.grid(row=1, column=0, padx=10, pady=10)
    entry2 = tk.Entry(window2, width=40)
    entry2.grid(row=1, column=1, padx=10, pady=10)
    button1 = tk.Button(window2, text="Proceed", command=lambda: encrypt_true(entry1, entry2))
    button1.grid(row=2, column=0, columnspan=2, pady=10)
    window2.mainloop()


def decrypt():
    window3 = tk.Tk()
    window3.geometry("500x400")
    window3.configure(bg = "red")
    window3.title("Decryption Page")
    label1 = tk.Label(window3, text="Text to be Decrypted ->")
    label1.grid(row=0, column=0, padx=10, pady=10)
    entry1 = tk.Entry(window3, width=40)
    entry1.grid(row=0, column=1, padx=10, pady=10)
    label2 = tk.Label(window3, text="Shift Value ->")
    label2.grid(row=1, column=0, padx=10, pady=10)
    entry2 = tk.Entry(window3, width=40)
    entry2.grid(row=1, column=1, padx=10, pady=10)
    button1 = tk.Button(window3, text="Proceed", command=lambda: decrypt_true(entry1, entry2))
    button1.grid(row=2, column=0, columnspan=2, pady=10)
    window3.mainloop()
def encrypt_true(entry1, entry2):
    #try:
        
        text = entry1.get()
        shift = int(entry2.get())
        encrypted_text = ""
        for x in text :
            if x.isalpha():
                shift_cycle = shift %26
                new_char = ord(x)+shift_cycle
                if x.islower():
                    if new_char > ord("z"):
                        new_char -= 26
                    encrypted_text += chr(new_char)
                elif x.upper():
                    if new_char > ord("Z"):
                        new_char -= 26
                    encrypted_text += chr(new_char)
            else:
                encrypted_text += x
        messagebox.showinfo("Encrypted text","Encrypted text is ->" + encrypted_text )
    #except Exception as e:
        #messagebox.showerror("Error","Encounted error ->" + str(e))
def decrypt_true(entry1, entry2):
    try:
        
        text = entry1.get()
        shift = int(entry2.get())
        shift = -shift
        decrypted_text = ""
        for x in text :
            if x.isalpha():
                shift_cycle = shift %26
                new_char = ord(x)+shift_cycle
                if x.islower():
                    if new_char > ord("z"):
                        new_char -= 26
                    decrypted_text += chr(new_char)
                elif x.upper():
                    if new_char > ord("Z"):
                        new_char -= 26
                    decrypted_text += chr(new_char)
            else:
                decrypted_text += x
        messagebox.showinfo("Encrypted text","Encrypted text is ->" + decrypted_text )
    except Exception as e:
        messagebox.showerror("Error","Encounted error ->" + str(e))
    
window1 =  tk.Tk()
window1.geometry("600x400")
window1.configure(bg = "blue")
window1.title("Main Page")

tk.Label(window1,text = "Welcome to Text Encryptor and Decryptor").pack()
tk.Label(window1,text = "Developed by Mr. Suryakanti Ghosh").pack(pady = 20)
tk.Button(window1, text = "Text Encryption", command= lambda:encrypt()).pack(pady = 20)
tk.Button(window1, text = "Text Decryption", command = lambda:decrypt()).pack(pady = 20)
window1.mainloop()
