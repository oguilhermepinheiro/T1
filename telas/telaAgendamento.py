from telas.abstractTela import AbstractTela
import PySimpleGUI as sg


class TelaAgendamento(AbstractTela):
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_components(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('SISTEMA DE CONTROLE DE AGENDAMENTOS', font=("Garamond", 25, 'bold'))],
            [sg.Text('Escolha sua opção', font=("Garamond", 20, 'bold'))],
            [sg.Radio('Inserir Agendamento', "RD1", key='1', font=("Garamond", 20))],
            [sg.Radio('Alterar Agendamento', "RD1", key='2', font=("Garamond", 20))],
            [sg.Radio('Excluir Agendamento', "RD1", key='3', font=("Garamond", 20))],
            [sg.Radio('Listar Agendamentos', "RD1", key='4', font=("Garamond", 20))],
            [sg.Radio('Retornar', "RD1", key='0', font=("Garamond", 20))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de controle dos Agendamentos').Layout(layout)

    def pega_dados_agendamento(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('---------- DADOS DO AGENDAMENTO ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('Horário:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='horario')],
            [sg.Text('Data:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='data')],
            [sg.Text('CPF do Cliente:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='cpf_cliente')],
            [sg.Text('CPF do Médico ou Enfermeiro:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='cpf_medico_ou_enfermeiro')],
            [sg.Text('Digite apenas 1 ou 2 - [1] Vacina [2] Consulta:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='numero_tipoAgendamento')],
            [sg.Text('Digite a especialidade ou tipo de vacina:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='nome_tipoAgendamento')],
            [sg.Text('Código:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados do Agendamento').Layout(layout)

        button, values = self.open()

        horario = values['horario']
        data = values['data']
        cpf_cliente = values['cpf_cliente']
        cpf_medico_ou_enfermeiro = int(values['cpf_medico_ou_enfermeiro'])
        numero_tipoAgendamento = int(values['numero_tipoAgendamento'])
        nome_tipoAgendamento = values['nome_tipoAgendamento']
        codigo = int(values['codigo'])

        self.close()

        return {"horario": horario, "data": data, "codigo": codigo, "cpf_cliente": cpf_cliente, "numero_tipoAgendamento": numero_tipoAgendamento, "nome_tipoAgendamento": nome_tipoAgendamento, "cpf_medico_ou_enfermeiro": cpf_medico_ou_enfermeiro}

    def pega_dados_para_alterar_agendamento(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('---------- DADOS DO AGENDAMENTO ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('Horário:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='horario')],
            [sg.Text('Data:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='data')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Dados para alterar o agendamento').Layout(layout)

        button, values = self.open()

        horario = values['horario']
        data = values['data']
        return {"horario": horario, "data": data}

    def seleciona_agendamento(self):
        sg.ChangeLookAndFeel('LightBrown2')
        layout = [
            [sg.Text('-------- SELECIONAR AGENDAMENTO ----------', font=("Garamond", 25, 'bold'))],
            [sg.Text('Digite o código do agendamento que deseja selecionar:', font=("Garamond", 20))],
            [sg.Text('Código:', size=(15, 1), font=("Garamond", 18)), sg.InputText('', key='codigo_agendamento')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Agendamento').Layout(layout)

        button, values = self.open()
        codigo_agendamento = values['codigo_agendamento']
        self.close()
        return int(codigo_agendamento)

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def mostra_agendamento(self, dados_agendamento):
        string_todos_agendamentos = ""
        for dado in dados_agendamento:
            string_todos_agendamentos = string_todos_agendamentos + "HORÁRIO: " + dado["horario"] + '\n'
            string_todos_agendamentos = string_todos_agendamentos + "DATA: " + dado["data"] + '\n'
            string_todos_agendamentos = string_todos_agendamentos + "VALOR (R$): " + str(dado["valor"]) + '\n'
            string_todos_agendamentos = string_todos_agendamentos + "CÓDIGO : " + str(dado["codigo"]) + '\n\n'

        sg.Popup('-------- LISTA DE FUNCIONÁRIOS DA LIMPEZA ----------', string_todos_agendamentos)