class Funcionario:
    def __init__(self, titular, cargo, saldo_inicial=0):
        self.nome = titular
        self.cargo = cargo
        self.__saldo = saldo_inicial

    def aumentar(self, aumento):
        if aumento > 0:
            self.__saldo += aumento
            # Correção aqui: mudado self._saldo para self.__saldo
            print(f"Olá {self.nome}, você obteve {aumento:.2f} reais, agora seu saldo é de {self.__saldo:.2f}.")
        else:
            print(f"Olá {self.nome}, o aumento deve ser positivo.")

    def get_saldo(self):
        return self.__saldo

class Gerente(Funcionario):
    def __init__(self, titular, cargo, saldo, bonus=0):
        super().__init__(titular, cargo, saldo)
        self.bonus = bonus

    def get_saldo(self):
        # Correção: Mudança de self._Fucionario__saldo para self._Funcionario__saldo
        return super().get_saldo() + self.bonus

def main():
    funcionario = Funcionario("Felipe", "Balconista", 1200)
    print(f"Salário inicial do funcionário {funcionario.nome}: R${funcionario.get_saldo():.2f}")

    funcionario.aumentar(400)
    print(f"Após o aumento do funcionário {funcionario.nome}: R${funcionario.get_saldo():.2f}")

    conta_gerente = Gerente("Bob", "Gerente", 1700, 10)
    print(f"Salário inicial do gerente {conta_gerente.nome}: R${conta_gerente.get_saldo():.2f}")
    
    conta_gerente.aumentar(150)
    print(f"Após o aumento do gerente {conta_gerente.nome}: R${conta_gerente.get_saldo():.2f}")

if __name__ == "__main__":
    main()
