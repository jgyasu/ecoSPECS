def few_shot_prompt(user_prompt):
    """Generates a prompt for few-shot learning.
    Takes advantage of the fact that LLMs are few-shot learners."""
    
    examples = [
        {
            "user_prompt": "Fill in a table of popular programming languages and their characteristics.",
            "intro": "Programming languages vary in their design philosophies and usage contexts. Here's a comparison of some popular ones based on typing, paradigms, and origin dates.",
            "table": """| Language   | Typing Discipline | Paradigm              | First Appeared |
                        |------------|-------------------|------------------------|----------------|
                        | Python     | Dynamic           | Object-Oriented, Procedural | 1991           |
                        | Java       | Static            | Object-Oriented        | 1995           |
                        | JavaScript | Dynamic           | Multi-paradigm         | 1995           |
                        | C++        | Static            | Object-Oriented, Procedural | 1985           |
                        | Haskell    | Static            | Functional             | 1990           |"""
        },
        {
            "user_prompt": "Show a comparison of renewable energy sources.",
            "intro": "Renewable energy sources differ in terms of implementation cost, efficiency, and environmental footprint. The table below outlines a comparison of key options.",
            "table": """| Source     | Cost       | Efficiency | Environmental Impact      |
                        |------------|------------|------------|---------------------------|
                        | Solar      | Medium     | Medium     | Low emissions             |
                        | Wind       | Low        | High       | Minimal, land use concern |
                        | Hydro      | High       | Very High  | Ecosystem disruption      |
                        | Geothermal | Medium     | High       | Low emissions             |"""
        },
        {
            "user_prompt": "Compare different smartphone brands and their features in terms of price, performance, and camera quality.",
            "intro": "Smartphone brands differ in price, performance, and camera features. Here's a comparison based on these factors.",
            "table": """| Brand     | Price   | Performance  | Camera Quality | Operating System |
                        |-----------|---------|--------------|----------------|------------------|
                        | Apple     | High    | Very High    | Excellent      | iOS              |
                        | Samsung   | Medium  | High         | Good           | Android          |
                        | OnePlus   | Medium  | High         | Very Good      | Android          |
                        | Xiaomi    | Low     | Medium       | Fair           | Android          |"""
        }
    ]

    prompt = (
        "You are a helpful assistant. For each user prompt, first write a short, informative introduction "
        "about the subject. Then, based on your understanding of the prompt, generate a table with relevant headers (rows and columns), "
        "and fill in the table with accurate and plausible information.\n\n"
    )

    for ex in examples:
        prompt += f"**User Prompt:**\n{ex['user_prompt']}\n"
        prompt += f"**Expected Output:**\n{ex['intro']}\n{ex['table']}\n\n"

    prompt += "**Your Turn:**\n"
    prompt += f"**User Prompt:**\n{user_prompt}\n"
    prompt += "**Expected Output:**\n"

    prompt += ("For the given prompt, generate appropriate headers (rows and columns) based on the subject. "
               "Then, complete the table with relevant information. The headers should make sense according to the context of the prompt.\n")

    return prompt
