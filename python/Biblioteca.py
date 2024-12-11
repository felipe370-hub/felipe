class Livros:
    def __init__ (self,titulo, autor, ano):
        self.titulo=titulo
        self.autor=autor
        self.ano=ano
        self.status="disponivel"
    
    def emprestar(self):
        if self.status =='disponivel':
            self.status ='emprestado'
            print (f'"{self.titulo}" emprestado')
            return True
        else:
            print(f'"{self.titulo}" não disponivel')
            return False
    
    def devolver(self):
        if self.status == 'emprestado':
            self.status ='disponivel'
            print(f'{self.titulo} devolvido')
        else:
            print(f'{self.titulo} já está disponivel.')

    def __str__(self):
        return f"{self.titulo} -{self.autor} - {'Disponivel' if self.status == 'disponivel' else 'indesponivel'}"   

class Usuario:
    def __init__ (self, nome, idade, id = None):
        self.nome= nome
        self.idade = idade
        self.id= id
        self.livros_emprestado=[]

    def pegar_emprestado(self, livro):
        if livro.emprestar():
            self.livros_emprestado.append(livro)
            print(f'"{livro.titulo}" emprestado para {self.nome}') 
        else:
            print(f'"{livro.titulo}"indiponivel')
        

    def devolver_livro (self, livro): 
        if livro in self.livros_emprestado:
            livro.devolver()
            self.livros_emprestado.remove(livro)
            print(f'"{livro.titulo}" devolvido por {self.nome}.')
        else:
            print(f'"{self.nome}" não tem o livro{livro.titulo}.')
  
    def __str__(self):
        return f"{self.nome} {self.idade} - id:{self.id}"

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios  = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def relatorio_livros_disponiveis(self):
        print("livros disponiveis:")
        for livro in self.livros:
            if livro.status == 'disponivel':
                print(livro)

    def relatorio_livro_com_usuarios(self):
        print("livros com usuarios:")
        for usuario in self.usuarios:
            if usuario.livros_emprestado:
                print(f"{usuario.nome}- esta com os seguintes livros")
                for  livro in usuario.livros_emprestado:
                    print(f" - {livro.titulo}") 

livro1= Livros("o senhor dos aneis", "J.R.R Tolkien",1954)
livro2= Livros("Harry Potter e a pedra filosofal", "J.K Rowling", 1997)
livro3= Livros("A Biblioteca da meia-noite", "Matt Haig", 2020 )
livro4= Livros("Five Nigths at Freddy Olhos Prateados", " Scott Cawthon", 2017)

usuario1= Usuario("Lira",  25 , "2431")
usuario2= Usuario("Maria", 18 , "7898")

biblioteca= Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)
biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)

usuario1.pegar_emprestado(livro1)
usuario2.pegar_emprestado(livro2)

biblioteca.relatorio_livros_disponiveis()

biblioteca.relatorio_livro_com_usuarios()

usuario1.devolver_livro(livro1)

biblioteca.relatorio_livros_disponiveis()
biblioteca.relatorio_livro_com_usuarios()