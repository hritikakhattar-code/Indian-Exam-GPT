# Indian-Exam-GPT
ndianExamGPT is an AI-powered platform designed to help students prepare for Indian competitive exams. It uses the latest advancements in Natural Language Processing (NLP) and Machine Learning (ML) to extract useful information from exam PDFs, providing students with intelligent insights and detailed answers to specific questions.

Features
Upload Exam PDFs: Users can upload PDFs of Indian competitive exam question papers or study materials.

AI-Powered Question Answering: Using the LangChain framework, OpenAI's GPT, and FAISS (a fast similarity search engine), the app allows users to ask questions related to the exam content.

FAISS Vector Store: The system uses FAISS to efficiently search through large PDF content for relevant answers.

Streamlit Interface: A simple and intuitive interface built with Streamlit, enabling users to easily interact with the system.

Tech Stack
Python: Programming language used for the backend.

Streamlit: For building the user interface.

LangChain: To manage large language models (LLMs) and integrate OpenAI with FAISS.

OpenAI GPT-3/4: Language model used for natural language understanding and response generation.

FAISS: For fast similarity search on exam PDFs.

Pandas: For data manipulation (if needed).

PyPDF2 or pdfplumber: To extract text from PDFs.

Setup and Installation
Follow these steps to run the project locally:

1. Clone the Repository
bash
Copy code
git clone https://github.com/hritikakhattar-code/Indian-Exam-GPT.git
cd Indian-Exam-GPT
2. Create a Virtual Environment
bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows:

bash
Copy code
.\venv\Scripts\activate
macOS/Linux:

bash
Copy code
source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Set Up API Keys
Create a .env file in the root directory and add your OpenAI API key:

ini
Copy code
OPENAI_API_KEY=your-api-key-here
Make sure to never push your .env file to GitHub. It should be ignored in the .gitignore file.

5. Run the Application
bash
Copy code
streamlit run main.py
Open the link provided in your browser to interact with the app.

How to Use
Upload the exam PDF: Choose a file from your local machine.

Ask a Question: Enter your question based on the content of the uploaded PDF.

Get the Answer: The system will use AI to analyze the content and provide a relevant response.

Contributing
Contributions are welcome! To contribute to this project:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature).

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature/your-feature).

Create a new Pull Request.
