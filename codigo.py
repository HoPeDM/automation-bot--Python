import pyautogui
import time 
import sqlite3
conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    codigo TEXT,
    marca TEXT,
    tipinho TEXT,
    categoria TEXT,
    preco_unitario TEXT,
    custo TEXT,
    obs TEXT
)
               ''')

# PASSO A PASSO DO SEU PROGAMA
# PASSO 1: ENTRAR NO SISTEMA DA EMPRESA
#PASSO 2 : FAZER O LOGIN
#PASSO 3: ABRIR A BASE DE DADOS 
#PASSO 4: CADASTRAR 1 PRODUTO
#PASSO 5: REPETIR O PASSO 4 ATE ACABAR A LISTA
link = 'file:///C:/Users/pablo/Downloads/estudo/pasta.py/.vscode/site.html?'
# pip install pyautogui
pyautogui.press('win') # ABRE O MENU INICIAR
pyautogui.write('Google Chrome') # DIGITA CHROME
pyautogui.press('enter') # ABRE O CHROME
time.sleep(2) # ESPERA 2 SEGUNDOS PARA O CHROME ABRIR
pyautogui.write(link)
time.sleep(1)   
pyautogui.press('enter') # ABRE O LINK
pyautogui.click(x=99, y=299) # CLICA NO CAMPO DE USUÁRIO


#PASSO 3: ABRIR A BASE DE DADOS 
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv", dtype=str)
 # LÊ A BASE DE DADOS
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=99, y=299)
    pyautogui.PAUSE = 0.1 # ESPERA 0.1 SEGUNDOS PARA O PROGAMA   

    # PASSO 4: CADASTRAR 1 PRODUTO
    #codigo
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo) # DIGITA O CODIGO DO PRODUTO
    pyautogui.press('tab') # APERTA O TAB PARA IR PARA O PROXIMO CAMPO
        
    #marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca) # DIGITA A MARCA DO PRODUTO
    pyautogui.press('tab') 

    #tipo
    tipo = str(tabela.loc[linha, 'tipinho'])
    pyautogui.write(tipo) # DIGITA O TIPO DO PRODUTO
    pyautogui.press('tab') 

    #categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    #preco_unitario
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')

    #custo
    custo = f"{float(tabela.loc[linha, 'custo']):.2f}" 
#tabela.loc[linha, 'custo']: Pega o valor bruto que está na célula da coluna "custo".
# float(...): Força esse valor a ser um número decimal. Isso é fundamental para remover a notação científica (o problema da letra 'e'). Se o valor for 1e+02, o float entende que é 100.0.
# f"...": É uma f-string. Ela permite colocar variáveis e comandos dentro de um texto usando as chaves { }.
# :.2f: É a instrução de formatação:
# : indica que vai começar uma regra.
# .2 diz que você quer 2 casas decimais.
# f diz que o número é um float (decimal)
    pyautogui.write(custo, interval=0.1)
    pyautogui.press('tab')  

    #obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != "nan" and obs != "None": # VERIFICA SE O CAMPO DE OBS ESTA VAZIO 
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter') # APERTA O ENTER PARA CADASTRAR O PRODUTO

    #voltar para o inicio do cadastro
    pyautogui.scroll(5000) # SCROLL PARA VOLTAR PARA O INICIO DO CADASTRO 


   # 3. SALVAR NO BANCO DE DADOS (Aqui entra o comando das interrogações)
    # Isso salva a linha atual que o robô acabou de digitar
    cursor.execute('''
    INSERT INTO produtos (codigo, marca, tipinho, categoria, preco_unitario, custo, obs)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (codigo, marca, tipo, categoria, preco, custo, obs))

     # IMPORTANTE: Salva as alterações no arquivo a cada produto cadastrado
    conn.commit()

# --- PASSO 4: FECHAR CONEXÃO (Depois que o loop acabar) ---
conn.close()
print("Automação finalizada e dados salvos no SQLite!")