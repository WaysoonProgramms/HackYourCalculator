from PIL import Image
import customtkinter
from tkinter.messagebox import showerror
import webbrowser
import datetime
from pygame import mixer

mixer.init()

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("430x330")
app.title("HackYourClaculator")
app.iconbitmap('icon.ico')
app.resizable(False, False)

def button_callback():
    global txt
    err = 0
    txt = entry_1.get()[::-1]
    txt = txt.lower()
    prt = ''
    for i in range(len(txt)):
        if txt[i] == 'l':
            tx = '7'
        elif txt[i] == 'b':
            tx = '9'
        elif txt[i] == 'h':
            tx = '4'
        elif txt[i] == 's':
            tx = '5'
        elif txt[i] == 'g':
            tx = '6'
        elif txt[i] == 'e':
            tx = '3'
        elif txt[i] == 'i':
            tx = '1'
        elif txt[i] == 'o':
            tx = '0'
        else:
            msg = "Некоректный запрос! Возможно некоторые символы не подлежат шифрованию. Попробуйте снова              \
                  Рекомендации:                                                            \
                   - Напишите слово латинскими буквами                 \
                   - Обратитесь к таблице символов (data.xlsx)"
            showerror(title="Ошибка!", message=msg)
            f = open('history.txt', 'a')
            now = datetime.datetime.now()
            text_1.insert("0.0", '[' + str(now.time()) + ']' + ' ВВОД: ' + txt[::-1] + ', ВЫВОД: ' + "(Ошибка!)" + '\n')
            f.write('[' + str(now) + ']' + ' ВВОД: ' + txt[::-1] + ', ВЫВОД: ' + "(Ошибка!)" + '\n')
            f.close()
            err = 1
            break
        prt += tx
    if err == 0:
        now = datetime.datetime.now()
        text_1.insert("0.0", '[' + str(now.time()) + ']' + ' ВВОД: ' + txt[::-1] + ', ВЫВОД: ' + prt + '\n')
        f = open('history.txt', 'a')
        f.write('[' + str(now) + ']' + ' ВВОД: ' + txt[::-1] + ', ВЫВОД: ' + prt + '\n')
        f.close()

        mixer.music.load("message.mp3")
        mixer.music.play()

def button_callback_2():
    webbrowser.open('https://github.com/WaysoonProgramms/HackYourCalculator/tree/main')

def button_callback_3():
    webbrowser.open('history.txt')

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=15, padx=10, fill="both", expand=True)

logo = customtkinter.CTkImage(dark_image=Image.open("txt.png"), size=(400,40))
label_1 = customtkinter.CTkLabel(master=frame_1, text='', image=logo)
label_1.pack(pady=10, padx=0)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Введите слово", font=('Courier New', 13))
entry_1.pack(pady=0, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, text="Шифровать...", command=button_callback, font=('Courier New', 13))
button_1.pack(pady=10, padx=10)

label_1 = customtkinter.CTkLabel(master=frame_1, text='2.0 | by Waysoon', justify=customtkinter.LEFT, font=('Courier New', 13))
label_1.pack(pady=0, padx=0)

web = customtkinter.CTkImage(dark_image=Image.open("web.ico"), size=(9,9))
button_2 = customtkinter.CTkButton(master=frame_1, text="", image=web, command=button_callback_2, width=20, height=20)
button_2.place(x=5, y=140)

button_3 = customtkinter.CTkButton(master=frame_1, text="#", command=button_callback_3, width=25, height=20)
button_3.place(x=31, y=140)

frame_2 = customtkinter.CTkFrame(master=app)
frame_2.pack(pady=10, padx=10, fill="both", expand=True)

text_1 = customtkinter.CTkTextbox(master=frame_2, width=400, height=100, font=('Courier New', 13))
text_1.pack(pady=5, padx=0)
text_1.insert("0.0", 'Здесь будет отображена история за эту сессию...\n')


app.mainloop()
