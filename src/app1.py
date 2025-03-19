import customtkinter as ctk

janela = ctk.CTk(
    # fg_color="green"
)
# janela._set_appearance_mode("light")

#Configurando janela CTK
janela.title("App teste")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=True, height=False)
# janela.iconify()
# janela.deiconify()

# Criando nova Janela

def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="#F2F2F2")
    nova_janela.geometry("500x250")

frame1 = ctk.CTkFrame(master=janela, width=200, height=330, 
                      fg_color="teal", bg_color="transparent", border_width=10, corner_radius=30
                      ).place(x=10, y=60)
frame2 = ctk.CTkFrame(master=janela, width=200, height=330).place(x=230, y=60)
frame3 = ctk.CTkFrame(master=janela, width=200, height=330).place(x=450, y=60)


btn_nova_tela = ctk.CTkButton(frame2, text="Abrir Nova Janela", command=nova_tela).place(x=10, y=10)




janela.mainloop()