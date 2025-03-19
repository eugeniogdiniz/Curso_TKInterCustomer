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
#Tabview

tabview = ctk.CTkTabview(master=janela, width=400, corner_radius=20, 
                         border_width=1, border_color="red", fg_color="teal", 
                         segmented_button_fg_color="red", segmented_button_selected_color="green",
                         segmented_button_unselected_hover_color="blue")
tabview.pack()
tabview.add("Nomes")
tabview.add("Idades")
tabview.add("Genero")
tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Idades").grid_columnconfigure(0, weight=1)
tabview.tab("Genero").grid_columnconfigure(0, weight=1)

# Adicionando elementos na nossa tab

nom = ctk.CTkLabel(tabview.tab("Nomes"), text="Salvador Eduardo\nEugenio Eduardo\nAntonia Tomocene")
nom.pack()
idd = ctk.CTkLabel(tabview.tab("Idades"), text="23\n31\n42")
idd.pack()
gen = ctk.CTkLabel(tabview.tab("Genero"), text="Homem\nHomem\nMulher")
gen.pack()



janela.mainloop()