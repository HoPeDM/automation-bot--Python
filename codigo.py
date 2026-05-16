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


link = 'file:///C:....'

pyautogui.press('win') 
pyautogui.write('Google Chrome') 
pyautogui.press('enter') 
time.sleep(2) 
pyautogui.write(link)
time.sleep(1)   
pyautogui.press('enter') 
pyautogui.click(x=99, y=299) 



import pandas

tabela = pandas.read_csv("produtos.csv", dtype=str)

print(tabela)

for linha in tabela.index:
    pyautogui.click(x=99, y=299)
    pyautogui.PAUSE = 0.1 # ESPERA 0.1 SEGUNDOS PARA O PROGAMA   

   
    #codigo
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo) # DIGITA O CODIGO DO PRODUTO
    pyautogui.press('tab') # APERTA O TAB PARA IR PARA O PROXIMO CAMPO
        
    #marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca) 
    pyautogui.press('tab') 

    #tipo
    tipo = str(tabela.loc[linha, 'tipinho'])
    pyautogui.write(tipo)
    pyautogui.press('tab') 

    #categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    #preco_unitario
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')


    custo = f"{float(tabela.loc[linha, 'custo']):.2f}" 

    pyautogui.write(custo, interval=0.1)
    pyautogui.press('tab')  

    
    obs = str(tabela.loc[linha, 'obs'])
    if obs != "nan" and obs != "None": # VERIFICA SE O CAMPO DE OBS ESTA VAZIO 
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter') 

    
    pyautogui.scroll(5000) 


   # 3. SALVAR NO BANCO DE DADOS 
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
