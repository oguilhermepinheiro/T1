from entidade.funcionario import Funcionario


class Enfermeiro(Funcionario):
    def __init__(self, nome: str, cpf: str, idade: int, rua: str, numero: int, complemento: str, matricula: int, salario: float):
        super().__init__(nome, cpf, idade, rua, numero, complemento, matricula, salario)
