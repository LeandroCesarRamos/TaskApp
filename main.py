# 1. Importações
import tkinter as tk
from tkinter import ttk, font, messagebox

# 2. Definição das funções
def add_task(): # Função para adicionar uma nova tarefa
    global frame_in_editing # Frame da tarefa em edição
    task = entry_task.get().strip() # Obtém o texto do campo de entrada e remove espaços em branco no início/fim
    if task and task != "✍️ Write your task here...": # Verifica se a tarefa não está vazia ou se não é o texto do placeholder
       if frame_in_editing is not None: # Se estamos editando uma tarefa, atualiza
           update_task(task) # Atualiza a tarefa em edição
           frame_in_editing = None # Redefine o frame de edição
       else: # Se estamos adicionando uma nova tarefa, crie
           add_item_task(task) # Adiciona a nova tarefa
           entry_task.delete(0, tk.END) # Limpa o campo de entrada
    else: # Se a tarefa estiver vazia, mostra uma mensagem de aviso
        messagebox.showwarning("❌Warning❌", "❗Please enter a task❗")

def delete_task(frame_task): # Função para excluir uma tarefa
    frame_task.destroy() # Destroi o frame da tarefa
    canvas.update_idletasks() # Atualiza as tarefas pendentes
    canvas.configure(scrollregion=canvas.bbox("all")) # Atualiza a região de rolagem

def prepare_editing(frame_task, label_task): # Função para preparar a edição de uma tarefa
    global frame_in_editing # Frame da tarefa em edição
    frame_in_editing = frame_task # Armazena o frame da tarefa em edição
    entry_task.delete(0, tk.END) # Limpa o campo de entrada
    entry_task.insert(0, label_task.cget("text")) # Insere o texto atual da tarefa

def update_task(new_task): # Função para atualizar uma tarefa
    global frame_in_editing # Frame da tarefa em edição
    for widget in frame_in_editing.winfo_children(): # Itera sobre os widgets "children" do frame em edição
        if isinstance(widget, tk.Label): # Verifica se o widget é um label (rótulo)
            widget.config(text=new_task) # Atualiza o texto do label (rótulo)
            break # Interrompe o loop após atualizar a tarefa

def toggle_underline(label): # Função para alternar sublinhado
    current_font = label.cget("font") # Obtém a fonte atual do label (rótulo)
    if isinstance(current_font, tuple): # Verifica se a fonte é uma tupla
        font_family, font_size = current_font[0], current_font[1] # Obtém a família e o tamanho da fonte
        current_font = f"{font_family} {font_size}" # Converte a fonte para string

    # Alterna "overstrike" (riscado) (strikethrough)
    if "overstrike" in str(current_font): # Verifica se o texto "overstrike" (riscado) está na fonte
        new_font = str(current_font).replace(" overstrike", "") # Remove o "overstrike"
    else: # Se "overstrike" (riscado) não estiver na fonte
        new_font = str(current_font) + " overstrike" # Adiciona o "overstrike" (riscado)

    label.config(font=new_font) # Atualiza a fonte do label (rótulo)

def clear_entry(): # Função para limpar o campo de entrada
    """Clear the entry field and restore placeholder if empty"""
    entry_task.delete(0, tk.END) # Limpa o campo de entrada
    return "break"  # Previne o comportamento padrão

def select_all_text(): # Função para selecionar todo o texto
    """Select all text in the entry field"""
    entry_task.select_range(0, tk.END) # Seleciona todo o texto no campo de entrada
    return "break"  # Previne o comportamento padrão

def focus_entry(): # Função para focar no campo de entrada
    """Focus on the entry field and clear placeholder if present"""
    entry_task.focus_set() # Define o foco no campo de entrada
    if entry_task.get() == "✍️ Write your task here...":
        entry_task.delete(0, tk.END) # Limpa o campo de entrada
        entry_task.config(fg="black") # Altera a cor do texto para preto

def show_help(): # Função para mostrar ajuda
    """Show keyboard shortcuts help"""
    help_text = """🎯 Keyboard Shortcuts:

📝 Input Field:
• Enter - Add task
• Escape - Clear field
• Ctrl+A - Select all

🌍 Global:
• Ctrl+N - New task (focus on entry field)
• Ctrl+Q - Quit application
• F1 - Show this help

💡 Tip: Use Tab to navigate between elements!"""

    messagebox.showinfo("📚 Help - Keyboard Shortcuts", help_text)

def setup_global_shortcuts(): # Função para configurar atalhos de teclado globais
    """Setup global keyboard shortcuts for the entire application"""
    # Ctrl+N para nova tarefa (focar no campo de entrada)
    window.bind("<Control-n>", lambda event: focus_entry()) # Foca no campo de entrada
    # Ctrl+Q para sair da aplicação
    window.bind("<Control-q>", lambda event: window.quit()) # Sai da aplicação
    # F1 para ajuda/sobre
    window.bind("<F1>", lambda event: show_help()) # Mostra a ajuda

# 3. Configuração da janela principal
window = tk.Tk() # Cria a janela principal
window.title("Task Application") # Define o título da janela
window.configure(bg="#5B5656") # Define a cor de fundo da janela
window.geometry("500x600") # Define o tamanho da janela

# 4. Criação dos frames e widgets
# Cabeçalho
font_header = font.Font(family="Helvetica", size=24, weight="bold") # Define a fonte do cabeçalho
label_header = tk.Label(window, text="📝 Task Application", font=font_header, bg="#5B5656", fg="white") # Cria o label (rótulo) do cabeçalho
label_header.pack(pady=20) # Adiciona o label (rótulo) ao layout

# Frame de entrada e botão
frame = tk.Frame(window, bg="#5B5656") # Cria o frame para o campo de entrada e o botão
frame.pack(side=tk.TOP, anchor=tk.W, pady=10) # Adiciona o frame ao layout

entry_task = tk.Entry(frame, font=("Helvetica", 14), relief=tk.FLAT, bg="white", fg="grey", width=30) # Cria o campo de entrada
entry_task.pack(side=tk.LEFT, padx=10) # Adiciona o campo de entrada ao layout

# Adiciona texto de placeholder ao campo de entrada
entry_task.insert(0, "✍️ Write your task here...") # Adiciona o texto de placeholder

# Adiciona manipuladores de eventos para o texto de placeholder
def on_entry_click(event): # Quando o campo de entrada é clicado
    if entry_task.get() == "✍️ Write your task here...": # Verifica se o texto é o placeholder
        entry_task.delete(0, tk.END) # Limpa o campo de entrada
        entry_task.config(fg="black") # Altera a cor do texto para preto

def on_focus_out(event): # Quando o campo de entrada perde o foco
    if entry_task.get() == "": # Verifica se o campo está vazio
        entry_task.insert(0, "✍️ Write your task here...") # Adiciona o texto de placeholder
        entry_task.config(fg="grey") # Altera a cor do texto para cinza

# Bind (liga) os eventos ao campo de entrada
entry_task.bind("<FocusIn>", on_entry_click) # Quando o campo de entrada é clicado
entry_task.bind("<FocusOut>", on_focus_out) # Quando o campo de entrada perde o foco
# bind (liga) à tecla Enter para adicionar tarefa
entry_task.bind("<Return>", lambda event: add_task()) # Quando a tecla Enter é pressionada
# bind (liga) à tecla Escape para limpar o campo de entrada
entry_task.bind("<Escape>", lambda event: clear_entry()) # Quando a tecla Escape é pressionada
# bind (liga) Ctrl+A para selecionar todo o texto
entry_task.bind("<Control-a>", lambda event: select_all_text()) # Quando Ctrl+A é pressionado

# Adiciona o botão "➕ Add Task" à interface
button_add = tk.Button(frame, text="➕ Add Task", font=("Roboto", 11), bg="#4CAF50", fg="white", height=1, width=15, relief=tk.RIDGE, command=add_task) # Botão para adicionar tarefa
button_add.pack(side=tk.LEFT, padx=10) # Adiciona o botão ao layout
# Bind (liga) o botão à tecla Enter
button_add.bind('<Return>', lambda event: add_task()) # Quando a tecla Enter é pressionada

# Para o próximo passo, criaremos um frame com tarefas roláveis
frame_tasks = tk.Frame(window, bg="#FFFFFF") # Frame para as tarefas
# coloca o frame na parte superior da janela e permite que ele preencha o espaço disponível
frame_tasks.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 0)) # Adiciona o frame ao layout

# Agora, criaremos um canvas dentro do frame para conter as tarefas
canvas = tk.Canvas(frame_tasks, bg="#FFFEFE") # Canvas para as tarefas
# define o canvas para preencher o frame e expandir para se ajustar à janela
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) # Adiciona o canvas ao layout

# Cria uma scrollbar (barra de rolagem) vertical para o canvas
vertical_scrollbar = ttk.Scrollbar(frame_tasks, orient="vertical", command=canvas.yview) # Barra de rolagem vertical
# e define a scrollbar (barra de rolagem) para preencher o lado direito do frame
vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # Adiciona a barra de rolagem vertical ao layout

# Cria uma scrollbar (barra de rolagem) horizontal para o canvas (anexada à janela principal)
horizontal_scrollbar = ttk.Scrollbar(window, orient="horizontal", command=canvas.xview) # Barra de rolagem horizontal
# e define a scrollbar (barra de rolagem) para preencher a parte inferior de toda a janela
horizontal_scrollbar.pack(side=tk.BOTTOM, fill=tk.X) # Adiciona a barra de rolagem horizontal ao layout

# Configura o canvas para trabalhar com ambas as barras de rolagem
canvas.configure(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set) # Configura o canvas para trabalhar com ambas as barras de rolagem
# cria um frame dentro do canvas para segurar as tarefas
canvas_interior = tk.Frame(canvas, bg="#FFFEFE") # Frame interior do canvas
# define o canvas para rolar o frame interior
canvas.create_window((0, 0), window=canvas_interior, anchor="nw") # Cria uma janela no canvas para o frame interior
# bind (liga) o canvas à barra de rolagem para permitir a rolagem
canvas_interior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))) # Liga o canvas à barra de rolagem

# Adiciona funcionalidade de rolagem com o scroll (roda) do mouse
def on_mouse_wheel(event): # Função para rolagem com o mouse
    """Handle mouse wheel scrolling for vertical movement"""
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units") # Rola o canvas na direção vertical

# Bind (liga) os eventos do mouse wheel (roda do mouse) para canvas
canvas.bind("<MouseWheel>", on_mouse_wheel)  # Windows
canvas.bind("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # Linux scroll up
canvas.bind("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))   # Linux scroll down

# bind (liga) o canvas_interior para que a rolagem funcione em qualquer lugar na área da tarefa
canvas_interior.bind("<MouseWheel>", on_mouse_wheel)  # Windows
canvas_interior.bind("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # Linux scroll up
canvas_interior.bind("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))   # Linux scroll down


frame_in_editing = None # Variável global para segurar o frame sendo editado

# Função para adicionar tarefas
def add_task(): # Função para adicionar tarefas
    global frame_in_editing # Variável global para segurar o frame sendo editado
    task = entry_task.get().strip() # Obter o texto do campo de entrada e remover espaços em branco
    if task and task != "✍️ Write your task here...": # Verificar se a tarefa não está vazia ou é o texto de espaço reservado
       if frame_in_editing is not None: # Se estamos editando uma tarefa, atualizá-la
           update_task(task) # Atualiza a tarefa existente
           frame_in_editing = None # Resetar o frame de edição
       else: # Se estamos adicionando uma nova tarefa, criá-la
           add_item_task(task) # Adiciona a nova tarefa
           entry_task.delete(0, tk.END) # Limpar o campo de entrada
    else: # Se a tarefa estiver vazia, mostrar uma mensagem de aviso
        messagebox.showwarning("❌Warning❌", "❗Please enter a task❗")

# Função para adicionar um item à lista de tarefas
def add_item_task(task): # Função para adicionar um item à lista de tarefas
        # Criar um frame para cada tarefa
        task_frame = tk.Frame(canvas_interior, bg="#FFFEFE", relief=tk.SUNKEN, bd=1) # Frame da tarefa
        task_frame.pack(fill=tk.X, padx=5, pady=5) # Adiciona o frame da tarefa ao canvas interior

        # Criar um label (rótulo) para a tarefa
        task_label = tk.Label(task_frame, text=task, font=("Garamond", 16), bg="#FFFEFE", anchor="w") # Label (rótulo) da tarefa
        task_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=5) # Adiciona o label (rótulo) da tarefa ao frame da tarefa

        # Adicionar um botão de edição com símbolo Unicode
        edit_button = tk.Button(task_frame, text="🖌 Editar", # Botão de edição
                               command=lambda f=task_frame, l=task_label: prepare_editing(f, l), # Prepara a edição da tarefa
                               bg="#FFA500", fg="white", relief=tk.RAISED, font=("Arial", 9), width=8) # Botão de edição
        # e colocar o botão no frame, para que apareça ao lado do campo de entrada
        edit_button.pack(side=tk.RIGHT, padx=2, pady=5) # Adiciona o botão de edição ao frame da tarefa
        # bind (ligar) o botão à tecla Editar
        edit_button.bind('<Return>', lambda event, f=task_frame, l=task_label: prepare_editing(f, l)) # Prepara a edição da tarefa

        # Adicionar um botão de exclusão com símbolo Unicode
        delete_button = tk.Button(task_frame, text="🗑️ Del", # Botão de exclusão
                                 command=lambda f=task_frame: delete_task(f), # Prepara a exclusão da tarefa
                                 bg="#FF4444", fg="white", relief=tk.RAISED, font=("Arial", 9), width=8) # Botão de exclusão
        # e colocar o botão no frame, para que apareça ao lado do campo de entrada
        delete_button.pack(side=tk.RIGHT, padx=2, pady=5) # Adiciona o botão de exclusão ao frame da tarefa
        delete_button.bind('<Return>', lambda event, f=task_frame: delete_task(f)) # Prepara a exclusão da tarefa

        # Adicionar o botão de verificação ao item da tarefa
        check_button = ttk.Checkbutton(task_frame, command=lambda label=task_label: toggle_underline(label)) # Botão de verificação
        check_button.pack(side=tk.RIGHT, padx=5) # Adiciona o botão de verificação ao frame da tarefa

        # Habilitar o scroll do mouse no frame da tarefa e seus "children"
        def bind_mouse_wheel_to_widget(widget): # Função para habilitar o scroll do mouse
            """Bind mouse wheel events to a widget and all its children"""
            widget.bind("<MouseWheel>", on_mouse_wheel)  # Windows
            widget.bind("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # Linux scroll up
            widget.bind("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))   # Linux scroll down

            # Recursivamente bind (ligar) a todos os widgets "children"
            for child in widget.winfo_children(): # Habilitar o scroll do mouse em todos os "children"
                bind_mouse_wheel_to_widget(child) # Recursão para "children"

        # Habilitar o scroll do mouse no frame da tarefa
        bind_mouse_wheel_to_widget(task_frame)

        # Atualizar a região de scroll
        canvas.update_idletasks() # Atualiza as tarefas pendentes
        canvas.configure(scrollregion=canvas.bbox("all")) # Atualiza a região de scroll

# Função para preparar a edição de uma tarefa e seu campo de entrada
def prepare_editing(frame_task, label_task): # Função para preparar a edição de uma tarefa
    global frame_in_editing # Frame que está sendo editado
    frame_in_editing = frame_task # Frame que está sendo editado
    entry_task.delete(0, tk.END) # Limpa o campo de entrada
    entry_task.insert(0, label_task.cget("text")) # Insere o texto da tarefa atual

# Função para atualizar uma tarefa durante a edição e seu campo de entrada
def update_task(new_task): # Função para atualizar uma tarefa durante a edição
    global frame_in_editing # Frame que está sendo editado
    # Encontrar a label (rótulo) no frame e atualizar seu texto
    for widget in frame_in_editing.winfo_children(): # Itera sobre todos os widgets "children" do frame
        if isinstance(widget, tk.Label): # Verifica se o widget é um label (rótulo)
            widget.config(text=new_task) # Atualiza o texto do label (rótulo)
            break # Interrompe o loop após encontrar o label (rótulo)

# Função para excluir uma tarefa e seu frame
def delete_task(frame_task): # Função para excluir uma tarefa
    # Destruir o frame da tarefa
    frame_task.destroy() # Destrói o frame da tarefa
    # Atualizar a região de scroll
    canvas.update_idletasks() # Atualiza as tarefas pendentes
    canvas.configure(scrollregion=canvas.bbox("all")) # Atualiza a região de scroll

# Função para alternar o sublinhado para tarefas concluídas e seu estado
def toggle_underline(label): # Função para alternar o sublinhado para tarefas concluídas
    current_font = label.cget("font") # Obtém a fonte atual do label (rótulo)
    # Converter a fonte para string se for uma tupla
    if isinstance(current_font, tuple): # Verifica se a fonte é uma tupla
        font_family, font_size = current_font[0], current_font[1] # Obtém a família e o tamanho da fonte
        current_font = f"{font_family} {font_size}" # Converte a fonte para string

    # Alternar "overstrike" (riscado) (strikethrough)
    if "overstrike" in str(current_font): # Verifica se "overstrike" (riscado) está na fonte atual
        new_font = str(current_font).replace(" overstrike", "") # Remove o "overstrike" (riscado)
    else: # Adiciona o "overstrike" (riscado)
        new_font = str(current_font) + " overstrike" # Adiciona o "overstrike" (riscado)

    label.config(font=new_font) # Atualiza a fonte do label (rótulo)


# 5. Configuração dos atalhos e binds
setup_global_shortcuts() # Configura os atalhos globais
# ...outros binds...

# 6. Início do loop principal
window.mainloop() # Inicia o loop principal da interface gráfica