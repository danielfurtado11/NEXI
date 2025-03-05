import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os


def format_time(hour, minute):
    if (minute < 60):
        return f"{hour:02d}:{minute:02d}"
    else:
        return f"{hour+1:02d}:{minute-60:02d}"
def read_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return None
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

## VARIABLES NEED TO UPDATE MANUALLY ##
start_hour, start_minute = 17, 1

st.set_page_config(page_title="Meeting Analysis", layout="wide")

row = st.columns(2)
row[0].image("logo.png", width=150)

st.write("")
st.write("")
st.write("")


##  -------------------  INFO & GOALS -------------------

file = "pages/Reuniao_27_02_2025/Files/info_&_goals.json"

with open(file, "r", encoding="utf-8") as f:
    info_data = json.load(f)

participants = ", ".join(info_data["participants"])
end_time = format_time(start_hour, start_minute + info_data['duration'])
duration = f"{start_hour}:0{start_minute} - {end_time} ({info_data['duration']} minutes)"

st.title("📊 Meeting Analysis (27-02-2025)")
st.write("")
st.write(f"##### Participants: <span style='font-weight:normal;'>{participants}.</span>", unsafe_allow_html=True)
st.write(f"##### Duration: <span style='font-weight:normal;'>{duration}</span>", unsafe_allow_html=True)
st.write("")


st.header("🎯 Goals", divider="gray")

for goal in info_data["goals"]:
    st.write(f"###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ {goal['goal']}", unsafe_allow_html=True)
    st.write(f"###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✔️ Objective Achieved: <span style='font-weight:normal;'>{goal['status']}</span>", unsafe_allow_html=True)
    st.write("")


st.write("")
st.write("")
st.write("")


##  -------------------  EVALUATION  -------------------

file = "pages/Reuniao_27_02_2025/Files/evaluation.json"
with open(file, "r", encoding="utf-8") as f:
     evaluation_data = json.load(f)

overall_score = evaluation_data["evaluation"]["overall_score"]

st.header("📊 Evaluation", divider="gray")
st.write(f"#### Meeting Effectiveness Rating: {overall_score}/100")
st.write("###### Evaluation Criteria:")

table_data = {
    "Criteria": [crit["criterion"] for crit in evaluation_data["evaluation"]["criteria"]],
    "Weight (%)": [crit["weight"] for crit in evaluation_data["evaluation"]["criteria"]],
    "Score (0-100)": [crit["score"] for crit in evaluation_data["evaluation"]["criteria"]],
    "Justification": [crit["justification"] for crit in evaluation_data["evaluation"]["criteria"]],
}
table_df = pd.DataFrame(table_data)
st.dataframe(table_df) 

# Strong Points
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Strengths:")
for strength in evaluation_data["evaluation"]["strengths"]:
    st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - {strength}")

# Improvement Points
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ Areas for Improvement:")
for improvement in evaluation_data["evaluation"]["areas_for_improvement"]:
    st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - {improvement}")



##  -------------------  THEMES  -------------------

st.header("📅 Topics Covered", divider="gray")

file = "pages/Reuniao_27_02_2025/Files/themes.json"

with open(file, "r", encoding="utf-8") as f:
    themes_data = json.load(f)

for item in themes_data:
        start_time = format_time(start_hour, start_minute + item['minute_start'])
        end_time = format_time(start_hour, start_minute + item['minute_end'])
        st.write(f"##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 {item['topic']} <span style='font-weight:normal;'>({start_time} - {end_time})</span>", unsafe_allow_html=True)
        formatted_points = "".join([f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- {point}<br>" for point in item['subtopics']])
        st.write(f"""
            {formatted_points}
        """, unsafe_allow_html=True)


##  -------------------  SUMMARY  -------------------

st.header("📝 Summary",divider="gray")

summary = read_file('pages/Reuniao_27_02_2025/Files/summary.txt')

st.text = summary

with st.container(height=500, border=True):
    st.write(st.text)

st.write("")
st.write("")
st.write("")


##  -------------------  HIGHLIGHTS & NEXT STEPS  -------------------

file = "pages/Reuniao_27_02_2025/Files/highlights_&_next_steps.json"

with open(file, "r", encoding="utf-8") as f:
     highlights_file = json.load(f)

highlights = highlights_file['highlights'] 
next_steps = highlights_file['next_steps']

st.header("✅ Highlights", divider="gray")
for item in highlights:
    st.write(f"###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 <span style='font-weight:normal;'>{item}</span>", unsafe_allow_html=True)
st.write("\n\n\n")


st.header("👣 Next Steps", divider="gray")
for item in next_steps:
         st.write(f" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 {item}")
st.write("\n\n\n")


##  -------------------  ASSIGNED TASKS  -------------------

st.header("✍🏻 Assigned Tasks", divider="gray")

file = "pages/Reuniao_27_02_2025/Files/tasks.json"
with open(file, "r", encoding="utf-8") as f:
     tasks_file = json.load(f)

tasks = {person["name"]: person["assigned_tasks"] for person in tasks_file["tasks"]}

st.write("\n\n\n")

selected_people = []
for person in tasks.keys():
    if st.checkbox(person, value=True):  # Começa marcado por padrão
        selected_people.append(person)

for person in selected_people:
    st.write(f"#### {person}")
    for task in tasks[person]:
        st.write(f" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ {task}")


##  -------------------  RELEVANT QUESTIONS  -------------------

st.header("❔ Relevant Questions", divider="gray")

file = "pages/Reuniao_27_02_2025/Files/questions.json"  # Substitua pelo nome correto do ficheiro
with open(file, "r", encoding="utf-8") as f:
    questions_file = json.load(f)

for person in questions_file["questions"]:
    name = person["name"]
    for qa in person["questions_and_answers"]:
        question = qa["question"]
        answer = qa["answer"]

        st.write(f"###### 🔸 {question} <span style='font-weight:normal;'>({name})</span>", unsafe_allow_html=True)
        st.write(f"###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Answer: <span style='font-weight:normal;'>{answer}</span>", unsafe_allow_html=True)
        st.write("\n")   


##  -------------------  MEETING FEEDBACK  -------------------

st.header("🫡 Meeting Feedback", divider="gray")

file = "pages/Reuniao_27_02_2025/Files/feedback.json"  # Substitua pelo nome correto do ficheiro
with open(file, "r", encoding="utf-8") as f:
    feedback_file = json.load(f)

for person in feedback_file["feedback"]:
    name = person["name"]
    postive = person["positive_aspects"]
    improvement = person["improvement_aspects"]

    # Exibir nome da pessoa
    st.write(f"### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{name}")

    # Exibir aspetos positivos
    st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Positive Aspects:")
    for asp in postive:
        st.write(f" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - {asp}")

    # Exibir aspetos a melhorar
    st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ Areas for Improvement:")
    for asp in improvement:
        st.write(f" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - {asp}")

    st.write("\n")  # Espaçamento entre participantes



topics = {
    "Global": None,
    "Data Cataloging and Thesis Guidance": ("00:03", "00:12"),
    "Project Development and Data Sets": ("00:12", "00:20"),
    "Professor Engagement and Thesis Support": ("00:20", "00:30"),
    "Technical Implementation of the Project": ("00:30", "00:40"),
    "Meeting Logistics and Future Planning": ("00:40", "00:50"),
    "Celebration of Milestones": ("00:50", "01:00"),
}




st.header("📈 Engagement", divider="gray")

data = pd.read_csv("pages/Reuniao_27_02_2025/Files/data_final.csv")
data["datetime"] = pd.to_datetime(data["datetime"])

time_adjust = "1min" 


plot_data = []

data_global = data.set_index('datetime').resample(time_adjust)["engagement"].mean().reset_index()
data_global['person'] = 'Média Global' 


selected_topic = st.selectbox("🔍 Filtrar Tema:", list(topics.keys(),), key="engagement")
if selected_topic != "Global":
    start_time, end_time = topics[selected_topic]
    mask_time = (data['datetime'].dt.strftime("%H:%M") >= start_time) & (data['datetime'].dt.strftime("%H:%M") <= end_time)
    mask_time1 = (data_global['datetime'].dt.strftime("%H:%M") >= start_time) & (data_global['datetime'].dt.strftime("%H:%M") <= end_time)
    data_filtered = data[mask_time]
    data_filtered_global = data_global[mask_time1]
else:
    data_filtered = data
    data_filtered_global = data_global



for person in data['person'].unique():
    data_person = data_filtered[data_filtered['person'] == person].set_index('datetime')
    grouped_data = data_person["engagement"].resample(time_adjust).mean().reset_index()
    grouped_data['person'] = f'{person}'
    plot_data.append(grouped_data)


plot_data.append(data_filtered_global)
plot_df = pd.concat(plot_data)

fig = px.line(
    plot_df, 
    x="datetime", 
    y="engagement", 
    color="person",
    title="Engagement ao Longo do Tempo",
    labels={"datetime": "Tempo", "engagement": "Engagement (%)", "person": "Participantes"},
    template="plotly_white",
    line_dash="person",
    line_group="person",
    line_dash_map={"Média Global": "dash", "André Neiva": "solid", "Daniel Furtado": "solid", "Francisco Falcão": "solid", "Diogo Feio": "solid"},
    range_y=[0, 1]
)

st.plotly_chart(fig, use_container_width=True)


st.write("")
st.write("")
st.write("")


st.header("🎭 Expressão Facial", divider="gray")

time_adjust = '1 min'



people_list = data['person'].unique()
people_list = ["Global"] + list(people_list)

selected_topic = st.selectbox("🔍 Filtrar por Tema:", list(topics.keys()), key="facial_expression")
selected_person = st.selectbox("👤 Filtrar por Pessoa:", people_list)

if selected_topic != "Global":
    start_time, end_time = topics[selected_topic]
    mask_time = (data['datetime'].dt.strftime("%H:%M") >= start_time) & (data['datetime'].dt.strftime("%H:%M") <= end_time)
    data_filtered = data[mask_time]
else:
    data_filtered = data

if selected_person != "Global":
    data_filtered = data_filtered[data_filtered['person'] == selected_person]

expression_counts = data_filtered.groupby(
    [pd.Grouper(key='datetime', freq=time_adjust), 'facial_expression']
).size().unstack(fill_value=0)

expression_normalized = expression_counts.div(expression_counts.sum(axis=1), axis=0).fillna(0)

expression_smoothed = expression_normalized.rolling(window=5, min_periods=1).mean()

plot_data = expression_smoothed.reset_index().melt(id_vars="datetime", var_name="Expression", value_name="Frequency")

# Criar o gráfico interativo com Plotly Express
fig = px.line(
    plot_data, 
    x="datetime", 
    y="Frequency", 
    color="Expression", 
    title=f"Variação da Expressão Facial - {selected_topic} ({selected_person})",
    labels={"datetime": "Tempo", "Frequency": "Expressão Facial (%)", "Expression": "Expressão Facial"},
    template="plotly_white"
)
st.plotly_chart(fig, use_container_width=True)

if st.button("Back"):
    st.switch_page("main.py")
