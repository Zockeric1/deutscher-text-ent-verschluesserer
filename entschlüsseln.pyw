while True:
    import subprocess
    try:
        import easygui
        import tkinter as tk
        import pyperclip

        pw = easygui.passwordbox("Bitte gib das Passwort ein um Text-Nachrichten entschlüsseln zu können!", "Passwort")
        if pw == "12345":
            vn = ""

            def kopieren():
                global vn
                pyperclip.copy(vn)

            def entschlüsseln():
                wtwt = wt.get()
                a = 0
                global vn
                vt.configure(text=f"{vn}", bg="black")

                for x in range(8):
                    vn = ""
                    for i in wtwt:
                        a += 1
                        if a % 3 == 0:  #
                            shift = -7
                        elif a % 2 == 0:
                            shift = 4
                        else:
                            shift = -2
                        if i >= "a" and i <= "z":
                            pos = ord(i) - ord("a")
                            pos = (pos + shift) % 26
                            vn = vn + chr(pos + ord("a"))
                        elif i >= "A" and i <= "Z":
                            pos = ord(i) - ord("A")
                            pos = (pos + shift) % 26
                            vn = vn + chr(pos + ord("A"))
                        elif i >= "0" and i <= "9":
                            pos = ord(i) - ord("0")
                            pos = (pos + shift) % 10
                            vn = vn + chr(pos + ord("0"))
                        elif i >= " " and i <= "/":  #
                            pos = ord(i) - ord(" ")
                            pos = (pos + shift) % 16
                            vn = vn + chr(pos + ord(" "))
                        elif i >= ":" and i <= ">":  #
                            pos = ord(i) - ord(":")
                            pos = (pos + shift) % 5
                            vn = vn + chr(pos + ord(":"))
                        elif i >= "[" and i <= "_":  #
                            pos = ord(i) - ord("[")
                            pos = (pos + shift) % 5
                            vn = vn + chr(pos + ord("["))
                        else:
                            vn = vn + i
                vt.configure(text=f"{vn}", bg="darkgreen")
                cp = tk.Button(root, text="Kopieren", command=kopieren, bg="darkred")
                cp.grid(row=1, column=2)


            root = tk.Tk()
            root.title("Text-entschlüssler")
            root.configure(bg="black")
            wv = tk.Label(root, text="Welchen Text möchtest du entschlüsseln?:", bg="darkgreen")
            wv.grid(row=0, column=0)
            wt = tk.Entry(root, bg="grey")
            wt.grid(row=0, column=1)
            vb = tk.Button(root, text="entschlüsseln", command=entschlüsseln, bg="darkblue")
            vb.grid(row=0, column=2)
            wht = tk.Label(root, text="Entschlüsselter Text: ", bg="darkgreen")
            wht.grid(row=1, column=0)
            vt = tk.Label(root, text="", bg="black")
            vt.grid(row=1, column=1)
            auth = tk.Label(root, text="@Author: Eric Fellinger", bg="yellow")
            auth.grid(row=2, column=2)
            
            root.mainloop()
            break
        break

    except ImportError:
        subprocess.call("pip install easygui", shell=True)
        subprocess.call("pip install pyperclip", shell=True)

