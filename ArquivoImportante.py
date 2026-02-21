print("Arquivo importante carregado com sucesso!")
print("Este arquivo é essencial para o funcionamento do programa, por favor, não o exclua ou modifique sem autorização.")
print("Delícia de código! :")
#biblioteca de livros
biblioteca = []     
#função para adicionar livros
def adicionarLivro():
    try:
        titulo = input("Digite o título do livro: ")
    except ValueError as v:
        print("Erro! {v}")
    else:
        livro = {
            "titulo": titulo.strip().lower().title(),
            "disponivel": True
        }
        biblioteca.append(livro)
        print(f"Livro \"{titulo}\" adicionado com sucesso!\n")

print("Delícia de código! :")
