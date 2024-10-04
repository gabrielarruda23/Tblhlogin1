
import customtkinter as ctk
from tkinter import *
janela = ctk.CTk()

class Aplication():
    def __init__(self):
      self.janela=janela
      self.tema()
      self.tela()
      self.tela_login()
      janela.mainloop()


    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("700x400")
        janela.title("Sistema de login")
        janela.iconbitmap("icon.ico")
        janela.resizable(False, False) 

    def tela_login(self):
        #Trabalhando com a imagem de tela
        img = PhotoImage(file="log.png")
        label_img = ctk.CTkButton(master=janela, image=img, text=None, hover=None, fg_color=None).place(x=5, y=65)

        title_frame = ctk.CTkLabel(master=janela, text="Entre na sua conta", font=("Roboto", 18), text_color="#00B0F0").place(x=10, y=10)

        #frame  
        login_frame = ctk.CTkFrame(master=janela, width=350, height=400)
        login_frame.pack(side=RIGHT,)

        # widgets dentro da tela de login 
       
        label = ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=ctk.CTkFont(family='Roboto', size=20))
        label.place(x=25, y=10)

        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Nome do usuário", width=300, font=('Roboto', 12)).place(x=25, y=105)
        username_label = ctk.CTkLabel(master=login_frame, text="O campo nome do usuário é de caráter obrigatório.", text_color="green", font=("Roboto", 8)).place(x=25, y=135)


        text_front = ctk.CTkEntry(master=login_frame, placeholder_text="Senha do usuário", width=300, font=('Roboto', 14), show="🔒").place(x=25, y=175)
        password_label = ctk.CTkLabel(master=login_frame, text="O campo senha do usuário é de caráter obrigatório.", text_color="green", font=("Roboto", 8)).place(x=25, y=205)

        checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembrar de mim sempre").place(x=25, y=235)

        login_button = ctk.CTkButton(master=login_frame, text="LOGIN", width=300).place(x=25, y=285)


        register_span = ctk.CTkLabel(master=login_frame, text="Se não tem uma conta").place (x=25, y=325)

       
        def tela_registro():
            #Removendo a Frame de login
            login_frame.pack_forget()

            #Crinda tela de cadastro 
            rg_frame = ctk.CTkFrame(master=janela, width=350, height=400)
            rg_frame.pack(side=RIGHT,)

            label = ctk.CTkLabel(master=rg_frame, text="Sistema de Login", font=ctk.CTkFont(family='Roboto', size=20))
            label.place(x=25, y=10)

            

        pass
        register_button = ctk.CTkButton(master=login_frame, text="cadastre-se", width=150,
        fg_color="green", hover_color="#2D9334").place (x=175, y=325)

Aplication()