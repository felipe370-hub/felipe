class Funcionario:
    def __init__(self, nome, cargo, salario=0):
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def aumentar_salario(self, aumento):
        if aumento > 0:
            self.__salario += aumento
            print(f"Olá {self.nome}, seu salário foi aumentado para R${self.__salario:.2f}.")
        else:
            print("O aumento deve ser positivo.")

class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, bonus=0):
        super().__init__(nome, cargo, salario)
        self.bonus = bonus

    def get_salario(self):
        return super().get_salario() + self.bonus

def main():
    funcionario = Funcionario("Alice", "Desenvolvedora", 5000)
    print(f"Salário inicial do funcionário {funcionario.nome}: R${funcionario.get_salario():.2f}")

    funcionario.aumentar_salario(600)
    print(f"Salário após aumento do funcionário {funcionario.nome}: R${funcionario.get_salario():.2f}")

    gerente = Gerente("Bob", "Gerente de Projetos", 8000, 2000)
    print(f"Salário inicial do gerente {gerente.nome}: R${gerente.get_salario():.2f}")

    gerente.aumentar_salario(1000)
    print(f"Salário após aumento do gerente {gerente.nome}: R${gerente.get_salario():.2f}")

if __name__ == "__main__":
    main()
