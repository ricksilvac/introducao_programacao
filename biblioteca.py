'''
Prova Prática de Python: Gestão de Biblioteca

O objetivo é criar um sistema básico de gestão de livros para uma pequena biblioteca, 
utilizando os conceitos solicitados.

Enunciado e Requisitos

Você deve implementar as seguintes funcionalidades:

Estrutura de Dados Inicial: Use uma lista global chamada biblioteca para 
armazenar os livros. Cada livro será um dicionário com as seguintes 
chaves: "titulo" (string), "autor" (string), "ano" 
(tupla com ano de publicação e número de edição), e "disponivel" (booleano).

Função para Adicionar Livro: Crie uma função chamada 
adicionar_livro(titulo, autor, ano_publicacao, edicao) que adicione um novo 
dicionário de livro à lista biblioteca. A chave "disponivel" deve ser True por padrão.

Função para Listar Livros: Crie uma função chamada listar_livros() que percorra 
a lista biblioteca usando um loop (for) e exiba os detalhes de cada livro em um 
formato legível. Use condicionais (if/else) para indicar se o livro está "Disponível" 
ou "Emprestado".

Função para Emprestar Livro: Crie uma função chamada emprestar_livro(titulo_desejado) 
que use um loop para encontrar o livro pelo título. Se encontrado e disponivel for True, 
mude o status para False e exiba uma mensagem de sucesso (use condicionais). 
Se não encontrado ou já emprestado, exiba mensagens de erro apropriadas.


Função para Devolver Livro: Crie uma função chamada devolver_livro(titulo_desejado) 
que use um loop para encontrar o livro pelo título. Se encontrado e disponivel for False,
 mude o status para True e exiba uma mensagem de sucesso. Caso contrário, exiba mensagens de erro.

Função Principal (main) e Interação: Crie uma função main() 
que apresente um menu de opções ao usuário (adicionar, listar, emprestar, devolver, sair) 
e use um loop (while) e condicionais para chamar as funções apropriadas com base na 
entrada do usuário. As entradas do usuário serão processadas como strings

'''
#função para adicionar livros
def adicionarLivro():
    try:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o nome do autor: ")
        dataPublicacao = input("Digite o ano no formato \"dd/mm/aaaa\": ")
        edicao = int(input("Digite o número da edição: "))

    except ValueError as v:
        print(f"Erro! Valor incorreto: {v}")
    except Exception as e:
        print(f"Erro {e}")
    else:
        lista = []
        lista.append(dataPublicacao)
        lista.append(edicao)

        ano = tuple(lista)
                            
        livro = {
                "titulo": titulo.strip().lower().title(),
                "autor": autor.strip().lower().title(),
                "ano": ano,
                "disponivel" :True
        }
        biblioteca.append(livro)
        print(f"Livro {titulo} adicionado\n")

#função para mostrar livros
def mostrarLivro():
    if not biblioteca:
        print("Biblioteca vazia\n")
        return
    
    print(f"{biblioteca} \n")

    for livro in biblioteca:
        #mostra se o livro está disponível ou emprestado
        if livro["disponivel"]:
            print(f"{livro["titulo"]} Disponível\n")
        else:
            print(f"{livro["titulo"]} Emprestado\n")

#função para emprestar livro
def emprestarLivros():
    try:
        escolha = input("Digite o livro que está buscando: ")
    except ValueError as v:
        print("Erro! {v}")
    else:
        for livro in biblioteca:
            if escolha.strip().lower().title() == livro["titulo"]:
                if livro["disponivel"]:
                    livro["disponivel"] = False
                    print(f"\"{livro["titulo"]}\" será emprestado a você\n")
                    break
                else:
                    print(f"O livro \"{livro["titulo"]}\" já está em emprestimo\n")
            else:
                print("Erro! Livro não existe na biblioteca\n")

#função para devolver livro
def devolverLivros():
    try:
        escolha = input("Digite o livro que deseja devolver: ")
    except ValueError as v:
        print("Erro! {v}")
    else:
        for livro in biblioteca:
            if escolha.strip().lower().title() == livro["titulo"]:
                if not livro["disponivel"]:
                    livro["disponivel"] = True
                    print(f"\"{livro["titulo"]}\" devolvido com sucesso\n")
                    break
                else:
                    print(f"O livro \"{livro["titulo"]}\" já está na biblioteca\n")
            else:
                print("Erro! Livro não existe na biblioteca\n")
            
#trecho principal do código
if __name__ == "__main__":
    global biblioteca
    biblioteca = []

    opcao = -1

    while opcao != 0:
        print("5 - Adicionar livro")
        print("2 - Mostrar livros disponíveis")
        print("3 - Emprestar livros")
        print("4 - Devolver livros")
        print("0 - Sair")
        try:
            opcao = int(input("Opção: "))
        except ValueError as v:
            print(f"Erro! {v}")
        except Exception as e:
            print(f"Erro! {e}")
        else:
            match opcao: #na questão pede para q seja em string, mas fiz com int mesmo pra facilitar
                case 5:
                    adicionarLivro()
                case 2:
                    mostrarLivro()
                case 3:
                    emprestarLivros()
                case 4:
                    devolverLivros()
                case 0:
                    print("Encerrando")
                case _:
                    print("Inválido")