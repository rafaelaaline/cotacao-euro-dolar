import requests
import json
from tkinter import *

def pegar_cotacoes():
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacoes = cotacoes.json()
    cotacao_dolar = cotacoes['USDBRL']['bid']
    cotacao_euro = cotacoes['EURBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}'''

    texto_cotacoes['text'] = texto

janela = Tk()
janela.title('Cotação Atual de Moedas')
texto_orientacao = Label(janela, text='Clique no botão para ver as cotações:')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='Buscar cotações dólar/euro', command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
