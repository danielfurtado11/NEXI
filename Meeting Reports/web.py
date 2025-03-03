import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
from utils import format_time, read_file
import json

## VARIABLES NEED TO UPDATE MANUALLY ##
person = "Daniel"
start_hour, start_minute = 11, 35

st.set_page_config(page_title="Meeting Analysis", layout="wide")

row = st.columns(1)

row[0].image("Images/nexi.jpg", width=250)
row[0].markdown(f"## 👋 Welcome, {person}!")

st.write("")
st.write("")
st.write("")


##  -------------------  INFO & GOALS -------------------

file = "Files/info_&_goals.json"

with open(file, "r", encoding="utf-8") as f:
    info_data = json.load(f)

participants = ", ".join(info_data["participants"])
end_time = format_time(start_hour, start_minute + info_data['duration'])
duration = f"{start_hour}:{start_minute} - {end_time} ({info_data['duration']} minutes)"

st.title("📊 Meeting Analysis (13-02-2025)")
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

file = "Files/evaluation.json"
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

file = "Files/themes.json"

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

summary = read_file('Files/summary.txt')

st.text = summary

with st.container(height=500, border=True):
    st.write(st.text)

st.write("")
st.write("")
st.write("")


##  -------------------  HIGHLIGHTS & NEXT STEPS  -------------------

file = "Files/highlights_&_next_steps.json"

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

file = "Files/tasks.json"
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

file = "Files/questions.json"  # Substitua pelo nome correto do ficheiro
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

file = "Files/feedback.json"  # Substitua pelo nome correto do ficheiro
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