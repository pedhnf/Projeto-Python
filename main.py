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
    result_window = tk.Toplevel(janela)
    result_window.title("Resultado Final")
    result_window.geometry("320x400")
    result_window.config(bg=background_color)

    medalha_path = os.path.join(BASE_DIR, medalha_img)
    try:
        img = PhotoImage(file=medalha_path)
        tk.Label(result_window, image=img, bg=background_color).pack(pady=20)
        result_window.image = img  # Importante manter referência
    except Exception as e:
        print(f"Erro ao carregar imagem {medalha_path}: {e}")
        tk.Label(result_window, text="[Imagem não encontrada]", bg=background_color, fg=text_color, font=(font_family, 12, "italic")).pack(pady=20)

    tk.Label(result_window, text=mensagem, bg=background_color, fg=text_color, font=(font_family, 14, "bold")).pack(pady=10)
    tk.Label(result_window, text=f"Pontuação: {score}/{len(questions)}", bg=background_color, fg=text_color, font=(font_family, 12)).pack(pady=5)
    tk.Button(result_window, text="Jogar Novamente", command=lambda: [result_window.destroy(), play_again()], bg=button_color, fg=button_text_color, font=(font_family, 12)).pack(pady=20)

# Reiniciar o jogo
def play_again():
    global score, current_question
    score = 0
    current_question = 0
    random.shuffle(questions)
    display_question()

# Função para mudar cor do botão ao passar o mouse
def on_enter(e):
    e.widget['background'] = button_hover_color

def on_leave(e):
    e.widget['background'] = button_color

# Criação da janela principal
janela = tk.Tk()
janela.title("Quiz Interativo")
janela.geometry("420x480")
janela.config(bg=background_color)

# Tela inicial
start_frame = tk.Frame(janela, bg=background_color)

logo_path = os.path.join(BASE_DIR, "logo.png")
try:
    logo_img = PhotoImage(file=logo_path)
    tk.Label(start_frame, image=logo_img, bg=background_color).pack(pady=10)
    start_frame.image = logo_img  # Mantém referência
except Exception as e:
    print(f"Erro ao carregar logo {logo_path}: {e}")
    tk.Label(start_frame, text="[Logo não encontrada]", bg=background_color, fg=text_color, font=(font_family, 14, "italic")).pack(pady=10)

tk.Label(start_frame, text="Bem-vindo ao Quiz!", font=(font_family, 18, "bold"), bg=background_color, fg=text_color).pack(pady=10)
tk.Label(start_frame, text="Clique no botão abaixo para começar.", bg=background_color, fg=text_color, font=(font_family, 12)).pack(pady=5)
start_button = tk.Button(start_frame, text="Começar Quiz", command=display_question, bg=button_color, fg=button_text_color, width=25, font=(font_family, 14, "bold"))
start_button.pack(pady=20)
start_button.bind("<Enter>", on_enter)
start_button.bind("<Leave>", on_leave)
start_frame.pack()

# Tela de perguntas
quiz_frame = tk.Frame(janela, bg=background_color)
question_label = tk.Label(quiz_frame, text="", wraplength=380, bg=background_color, fg=text_color, font=(font_family, 14, "bold"))
question_label.pack(pady=20)

timer_label = tk.Label(quiz_frame, text="", bg=background_color, fg="red", font=(font_family, 12, "bold"))
timer_label.pack(pady=10)

option1_btn = tk.Button(quiz_frame, text="", width=30, bg=button_color, fg=button_text_color, font=(font_family, 12))
option2_btn = tk.Button(quiz_frame, text="", width=30, bg=button_color, fg=button_text_color, font=(font_family, 12))
option3_btn = tk.Button(quiz_frame, text="", width=30, bg=button_color, fg=button_text_color, font=(font_family, 12))
option4_btn = tk.Button(quiz_frame, text="", width=30, bg=button_color, fg=button_text_color, font=(font_family, 12))

for btn in [option1_btn, option2_btn, option3_btn, option4_btn]:
    btn.pack(pady=5)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Iniciar interface
janela.mainloop()
