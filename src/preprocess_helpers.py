# Preprocess text (username and link placeholders)
def preprocess(text: str) -> str:
    """Function provided by model developer to replace specific words prior to tokenization.

    Args:
        text (str): Input text string to normalize.

    Returns:
        str: String after processing with text substitutions.
    """
    new_text = []
 
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)