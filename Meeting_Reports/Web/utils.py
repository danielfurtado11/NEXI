import pandas as pd
import plotly.graph_objects as go
import os
import streamlit as st

def load_data(file):
    file_path = file
    df = pd.read_csv(file_path)
    return df

def filter_by_person(df, person_id):
    return df[df['person'] == person_id]

def create_engagement_chart(df):
    mean_engagement = df['engagement'].mean()  ### ALTERAR PARA ENGAGEMENT
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=mean_engagement,
        gauge={'axis': {'range': [0, 1]}}
    ))
    fig.update_layout(
        title="Avarege Engagement",
        title_x=0.36,
        title_font=dict(size=24)
    )
    return fig

def create_facial_expression_chart(df):

    if df.empty or 'facial_expression' not in df.columns:
        st.warning("No facial expression data available.")
        return go.Figure()  # retorna um gráfico vazio para evitar erros
    
    expression_counts = df['facial_expression'].value_counts()
    
    if expression_counts.empty:
        st.warning("No facial expressions detected.")
        return go.Figure()

    predominant_expression = expression_counts.idxmax()
    
    fig = go.Figure(go.Pie(
        labels=expression_counts.index,
        values=expression_counts.values,
        hole=0.4
    ))
    
    fig.add_annotation(
        text=f"{predominant_expression}",
        x=0.5, y=0.5,
        showarrow=False,
        font=dict(size=20)
    )
    fig.update_layout(
        title="Facial Expression Distribution",
        title_x=0.36,
        title_font=dict(size=24)
    )
    return fig



def load_data_from_all_files(pages_dir, person_id):
    all_data = []

    for root, dirs, _ in os.walk(pages_dir):
        if "Files" in dirs:
            file_path = os.path.join(root, "Files", "data_final.csv")
            if os.path.exists(file_path):
                df = load_data(file_path)
                filtered_df = filter_by_person(df, person_id)
                all_data.append(filtered_df)
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        return combined_df
    else:
        return None

