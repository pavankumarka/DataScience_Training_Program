
#string collection
from collections import Counter
import re

def analyze_text_data(text_data):
    print(text_data)
    combined_text = ' '.join(text_data)

    combined_text = combined_text.lower()

    words = re.findall(r'\b\w+\b', combined_text)

    keywords = ['user', 'text', 'This', 'This'.lower()]

    keywords_count = Counter(words)

    for keyword in keywords:
        print(f'The keyword "{keyword}" appears {keywords_count[keyword]} times.')

text_data = [
"user-gen text data.",
"Analyze text data to understand preference.",
"This is an example in Python."
]
analyze_text_data(text_data)
