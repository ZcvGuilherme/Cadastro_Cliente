import pyautogui as pg
import pandas as pd
import time


def go_and_click(x, y):
    pg.moveTo(x, y)
    pg.click()


def cadastrar_clientes():
    pg.PAUSE = 0.7
    time.sleep(2)
    clientes = pd.read_excel("clientes.xlsx")
    for index, row in clientes.iterrows():
        nome = row['Nome']
        email = row['Email']
        telefone = row['Telefone']
        data_nasc = row['Data_nasc']
        sexo = row['Sexo']

        go_and_click(712, 276)
        pg.write(nome)

        go_and_click(714, 327)
        pg.write(email)

        go_and_click(721, 386)
        pg.write(telefone)

        go_and_click(657, 451)
        pg.write(data_nasc.strftime("%d/%m/%Y"))  # Convertendo a data para o formato string

        go_and_click(717, 499)
        if sexo == "Masculino":
            go_and_click(716, 546)
        else:
            go_and_click(707, 573)

        go_and_click(585, 558)
        time.sleep(0.5)  

time.sleep(3)
cadastrar_clientes()