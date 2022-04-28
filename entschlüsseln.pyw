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

            def verschlüsseln():
                wtwt = wt.get()
                a = 0
                global vn
                vt.configure(text=f"{vn}", bg="black")

                for x in range(8):
                    vn = ""
                    for i in wtwt:
                        a += 1
                        if a % 3 == 0: #
                            shift = -7
                            if i >= "a" and i <= "z":
                                pos = ord(i) - ord("a")
                                pos = (pos + shift) % 26
                                vn = vn + chr(pos + ord("a"))
                            elif i >= "A" and i <= "Z":
                                pos = ord(i) - ord("A")
                                pos = (pos + shift) % 26
                                vn = vn + chr(pos + ord("A"))
                            else:
                                vn = vn + i
                        elif a % 2 == 0:
                            shift = 4#
                            if i >= "a" and i <= "z":
                                pos = ord(i) - ord("a")
                                pos = (pos+shift) % 26
                                vn = vn + chr(pos + ord("a"))
                            elif i >= "A" and i <= "Z":
                                pos = ord(i) - ord("A")
                                pos = (pos+shift) % 26
                                vn = vn + chr(pos + ord("A"))
                            else:
                                vn = vn + i
                        else:
                            shift = -2
                            if i >= "a" and i <= "z":
                                pos = ord(i) - ord("a")
                                pos = (pos+shift) % 26
                                vn = vn + chr(pos + ord("a"))
                            elif i >= "A" and i <= "Z":
                                pos = ord(i) - ord("A")
                                pos = (pos+shift) % 26
                                vn = vn + chr(pos + ord("A"))
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
            vb = tk.Button(root, text="entschlüsseln", command=verschlüsseln, bg="darkblue")
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

