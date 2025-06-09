#Pedro
import tkinter as tk
from tkinter import PhotoImage
import random
import os

button_color = "#666666"
button_hover_color = "#888888"
button_text_color = "#FFFFFF"
font_family = "Arial"
background_color = "#003366"
text_color = "#FFFFFF"

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

# Inicializa variáveis globais
score = 0
current_question = 0
BASE_DIR = os.path.dirname(__file__) 

# Variáveis globais do temporizador
time_left = 30
timer_id = None

# Função que verifica a resposta e avança
def check_answer(answer=None):
    global score, current_question, timer_id
    if timer_id:
        janela.after_cancel(timer_id)
    _, o1, o2, o3, o4, correct = questions[current_question]
    if answer == correct:
        score += 1
    current_question += 1
    if current_question < len(questions):
        display_question()
    else:
        show_result()

# Exibe a pergunta e opções na tela
def display_question():
    global time_left, timer_id
    start_frame.pack_forget()
    quiz_frame.pack()
    q, o1, o2, o3, o4, _ = questions[current_question]
    question_label.config(text=q)
    option1_btn.config(text=o1, command=lambda: check_answer(1))
    option2_btn.config(text=o2, command=lambda: check_answer(2))
    option3_btn.config(text=o3, command=lambda: check_answer(3))
    option4_btn.config(text=o4, command=lambda: check_answer(4))
    time_left = 30
    update_timer()

# Função que atualiza o temporizador na tela
def update_timer():
    global time_left, timer_id
    timer_label.config(text=f"Tempo restante: {time_left} s")
    if time_left > 0:
        time_left -= 1
        timer_id = janela.after(1000, update_timer)
    else:
        check_answer(None)  # Tempo acabou, avança sem resposta

# Exibe o resultado final com medalha
def show_result():
    percentual = score / len(questions)
    if percentual >= 0.8:
        medalha_img = "medalha_ouro.png"
        mensagem = "Incrível! Medalha de OURO!"
    elif percentual >= 0.5:
        medalha_img = "medalha_prata.png"
        mensagem = "Muito bem! Medalha de PRATA!"
    else:
        medalha_img = "medalha_bronze.png"
        mensagem = "Continue tentando! Medalha de BRONZE."
#Tainara

