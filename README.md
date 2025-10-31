# 🤖 AI Resume and Cover Letter Generator

This Streamlit application is an intelligent resume and cover letter generator. It uses a modular, agent-based architecture to take a user's professional details and a specific job description, and then generates tailored documents using the Google Gemini API.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You need to have Python 3.7 or later installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

You will also need a Google Gemini API key. You can get one from the [Google AI for Developers](https://ai.google.dev/) website.

### Installation

1.  Clone the repository to your local machine:
    ```bash
    git clone <repository-url>
    ```
2.  Navigate to the project directory:
    ```bash
    cd <project-directory>
    ```
3.  Create a virual environment and activate the environment
    ```bash
    python -m venv <env_name>
    source <env_name>/bin/activate
    deactivate
    ```
4.  Install the required Python packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  Run the Streamlit application from your terminal:
    ```bash
    streamlit run streamlit_app.py
    ```
2.  Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).
3.  Enter your Gemini API key and fill in the required information to generate your resume and cover letter.
