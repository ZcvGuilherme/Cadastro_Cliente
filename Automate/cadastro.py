import pyautogui as pg
import pandas as pd
import time


def go_and_click(x, y):
    pg.moveTo(x, y)
    pg.click()

def cadastrar_produtos():
    pg.PAUSE = 0.7
    produtos = pd.read_excel("produtos2.xlsx")
    time.sleep(3)

    for index, row in produtos.iterrows():
        nome = row['Nome']
        quantidade = row['Quantidade']
        valor = row['Valor']

        time.sleep(2)
        go_and_click(715, 328)
        pg.write(nome, interval=0.03)

        go_and_click(711, 381)
        pg.write(str(quantidade), interval=0.03)

        go_and_click(716, 427)
        pg.write(str(valor), interval=0.03)

        go_and_click(699, 477)


def cadastrar_clientes():
    pg.PAUSE = 0.7
    time.sleep(2)
    clientes = pd.read_excel("clientes2.xlsx")
    for index, row in clientes.iterrows():
        nome = row['Nome']
        email = row['Email']
        telefone = row['Telefone']
        data_nasc = row['Data_nasc']
        sexo = row['Sexo']

        go_and_click(712, 276)
        pg.write(nome, interval=0.03)

        go_and_click(714, 327)
        pg.write(email, interval=0.03)

        go_and_click(721, 386)
        pg.write(telefone, interval=0.03)

        go_and_click(657, 451)
        pg.write(data_nasc.strftime("%d/%m/%Y"), interval=0.03)  # Convertendo a data para o formato string

        go_and_click(717, 499)
        if sexo == "Masculino":
            go_and_click(716, 546)
        else:
            go_and_click(707, 573)

        go_and_click(585, 558)
        time.sleep(1)  

time.sleep(3)
cadastrar_produtos()