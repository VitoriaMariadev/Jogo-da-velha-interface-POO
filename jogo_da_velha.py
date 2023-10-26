import PySimpleGUI as sg
import json
from creditos import creditos

def salvar_dicionarios(dicionario, nome_do_arquivo):
    """
    Função que salva os dicionarios principais do código em arquivos '.json'.
    """
    with open(f'{nome_do_arquivo}.json', 'w') as file:
        json.dump(dicionario, file)
        
def pegar_dicionario(nome_do_arquivo):
    """
    Função que carrega os dicionarios principais do codigo que estão salvos em arquivos '.json'.
    """
    with open(f'{nome_do_arquivo}.json', 'r') as file:
        return json.load(file)

placar = pegar_dicionario('placar')

sg.theme('Default')
sg.set_options(font=('Arial 12'), text_color='black')

jogador = 'O'

layout = [  
            [sg.Text('Jogo da velha', font=('Arial 16'))],
            [sg.Text(f'Jogador X: {placar["Jogador X"]}', font=('Arial 14'), key='jogador_x'), sg.Text(f'Jogador O: {placar["Jogador O"]}', font=('Arial 14'), key='jogador_o')],
            [sg.Text(f'Jogador: {jogador}', font=('Arial 12'), key='jogador')],
            [sg.Button('', size=(7,3), key='1'), sg.Button('', size=(7,3), key='2'), sg.Button('', size=(7,3), key='3')],
            [sg.Button('', size=(7,3), key='4'), sg.Button('', size=(7,3), key='5'), sg.Button('', size=(7,3), key='6')],
            [sg.Button('', size=(7,3), key='7'), sg.Button('', size=(7,3), key='8'), sg.Button('', size=(7,3), key='9')],
            [sg.Button('Sobre',font=('Arial 14'), size=(9,1), key='sobre')],
        ]

janela = sg.Window('Produtos', layout, element_justification='c')

lista_de_jogadas = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9'
]

def mudar_jogador():
    global jogador
    if jogador == 'O':
        jogador = 'X'
    else:
        jogador = 'O'

def checar_casa(tabuleiro, casa):
    if tabuleiro[casa] in 'OX':
        return False

    return True

def ver_quem_ganhou(tabuleiro):
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
        return True
    elif tabuleiro[3] == tabuleiro[4] == tabuleiro[5]:
        return True
    elif tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
        return True
    
    elif tabuleiro[0] == tabuleiro[3] == tabuleiro[6]:
        return True
    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
        return True
    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
        return True
    
    elif tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
        return True

    elif tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
        return True

contador = 0

def limpar_tabuleiro():
    global lista_de_jogadas
    global contador
    janela['1'].update('')
    janela['2'].update('')
    janela['3'].update('')
    janela['4'].update('')
    janela['5'].update('')
    janela['6'].update('')
    janela['7'].update('')
    janela['8'].update('')
    janela['9'].update('')

    lista_de_jogadas = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9'
    ]

    contador = 0

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED: 
        break
    if eventos != 'sobre':

        if checar_casa(lista_de_jogadas, int(eventos) - 1):
            janela[eventos].update(jogador)
            lista_de_jogadas[int(eventos) - 1] = jogador

            if ver_quem_ganhou(lista_de_jogadas):
                sg.popup(f'Jogador {jogador} ganhou!')
                valor = placar[f'Jogador {jogador}']
                placar[f'Jogador {jogador}'] = valor + 1
                salvar_dicionarios(placar, 'placar')
                janela['jogador_x'].update(f'Jogador X: {placar["Jogador X"]}')
                janela['jogador_o'].update(f'Jogador O: {placar["Jogador O"]}')
                if sg.popup_yes_no('Deseja continuar jogando?') == 'Yes':
                    limpar_tabuleiro()
                    continue
                else:
                    break
                
            contador += 1

            if contador == 9:
                sg.popup(f'O jogo deu velha!')     
                if sg.popup_yes_no('Deseja continuar jogando?') == 'Yes':
                    limpar_tabuleiro()
                    continue
                else:
                    break
            mudar_jogador()
            janela['jogador'].update(f'Jogador: {jogador}')
        else:
            sg.popup('Casa ocupada')

    elif eventos == 'sobre':
        janela.hide()
        creditos()
        janela.un_hide()
    