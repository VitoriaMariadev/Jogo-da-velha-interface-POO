import PySimpleGUI as sg

def creditos():
    sg.theme('Default')
    sg.set_options(font=('Arial 12'), text_color='black')

    layout = [  
                [sg.Text('Creditos', font=('Arial 16'))],
                [sg.Text('Rian Costa', font=('Arial 14'))],
                [sg.Text('Vitória Maria', font=('Arial 14'))],
                [sg.Button('Voltar')],
            ]

    janela = sg.Window('Produtos', layout, element_justification='c', size=(200,150))

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED or eventos == 'Voltar': 
            break
