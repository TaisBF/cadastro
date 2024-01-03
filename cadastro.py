from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkmacosx import Button
import ast


window = Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

def signup():
    username = user.get()
    password = code.get()
    conform = conform_code.get()

    if not (password and conform):
        messagebox.showerror('Invalid', 'Password fields cannot be empty')
        return

    if password == conform:
        try:
            file = open('darasheet.txt', 'r+')
            d = file.read()
            file.close()
            r = ast.literal_eval(d)

            dict2 = {username: password}
            r.update(dict2)

            file = open('darasheet.txt', 'w')
            w = file.write(str(r))
            file.close()

            messagebox.showinfo('Signup', 'Successfully signed up')

        except Exception as e:
            print(f"Erro: {e}")
            file = open('darasheet.txt', 'w')
            pp = str({username: password})
            file.write(pp)
            file.close()
            messagebox.showerror('Invalid', 'An error occurred during signup')

    else:
        messagebox.showerror('Invalid', 'Both Password should match')


# Caminho para a imagem original
caminho_da_imagem_original = '/Users/taisfigueiredo/Cursos/Python/Cadastro/cadastro-positivo.jpg'

# Carregar e converter a imagem usando o Pillow
try:
    imagem_pillow = Image.open(caminho_da_imagem_original)
    resize_image = imagem_pillow.resize((380, 380))
    imagem_convertida = ImageTk.PhotoImage(resize_image)

    # Exibir a imagem convertida em um rótulo
    label = Label(window, image=imagem_convertida, bg='white',  border=0,)
    label.place(x=40, y=50)
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")

frame=Frame(window, width=350, height=390, bg='white')
frame.place(x=480, y=50)


heading=Label(frame, text='Sing up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

###--------------------------------------------------------------------------\

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    if user.get()=='':
        user.insert(0, 'Username')


user = Entry(frame, width=35, fg='black', highlightbackground='white', highlightcolor='white', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user. place(x=35,y=70)
user.insert(0,'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=1, bg='black').place(x=25, y=97)

###--------------------------------------------------------------------------\

def on_enter_password(e):
    code.delete(0,'end')
    code.config(show="*")

def on_leave_password(e):
    password=code.get()
    if password=='':
        code.insert(0, 'Password')
        code.config(show='')



code = Entry(frame, width=35, highlightbackground='white', highlightcolor='white',  fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=35,y=130)
code.insert(0,'Password')
code.bind("<FocusIn>", on_enter_password)
code.bind("<FocusOut>", on_leave_password)

Frame(frame, width=295, height=1, bg='black').place(x=25, y=157)

###--------------------------------------------------------------------------\

def on_enter_conform(e):
    conform_code.delete(0,'end')
    conform_code.config(show="*")

def on_leave_conform(e):
    conform = conform_code.get()
    if not conform:
        conform_code.insert(0, 'Conform Password')
        conform_code.config(show='')


conform_code = Entry(frame, width=35, highlightbackground='white', highlightcolor='white', fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
conform_code. place(x=35,y=188)
conform_code.insert(0,'conform Password')
conform_code.bind("<FocusIn>", on_enter_conform)
conform_code.bind("<FocusOut>", on_leave_conform)

Frame(frame, width=295, height=1, bg='black').place(x=25, y=215)

###--------------------------------------------------------------------------\

Button(frame, width=300, pady=7, text='Sign up', highlightbackground='white', bg='#00f', fg='white', border=0, command=signup). place(x=24, y=245)
label=Label(frame,text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=90,y=310)

signin=Button(frame, width=100, text='Sign in', border=0, bg='white', highlightbackground='white',  cursor='hand', fg='#00f')
signin.place(x=180, y=305)



window.mainloop() 