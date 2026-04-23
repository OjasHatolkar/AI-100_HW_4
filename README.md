AI-100 HW 4 — LLM Task Prioritizer
A Python command-line application that uses the Google Gemini API to prioritize a list of tasks. The user can add tasks with a name, description, and due date, and the program uses Gemini to assign each task a priority score from 0–100 based on the full context of all entered tasks.


Running this code requires the following:
Create a .env file in the project root with your Gemini API key:
    GEMINI_API_KEY=your_key_here
You can obtain a free API key from Google AI Studio.
Usage
Run the program with:
python AI-100_HW_4.py


User Experience:

Users will be prompted to choose from three options:

Add a new task (name, description, due date)
Update progress on an existing task
View all tasks sorted from highest to lowest priority

Prompt Design & Experimentation
Each task is sent to Gemini individually, with the full list of other tasks included as context. This allows Gemini to weigh each task's priority relative to the others rather than in isolation. The prompt explicitly instructs Gemini to return a single integer from 0–100, which is then used to sort the task list.
Prompts were tested using real student tasks such as homework assignments across different courses (e.g. AI 100 HW 4, MATH 220 Written HW 9). The prompt was refined to include due dates and progress information so that Gemini could factor in urgency and remaining work when assigning priority scores.

Notes:
The .env file is not included in this repository. You must supply your own Gemini API key.
Task.py defines the Task class used to represent each task.
