              CareerFlow AI – AI-Based Career Recommendation System using Endee

## 📌 Project Overview

CareerFlow AI is an intelligent system that recommends suitable career paths based on a user’s skills, interests, and preferences.
It uses **semantic search with Endee vector database** and follows a **RAG (Retrieval-Augmented Generation) approach** to match user input with relevant career options.


## 🧠 How It Works

1. User enters skills or interests (e.g., "I like coding and problem solving")
2. The system converts input into vector embeddings
3. Endee performs similarity search on stored career data (**Retrieval step in RAG**)
4. The system generates the most relevant career suggestions (**Generation step in RAG**)

If new inputs are given, the system can store them and improve over time.

## ⚙️ Tech Stack

* Python,html
* Endee (Vector Database)
* Sentence Transformers (for embeddings)
* REST API

## 💡 Features

* Semantic understanding of user skills
* Intelligent career recommendations
* Fast and scalable vector search
* Dynamic learning (stores new inputs)
* Easy to extend with more career data
* Implements **RAG (Retrieval-Augmented Generation)** for better accuracy


## 📂 Project Structure

CareerFlowAI
└── backend
  ├── main.py
  ├── agent.py
  ├── endee_store.py
  ├── requirements.txt
  └── README.md
└── frontend
  └── index.html

## 🧪 Example

**Input:**

I love math and data analysis

**Output:**

Recommended Career: Data Scientist
Reason: Matches analytical and statistical skills


## 🔥 Use Cases

* Career guidance for students
* Skill-based job recommendations
* Educational counseling systems
* AI-based mentorship tools


## 📈 Future Enhancements

* Resume upload and analysis
* Job matching integration
* Web UI (React / Flask)
* Personalized career roadmap


## 📌 Conclusion

CareerFlow AI demonstrates how **vector databases like Endee** can be used to build intelligent recommendation systems using semantic understanding.
It leverages a **RAG (Retrieval-Augmented Generation) pipeline** to improve the relevance and accuracy of career suggestions.


## 🙌 Author

Aberami
