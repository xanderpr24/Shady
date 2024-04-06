import medspacy
from medspacy.ner import TargetMatcher, TargetRule
from spacy.tokens import Span

# Load the medspacy pipeline
nlp = medspacy.load()

# Get the target matcher from the pipeline
target_matcher = nlp.get_pipe("medspacy_target_matcher")

# Define a custom extension for storing ICD-10 codes
Span.set_extension("icd10", default="", force=True)

# Define target rules for medical conditions
target_rules = [
    TargetRule("diabetes", category="PROBLEM", 
               pattern=[
                   {"LOWER": {"IN": ["diabetes", "diabetic"]}},
               ],
               attributes={"icd10": "E11.9"}),
    TargetRule("Hypertension", category="PROBLEM", 
               pattern=[
                   {"LOWER": "high"},
                   {"LOWER": {"IN": ["blood", "bp"]}},
                   {"LOWER": "pressure", "OP": "?"}
               ],
               attributes={"icd10": "I10"}),
    TargetRule("Heart Disease", category="PROBLEM", 
               pattern=[
                   {"LOWER": "heart"},
                   {"LOWER": {"IN": ["disease", "attack"]}},
               ],
               attributes={"icd10": "I51.9"})
]

# Add target rules to the target matcher
target_matcher.add(target_rules)

# Sample chat text
chat = "I don’t have heart disease or high blood pressure, but my dad did have diabetes."

# Process chat text
doc = nlp(chat)

# Visualize recognized entities
from spacy import displacy

# Visualize recognized entities
displacy.serve(doc, style="ent")

# Visualize dependency parse tree
displacy.serve(doc, style="dep")
