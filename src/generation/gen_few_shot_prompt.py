"""Utility to generate a few shot prompt."""

def generate_few_shot_prompt(user_prompt, headers):
        examples = [
            {
                "user_prompt": "Fill in a table of popular programming languages and their characteristics.",
                "headers": {"columns": ["Language", "Typing Discipline", "Paradigm", "First Appeared"]},
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
                "headers": {
                    "rows": ["Solar", "Wind", "Hydro", "Geothermal"],
                    "columns": ["Cost", "Efficiency", "Environmental Impact"]
                },
                "table": """| Source     | Cost       | Efficiency | Environmental Impact      |
                            |------------|------------|------------|---------------------------|
                            | Solar      | Medium     | Medium     | Low emissions             |
                            | Wind       | Low        | High       | Minimal, land use concern |
                            | Hydro      | High       | Very High  | Ecosystem disruption      |
                            | Geothermal | Medium     | High       | Low emissions             |"""
            },
            {
                "user_prompt": "Make a table comparing planets in our solar system.",
                "headers": {
                    "rows": ["Mercury", "Venus", "Earth", "Mars"],
                    "columns": ["Diameter (km)", "Moons", "Atmosphere"]
                },
                "table": """| Planet  | Diameter (km) | Moons | Atmosphere            |
                            |---------|----------------|-------|------------------------|
                            | Mercury | 4,879          | 0     | Thin, mostly oxygen    |
                            | Venus   | 12,104         | 0     | CO₂, sulfuric acid     |
                            | Earth   | 12,742         | 1     | Nitrogen, oxygen       |
                            | Mars    | 6,779          | 2     | CO₂, thin atmosphere   |"""
            }
        ]

        prompt = "You are a helpful table-completion assistant. Given a general instruction and prescribed headers (rows, columns, or both), you must complete the table with coherent and plausible entries.\n\n"

        for ex in examples:
            prompt += f"**User Prompt:**\n{ex['user_prompt']}\n"
            ex_headers = []
            if "columns" in ex["headers"]:
                ex_headers.append("Columns: " + ", ".join(ex["headers"]["columns"]))
            if "rows" in ex["headers"]:
                ex_headers.append("Rows: " + ", ".join(ex["headers"]["rows"]))
            prompt += f"**Headers:**\n" + "\n".join(ex_headers) + "\n"
            prompt += f"**Expected Output:**\n{ex['table']}\n\n"

        # User input
        prompt += "**Your Turn:**\n"
        prompt += f"**User Prompt:**\n{user_prompt}\n"

        input_headers = []
        if "columns" in headers:
            input_headers.append("Columns: " + ", ".join(headers["columns"]))
        if "rows" in headers:
            input_headers.append("Rows: " + ", ".join(headers["rows"]))
        prompt += "**Headers:**\n" + "\n".join(input_headers) + "\n"
        prompt += "**Expected Output:**\n"

        return prompt
