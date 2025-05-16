from transformers import pipeline

style_generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-xl",
    tokenizer="google/flan-t5-xl",
    framework="pt"
)

def style_suggestions(input_text, outfit_style, season, occasion):
    """
    Generate a concise styling suggestion with personalization for outfit style, season, and occasion.

    Args:
        input_text (str): User-provided text description or clothing caption.
        outfit_style (str): Selected outfit style (e.g., Casual, Formal).
        season (str): Selected season (e.g., Spring, Summer, Fall, Winter).
        occasion (str): Selected occasion.

    Returns:
        str: Minimal styling suggestion (e.g., "black pair of shoes, black jeans").
    """
    context_parts = []

    if outfit_style and outfit_style.lower() != "none":
        context_parts.append(f"{outfit_style.lower()} outfit")
    if season and season.lower() != "none":
        context_parts.append(f"suitable for {season.lower()}")
    if occasion and occasion.lower() != "none":
        context_parts.append(f"tailored for {occasion.lower()}")

    context_description = " and ".join(context_parts)

    prompt = (
        f"The user wants a {context_description or 'personalized outfit'}. "
        f"Their input is: '{input_text}'. "
        f"Provide a concise styling suggestion with items like clothing and accessories, "
        f"using only the format: '<item 1>, <item 2>, <item 3>'. Avoid extra words."
    )

    response = style_generator(prompt, max_length=100, num_return_sequences=1, do_sample=False)
    return response[0]["generated_text"]