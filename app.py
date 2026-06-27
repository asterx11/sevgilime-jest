import customtkinter as ctk
import webbrowser

app=ctk.CTk()
app.geometry("400*500")
app.title("For you my love")

ctk.set_appearance_mode("dark")
app.configure(fg_color="#281C59")

tit=ctk.CTkLabel(app,text="Bu kendimi affettirmek için yaptığım bir şey değil bayadır aklımdaydı umarım seversin ❤️Nasıl hissediyorsun?",
                 font=("Courier New",20,"bold"),text_color="#EDF7BD")
tit.pack(pady=50)

def sad():
    webbrowser.open("https://www.youtube.com/watch?v=zO_532nbu0c")

def happy():
    webbrowser.open("https://www.youtube.com/watch?v=KlyXNRrsk4A")

def angry():
    webbrowser.open("https://www.youtube.com/watch?v=LYU-8IFcDPw")

def energetic():
    webbrowser.open("https://www.youtube.com/watch?v=5dbEhBKGOtY")

def özledim():
    webbrowser.open("https://www.youtube.com/watch?v=gpG9QRV9gTk")

btn1_sad=ctk.CTkButton(app,
                      text="Ağlamama ramak kaldı ama güçlü de kalmam lazım...",
                      command=sad,
                        width=280,
                        height=45,
                        font=("Consolas", 12, "bold"),
                        corner_radius=20,
                      fg_color="#4E8D9C",
                      hover_color="#85C79A",)
btn1_sad.pack(pady=10)

btn2_happy=ctk.CTkButton(app,
                        text="Mutluluk denince de bu şarkı ve totosuna patapata yapan foklar 🦭",
                        command=happy,
                        width=280,
                        height=45,
                        font=("Consolas", 12, "bold"),
                        corner_radius=20,
                        fg_color="#4E8D9C",
                        hover_color="#85C79A",)
btn2_happy.pack(pady=10)

btn3_angry=ctk.CTkButton(app,
                        text="Sinirden önümü göremiyorum o derece sinirliyim(Sıkıntı kardeşim)",
                        command=angry,
                        width=280,
                        height=45,
                        font=("Consolas", 12, "bold"),
                        corner_radius=20,
                        fg_color="#4E8D9C",
                        hover_color="#85C79A",)
btn3_angry.pack(pady=10)

btn4_energetic=ctk.CTkButton(app,
                            text="Shake your buttt nigarr type energy 👾",
                            command=energetic,
                            width=280,
                            height=45,
                            font=("Consolas", 12, "bold"),
                            corner_radius=20,
                            fg_color="#4E8D9C",
                            hover_color="#85C79A",)
btn4_energetic.pack(pady=10)

btn5_özledim=ctk.CTkButton(app,
                          text="Özledim lan çoook özledimmmm ölücem öldürücem hasretten 🦢",
                          command=özledim,
                          width=280,
                          height=45,
                          font=("Consolas", 12, "bold"),
                          corner_radius=20,
                          fg_color="#4E8D9C",
                          hover_color="#85C79A",)
btn5_özledim.pack(pady=10)

app.mainloop()
