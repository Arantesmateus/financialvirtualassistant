import json
import pandas as pd
import streamlit as st
import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# --------- SETTINGS ---------
load_dotenv()
OLLAMA_URL = os.getenv('OLLAMA_URL')
MODEL = os.getenv('MODEL')

# --------- Functions ----------
def hora_atual():
  return datetime.now().strftime("%H:%M")

def load_file(file_path:str, wrap_style: bool=False):
  with open(file_path) as f:
    content = f.read()
  if wrap_style:
    content = f'<style>{content}</style>'
  st.markdown(content, unsafe_allow_html=True)

def load_promt(file_path:str):
  with open(file_path) as f:
    return f.read()


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

SYSTEM_PROMPT = load_promt('./prompts/system_prompt.txt')


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



# ----------- INTERFACE ----------
st.set_page_config(page_title="Investa", page_icon="None", layout='centered')

# ---------- Custom CSS for the chat ----------
load_file('./style.css', wrap_style = True)


# ---------- Initilize the history conversation ----------
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
    welcome = f"Olá {profile['nome']}! Sou a **Investa**, Como posso te ajudar hoje?"
    st.title(welcome)

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
    
    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    