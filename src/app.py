from ctypes import alignment
import json
import pandas as pd
import streamlit as st
import requests
from datetime import datetime

# --------- SETTINGS ---------
OLLAMA_URL = 'http://127.0.0.1:11434/api/generate'
MODEL = 'phi4-mini'


# --------- Load knowleadge base ---------
history = pd.read_csv('data/historico_atendimento.csv')
transactions = pd.read_csv('data/transacoes.csv')
profile = json.load(open('data/perfil_investidor.json'))
products = json.load(open('data/produtos_financeiros.json'))

# --------- Context ---------
context = f'''
    CUSTOMER: {profile['nome']}, PROFILE: {profile['idade']} anos, PROFILE {profile['perfil_investidor']}
    OBJECTIVE: {profile['objetivo_principal']}
    PATRIMONY: {profile['patrimonio_total']} | RESERVE: R$ {profile['reserva_emergencia_atual']} 

    LAST TRANSACTIONS:
    {transactions.to_string(index=False)}

    LAST ASSISTANCES:
    {history.to_string(index=False)}

    AVAILABLE PRODUCTS:
    {json.dumps(products, indent=2, ensure_ascii=False)}    
    '''

# --------- SYSTEM PROMPT ---------

SYSTEM_PROMPT = ''' 
Você é uma assistente virtual chamada Investa, você deve agir como humano então você tem um nome pessoal.

REGRAS:
- Nunca recomende investimentos específicos, apenas explique como funcionam;
- Jamais responda a perguntas fora do tema finanças pessoais. Quando ocorrer, responda lembrando o seu papel de assistente financeira
- Não responda sobre coisas fora do assunto de finanças pessoais
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 3 parágrafos.
- Sempre responda no feminino
- Seja simpática e acolhedora
- Certifique-se de que as palavras estão corretas antes de falar com o clientes
- Sempre pular uma linha quando terminar de escrever um paragrafo
'''

# --------- CALL OLLAMA ---------

def perguntar(msg):
    prompt = f'''
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {context}

    Pergunta: {msg}
    '''
    
    #---------- Run Local -------------------
    r = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt, "stream":False})
    return r.json()['response']

def hora_atual():
  return datetime.now().strftime("%H:%M")

def load_file(file_path:str, wrap_style: bool=False):
  with open(file_path) as f:
    content = f.read()
  if wrap_style:
    content = f'<style>{content}</style>'
  st.markdown(content, unsafe_allow_html=True)


# ----------- INTERFACE ----------
st.set_page_config(page_title="Investa. Sua assistente de investimentos", page_icon="💰", layout='centered')

# ---------- Custom CSS for the chat ----------
load_file('./style.css', wrap_style = True)

# --------- Custom title -------
load_file('./html/header.html')

# ---------- Initilize the history conversation ----------
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
    welcome = "Olá! Sou a **Investa**, sua assistente financeira 💚 Como posso te ajudar hoje?"
    st.session_state['messages'].append({
        'role': 'assistant',
        'content': welcome,
        'time': hora_atual()
    })

# --------- Show consersation history --------
for msg in st.session_state['messages']:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])
        st.caption(msg['time'])


# ------- User input ---------
if question := st.chat_input('Sua dúvida sobre investimentos...'):
    # Add user message to session history
    st.session_state['messages'].append({
      'role':'user', 
      'content': question, 
      'time':hora_atual()
    })
    with st.chat_message('user'):
      st.markdown(question)
      st.caption(hora_atual())

    # Add assistant message to session history
    with st.spinner('...'):
      answer = perguntar(question)
      st.session_state['messages'].append({
        'role':'assistant', 
        'content':answer, 
        'time':hora_atual()
      })
      with st.chat_message('assistant'):
        st.markdown(answer)
        st.caption(hora_atual())
    
    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    