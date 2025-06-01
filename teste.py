class ContaBancaria:
    def __init___(self, titular, saldo):
        self.titular = titular          #publico, acessivel fora da classe
        self._saldo = saldo             #protegido porem com acesso
        self.__senha = "12234"          #privado, não acessivel fora da classe

    def mostrar_dados(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self._saldo}")
        print(f"Senha: {self.__senha}")  # Acesso permitido dentro da classe

conta = ContaBancaria("João", 225)

print(conta.titular)  # Acesso permitido
print(conta._saldo)   # Acesso permitido, mas não recomendado
print(conta.__senha)  # Acesso negado, gera erro
