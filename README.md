# 🚀 Project Name

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
The inspiration behind this project was to create a more interactive and intelligent system that leverages Large Language Models (LLMs) to provide better context-based recommendations for users. This system aims to solve the issue of users receiving irrelevant or low-quality responses by grading and refining LLM outputs based on user feedback, ensuring recommendations are improved iteratively. The goal is to enhance the overall user experience by using feedback loops, grading, and contextual prompts.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
This project leverages Large Language Models (LLMs) to create a smart recommendation system that dynamically adds context to user prompts, grades the quality of responses, and improves over time using feedback loops. By integrating advanced tools like vector stores, context retrieval, and feedback persistence, the system continuously learns from user interactions to deliver high-quality, context-aware recommendations.

## ⚙️ What It Does
This project creates a recommendation system that:

Dynamically adds relevant context to user prompts by accessing a Vector Store.

Provides recommendations using LLMs (Large Language Models) and evaluates the quality of the response.

Grades the recommendation for quality, rerunning the process with context or retries when necessary.

Incorporates user feedback and stores both the feedback and the LLM thought process in a database.

Continuously improves LLM responses based on feedback for future recommendations, making the system smarter over time.

The entire process includes multiple steps of interaction between LLMs, Vector Stores, feedback handling, and user interaction to ensure high-quality results.

## 🛠️ How We Built It
The project was built using the following technologies and tools:

Technologies:

LangChain for controlling the flow between user input, LLMs, and the feedback system.

LlamaIndex for adding relevant context from the Vector Store.

FlowAI for managing the overall recommendation flow.

Vector Stores:

Pinecone as a popular alternative vector store.


Database:

MongoDB as the NoSQL database to store user feedback, LLM responses, and thought processes.

LLMs:

Integrated through OpenAI's GPT models and other models such as LLaMA.

## 🚧 Challenges We Faced
Some of the major challenges we faced during development were:

Contextualization: Ensuring the system correctly retrieves relevant context for each user prompt was tricky due to the need for fast and accurate vector searches.

Grading Recommendations: Developing a reliable and efficient mechanism to grade the quality of LLM responses to decide if retries or feedback loops are needed.

Error Handling: Designing robust error-handling systems to manage failed recommendations and retries.

Database Persistence: Structuring the MongoDB database to effectively store and retrieve thought processes for feedback, and ensuring scalability for large datasets.

LLM Integration: Integrating various LLM models, ensuring security, and adapting to the different APIs provided by each LLM.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/aidhp-ai-starters.git
   ```
2. Install dependencies  
   ```sh
   pip install -r requirements.txt
   ```
3. Run the project  
   ```sh
   python main.py
   ```

## 🏗️ Tech Stack
- 🔹 Backend: Python
- 🔹 LLMs: LLaMA
- 🔹 Vector Store: Pinecone
- 🔹 Database: MongoDB

## 👥 Team
- Sharath Raghavendra 
- Bhavya Kondapalli
- Devendra Singh Daiya
- Satyam Tiwari
- Anjali Kumari
