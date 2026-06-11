class Tarefa:
    def __init__(self, nome):
        self.nome = nome
        self.concluida = False
    
    def concluir(self):
        self.concluida = True
    def descricao(self):
        return f"{self.nome} - {'[✓]' if self.concluida else '[ ]'}"

tarefas = []

def mostrar_menu():
    print("=== MENU DE TAREFAS ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Sair")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Digite o nome da tarefa: ")
        tarefas.append(Tarefa(nome))
        print("Tarefa adicionada!")
    elif opcao == "2":
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1}. {tarefa.descricao()}")
    elif opcao == "3":
        indice = int(input("Digite o número da tarefa para concluir: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice].concluir()
            print("Tarefa concluída!")
        else:
            print("Índice inválido!")
    elif opcao == "4":
        print("Até logo!")
        break
    else:
        print("Opção inválida")