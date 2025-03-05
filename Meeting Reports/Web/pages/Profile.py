import streamlit as st
import streamlit_authenticator as stauth
import yaml

# Verifica autenticação
if not st.session_state.get('authentication_status'):
    st.error('You need to log in to access this page.')
    st.stop()

# Carrega o config da sessão
config = st.session_state.get('config', {})

# Obtém os dados do usuário logado
username = st.session_state.get('username')
user_data = config.get('credentials', {}).get('usernames', {}).get(username, {})
first_name = user_data.get('first_name', 'Not available')
last_name = user_data.get('last_name', 'Not available')

row = st.columns(2)
row[0].image("logo.png", width=150)

# Exibe título
st.write(f"# 👤  {first_name} {last_name}")

st.write("")
st.write("")
st.write("")

with st.container(height=140, border=True):
    st.write(f"##### • Username: <span style='font-weight:normal;'>{username}</span>", unsafe_allow_html=True)
    st.write(f"##### • First Name: <span style='font-weight:normal;'>{first_name}</span>", unsafe_allow_html=True)
    st.write(f"##### • Last Name: <span style='font-weight:normal;'>{last_name}</span>", unsafe_allow_html=True)

# Botão para abrir o modal
if st.button("Change Password 🔒"):
    st.session_state['show_password_modal'] = True

# Exibe o modal se for ativado
if st.session_state.get('show_password_modal'):
    st.markdown("## Change Your Password")
    
    # Configura autenticação
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )
    
    try:
        if authenticator.reset_password(username):
            st.success('Password changed successfully! ✅')

            # Atualiza o config.yml
            with open("config.yml", "w", encoding="utf-8") as f:
                yaml.dump(config, f, allow_unicode=True)

            # Atualiza o config na sessão
            st.session_state['config'] = config

            # Fecha o modal
            st.session_state['show_password_modal'] = False
    except Exception as e:
        st.error(f"Error: {e}")
    
    # Botão para fechar o modal
    if st.button("Cancel"):
        st.session_state['show_password_modal'] = False
        st.rerun()

# Botão para abrir modal de atualização de username
if st.button("Change Username ✏️"):
    st.session_state['show_username_modal'] = True

# Modal para atualizar o username
if st.session_state.get('show_username_modal'):
    st.markdown("## Update Your Username")

    new_username = st.text_input("New Username", key="new_username")

    # Lista todos os usernames existentes
    existing_usernames = config['credentials']['usernames'].keys()

    if st.button("Update Username"):
        if not new_username:
            st.error("Username cannot be empty.")
        elif new_username == username:
            st.error("New username cannot be the same as the current one.")
        elif new_username in existing_usernames:
            st.error("Username already exists. Please choose a different one.")
        else:
            # Atualiza o username no config
            config['credentials']['usernames'][new_username] = config['credentials']['usernames'].pop(username)
            st.session_state['username'] = new_username

            # Atualiza o arquivo config.yml
            with open("config.yml", "r", encoding="utf-8") as f:
                yaml.dump(config, f, allow_unicode=True)

            # Atualiza o config na sessão
            st.session_state['config'] = config

            st.success(f"Username updated successfully! ✅ New username: {new_username}")
            st.session_state['show_username_modal'] = False
            st.rerun()

    if st.button("Cancel"):
        st.session_state['show_username_modal'] = False
        st.rerun()

if st.button("Back"):
    st.switch_page("main.py")