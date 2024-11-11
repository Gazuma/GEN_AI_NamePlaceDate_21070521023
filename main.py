import spacy
import re
import json

# Load spacy's English model for POS tagging
nlp = spacy.load("en_core_web_sm")

# Regular expression pattern to match common date formats
date_pattern = r'\b(?:\d{1,2}[/-])?(?:\d{1,2}[/-])?\d{2,4}\b|\b(?:\d{1,2}\s)?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s\d{1,2},?\s\d{2,4}\b'

#Loading JSON file of cities data
with open('cities2.json', 'r') as file:
    cities = json.load(file)
    known_places = set()
    # Access and print the city data
    for city in cities:
        known_places.add(city['name'])


# Function to extract names, places, and dates
def extract_entities(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    #POS Tagging
    doc = nlp(text)

    #Extracting names from POS
    names = [token.text for token in doc if token.pos_ == "PROPN"]

    #Extract dates using Regular Expression
    dates = re.findall(date_pattern, text)

    #Extract places by searching set of cities
    places = [word for word in text.split() if word in known_places]

    return names, places, dates

# Specify the path to the text file
file_path = "file.txt"

# Run extraction
names, places, dates = extract_entities(file_path)

# Display the results
print("Names:", names)
print("Places:", places)
print("Dates:", dates)
