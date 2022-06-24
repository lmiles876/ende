import tkinter as tk
import encryption as e
import decryption as d


def get_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key


def en_shift():
    L1 = tk.Label(root, text='Shift Encryption')
    B = tk.Button(root, text='Random Shift', bg='green', command=en_rand_shift_setup)
    B2 = tk.Button(root, text='Known Shift', bg='green', command=en_known_shift_setup)
    L1.pack()
    B.pack()
    B2.pack()


def e_k_s():
    string = str(eks_box_string.get())
    shift = int(eks_box_shift.get())
    E = e.known_shift(string, shift)  # call to encrypt function
    L2 = tk.Label(eks, text=f'Encryption: {E}')
    L2.pack()


def en_known_shift_setup():
    global eks_box_string
    global eks_box_shift
    global eks
    root.destroy()
    eks = tk.Tk()
    eks.geometry('500x500')
    eks.title('Known Shift Encryption')
    L = tk.Label(eks, text='Please enter text to be encrypted: ')
    L2 = tk.Label(eks, text='Please enter shift:')
    eks_box_string = tk.Entry(eks, bd='5')
    eks_box_shift = tk.Entry(eks, bd='2')
    submit = tk.Button(eks, text='Submit', command=e_k_s)
    L.pack()
    eks_box_string.pack()
    L2.pack()
    eks_box_shift.pack()
    submit.pack()
    eks.mainloop()


def e_r_s():
    E, shift = e.unknown_shift(ers_box.get())  # call to encrypt function
    L2 = tk.Label(ers, text=f'Encryption: {E}')
    C = tk.Label(ers, text=f'Shift Used: {shift}')
    L2.pack()
    C.pack()


def en_rand_shift_setup():
    global ers_box
    global ers
    root.destroy()
    ers = tk.Tk()
    ers.geometry('500x500')
    ers.title('Random Shift Encryption')
    L = tk.Label(ers, text='Please enter text to be encrypted: ')
    ers_box = tk.Entry(ers, bd='5')
    submit = tk.Button(ers, text='Submit', command=e_r_s)
    L.pack()
    ers_box.pack()
    submit.pack()
    ers.mainloop()


def e_r_m():
    E, cipher = e.unknown_mono(erm_box.get())  # call to encrypt function
    L2 = tk.Label(erm, text=f'Encryption: {E}')
    C = tk.Label(erm, text=f'Cipher Used: ')
    L2.pack()
    C.pack()
    for key, val in cipher.items():
        key = chr(key)
        L = tk.Label(erm, text=f'{val} --> {key}')
        L.pack()


def en_rand_m_setup():
    global erm_box
    global erm
    root.destroy()
    erm = tk.Tk()
    erm.geometry('500x500')
    erm.title('Random Monoalphabetic Encryption')
    L = tk.Label(erm, text='Please enter text to be encrypted: ')
    erm_box = tk.Entry(erm, bd='5')
    submit = tk.Button(erm, text='Submit', command=e_r_m)
    L.pack()
    erm_box.pack()
    submit.pack()
    erm.mainloop()


def e_k_m(cipher):
    string = str(ekm_box_string.get())
    E = e.known_mono(string, cipher)  # call to encrypt function

    L2 = tk.Label(ekm, text=f'Encryption: {E}')
    L2.pack()


def e_convert_to_dic():
    value = [str(entry.get()) for entry in entries_d]
    cipher = {ord(str(value[i])[-1]): str(value[i])[0]for i in range(len(value))}
    e_k_m(cipher)


def cipher_input():
    c_input = tk.Tk()
    c_input.geometry('700x700')
    c_input.title('Input cipher')


def en_known_m_setup():
    global ekm_box_string
    global ekm
    root.destroy()
    ekm = tk.Tk()
    ekm.geometry('500x500')
    ekm.title('Known Monoalphabetic Encryption')
    L = tk.Label(ekm, text='Please enter text to be encrypted: ')
    ekm_box_string = tk.Entry(ekm, bd='5')
    global entries
    entries = []
    L3 = tk.Label(ekm, text='Enter new alphabet: ')
    L3.pack()
    for i in range(26):
        L = tk.StringVar(ekm, f'{chr(i + 97)}: ')
        entry = tk.Entry(ekm, textvariable=L, bd='1')
        entries.append(entry)
        entry.pack()
    L2 = tk.Label(ekm, text=' Enter text to be encrypted: ')
    L2.pack()
    ekm_box_string.pack()
    sub = tk.Button(ekm, text='Submit', command=e_convert_to_dic)
    sub.pack()
    ekm.mainloop()


def en_m():
    L1 = tk.Label(root, text='Monoalphabetic Encryption')
    B = tk.Button(root, text='Random Cipher', bg='green', command=en_rand_m_setup)
    B2 = tk.Button(root, text='Known Cipher', bg='green', command=en_known_m_setup)
    L1.pack()
    B.pack()
    B2.pack()



def e_k_h():
    E = e.hill(ekh_box_string.get(), ekh_box_key.get())
    L = tk.Label(ekh, text=f'Encryption: {E}')
    L.pack()
def en_known_hill_setup():
    global ekh_box_string
    global ekh_box_key
    global ekh
    root.destroy()
    ekh = tk.Tk()
    ekh.geometry('500x500')
    ekh.title('Known Monoalphabetic Encryption')
    L = tk.Label(ekh, text='Please enter text to be encrypted: ')
    L2 = tk.Label(ekh, text='Please enter 9 letter key: ')
    ekh_box_string = tk.Entry(ekh, bd='5')
    ekh_box_key = tk.Entry(ekh, bd='5')
    L.pack()
    ekh_box_string.pack()
    L2.pack()
    ekh_box_key.pack()
    sub = tk.Button(ekh, text='Submit', command=e_k_h)
    sub.pack()
    ekh.mainloop()
def En():
    L2 = tk.Label(root, text='Please select the type of encryption: ')
    s = tk.Button(root, text="Shift", bg='yellow', activebackground='green', command=en_shift)
    m = tk.Button(root, text="Monoalphabetic", bg='yellow', activebackground='green', command=en_m)
    h = tk.Button(root, text="Hill", bg='yellow', activebackground='green', command=en_known_hill_setup)
    L2.pack()
    s.pack()
    m.pack()
    h.pack()


def d_u_s():
    E, shift = d.unknown_shift(dus_box.get())  # call to encrypt function
    L2 = tk.Label(dus, text=f'Most likely decryption: {E}')
    C = tk.Label(dus, text=f'Most likely shift used: {shift}')
    L2.pack()
    C.pack()


def de_unknown_shift_setup():
    global dus_box
    global dus
    root.destroy()
    dus = tk.Tk()
    dus.geometry('500x500')
    dus.title('Unknown Shift')
    L = tk.Label(dus, text='Please enter text to be decrypted: ')
    dus_box = tk.Entry(dus, bd='5')
    submit = tk.Button(dus, text='Submit', command=d_u_s)
    L.pack()
    dus_box.pack()
    submit.pack()
    dus.mainloop()


def d_k_s():
    string = str(dks_box_string.get())
    shift = int(dks_box_shift.get())
    E = d.known_shift(string, shift)  # call to encrypt function
    L2 = tk.Label(dks, text=f'Decryption: {E}')
    L2.pack()


def de_known_shift_setup():
    global dks_box_string
    global dks_box_shift
    global dks
    root.destroy()
    dks = tk.Tk()
    dks.geometry('500x500')
    dks.title('Known Shift Decryption')
    L = tk.Label(dks, text='Please enter text to be decrypted: ')
    L2 = tk.Label(dks, text='Please enter shift:')
    dks_box_string = tk.Entry(dks, bd='5')
    dks_box_shift = tk.Entry(dks, bd='2')
    submit = tk.Button(dks, text='Submit', command=d_k_s)
    L.pack()
    dks_box_string.pack()
    L2.pack()
    dks_box_shift.pack()
    submit.pack()
    dks.mainloop()


def de_shift():
    L1 = tk.Label(root, text='Shift Decryption')
    B = tk.Button(root, text='Unknown Shift', bg='green', command=de_unknown_shift_setup)
    B2 = tk.Button(root, text='Known Shift', bg='green', command=de_known_shift_setup)
    L1.pack()
    B.pack()
    B2.pack()


def d_k_m(cipher):
    string = str(dkm_box_string.get())
    E = d.known_mono(string, cipher)  # call to encrypt function
    L2 = tk.Label(dkm, text=f'Encryption: {E}')
    L2.pack()


def d_convert_to_dic():
    value = [str(entry.get()) for entry in entries_d]
    cipher = {ord(str(value[i])[-1]): str(value[i])[0]for i in range(len(value))}
    d_k_m(cipher)


def de_m():
    global dkm_box_string
    global dkm
    root.destroy()
    dkm = tk.Tk()
    dkm.geometry('500x500')
    dkm.title('Known Monoalphabetic Decryption')
    dkm_box_string = tk.Entry(dkm, bd='5')
    global entries_d
    entries_d = []
    L3 = tk.Label(dkm, text='Enter new alphabet: ')
    L3.pack()
    for i in range(26):
        L = tk.StringVar(dkm, f'{chr(i + 97)}: ')
        entry = tk.Entry(dkm, textvariable=L, bd='1')
        entries_d.append(entry)
        entry.pack()
    L2 = tk.Label(dkm, text=' Enter text to be decrypted: ')
    L2.pack()
    dkm_box_string.pack()
    sub = tk.Button(dkm, text='Submit', command=d_convert_to_dic)
    sub.pack()
    dkm.mainloop()


def d_k_h():
    string = str(dkh_box_string.get())
    shift = str(dkh_box_shift.get())
    E = d.hill(string, shift)
    L2 = tk.Label(dkh, text=f'Decryption: {E}')
    L2.pack()


def de_h():
    global dkh_box_string
    global dkh_box_shift
    global dkh
    root.destroy()
    dkh = tk.Tk()
    dkh.geometry('500x500')
    dkh.title('Known Hill Decryption')
    L = tk.Label(dkh, text='Please enter text to be decrypted: ')
    L2 = tk.Label(dkh, text='Please enter key:')
    dkh_box_string = tk.Entry(dkh, bd='5')
    dkh_box_shift = tk.Entry(dkh, bd='2')
    submit = tk.Button(dkh, text='Submit', command=d_k_h)
    L.pack()
    dkh_box_string.pack()
    L2.pack()
    dkh_box_shift.pack()
    submit.pack()
    dkh.mainloop()


def De():
    L2 = tk.Label(root, text='Please select the type of decryption: ')
    s = tk.Button(root, text="Shift", bg='yellow', activebackground='green', command=de_shift)
    m = tk.Button(root, text="Monoaplhabetic", bg='yellow', activebackground='green', command=de_m)
    h = tk.Button(root, text="Hill", bg='yellow', activebackground='green', command=de_h)
    L2.pack()
    s.pack()
    m.pack()
    h.pack()


root = tk.Tk()
root.geometry('500x500')
root.title('Encrypt/Decrypt')
L1 = tk.Label(root, text='Would you like to Encrypt or Decrypt?')
B1 = tk.Button(root, text='Encrypt', activebackground='green', command=En)
B2 = tk.Button(root, text='Decrypt', activebackground='green', command=De)
L1.pack()
B1.pack()
B2.pack()
root.mainloop()