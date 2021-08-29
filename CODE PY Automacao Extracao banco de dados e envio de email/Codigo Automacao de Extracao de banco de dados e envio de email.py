#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

# passo 1 - Entrar no drive ou nuvem onde esteja o arquivo que precise exportar
pyautogui.hotkey('ctrl', 't')

link = #" insira o link "

pyperclip.copy(link)

pyautogui.hotkey("ctrl", "v")

pyautogui.press("enter")


# passo 2 - navegar no sistema (entrar na pasta onde esteja o arquivo)
time.sleep(5)
pyautogui.click(x=370, y=293, clicks=2)

# passo 3 - baixar o arquivo de vendas
time.sleep(5)
pyautogui.click(x=387, y=378)

time.sleep(2)
pyautogui.click(x=1150, y=190)

time.sleep(2)
pyautogui.click(x=963, y=589)

time.sleep(6)

# passo 4 - calcular o faturamento e quantidade de produtos vendidos
import pandas as pd

tabela = pd.read_#UTILIZE TAB PARA ESCOLHER A EXTENSÃO DO ARQUIVO! (r" diretorio onde baixou o arquivo ")
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
display(tabela)
print(faturamento)
print(quantidade)

# passo 5 - enviar por email 
pyautogui.hotkey('ctrl', 't')

link = "https://mail.google.com/" #Pode ser qualquer provedor de email ou utilitario de e-mail como outlook ou thunderbird

pyperclip.copy(link)

pyautogui.hotkey("ctrl", "v")

pyautogui.press("enter")

### escrever e-mail

# clicar no botão escrever e-mail
time.sleep(5)
pyautogui.click(x=92, y=207)

# escrever destinatario
time.sleep(2)
pyautogui.write(" Email de destino ")
pyautogui.press("tab") # escolher o email
pyautogui.press("tab") # passar para campo assunto

# escrever assunto
pyautogui.write(" Texto assunto ")
pyautogui.press("tab") # passar para corpo do email

# escrever corpo do e-mail
texto = f""" 
Prezados, bom dia

O faturamento foi de R${faturamento:,.2f}
A quantidade foi de {quantidade:,}

Abs
XXXXX XXXXXX
"""
pyautogui.write(texto)

# enviar e-mail
pyautogui.hotkey("ctrl", "enter")


### Use esse código para descobrir qual a posição de um item que queira clicar
## De preferencia utilize este codigo em outra celula separada do codigo 
# Lembre-se: a posição pode mudar dependendo da reseolução ou tamanho do monitor!

import time

time.sleep(5)
pyautogui.position()

