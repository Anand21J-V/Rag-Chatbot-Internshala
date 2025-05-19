
# 🧠 Rag-Chatbot-Assignment
A Retrieval-Augmented Generation (RAG) chatbot built using LangChain and the Groq API, designed to deliver intelligent, context-aware responses over custom datasets. This project was developed as part of an Internshala assignment.

---

## 📌 Table of Contents

* Overview
* Features
* Architecture
* Project Structure
* Installation
* Usage
* Customization
* License

---

## Overview

The Rag-Chatbot-Internshala project implements a chatbot that leverages Retrieval-Augmented Generation to provide accurate and contextually relevant answers to user queries. By integrating LangChain for orchestrating the retrieval and generation processes and utilizing the Groq API for efficient language model inference, the chatbot can handle domain-specific questions effectively.

---

## Features

* **Retrieval-Augmented Generation**: Combines information retrieval with language generation to produce informed responses.
* **LangChain Integration**: Utilizes LangChain to manage the retrieval and generation workflow seamlessly.
* **Groq API Utilization**: Employs the Groq API for high-performance language model inference.
* **Custom Dataset Support**: Designed to work with user-provided datasets for domain-specific applications.
* **Interactive Interface**: Includes a Streamlit-based web interface for user interaction.
* **Modular Design**: Structured for easy customization and scalability.([arXiv][1])

---

## Architecture

The chatbot's architecture follows a modular design, integrating various components to achieve efficient and accurate responses:

1. **User Interface (UI)**: Built with Streamlit, providing an interactive platform for users to input queries and receive responses.
2. **Retrieval Module**: Uses LangChain to fetch relevant documents or data segments from the custom dataset based on the user's query.
3. **Generation Module**: Leverages the Groq API to generate responses by combining the retrieved information with the user's query.
4. **Response Delivery**: Presents the generated answer to the user through the Streamlit interface.

This architecture ensures that responses are both contextually relevant and grounded in the provided dataset.

---

## Project Structure

The repository is organized as follows:

```

├── .devcontainer/           # Development container configuration
├── Project_Structure/       # Documentation or diagrams detailing project architecture
├── Setup/                   # Setup scripts and configuration files
├── data/                    # Contains the custom dataset files
├── template/                # Templates for prompts or UI components
├── chatbot.py               # Core chatbot logic integrating retrieval and generation
├── streamlit_app.py         # Streamlit application for the chatbot interface
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── LICENSE                  # MIT License
└── .gitignore               # Git ignore file
```



---

## ⚙Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Anand21J-V/Rag-Chatbot-Internshala.git
   cd Rag-Chatbot-Internshala
   ```



2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies:

   ```bash
   python3 -m venv venv
   source venv\Scripts\activate
   ```



3. **Install Dependencies**

   Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```



4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your Groq API key:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```



Ensure that the application loads environment variables from this file.

---

## Usage

To run the chatbot application:

```bash
streamlit run streamlit_app.py
```



This command will launch the Streamlit web interface in your default browser.

**Interacting with the Chatbot:**

1. Enter your query in the input field.
2. The chatbot retrieves relevant information from the custom dataset.
3. It then generates a response using the Groq API.
4. The response is displayed in the interface.([arXiv][1])
5. 
---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software in accordance with the license terms.

## Author

Anand Kumar Vishwakarma || anandvishwakarma21j@gmail.com 
---

