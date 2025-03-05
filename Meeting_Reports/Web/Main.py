import os
import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from utils import create_engagement_chart, create_facial_expression_chart, load_data_from_all_files


# Page config
st.set_page_config(
    page_title="NEXI Meetings",
    page_icon="https://raw.githubusercontent.com/danielfurtado11/test/main/icon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "mailto:daniel.furtado@nexi.plus", 
        "About": "This app is about personalize your focus on meetings and study!\nContact: daniel.furtado@nexi.plus to know more."
    }
)

row = st.columns(2)
row[0].image("logo.png", width=150)


# Load the config file
with open("config.yml", "r", encoding="utf-8") as f:
    config = yaml.load(f, Loader=SafeLoader)



# Save the config in the session
st.session_state['config'] = config
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)


# Login
try:
    authenticator.login()
except Exception as e:
    st.error(e)





if st.session_state.get('authentication_status'):

    # Get the data of the authenticated user
    username = st.session_state.get('username')
    user_data = config['credentials']['usernames'].get(username, {})
    first_name = user_data.get('first_name', '')
    last_name = user_data.get('last_name', '')


    col1, col2 = st.columns([7, 1]) 
    with col1:
        st.write(f"### Welcome {first_name} {last_name}! ")
    with col2:
        authenticator.logout("Logout", "main")

    st.write("\n\n\n")
    pages_dir = "pages"

    def get_reports():
        return sorted([f for f in os.listdir(pages_dir) if f.endswith(".py")])
    
    st.title("📈 Your performance:")

    dataset = "data.csv"
    name = first_name + ' ' + last_name
    average_data = load_data_from_all_files(pages_dir, name)
    st.write("\n\n\n")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if average_data is not None:
            st.plotly_chart(create_engagement_chart(average_data))
        else:
            st.warning("No data available.")
    with col3:
        if average_data is not None:
            st.plotly_chart(create_facial_expression_chart(average_data))
        else:
            st.warning("No data available.")


            
    st.write("")
    st.write("")
    st.write("")
    
    st.title("📄 Meeting Reports:")

    reports = get_reports()

    if not reports:
        st.warning("No reports available.")


    # List the available reports
    for report in reports:
        page_name = report.replace(".py", "").replace("_", " ").title()
        if page_name != "Profile":
            st.page_link(f"{pages_dir}/{report}", label=page_name)


    # Reload the page if new reports are detected
    if set(get_reports()) != set(reports):
        st.rerun() 




# Authentication status when the user fails to authenticate
elif st.session_state.get('authentication_status') is False:
    st.error('Username or password incorrects. Try again.')
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] {display: none;}
        </style>
        """,
        unsafe_allow_html=True
    )
    if 'show_forgot_password' not in st.session_state:
        st.session_state['show_forgot_password'] = False

    if not st.session_state['show_forgot_password']:
        if st.button('Forgot the password 🔐'):
            st.session_state['show_forgot_password'] = True
            st.rerun()
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            try:
                username_of_forgotten_password, _, new_random_password = authenticator.forgot_password()
                if username_of_forgotten_password:
                    st.success('A new password was created.\nPlease, change your password after login.')
                    st.write(f"**Username:** {username_of_forgotten_password}")
                    st.write(f"**New password:** `{new_random_password}`")
                    with open("config.yml", "w", encoding="utf-8") as f:
                        yaml.dump(config, f, allow_unicode=True)
                elif username_of_forgotten_password is False:
                    st.error('User not found.')
            except Exception as e:
                st.error(e)


# Authentication status when the user has not yet authenticated
elif st.session_state.get('authentication_status') is None:
    st.warning('Please, enter your credentials to access the app.')
    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] {display: none;}
        </style>
        """,
        unsafe_allow_html=True
    )