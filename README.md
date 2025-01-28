# SmartClick - Auto Clicker Personalizado

**SmartClick** é uma aplicação simples e eficiente para automação de cliques, desenvolvida com Python e PyAutoGUI. Ele permite que o usuário grave coordenadas específicas na tela e automatize cliques nessas posições repetidamente. Ideal para tarefas repetitivas que envolvem cliques em áreas específicas.

## 🛠️ Funcionalidades

- Gravação de coordenadas do mouse (para dois pontos: "Lead" e "Concluir").
- Execução de cliques automáticos com intervalo ajustável.
- Interface gráfica simples e amigável, feita com **Tkinter**.
- Atalho global (`F5`) para parar o Auto-Click a qualquer momento.
- Design com tema escuro e marca d'água personalizada (*StuartCripto*).

---

## 📥 Como usar

### 1. **Baixar e Executar o Arquivo**
- Baixe o executável mais recente da aba **Releases** aqui no GitHub.
- Extraia o arquivo `.zip` e clique duas vezes no arquivo `SmartClick.exe` para iniciar o programa.

### 2. **Gravar Coordenadas**
- Após abrir o programa:
  1. Clique no botão **Gravar Coordenadas**.
  2. Posicione o mouse sobre o **local do lead** e pressione **ENTER**.
  3. Posicione o mouse sobre o **botão Concluir** e pressione **ENTER**.
  4. As coordenadas serão salvas automaticamente.

### 3. **Iniciar o Auto-Click**
- Clique em **Iniciar Auto-Click** para começar a automação.
- O programa irá clicar automaticamente nas posições gravadas.

### 4. **Parar o Auto-Click**
- Pressione a tecla **F5** ou clique no botão **Parar Auto-Click** na interface.

---

## 💻 Requisitos

- **Sistema Operacional**: Windows 10 ou superior.
- **Python** (se estiver rodando o script, não o `.exe`):
  - Python 3.7 ou superior.
  - Bibliotecas: `pyautogui`, `keyboard`, `tkinter`.

> Obs: O executável (.exe) não requer instalação do Python no computador.

---

## 🛠️ Como Construir o Executável (Opcional)

Se você deseja rodar ou modificar o código Python e criar seu próprio `.exe`, siga as etapas abaixo:

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/SmartClick.git
   cd SmartClick
📜 Licença
Este projeto está licenciado sob a MIT License.
