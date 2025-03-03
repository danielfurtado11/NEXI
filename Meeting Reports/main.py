import os
import time
import streamlit as st
import sys

# Diretório onde estão os relatórios
pages_dir = "pages"

# Criar uma função para listar os arquivos no diretório pages/
def listar_paginas():
    return [f for f in os.listdir(pages_dir) if f.endswith(".py")]

# Armazena a lista inicial de arquivos
arquivos_atuais = set(listar_paginas())

st.title("Relatórios de Reunião 📄")

# Criar links para cada página
for page in arquivos_atuais:
    page_name = page.replace(".py", "").replace("_", " ").title()
    st.page_link(f"{pages_dir}/{page}", label=page_name)

# Verificar se há novos arquivos e reiniciar
def verificar_e_reiniciar():
    while True:
        novos_arquivos = set(listar_paginas())

        if novos_arquivos != arquivos_atuais:
            st.warning("Novos arquivos detectados! Reiniciando a aplicação...")

            # Reinicia o script principal
            python = sys.executable
            os.execl(python, python, "-m", "streamlit", "run", "main.py")

        time.sleep(2)  # Verifica mudanças a cada 2 segundos

# Iniciar monitoramento em uma thread separada
import threading
threading.Thread(target=verificar_e_reiniciar, daemon=True).start()
