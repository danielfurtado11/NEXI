from openai import OpenAI
import os
from dotenv import load_dotenv
from utils import read_file, save_to_file, extract_themes, generate_response

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI API key not found. Please check your .env file.")
client = OpenAI(api_key=API_KEY)

# Read the transcript of the meeting
file_path = "Files/transcription.txt"
transcription = read_file(file_path)


if transcription:

    # Create a summary of the meeting
    summary_prompt = f"Here's a transcript of a meeting:\n\n{transcription}\n\nMake a long summary without topics in english, just long text about this transcript of the meeting, detailed enough so that someone who didn't attend can understand what was discussed."
    summary_response = generate_response(client, summary_prompt, max_tokens=4000)
    save_to_file("Files/summary.txt", summary_response)


    # Extract the main info and goals
    info_prompt = (
        f"Here's a transcript of a meeting:\n\n{transcription}\n\n"
        "Identify the following details from all the meeting:\n\n"
        "1. **Participants**: List the names of all participants mentioned during the meeting.\n"
        "2. **Duration**: Calculate the total duration of the meeting in minutes.\n"
        "3. **Goals**: Identify the all the objectives discussed during all the meeting and state whether each goal was achieved, providing a brief explanation.\n\n"
        "Create a JSON file with the following structure:\n"
        "{\n"
        "    \"participants\": [\"Alice\", \"Bob\", \"Charlie\"],\n"
        "    \"duration\": 92,\n"
        "    \"goals\": [\n"
        "        (\"Presentation of the automatic transcription system and its applicability in training sessions and meetings.\", \"Objective Achieved: Yes, it was demonstrated how the tool works in real time and how reports can be generated automatically.\"),\n"
        "        (\"Discuss the integration of the platform with academic institutions.\", \"Objective Achieved: No, the conversation was preliminary, and further discussions are planned.\")\n"
        "    ]\n"
        "}\n\n"
        "Ensure the information is clear, concise, and accurate and get all the detailed goals.\n"
        "Ensure the information are concise and accurate. Respond with ONLY the JSON structure — no extra text no extra text (even the code language only the structure eg. (without ```json)) because I want to save the output direct to a json file.."
    )
    info_response = generate_response(client, info_prompt, max_tokens=4000)
    save_to_file("Files/info_&_goals.json", info_response)


    # Extract the Highlights and Next Steps
    highlights_prompt = (
        f"Here's a transcript of a meeting:\n\n{transcription}\n\n"
        "Identify the main topics discussed in the meeting and the subtopics covered under each main topic in a very detailed and accurate way.\n"
        "1. **Highlights**: Summarize the most important points discussed during the meeting, focusing on key decisions made, important insights shared by participants, and any significant conclusions reached.\n"
        "2. **Next Steps**: List all actions to be taken following the meeting, specifying tasks assigned to participants (if mentioned), deadlines, and any necessary follow-up actions.\n"
        "Create a JSON file with the following structure:\n"
        "{\n"
        "    \"highlights\": [\n"
        "        \"The presentation of the new project was well received by the team.\",\n"
        "        \"It was agreed that the data analysis model needs further testing before deployment.\",\n"
        "        \"A potential partnership with University X was discussed as a way to pilot the platform.\"\n"
        "    ],\n"
        "    \"next_steps\": [\n"
        "        \"Prepare a detailed project plan with deadlines and responsibilities.\",\n"
        "        \"Schedule a follow-up meeting with University X representatives next week.\",\n"
        "        \"Test the new data analysis model and compile a report by Friday.\"\n"
        "    ]\n"
        "}\n"
        "Ensure the information is **detailed and specific**, accurately capturing everything discussed without missing key points.\n"
        "Ensure the highlights are accurate and detailed. Respond with ONLY the JSON structure — no extra text no extra text (even the code language only the structure eg. (without ```json)) because I want to save the output direct to a json file.."
    )
    highlights_response = generate_response(client, highlights_prompt, max_tokens=4000)
    save_to_file("Files/highlights_&_next_steps.json", highlights_response)

    # Get the themes discussed in the meeting
    themes_prompt = (
        f"Here's a transcript of a meeting:\n\n{transcription}\n\n"
        "Identify the main topics discussed in the meeting and the subtopics covered under each main topic in a very detailed and accurate way.\n"
        "Format the output as a JSON array where each element is an object with the following structure:\n"
        "- 'minute_start': the starting minute of the topic.\n"
        "- 'minute_end': the ending minute of the topic.\n"
        "- 'topic': the main topic discussed.\n"
        "- 'subtopics': a list of subtopics discussed under the main topic.\n"
        "The JSON structure should look like this:\n"
        "{\n"
        "    {\n"
        "        'minute_start': 0,\n"
        "        'minute_end': 5,\n"
        "        'topic': 'Introduction and Participant Arrival',\n"
        "        'subtopics': [\n"
        "            'Welcoming participants',\n"
        "            'Meeting agenda overview',\n"
        "            'Explanation of meeting objectives'\n"
        "        ]\n"
        "    },\n"
        "    {\n"
        "        'minute_start': 5,\n"
        "        'minute_end': 15,\n"
        "        'topic': 'Review of Previous Meeting Report',\n"
        "        'subtopics': [\n"
        "            'Discussion of past meeting goals',\n"
        "            'Feedback on previous outcomes',\n"
        "            'Suggestions for improvements'\n"
        "        ]\n"
        "    }\n"
        "}\n\n"
        "I want you to be really detailed and accurate in the time, topics and subtopics. Elaborate well and make sure you don't miss any important point.\n"
        "Respond with **only** the JSON structure, with no additional text or explanations no extra text (even the code language only the structure eg. (without ```json)) because I want to save the output direct to a json file.."
    )
    themes_response = generate_response(client, themes_prompt, max_tokens=4000)
    save_to_file("Files/themes.json", themes_response)

    # Meeting Feedback
    feedback_prompt = (
        f"Here's a transcript of a meeting:\n\n{transcription}\n\n"
        "Analyze the performance of each participant and create a JSON file with the feedback for each person. "
        "Create a JSON file with the following structure:\n"
        "{\n"
        "   \"feedback\": [\n"
        "       {\n"
        "           \"name\": \"(Participant Name)\",\n"
        "           \"positive_aspects\": [\n"
        "               \"Clearly explained the project's structure and objectives.\",\n"
        "               \"Maintained active interaction with other participants.\",\n"
        "               \"Brought practical examples to illustrate the system's functionality.\"\n"
        "           ],\n"
        "           \"improvement_aspects\": [\n"
        "               \"Could communicate more concisely, avoiding lengthy explanations.\",\n"
        "               \"Reduce informal comments to maintain focus during the meeting.\",\n"
        "               \"Ensure others have space to speak, avoiding monopolizing the discussion.\"\n"
        "           ]\n"
        "       },\n"
        "       {\n"
        "           \"name\": \"(Another Participant)\",\n"
        "           \"positive_aspects\": [\n"
        "               \"Showed genuine interest and provided valuable insights about the system's application.\",\n"
        "               \"Clearly explained the challenges of online and in-person training.\"\n"
        "           ],\n"
        "           \"improvement_aspects\": [\n"
        "               \"Could be more concise to avoid repeating ideas.\",\n"
        "               \"Structure interventions better to keep the discussion focused.\"\n"
        "           ]\n"
        "       }\n"
        "   ]\n"
        "}\n\n"
        "I want you to identify the participants name and provide feedback on their performance during the meeting for every participant that you identify in the transcription!!! "
        "Make sure the feedback is specific and based on the content of the meeting. Respond with ONLY the JSON structure, no extra text no extra text (even the code language only the structure eg. (without ```json)) because I want to save the output direct to a json file.."
    )
    feedback_response = generate_response(client, feedback_prompt, max_tokens=4000)
    save_to_file("Files/feedback.json", feedback_response)
        
        
    # Relevant Questions
    questions_prompt = (
        f"Here's a transcript of a meeting:\n\n{transcription}\n\n"
        "Identify all relevant questions raised and their respective answers. "
        "Create a JSON file with the following structure:\n"
        "{\n"
        "   \"questions\": [\n"
        "       {\n"
        "           \"name\": \"(Participant Name)\",\n"
        "           \"questions_and_answers\": [\n"
        "               {\n"
        "                   \"question\": \"How can the platform ensure trainees have access to training materials after the course ends?\",\n"
        "                   \"answer\": \"Currently, trainees have limited access due to platform restrictions. Future plans include a personal space for each student to store all completed training and revisit materials as needed.\"\n"
        "               },\n"
        "               {\n"
        "                   \"question\": \"How can we store questions and answers during training in a useful way for trainees?\",\n"
        "                   \"answer\": \"The system can log participants' questions and organize them into a report for later review, including answers, support materials, and personalized study recommendations.\"\n"
        "               }\n"
        "           ]\n"
        "       },\n"
        "       {\n"
        "           \"name\": \"(Another Participant)\",\n"
        "           \"questions_and_answers\": [\n"
        "               {\n"
        "                   \"question\": \"Does the current model allow personalized learning recommendations based on trainee interaction?\",\n"
        "                   \"answer\": \"Yes, the platform analyzes each trainee's engagement level and suggests additional materials like videos, articles, or podcasts.\"\n"
        "               },\n"
        "               {\n"
        "                   \"question\": \"How do we ensure legal compliance when storing trainee data?\",\n"
        "                   \"answer\": \"The legal team is reviewing best practices to comply with data protection laws, such as anonymizing data or processing information in real-time without extended storage.\"\n"
        "               }\n"
        "           ]\n"
        "       }\n"
        "   ]\n"
        "}\n\n"
        "I want you to identify the participants name and provide the questions they asked and the answers they received during the meeting in english!!!!!! "
        "Ensure the answers are concise yet informative, and respond with ONLY the JSON structure — no extra text (even the code language only the structure eg. (without ```json)) because I want to save the output direct to a json file."
    )
    questions_response = generate_response(client, questions_prompt, max_tokens=4000)
    save_to_file("Files/questions.json", questions_response)


    # Assign Tasks
    tasks_prompt = (
        f"Here's a transcript of a meeting:\n\n{transcription}\n\n"
        "Identify all tasks assigned to each participant identified in the transcription, clearly linking the task to the respective person. "
        "Create a JSON file with the following structure:\n"
        "{\n"
        "   \"tasks\": [\n"
        "       {\n"
        "           \"name\": \"(Participant Name)\",\n"
        "           \"assigned_tasks\": [\n"
        "               \"Send an email to University X to formalize interest in a partnership and schedule a meeting.\",\n"
        "               \"Work on the visual presentation of reports to make them more intuitive and informative.\",\n"
        "               \"Coordinate with the team to organize the first controlled test of the platform.\"\n"
        "           ]\n"
        "       },\n"
        "       {\n"
        "           \"name\": \"(Another Participant)\",\n"
        "           \"assigned_tasks\": [\n"
        "               \"Improve the engagement measurement functionality in the system, incorporating facial expression and interaction analysis.\",\n"
        "               \"Implement technical adjustments to optimize real-time transcription and summary processing.\",\n"
        "               \"Develop a mechanism to customize reports according to training type and user needs.\"\n"
        "           ]\n"
        "       }\n"
        "   ]\n"
        "}\n\n"
        "I want you to identify the participants name and provide the tasks assigned to them during the meeting!!!!!! "
        "Ensure the tasks are concise, actionable, and clearly linked to the correct participant. Respond with ONLY the JSON structure — no extra text no extra text (even the code language only the structure eg. (without ```json)) because I want to save the output direct to a json file.."
    )
    tasks_response = generate_response(client, tasks_prompt, max_tokens=4000)
    save_to_file("Files/tasks.json", tasks_response)



    # Evaluation 
    evaluation_prompt = (
        f"Here's a transcript of a meeting:\n\n{transcription}\n\n"
        "Identify the meeting's evaluation criteria, scores, and justifications, along with the key strengths and areas for improvement. "
        "Create a JSON file with the following structure:\n"
        "{\n"
        "   \"evaluation\": {\n"
        "       \"overall_score\": \"Numerical score (0-100)\",\n"
        "       \"criteria\": [\n"
        "           {\n"
        "               \"criterion\": \"Criterion name (e.g., Fulfillment of objectives)\",\n"
        "               \"weight\": \"Percentage weight of the criterion (e.g., 30%)\",\n"
        "               \"score\": \"Score out of 100\",\n"
        "               \"justification\": \"Brief explanation of the score given.\"\n"
        "           }\n"
        "       ],\n"
        "       \"strengths\": [\n"
        "           \"Brief description of a positive point (e.g., Clear and practical demonstration of the system)\",\n"
        "           \"Another positive point.\"\n"
        "       ],\n"
        "       \"areas_for_improvement\": [\n"
        "           \"Brief description of an area to improve (e.g., Some discussions could have been more objective)\",\n"
        "           \"Another area for improvement.\"\n"
        "       ]\n"
        "   }\n"
        "}\n\n"
        "Ensure the justifications are concise, strengths are clearly stated, and areas for improvement are actionable. Respond with ONLY the JSON structure — no extra text no extra text (even the code language only the structure eg. (without ```json)) because I want to save the output direct to a json file.."
    )
    evaluation_response = generate_response(client, evaluation_prompt, max_tokens=4000)
    save_to_file("Files/evaluation.json", evaluation_response)