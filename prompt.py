def optimize_prompt(prompt):
    filler_words = ["just", "really", "very", "actually"]  # List of filler words

    # Remove filler words from the prompt
    optimized_prompt = ' '.join(word for word in prompt.split() if word.lower() not in filler_words)

    # Simplify sentence structures
    sentences = optimized_prompt.split(".")
    simplified_sentences = [s.strip() for s in sentences if s.strip()]
    optimized_prompt = ". ".join(simplified_sentences)

    # Use pronouns
    pronoun_mapping = {"programming languages": "them", "section": "it"}
    for key, value in pronoun_mapping.items():
        optimized_prompt = optimized_prompt.replace(key, value)

    return optimized_prompt

# Example usage
prompt = "write a code in python to make a pie chart of given input of programming languages with their popularity and have section with distinct color and also make one section pop out"
optimized_prompt = optimize_prompt(prompt)
print(optimized_prompt)
