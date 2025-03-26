# LLM Recommendation System

This project implements a recommendation system using Large Language Models (LLMs) with vector store context retrieval and feedback collection.

## Features
- Interacts with LLMs (like OpenAI)
- Retrieves context from a vector store (Pinecone, Qdrant)
- Collects and stores user feedback
- Grades recommendations and retries if the quality is low

## Folder Structure
├── code/src/ ├── code/config/ ├── code/tests/ ├── code/requirements.txt ├── code/README.md └── .gitignore


## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
