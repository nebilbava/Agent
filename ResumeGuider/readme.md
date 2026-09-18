# ResumeGuider 🤖

ResumeGuider is an AI-powered resume analysis and career guidance agent that analyzes a user's resume and provides personalized feedback, recommendations, and upskilling suggestions.

The project uses an LLM-based agent workflow to extract information from a resume, analyze the candidate's profile, recommend suitable career directions, suggest skills to improve, and provide an overall resume/ATS-oriented evaluation.

## 🚀 Features

* 📄 Resume text processing
* 🔍 Automatic extraction of resume information
* 🧠 AI-powered resume analysis
* 💼 Career and role recommendations
* 📚 Personalized upskilling suggestions
* 📊 Resume/ATS-oriented evaluation
* 🤖 Agent-based workflow
* 🔐 Environment-variable based API configuration

## 🏗️ Project Architecture

The application follows a modular agent-based architecture:

```
                ┌──────────────┐
                │  User Input  │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │   main.py    │
                └──────┬───────┘
                       │
                       ▼
                ┌──────────────┐
                │   agent.py   │
                └──────┬───────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    Extraction      Analysis    Recommendations
         │             │             │
         └─────────────┼─────────────┘
                       │
                       ▼
              Upskilling & Evaluation
                       │
                       ▼
                ┌──────────────┐
                │  display.py  │
                └──────────────┘
```

## 📁 Project Structure

ResumeGuider/
│
├── agent.py
├── context.py
├── data.py
├── display.py
├── file_reader.py
├── llm.py
├── main.py
├── prompt.py
│
├── resume.txt
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example

## 🛠️ Technologies Used

* Python
* LLM / Generative AI
* LiteLLM
* PyPDF
* python-dotenv

## ⚙️ Installation

Clone the repository:

git clone <your-github-repository-url>

cd ResumeGuider

Create and activate a virtual environment:

python -m venv venv

On Windows:

venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

## 🔐 Environment Variables

Create a .env file in the project directory and add your API configuration.

Example:

API_KEY=your_api_key_here

Do not commit your .env file or expose your API key.

Use .env.example as a template.

## ▶️ Running the Project

Run the application with:

python main.py

The agent will process the resume and generate:

* Resume information
* Candidate analysis
* Career recommendations
* Skill improvement suggestions
* Resume/ATS evaluation
