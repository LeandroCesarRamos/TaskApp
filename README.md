## Créditos

Exemplo original retirado de [usandopy.com](https://www.usandopy.com).

# Adaptações e melhorias: por Leandro Cesar Ramos.

# 📋 TaskApp - Gerenciador de Tarefas

Um aplicativo de gerenciamento de tarefas moderno e intuitivo desenvolvido em Python com tkinter.

![Python](https://img.shields.io/badge/Python-3.13.5-blue.svg)
![tkinter](https://img.shields.io/badge/GUI-tkinter-green.svg)
![Status](https://img.shields.io/badge/Status-Completo-success.svg)

## ✨ Funcionalidades

- ✅ **Adicionar Tarefas**: Interface simples para criar novas tarefas
- 🎨 **Emojis Integrados**: Adicione emojis às suas tarefas para melhor organização
- ✔️ **Marcar como Concluída**: Sistema de checkbox para controlar o progresso
- 🗑️ **Excluir Tarefas**: Remova tarefas desnecessárias facilmente
- 🖱️ **Scroll com Mouse**: Navegue pela lista usando a roda do mouse
- ⌨️ **Acessibilidade e Atalhos de Teclado**: 
  - `Enter`: Adicionar nova tarefa ou ativar botões de editar/deletar quando focados
  - `Escape`: Limpar campo de texto
  - `Ctrl+A`: Selecionar todo o texto do campo
  - `Tab`: Navegar entre os campos e botões

## 🖼️ Screenshots

### Interface Principal
- Interface limpa e moderna
- Lista de tarefas com scroll
- Campo de entrada intuitivo
- Botões de ação bem posicionados

## 🚀 Como Executar

### Opção 1: Executável (Recomendado)
1. Baixe o arquivo `TaskApp.exe` da pasta `dist/`
2. Execute diretamente - não precisa instalar Python!
3. Caso Windows Defender acuse, pode liberar. Este procedimento é normal neste executável!

### Opção 2: Código Fonte
```bash
# Clone o repositório
git clone https://github.com/LeandroCesarRamos/TaskApp.git

# Navegue para o diretório
cd TaskApp

# Execute o aplicativo
python main.py
```

## 📁 Estrutura do Projeto

```
TaskApp/
│
├── build/                     # Arquivos de build (PyInstaller)
├── dist/                      # Executável gerado
│   └── TaskApp.exe            # Aplicativo standalone
├── LICENSE                    # Licença MIT
├── main.py                    # Código principal do aplicativo
├── main.spec                  # Configuração do aplicativo
├── README.md                  # Explicação sobre o aplicativo
├── requirements.txt           # Requerimentos do aplicativo
└── TaskApp.spec               # Configuração do PyInstaller
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.13.5**: Linguagem principal
- **tkinter**: Framework para interface gráfica
- **PyInstaller**: Para criar executável standalone

## 🌎 Internacionalização

Todos os comentários do código estão em português para facilitar o entendimento de quem está aprendendo.

## 📋 Requisitos

### Para executar o código fonte:
- Python 3.7 ou superior
- tkinter (geralmente incluído no Python)

### Para executar o executável:
- Windows (qualquer versão)
- Nenhuma instalação adicional necessária

## 🔧 Como Construir o Executável

```bash
# Instalar PyInstaller
pip install pyinstaller

# Gerar executável
pyinstaller --onefile --windowed --name main.py
```

## 🎯 Funcionalidades Futuras

- [ ] Salvar tarefas em arquivo
- [ ] Categorias de tarefas
- [ ] Data de vencimento
- [ ] Notificações
- [ ] Temas personalizáveis

## 🤝 Contribuições


## ♿ Acessibilidade

O aplicativo permite navegação completa por teclado (Tab, Enter nos botões, atalhos para ações rápidas), tornando-o mais acessível para todos os usuários.

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

