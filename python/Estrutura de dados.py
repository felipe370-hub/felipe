
class Tarefa:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade
        self.estado = "pendente"  # Tarefa começa como pendente

    def marcar_como_concluida(self):
        self.estado = "concluída"

    def __str__(self):
        return f"{self.nome} - Prioridade: {self.prioridade} - Estado: {self.estado}"


class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, nome, prioridade):
        nova_tarefa = Tarefa(nome, prioridade)
        self.tarefas.append(nova_tarefa)
        print(f"Tarefa '{nome}' adicionada com sucesso!")

    def remover_tarefa(self, nome):
        tarefa_para_remover = None
        for tarefa in self.tarefas:
            if tarefa.nome.lower() == nome.lower():
                tarefa_para_remover = tarefa
                break
        if tarefa_para_remover:
            self.tarefas.remove(tarefa_para_remover)
            print(f"Tarefa '{nome}' removida com sucesso!")
        else:
            print(f"Tarefa '{nome}' não encontrada.")

    def listar_tarefas(self):
        pendentes = [tarefa for tarefa in self.tarefas if tarefa.estado == "pendente"]
        concluídas = [tarefa for tarefa in self.tarefas if tarefa.estado == "concluída"]
        
        print("\nTarefas Pendentes:")
        for tarefa in pendentes:
            print(tarefa)
        
        print("\nTarefas Concluídas:")
        for tarefa in concluídas:
            print(tarefa)

    def marcar_como_concluida(self, nome):
        for tarefa in self.tarefas:
            if tarefa.nome.lower() == nome.lower():
                tarefa.marcar_como_concluida()
                print(f"Tarefa '{nome}' marcada como concluída!")
                return
        print(f"Tarefa '{nome}' não encontrada.")

    def pesquisar_tarefa(self, nome):
        tarefas_encontradas = [tarefa for tarefa in self.tarefas if nome.lower() in tarefa.nome.lower()]
        if tarefas_encontradas:
            for tarefa in tarefas_encontradas:
                print(tarefa)
        else:
            print(f"Nenhuma tarefa encontrada com o nome '{nome}'.")



gerenciador = GerenciadorDeTarefas()

# Adicionando tarefas
gerenciador.adicionar_tarefa("Estudar Python", "alta")
gerenciador.adicionar_tarefa("Fazer compras", "média")
gerenciador.adicionar_tarefa("Lavar roupa", "baixa")

# Listando todas as tarefas
gerenciador.listar_tarefas()

# Marcando tarefa como concluída
gerenciador.marcar_como_concluida("Estudar Python")

# Listando novamente as tarefas
gerenciador.listar_tarefas()

# Remover tarefa
gerenciador.remover_tarefa("Fazer compras")

# Pesquisar tarefas
gerenciador.pesquisar_tarefa("roupa")
