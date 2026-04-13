from endee_store import search_incident, add_incident

def agent(query):
    print(f"\n[CareerAI Agent] Analyzing: '{query}'...")

    # 1. RETRIEVAL: Search Endee for the closest career match
    results = search_incident(query)

    # 2. AUGMENTATION: Format the retrieved data into a readable response
    response = format_response(results)

    # 3. AUTO-LEARNING: Log the query so you can improve the database later
    # This keeps your 'incidents' index growing!
    add_incident(query, "New Career Query", f"User searched for: {query}")

    return response

# ---------------- FORMAT OUTPUT (RAG Logic) ----------------
def format_response(results):
    if not results or len(results) == 0:
        return " I couldn't find a specific career match for that. Try searching for 'Cloud', 'Frontend', or 'Security'."

    output = " **Best Career Match Found:**\n"
    output += "-----------------------------------\n"

    # Endee returns a list of matches. We take the top one (index 0).
    top_hit = results[0]
    
    # Extract metadata we stored earlier
    metadata = top_hit.get('metadata', {})
    role = metadata.get('problem', 'Unknown Role')
    path = metadata.get('solution', 'Path details coming soon.')
    desc = metadata.get('explanation', 'Professional career path.')

    output += f" **Role:** {role}\n"
    output += f" **Learning Path:** {path}\n"
    output += f" **Description:** {desc}\n"
    output += "-----------------------------------\n"
    output += " *Tip: Focus on these skills to get hired fast!*"

    return output
