import tkinter as tk
from design import *


root = tk.Tk()
root.title('Final Project')
root.geometry('960x480')
root.resizable(False,False)
root.configure(bg=WINDOW_BACKGROUND)


left_frame = tk.Frame(root, bg=WINDOW_BACKGROUND)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

right_frame = tk.Frame(root, bg=WINDOW_BACKGROUND)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)

title_encryption = tk.Label(left_frame, text='Encryption', font=TITLE_DESIGN)
title_encryption.pack(side=tk.TOP)

title_decryption = tk.Label(right_frame, text='Decryption', font=TITLE_DESIGN)
title_decryption.pack(side=tk.TOP)

encrypt_text = tk.Button(left_frame, text='Encrypt Text!')
encrypt_text.pack(side = tk.LEFT,padx = 10)

encrypt_from_file = tk.Button(left_frame, text='Encrypt to File!')
encrypt_from_file.pack(side = tk.RIGHT,padx = 10)

decrypt_text = tk.Button(right_frame,text='Decrypt File!')
decrypt_text.pack(side=tk.LEFT,padx = 10)

decrypt_from_file = tk.Button(right_frame,text="Decrypt File!")
decrypt_from_file.pack(side=tk.RIGHT,padx = 10)


root.mainloop()