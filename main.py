# SISTEMA DE CLEINTES
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Ricardo Antonio Cardoso
# Created Date: Mai-2022
# version ='1.0'
# ---------------------------------------------------------------------------
import PySimpleGUI as sg
import siud
from valida_cpf import valida_cpf as v_cpf

if __name__ == "__main__":

    def cadastro():
        sg.theme('GreenTan')
        layout = [
            [sg.Text("URNA ELETRONICA", size=20)],
            [sg.Text("Nome do eleitor.", size=20)],
            [sg.Input(key="nome", size=100)],
            [sg.Text(f"{44 * '--'}", size=45)],
            [sg.Text("CPF do eleitor.", size=20)],
            [sg.Input(key="cpf", size=50)],
            [sg.Text("Selecione seu voto.", size=40)],
            [sg.Listbox(values=["Lula", "Bolsonaro", "João Doria", "Ciro Gomes", "Branco", "Nulo"],
                        key="voto", default_values=["Branco"], no_scrollbar=True, size=(50, 6))],
            [sg.Button('Votar', size=20), sg.Button("Sair", size=20)],
            [sg.Button('Gerar resultado parcial.', size=20)]
        ]
        return sg.Window('Voto eletronico.', size=(384, 380), icon="login.ico", layout=layout,
                         finalize=True)


    def parcial():
        sg.theme('GreenTan')
        layout = [
            [sg.Text("RESULTADO PARCIAL", size=50)],
            [sg.Output(size=(58, 60), background_color='lightgrey', text_color='Black',
                       font='Tahoma 10')],
        ]
        return sg.Window('Parcial dos resultados.', size=(350, 370), icon="login.ico", layout=layout,
                         finalize=True)


    def executa():
        janela1, janela2 = cadastro(), None
        while True:
            window, events, values = sg.read_all_windows()
            if events == janela1 and sg.WINDOW_CLOSED:
                break
            if window == janela1 and events == "Votar":
                if values["nome"] and len(values["cpf"]) == 11:
                    if v_cpf(values["cpf"]) != 0:
                        cpf_f = f"{values['cpf'][0:3]}.{values['cpf'][3:6]}.{values['cpf'][6:9]}-{values['cpf'][9:11]}"
                        if siud.buscar_cpf(cpf_f) == 0:
                            sg.popup_no_border("CPF ja cadastrado.", background_color="Gray",
                                               button_color="Silver")
                            janela1["cpf"].update("")
                            janela1["cpf"].set_focus()
                            continue
                        elif siud.buscar_cpf(cpf_f) != 0:
                            sg.popup_no_border("Seu voto foi computado.", background_color="Gray",
                                               button_color="Silver")
                            sg.popup_no_border("Finalizando voto. ", f"Seu voto foi em {values['voto'][0]}",
                                               background_color="silver", button_color="gray")
                            nome = values["nome"].title()
                            voto = values["voto"][0]
                            id_candidato = siud.buscar_idcandidato(voto)
                            siud.inserir_eleitor(nome, cpf_f, int(id_candidato))
                            janela1["nome"].update("")
                            janela1["cpf"].update("")
                            janela1["nome"].set_focus()
                            continue
                    else:
                        sg.popup_no_border("CPF precisa ter apenas digitos.", background_color="Gray",
                                           button_color="Silver")
                        janela1["cpf"].update("")
                        janela1["cpf"].set_focus()
                        continue
                elif not values["nome"]:
                    sg.popup_no_border("Digite seu nome.", background_color="Gray",
                                       button_color="Silver")
                    janela1["nome"].set_focus()
                    continue
                elif len(values["cpf"]) != 11:
                    sg.popup_no_border("CPF precisa ter 11 digitos.", background_color="Gray",
                                       button_color="Silver")
                    janela1["cpf"].set_focus()
                elif not values["cpf"]:
                    sg.popup_no_border("Insira seu CPF para votar.", background_color="Gray",
                                       button_color="Silver")
                    janela1["cpf"].set_focus()
                pass
            if window == janela1 and events == "Sair":
                sg.popup_no_border("Finalizando",
                                   background_color="silver", button_color="gray")
                break
            if window == janela1 and events == 'Gerar resultado parcial.':
                janela2 = parcial()
                siud.resultado_parcial()
                continue
            if window == janela1 and events == sg.WINDOW_CLOSED:
                break
            if window == janela2 and events == sg.WINDOW_CLOSED:
                janela2.hide()
                continue


    executa()
