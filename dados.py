import pandas as pd

# Lista de perguntas e respostas no formato:
# [pergunta, opção 1, opção 2, opção 3, opção 4, número da resposta correta]
questions = [
    ["Qual função é usada para imprimir algo na tela?", "show()", "print()", "display()", "output()", 2],
    ["Como se inicia um comentário em Python?", "//", "<!-- -->", "#", "*", 3],
    ["Qual dessas é uma variável válida em Python?", "1nome", "nome_completo", "nome-completo", "nome completo", 2],
    ["O que o código print(2 + 3 * 4) irá imprimir?", "20", "14", "24", "18", 2],
    ["Qual função lê uma entrada do usuário?", "input()", "read()", "scan()", "enter()", 1],
    ["Qual dessas estruturas é usada para repetir algo?", "if", "else", "for", "def", 3],
    ["Como se cria uma função em Python?", "function minhaFuncao():", "criar minhaFuncao():", "def minhaFuncao():", "func minhaFuncao():", 3],
    ["Qual dos seguintes é um tipo de dado em Python?", "texto", "number", "int", "palavra", 3],
    ["Qual comando é usado para verificar se x é igual a 10?", "x = 10", "x == 10", "x === 10", "x igual 10", 2],
    ["Qual índice representa o primeiro item de uma lista?", "0", "1", "-1", "primeiro", 1]
]

# Criar DataFrame com as colunas corretas
df = pd.DataFrame(questions, columns=["perguntas", "opção 1", "opção 2", "opção 3", "opção 4", "resposta"])

# Salvar em arquivo Excel
df.to_excel("questions.xlsx", index=False)

print("Arquivo 'questions.xlsx' criado com sucesso!")