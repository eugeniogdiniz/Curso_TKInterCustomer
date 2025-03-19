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

# Caixa de dialogo

def abrir():
    dialog = ctk.CTkInputDialog(title="Caixa de Dialogo",
                                text="Digite o seu numero de Celular",
                                entry_border_color="red")
    print(dialog.get_input())

btn = ctk.CTkButton(master=janela, text="Abrir caixa de Dialog",
                    command=abrir)
btn.pack()


janela.mainloop()