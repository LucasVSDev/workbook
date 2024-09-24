import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

ticker = input("Digite o codigo da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2024-01-01", end="2024-07-31")
fechamento = dados.Close
fechamento.plot()

maximo = round(fechamento.max(), 2)
minimo = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2) 

print(maximo)
print(minimo)
print(valor_medio)

destinatario = "Email"
assunto = "Análises de Projeto 2024"

messagem = f""" 
Prezado Gestor,

segue as análises solicitadas da ação {ticker}:

Cotação Máxima: R${maximo}
Cotação Mínima: R${minimo}
Cotação Médio: R${valor_medio}

Qualquer dúvida, estou à disposição!

Atte.
"""
# Abrir o navegador e ir para o Gmail
webbrowser.open("www.gmail.com")
time.sleep(5)

# configura uma pause de 4 segundo
pyautogui.PAUSE = 4

# Clicar no botão escrever
pyautogui.click(x = 81, y = 162)

# digita o email do destinataro e tecla TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digita o assunto do email
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

# digita a messagem 
pyperclip.copy(messagem)
pyautogui.hotkey("ctrl", "v")

# Enviar a messagem
pyautogui.click(x=792, y=701)

# Fechar o email
# pyautogui.click("ctrl", "f4")

print("Email enviador com sucesso!")