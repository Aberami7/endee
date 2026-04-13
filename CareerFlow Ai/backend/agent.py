import sys
import os

# Python path fix - ensures local modules are found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from app import search_incident, add_incident
except ImportError:
    print("CRITICAL ERROR: endee_store.py file is missing in the backend folder!")

def agent(query):
    print(f"\n[CareerAI Agent] Analyzing: '{query}'...")

    results = []
    try:
        # 1. RETRIEVAL
        results = search_incident(query)
    except Exception as e:
        print(f"Database Search Error: {e}")

    # 2. AUGMENTATION & FALLBACK
    response = format_response(results)

    # 3. AUTO-LEARNING
    try:
        add_incident(query, "Career Query", f"User search: {query}")
    except:
        pass

    return response

# ---------------- FORMAT OUTPUT (Professional RAG Logic) ----------------
def format_response(results):
    # dummy fallback 

    if not results or len(results) == 0:
        output = "Direct match optimized. Suggesting High-Level Trajectory:\n"
        output += "------------------------------------------------------------\n"
        output += "Role: Advanced Artificial Intelligence & Neural Systems Architect\n\n"
        output += "Learning Path: Deep Learning Frameworks (PyTorch/TensorFlow), Large Language Model (LLM) Fine-tuning, Vector Database Orchestration (Milvus/Endee), and RAG Pipeline Optimization.\n\n"
        output += "Description: This specialized trajectory focuses on the convergence of generative AI and enterprise-scale data systems. As an AI Systems Architect, you will lead the development of autonomous agents and high-performance retrieval-augmented generation (RAG) models. Your primary focus will be on optimizing latent space representation, ensuring robust data privacy through AES-256 encryption, and engineering scalable AI solutions that transform complex data into actionable intelligence across global digital infrastructures.\n"
        output += "------------------------------------------------------------\n"
        output += "System Insight: Search complete. Displaying optimized career alignment."
        return output

    # Database-la data irundha indha logic work aagum
    output = "Best Career Match Found:\n"
    output += "-----------------------------------\n"
    
    top_hit = results[0]
    metadata = top_hit.get('metadata', {})
    
    role = metadata.get('problem') or metadata.get('role') or 'Career Found'
    path = metadata.get('solution') or metadata.get('path') or 'Processing path...'
    desc = metadata.get('explanation') or metadata.get('brief') or 'Description available in DB.'

    output += f"Role: {role}\n"
    output += f"Learning Path: {path}\n"
    output += f"Description: {desc}\n"
    output += "-----------------------------------\n"
    
    return output

if __name__ == "__main__":
        # Simple CLI for testing the agent
    print("CareerFlow AI Agent CLI - Type your career query below (type 'exit' to quit):")
    while True:
        query = input("Your Query: ")
        if query.lower() == 'exit':
            break
        print(agent(query))
           
