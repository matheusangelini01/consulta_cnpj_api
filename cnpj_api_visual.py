# importar biblioteca visual
import customtkinter as ctk

# importar biblioteca para fazer requisições 
import requests

# aparencia da janela 
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

window_cnpj = ctk.CTk()
window_cnpj.title('Consuta CNPJ')
window_cnpj.geometry('800x600')

# Função Consulta CNPJ
def consulta_cnpj():
    cnpj = entry_cnpj.get().strip()
    if not cnpj:
        resultado.configure('CNPJ inválido')
        return
    
    try:
        url = f'https://api.opencnpj.org/{cnpj}'
        resposta = requests.get(url)
        dados = resposta.json()

        informacao = (
        f'CNPJ: {dados["cnpj"]}\n'
        f'Razão Social:{dados["razao_social"]}\n'
        f'Situação Cadastral:{dados["situacao_cadastral"]}\n'
    )
        resultado.configure(text=informacao)
    except:
        resultado.configure('Erro ao consultar CNPJ')

# titulo da janela (nome e caracteristicas)
titulo = ctk.CTkLabel(window_cnpj, 
                      text='Consulta de CNPJ',
                      font=('Arial', 22),
                      text_color='#016FFC')
titulo.pack(pady=30)

# entrada de dados
entry_cnpj = ctk.CTkEntry(window_cnpj, 
                          placeholder_text='Digite o CNPJ', 
                          width=400,
                          height=40, 
                          corner_radius=12)
entry_cnpj.pack(pady=20)

# Botão
consultar = ctk.CTkButton(window_cnpj, text='Consultar',
                          width=400,
                          height=40,
                          fg_color='#35BF38',
                          hover_color='#B20000')
consultar.pack(pady=30)

# Resultado
resultado = ctk.CTkLabel(window_cnpj, 
                      text='Resultado',
                      font=('Arial', 22),
                      text_color='#FC7A01')
resultado.pack(pady=30)

window_cnpj.mainloop()