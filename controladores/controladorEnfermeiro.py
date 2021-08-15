from entidade import enfermeiro
from entidade.enfermeiro import Enfermeiro
from telas.telaEnfermeiro import TelaEnfermeiro


class ControladorEnfermeiro():
    def __init__(self, controlador_sistema):
        self.__tela_enfermeiro = TelaEnfermeiro()
        self.__enfermeiros = []
        self.__controlador_sistema = controlador_sistema

    def inclui_enfermeiro(self):
        dados_enfermeiro = self.__tela_enfermeiro.pega_dados_enfermeiro
        enfermeiro = Enfermeiro(dados_enfermeiro["nome"], dados_enfermeiro["cpf"], dados_enfermeiro["idade"], dados_enfermeiro["rua"], dados_enfermeiro["numero"], dados_enfermeiro["complemento"], dados_enfermeiro["matricula"], dados_enfermeiro["salario"])
        matricula_enfermeiro = self.pega_enfermeiro_por_matricula(enfermeiro.matricula)
        if matricula_enfermeiro is None:
            self.__enfermeiros.append(enfermeiro)
            self.__tela_enfermeiro.mostra_mesagem('Funcionário da Limpeza adicionado com sucesso!')
        else:
            self.__tela_enfermeiro.mostra_mesagem('Não foi possível cadastrar o enfermeiro pois a matrícula já existe!')

    def exclui_enfermeiro(self):
        self.listar_enfermeiros()
        matricula_enfermeiro_excluido = self.__tela_enfermeiro.seleciona_enfermeiro()
        enfermeiro_excluido = self.pega_enfermeiro_por_matricula(matricula_enfermeiro_excluido)
        if enfermeiro_excluido not in self.__enfermeiros:
            self.__tela_enfermeiro.mostra_mesagem('Não foi possível excluir o enfermeiro, pois a matrícula informada não está na lista!')
        else:
            self.__enfermeiros.remove(enfermeiro_excluido)
            self.__tela_enfermeiro.mostra_mesagem('Enfermeiro excluído com sucesso!')

    def altera_enfermeiro(self):
        self.listar_enfermeiros()
        matricula_enfermeiro_alterado = self.__tela_enfermeiro.seleciona_enfermeiro()
        enfermeiro_alterado = self.pega_enfermeiro_por_matricula(matricula_enfermeiro_alterado)
        if enfermeiro_alterado is None:
            self.__tela_enfermeiro.mostra_mesagem('Não foi possível alterar o enfermeiro, pois a matrícula informada não está na lista!')
        else:
            novos_dados = self.__tela_enfermeiro.pega_dados_para_alterar_enfermeiro()
            enfermeiro_alterado.nome = novos_dados["nome"]
            enfermeiro_alterado.idade = novos_dados["idade"]
            enfermeiro_alterado.rua = novos_dados["rua"]
            enfermeiro_alterado.numero = novos_dados["numero"]
            enfermeiro_alterado.complemento = novos_dados["complemento"]
            enfermeiro_alterado.salario = novos_dados["salario"]
            self.__tela_enfermeiro.mostra_mesagem('Enfermeiro alterado com sucesso!\n')
            self.listar_enfermeiros()

    def listar_enfermeiros(self):
        print('Listagem de enfermeiros:\n')
        for enfermeiro in self.__enfermeiros:
            print(f'Nome: {enfermeiro.nome} | CPF: {enfermeiro.cpf} | Idade: {enfermeiro.idade} | Endereço: {enfermeiro.rua}, {enfermeiro.numero}, {enfermeiro.complemento} | Matrícula: {enfermeiro.matricula} ')

    def pega_enfermeiro_por_matricula(self, matricula: int):
        for enfermeiro in self.__enfermeiros:
            if enfermeiro.matricula == matricula:
                return enfermeiro
        return None
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_enfermeiro(self):
        opcoes = {0: self.retornar, 1: self.inclui_enfermeiro, 2: self.altera_enfermeiro, 3: self.exclui_enfermeiro, 4: self.listar_enfermeiros}
        while True:
            opcao = self.__tela_enfermeiro.tela_opcoes()
            funcao_escolhida = opcoes[opcao]
            funcao_escolhida()
