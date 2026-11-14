import tkinter as tk

root = tk.Tk()
root.title("JARVIS HUD - Lite")
root.geometry("560x135")
root.configure(bg="#0a0e14")
root.overrideredirect(True)

frame = tk.Frame(root, bg="#0a0e14", highlightbackground="#00d8ff", highlightthickness=1)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="🎤 LISTEN   Listening for your command.", fg="#00ff41", bg="#0a0e14", font=("Consolas", 11, "bold")).place(x=15, y=15)
tk.Label(frame, text="⚡ 99%  ▲", fg="#00d8ff", bg="#0a0e14", font=("Consolas", 10, "bold")).place(x=475, y=15)
tk.Label(frame, text="STT: Demo Mode | Full Pro Version: ayushpatel705.gumroad.com/l/kavvql", fg="#7f8c9b", bg="#0a0e14", font=("Consolas", 9)).place(x=15, y=52)

tk.Button(frame, text="Toggle Wi-Fi", fg="#00d8ff", bg="#112233", bd=0, font=("Consolas", 9), padx=10, pady=4).place(x=15, y=85)
tk.Button(frame, text="Toggle Bluetooth", fg="#00d8ff", bg="#112233", bd=0, font=("Consolas", 9), padx=10, pady=4).place(x=125, y=85)
tk.Button(frame, text="✕", fg="#ff4d4d", bg="#0a0e14", bd=0, command=root.destroy).place(x=535, y=5)

root.mainloop()
