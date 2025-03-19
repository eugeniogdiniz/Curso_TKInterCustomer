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

# Caixas de Texto

textbox = ctk.CTkTextbox(master=janela, width=300, height=350, 
                         scrollbar_button_color="teal", 
                         scrollbar_button_hover_color="green",
                         border_color="red", border_width=2,
                         corner_radius=15, border_spacing=20,
                         activate_scrollbars=True)
textbox.pack()

textbox.insert("0.0", "Título do seu texto\n\n" + 
               "Ola dev, estou aqui programando interface gráfica com customtkinter\n\n"*20)




janela.mainloop()