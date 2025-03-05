import streamlit as st
import pandas as pd
import plotly.express as px

from PIL import Image

st.set_page_config(page_title="Meeting Analysis", layout="wide")

row = st.columns(2)
row[0].image("logo.png", width=150)

st.write("")
st.write("")
st.write("")



st.title("📊 Meeting Analysis (13-02-2025)")

st.write("")
st.write("##### Participants: <span style='font-weight:normal;'>André Neiva, Daniel Furtado, Francisco Falcão, Rita Batista.</span>", unsafe_allow_html=True)
st.write("##### Duration: <span style='font-weight:normal;'>11:35 - 12:57 (92 minutes)</span>", unsafe_allow_html=True)


st.write("")

st.header("🎯 Goals", divider="gray")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Presentation of the automatic transcription system<span style='font-weight:normal;'> and its applicability in training sessions and meetings.</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✔️ Objective Achieved: <span style='font-weight:normal;'>Yes, it was demonstrated how the tool works in real time and how reports can be generated automatically.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Exploration of engagement analysis<span style='font-weight:normal;'> of trainees and its impact on the learning process.</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✔️ Objective Achieved: <span style='font-weight:normal;'>Yes, charts and metrics were presented showing how participation can be evaluated and improved.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Discussion on privacy and legal compliance<span style='font-weight:normal;'> in handling participants' data.</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✔️ Objective Achieved: <span style='font-weight:normal;'>Yes, ways to anonymize data and ensure compliance with regulations were discussed.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Presentation of future improvements<span style='font-weight:normal;'> for optimizing the interface and user experience.</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✔️ Objective Achieved: <span style='font-weight:normal;'>Yes, it was identified that interface adjustments are necessary for better usability.</span>", unsafe_allow_html=True)


st.header("📊 Evaluation", divider="gray")

st.write("#### Meeting Effectiveness Rating: 87/100")

st.write("###### Evaluation Criteria:")

data = {
    "Criteria": [
        "Achievement of objectives",
        "Clarity of discussions",
        "Decision-making and task assignment",
        "Engagement and participation of members",
        "Time efficiency"
    ],
    "Weight (%)": [30, 20, 20, 15, 15],
    "Score (0-100)": [95, 85, 90, 85, 80],
    "Justification": [
        "The main objectives were achieved, including the demonstration of the system’s features.",
        "Overall clarity was maintained, though some topics were debated extensively.",
        "Decisions were well distributed, but some tasks lacked defined deadlines.",
        "Active participation with relevant contributions from various attendees.",
        "The meeting could have been slightly more objective at certain moments."
    ]
}

import pandas as pd

df = pd.DataFrame(data)

st.dataframe(df)  # Uses an interactive table


st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Strengths:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Clear and practical demonstration of the system.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Productive discussions on engagement and data privacy.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - New ideas emerged to enhance the user experience.")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ Areas for Improvement:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Some discussions could have been more objective.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Better definition of deadlines for assigned tasks.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Refinements needed in the interface for optimized usability.")


st.write("")
st.write("")
st.write("")

st.header("📅 Topics Covered", divider="gray")

def format_time(hour, minute):
    if (minute < 60):
        return f"{hour:02d}:{minute:02d}"
    else:
        return f"{hour+1:02d}:{minute-60:02d}"


start_hour, start_minute = 11, 35

themes = [
    (0, 7, "Introduction and participant arrival.", [
        "Introduction of participants.",
        "Explanation of the meeting’s objective.",
        "Reference to recording and meeting report structure."
    ]),
    (7, 9, "Presentation of the previous meeting report.", [
        "Analysis of the automatically generated report.",
        "Objectives of the previous meeting and its effectiveness.",
        "Identification of improvements and suggestions for enhancement."
    ]),
    (9, 10, "Definition of next steps and task assignment.", [
        "Organization of actions to be taken.",
        "Distribution of responsibilities among participants.",
        "Importance of meeting documentation for future reviews."
    ]),
    (10, 11, "Discussion on training effectiveness and teaching methodologies.", [
        "How to evaluate the quality of training through reports.",
        "Using technology to measure student participation and comprehension.",
        "Benefits of structured feedback for trainers and trainees."
    ]),

    (11, 12, "Analysis of engagement and active participation.", [
        "Comparison of participant involvement based on visual and textual metrics.",
        "Identification of moments of higher or lower engagement.",
        "Importance of capturing student interest during training."
    ]),
    (12, 20, "Considerations on the use of technology in education.", [
        "Applications of the tool in corporate and sports training.",
        "Possibilities for integration with learning and management platforms.",
        "Benefits of maintaining an accessible history of past training sessions."
    ]),
    (20, 22, "Impact of funded training and motivation challenges.", [
        "Difference between mandatory and optional training sessions.",
        "How technology can ensure better monitoring of the learning process.",
        "Difficulties in maintaining participant attention and motivation."
    ]),
    (22, 29, "Management of material access and training certification.", [
        "Challenges faced by training institutions in providing content.",
        "Importance of an integrated system to store information from different courses.",
        "Comparison with platforms like Moodle and other e-learning solutions."
    ]),
    (29, 38, "Business model for digital training and centralized platform.", [
        "Possibility of creating a training marketplace.",
        "How to remunerate trainers and create a sustainable system.",
        "Example of a \"Spotify for Training,\" where content could be accessed."
    ]),
    (38, 46, "Legality and necessary authorizations for recordings and data processing.", [
        "Legal issues related to recording and using participant data.",
        "Methods to ensure compliance with data protection regulations.",
        "Alternatives for anonymizing sensitive information."
    ]),
    (46, 52, "Integration of the tool in academic contexts.", [
        "Potential use of the technology in universities.",
        "Discussion on a possible partnership with the University of Minho.",
        "Benefits of the tool for professors and students in higher education."
    ]),
    (52, 55, "Testing and implementation in real training sessions.", [
        "Proposal to test the tool in practical training.",
        "Approach to ensure trainer and student adherence.",
        "Identification of possible resistance and strategies to overcome it."
    ]),
    (55, 82, "Final reflection and next steps.", [
        "Conclusions on the meeting and action plans.",
        "Preparation for sending an email to the University of Minho.",
        "Discussion on communication strategies and tool presentation."
    ])
]

for start, end, title, points in themes:
    start_time = format_time(start_hour, start_minute + start)
    end_time = format_time(start_hour, start_minute + end)
    st.write(f"##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;📌 {title} <span style='font-weight:normal;'>({start_time} - {end_time})</span>", unsafe_allow_html=True)
    formatted_points = "".join([f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- {point}<br>" for point in points])
    st.write(f"""
        {formatted_points}
    """, unsafe_allow_html=True)


st.write("")
st.write("")
st.write("")

st.header("📝 Summary",divider="gray")

st.text = """

The meeting started promptly at 11:35 AM, with the presence of André Neiva, Rita Batista, Daniel Furtado, and Francisco Falcão. 
André opened the session by explaining the main objectives of the meeting, which involved presenting the models developed by the team, analyzing the previous meeting report, and discussing improvements for process automation. 
He also emphasized the importance of capturing objective data to enhance the quality of future training sessions and meetings. 
At the beginning, there was a brief exchange of views among participants on the need for an effective reporting system capable of providing valuable insights for trainers and organizations.

Following this introduction, André shared a report generated from the last meeting held two days ago. 
The document detailed the topics discussed, the effectiveness of the meeting, and member participation. 
Rita and Daniel shared their opinions on the report's content, noting that its structure was quite useful but that some aspects could be improved, such as the visual presentation of data and the inclusion of more detailed metrics on participant engagement. 
André mentioned that future versions of the report could include more intuitive graphs and customizable information to meet each user's specific needs.

The next agenda item addressed the effectiveness of training sessions and how technology can improve the teaching and learning process. 
André explained that one of the key functions of the tool they were developing was the ability to measure participant engagement in real-time.
This would allow trainers to identify moments of higher or lower attention from students and adjust their methodologies to maximize learning outcomes. 
Rita added that, in her experience, trainee motivation varies significantly depending on the nature of the training. 
For example, mandatory training sessions tend to generate less engagement, whereas optional courses attract more interested participants. 
Based on this observation, the team discussed the possibility of customizing reports to differentiate these scenarios and suggest specific interventions to improve student involvement.

Another important topic was the management of material access and training certification. 
Rita highlighted that many learning platforms restrict access to content once a course is completed, which can be detrimental to trainees who wish to review the material later. 
Francisco suggested creating a platform that would function as a centralized learning repository, where students could access their materials whenever needed. 
Comparisons were made with existing platforms like Moodle, but it became evident that the proposed solution would have a significant advantage by integrating different courses and training entities into a single accessible environment.

The meeting then moved on to the legal aspects of recording and processing participant data. 
Francisco explained that any recording would require explicit authorization and that it would be essential to ensure compliance with data protection regulations. 
Various approaches were considered to address potential concerns, such as anonymizing certain data or configuring a system that processes information without storing it permanently. 
André and Daniel reflected on the feasibility of these solutions, emphasizing that the technology could be adjusted to meet legal requirements without compromising the tool's functionality.

Next, the discussion turned to the potential expansion of the tool's use in academic settings, particularly at the University of Minho. 
Rita mentioned that the institution has a history of supporting innovative projects and could be a strategic partner for the initial implementation of the technology. 
André noted that he had already had a preliminary conversation with a university psychologist who expressed interest in the tool's potential to enhance the learning experience. 
The idea of scheduling a formal meeting with university representatives was well received, and Francisco suggested preparing a detailed presentation to highlight the platform's benefits.

Another topic discussed was the practical application of the technology in corporate training sessions. 
Rita shared a recent experience where evaluating training effectiveness was challenging due to a lack of objective data. With the developed tool, it would be possible to generate detailed reports on trainee performance and session dynamics. 
Francisco reinforced that adopting a continuous monitoring system could benefit both trainers and companies, providing a clearer overview of the return on investment in training programs.

In the final moments of the meeting, the next steps were reviewed. 
It was decided that an email would be sent to the University of Minho to formalize contact and schedule a meeting. 
Additionally, Francisco committed to consulting legal experts to ensure all legal issues were properly addressed before large-scale implementation. 
André mentioned that an initial test of the platform could be conducted in a controlled environment, allowing for adjustments before a broader rollout.

The meeting concluded with a positive sense of progress. 
All participants agreed that the discussions provided valuable insights for the project's evolution and that the next steps were well defined. 
It became clear that the developed technology has the potential to revolutionize how training sessions and meetings are conducted, offering an innovative method for performance analysis and monitoring. 
The expectation is that the upcoming implementation and testing phases will yield concrete results that confirm the benefits discussed throughout the meeting.

"""

with st.container(height=500, border=True):
    st.write(st.text)

st.write("")
st.write("")
st.write("")


st.header("✅ Highlights", divider="gray")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Main objective of the meeting: <span style='font-weight:normal;'>The meeting focused on analyzing the meeting transcription and summarization platform, as well as its application in education and professional training.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Analysis of the previous meeting report: <span style='font-weight:normal;'>A detailed report from the previous meeting was presented, highlighting strengths and necessary improvements to optimize the automatic report generation.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Engagement and Participation Measurement: <span style='font-weight:normal;'>The evolution of the system to capture facial expressions and interaction patterns was discussed, enabling better monitoring of participant involvement.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Application of Technology in Education and Training: <span style='font-weight:normal;'>The possibilities of using the tool in higher education and corporate training were explored, with an emphasis on potential collaboration with the University of Minho.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Legal Issues and Data Protection: <span style='font-weight:normal;'>The need for compliance with data protection regulations and possible solutions to anonymize sensitive information was debated.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Improvement of Interface and Report Presentation: <span style='font-weight:normal;'>The need to make reports more visual and intuitive, using clearer graphics and metrics, was identified.</span>", unsafe_allow_html=True)

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔸 Pilot Tests and Initial Implementation: <span style='font-weight:normal;'>The execution of an initial platform test in a controlled environment was discussed to evaluate its effectiveness before large-scale implementation.</span>", unsafe_allow_html=True)

st.write("\n\n\n")

st.header("👣 Next Steps", divider="gray")

st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Schedule a meeting with representatives from the University of Minho to discuss the feasibility of a partnership and the application of the tool in academia.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Consult legal experts to define the best approach regarding data protection and technology usage permissions.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Improve the system interface, making reports more intuitive and user-friendly.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Refine the \"engagement score\" and create more detailed indicators to assess trainee participation.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔹 Implement an initial test of the platform in a controlled environment to gather feedback and adjustments before project expansion.")

st.write("\n\n\n")

st.header("✍🏻 Assigned Tasks", divider="gray")

# Dictionary of assigned tasks per person
tasks = {
    "André Neiva": [
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Send an email to the University of Minho to formalize interest in the partnership and schedule a meeting.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Work on the visual presentation of reports to make them more intuitive and informative.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Coordinate with the team to organize the first controlled test of the platform."
    ],
    "Daniel Furtado": [
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Improve the engagement measurement functionality in the system, incorporating facial expression and interaction analysis.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Implement technical adjustments to optimize real-time transcription and summarization processing.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Develop a mechanism to customize reports according to training type and user needs."
    ],
    "Francisco Falcão": [
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Consult lawyers to ensure the platform’s legal compliance, especially regarding data protection and permissions.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Work on structuring reports to make them more accessible to end users."
    ],
    "Rita Batista": [
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Explore contacts at the University of Minho to facilitate communication and enable the tool presentation.",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➡️ Evaluate potential resistance from trainers and companies regarding technology adoption and suggest strategies to increase acceptance."
    ]
}

st.write("\n\n\n")

selected_people = []
for person in tasks.keys():
    if st.checkbox(person, value=True):  # Começa marcado por padrão
        selected_people.append(person)

# Exibir as tarefas das pessoas selecionadas
for person in selected_people:
    st.write(f"#### {person}")
    for task in tasks[person]:
        st.write(f" {task}")


st.write("\n\n\n")

st.header("❔ Relevant Questions", divider="gray")


st.write("###### 🔸 Does the platform allow trainees to access training content after completion? <span style='font-weight:normal;'>(Francisco Falcão)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Answer: <span style='font-weight:normal;'>Currently, trainees have limited access due to platform restrictions. The future goal is for each trainee to have a personal space where they can aggregate all their completed trainings and revisit materials whenever needed.</span>", unsafe_allow_html=True)

st.write("###### 🔸 How can we ensure that questions and answers during training are stored usefully for students? <span style='font-weight:normal;'>(Francisco Falcão)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Answer: <span style='font-weight:normal;'>The system can record participants' questions and organize them into a report, which can be consulted later. This report can include responses, supporting materials, and even personalized study recommendations, without identifying the question authors.</span>", unsafe_allow_html=True)

st.write("###### 🔸 Does the current model allow learning recommendations to be personalized based on trainee interaction? <span style='font-weight:normal;'>(André Neiva)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Answer: <span style='font-weight:normal;'>Yes, the platform can analyze each trainee's level of engagement and generate suggestions for complementary materials such as videos, articles, or podcasts. If the system detects that a certain topic was not well understood, it can suggest specific reinforcements for each student.</span>", unsafe_allow_html=True)

st.write("###### 🔸 How can we ensure legal compliance with trainee data storage? <span style='font-weight:normal;'>(André Neiva)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Answer: <span style='font-weight:normal;'>The legal team is reviewing best practices to ensure compliance with data protection laws. Alternatives include anonymizing trainee data, processing information in real-time without long-term storage, and ensuring participants have full transparency and control over their data.</span>", unsafe_allow_html=True)

st.write("###### 🔸 Can trainees opt out of engagement analysis? <span style='font-weight:normal;'>(Rita Batista)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Answer: <span style='font-weight:normal;'>Yes, participants can opt out of facial and engagement analysis. If they decline, their data will not be processed, and only general class information will be presented.</span>", unsafe_allow_html=True)

st.write("###### 🔸 How can we prevent the presence of cameras from influencing trainee behavior? <span style='font-weight:normal;'>(Rita Batista)</span>", unsafe_allow_html=True)
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Answer: <span style='font-weight:normal;'>Studies show that after the first few minutes, trainees stop worrying about the cameras and behave naturally. Additionally, the tool can operate in the background without permanent recording, only analyzing facial expressions and engagement in real-time.</span>", unsafe_allow_html=True)




st.header("🫡 Meeting Feedback", divider="gray")


st.write("### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;André Neiva")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Positive Aspects:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Clearly explained the project structure and the objectives of the developed tool.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Successfully maintained active interaction with other participants.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Provided practical examples to illustrate the system's functionality.")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ Areas for Improvement:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Communication could be more concise, avoiding lengthy explanations and unnecessary justifications.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Some jokes and informal comments could be reduced to keep the meeting focused (e.g., the reference to \"Trans Neiva\").")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Ensure that all participants have space to contribute, avoiding monopolizing the conversation.")

st.write("### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rita Batista")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Positive Aspects:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Showed genuine interest and provided valuable insights on the system's application in the training sector.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Clearly explained the challenges of online and in-person training.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Suggested valuable contacts, including with the University of Minho.")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ Areas for Improvement:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Some ideas were repeated throughout the meeting. Could be more concise.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Could structure interventions better to improve the flow of conversation and avoid topic deviations.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Some explanations were too lengthy and detailed, making it harder to grasp key points quickly.")

st.write("### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Francisco Falcão")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Positive Aspects:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Presented the legal and technical aspects of the tool well.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Made a strong connection between the tool and its impact on continuous training and certification.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Provided solid arguments on the project's importance and its applicability in different sectors.")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ Areas for Improvement:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Some explanations were too lengthy, which may have made certain points less clear.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Could summarize some concepts better to make the meeting more efficient.")

st.write("### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Daniel Furtado")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅ Positive Aspects:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Demonstrated technical knowledge and was attentive to the discussion.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Provided a relevant perspective on the potential adaptation of the platform with new features.")

st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ Areas for Improvement:")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Participation was very limited. Could engage more and clarify technical doubts when they arise.")
st.write(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Could take a more proactive approach in suggesting improvements to the project.")

st.write("\n\n\n")


topics = {
    "Global": None,
    "Introduction and participant arrival": ("11:35", "11:42"),
    "Presentation of the previous meeting report": ("11:42", "11:44"),
    "Definition of next steps and task assignment": ("11:44", "11:45"),
    "Discussion on training effectiveness and teaching methodologies": ("11:45", "11:46"),
    "Analysis of engagement and active participation": ("11:46","11:47"),
    "Considerations on technology use in education": ("11:47","11:55"),
    "Impact of funded training and motivation challenges": ("11:55","11:57"),
    "Access management for materials and certification": ("11:57","12:04"),
    "Business model for digital training and centralized platform": ("12:04","12:13"),
    "Legality and necessary authorizations for recordings and data processing": ("12:13","12:21"),
    "Integration of the tool in academic contexts": ("12:21","12:27"),
    "Testing and implementation in real training scenarios": ("12:27","12:30"),
    "Final reflection and next steps": ("12:30","12:57"),
}


st.header("📈 Engagement", divider="gray")

data = pd.read_csv("pages/Reuniao_13_02_2025/Files/data_final.csv")
data["datetime"] = pd.to_datetime(data["datetime"])

time_adjust = "1min" 


plot_data = []

data_global = data.set_index('datetime').resample(time_adjust)["engagement"].mean().reset_index()
data_global['person'] = 'Global Mean' 


selected_topic = st.selectbox("🔍 Filter by Theme:", list(topics.keys(),), key="engagement")
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

plot_df["Theme"] = "Global"  # Valor padrão

for tema, intervalo in topics.items():
    if intervalo:  # Verifica se o valor não é None
        start_time, end_time = intervalo
        mask = (plot_df["datetime"].dt.strftime("%H:%M") >= start_time) & \
               (plot_df["datetime"].dt.strftime("%H:%M") <= end_time)
        plot_df.loc[mask, "Theme"] = tema  # Atribui o tema correto


fig = px.line(
    plot_df, 
    x="datetime", 
    y="engagement", 
    color="person",
    title="Engagement Over the Time",
    labels={"datetime": "Time", "engagement": "Engagement (%)", "person": "Participants"},
    template="plotly_white",
    line_dash="person",
    line_group="person",
    line_dash_map={"Global Mean": "dash", "André Neiva": "solid", "Daniel Furtado": "solid", "Francisco Falcão": "solid", "Rita Batista": "solid"},
    hover_data=["Theme"],
    range_y=[0, 1]
)

st.plotly_chart(fig, use_container_width=True)

st.write("")

st.write("##### Relevant Moments")

col1, col2, col3, col4, b,c,d,e = st.columns(8)

# Inicializar estados para cada imagem
if "show_image_1623" not in st.session_state:
    st.session_state.show_image_1623 = False
if "show_image_1625" not in st.session_state:
    st.session_state.show_image_1625 = False


with col1:
    if st.button("11:49"):
        st.session_state.show_image_1623 = not st.session_state.show_image_1623

with col2:
    if st.button("12:34"):
        st.session_state.show_image_1625 = not st.session_state.show_image_1625



if st.session_state.show_image_1623:
    st.image(Image.open("pages/Reuniao_12_04_2025/Images/11_49.png"), caption="Low Engagement Moment", width=650)

if st.session_state.show_image_1625:
    st.image(Image.open("pages/Reuniao_12_04_2025/Images/12_34.png"), caption="High Engagement Moment", width=650)

st.write("")
st.write("")
st.write("")


st.header("📈 Participation", divider="gray")
st.write("")

st.write("##### 🗣️ Active Participation:")
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; •  André Neiva: <span style='font-weight:normal;'>00:27:13 (29.58%)</span>", unsafe_allow_html=True )
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; •  Daniel Furtado: <span style='font-weight:normal;'>00:06:26 (06.99%)</span>", unsafe_allow_html=True )
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; •  Rita Batista: <span style='font-weight:normal;'>00:34:28 (37.46%)</span>", unsafe_allow_html=True )
st.write("###### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; •  Francisco Falcão: <span style='font-weight:normal;'>00:21:52 (23.77%)</span>", unsafe_allow_html=True )




df_resampled = pd.read_csv("pages/Reuniao_13_02_2025/Files/interventions.csv", index_col=0, parse_dates=True)
df_resampled["Global Mean"] = df_resampled[["André Neiva", "Daniel Furtado", "Rita Batista", "Francisco Falcão"]].mean(axis=1)




participants = df_resampled.columns.tolist()




df_filtered = df_resampled[participants].reset_index()
df_melted = df_filtered.melt(id_vars=["time"], var_name="Participant", value_name="Interventions")

selected_topic = st.selectbox("🔍 Filter by Theme:", list(topics.keys(),), key="participation")
if selected_topic != "Global":
    start_time, end_time = topics[selected_topic]
    mask_time = (df_melted['time'].dt.strftime("%H:%M") >= start_time) & (df_melted['time'].dt.strftime("%H:%M") <= end_time)
    data_filtered = df_melted[mask_time]
else:
    data_filtered = df_melted


data_filtered["Theme"] = "Global"  # Valor padrão

for tema, intervalo in topics.items():
    if intervalo:  # Verifica se o valor não é None
        start_time, end_time = intervalo
        mask = (data_filtered["time"].dt.strftime("%H:%M") >= start_time) & \
               (data_filtered["time"].dt.strftime("%H:%M") <= end_time)
        data_filtered.loc[mask, "Theme"] = tema  # Atribui o tema correto





fig = px.line(data_filtered, x="time", y="Interventions", color="Participant",
            labels={"time": "Horário", "Interventions": "Number of Interventions"},
            line_dash="Participant",
            line_dash_map={"Global Mean": "dash", "André Neiva": "solid", "Daniel Furtado": "solid", "Francisco Falcão": "solid", "Rita Batista": "solid"},
            title="Participation Over the Time",
            hover_data=["Theme"]
            )



fig.update_xaxes(title="Time")
fig.update_yaxes(title="Number of Interventions")
fig.update_layout(legend_title="Participants")

st.plotly_chart(fig, use_container_width=True)



st.write("")
st.write("")
st.write("")


st.header("🎭 Facial Expression", divider="gray")

time_adjust = '1 min'



people_list = data['person'].unique()
people_list = ["Global"] + list(people_list)

selected_topic = st.selectbox("🔍 Filter by Theme:", list(topics.keys()), key="facial_expression")
selected_person = st.selectbox("👤 Filter by Person:", people_list)

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

plot_data["Tema"] = "Global"  # Valor padrão

for tema, intervalo in topics.items():
    if intervalo:  # Verifica se o valor não é None
        start_time, end_time = intervalo
        mask = (plot_data["datetime"].dt.strftime("%H:%M") >= start_time) & \
               (plot_data["datetime"].dt.strftime("%H:%M") <= end_time)
        plot_data.loc[mask, "Theme"] = tema  # Atribui o tema correto



# Criar o gráfico interativo com Plotly Express
fig = px.line(
    plot_data, 
    x="datetime", 
    y="Frequency", 
    color="Expression", 
    title=f"Facial Expression Variation - {selected_topic} ({selected_person})",
    labels={"datetime": "Time", "Frequency": "Facial Expression (%)", "Expression": "Facial Expression"},
    hover_data=["Theme"],
    template="plotly_white",
    range_y=[0, 1]

)
st.plotly_chart(fig, use_container_width=True)


