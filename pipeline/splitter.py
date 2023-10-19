import re


# Define section titles
section_titles = [
    "Materials and Methods",
    "Methods",
    "Results"
]


def split_sections(text):

    # Construct regex pattern
    pattern = r'|'.join(re.escape(title) for title in section_titles)

    # Split the text into sections
    sections = re.split(pattern, text)

    # Filter out empty strings and leading/trailing whitespace
    sections = [section.strip() for section in sections if section.strip()]

    return sections


def split_sections_by_length(text):
    chunks, chunk_size = len(text), len(text)//4

    sections = [ text[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]

    return sections