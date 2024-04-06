import medspacy
from medspacy.ner import TargetMatcher, TargetRule
from spacy.tokens import Span

nlp = medspacy.load()

target_matcher = nlp.get_pipe("medspacy_target_matcher")

# ICD Compatibility
Span.set_extension("icd10", default="", force=True)

# Target rules for medical conditions (add more)
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
               attributes={"icd10": "I51.9"}),
    # Fungal Infection
    TargetRule("Fungal Infection", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["itching", "skin_rash", "nodal_skin_eruptions", "dischromic_patches"]}},
               ],
               attributes={"icd10": "B49"}),

    # Allergy
    TargetRule("Allergy", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["continuous_sneezing", "shivering", "chills", "watering_from_eyes"]}},
               ],
               attributes={"icd10": "T78.4"}),

    # GERD
    TargetRule("GERD", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["stomach_pain", "acidity", "ulcers_on_tongue", "vomiting", "cough", "chest_pain"]}},
               ],
               attributes={"icd10": "K21.9"}),

    # Chronic Cholestasis
    TargetRule("Chronic Cholestasis", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["itching", "vomiting", "yellowish_skin", "nausea", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes"]}},
               ],
               attributes={"icd10": "K74.60"}),

    # Drug Reaction
    TargetRule("Drug Reaction", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["itching", "skin_rash", "stomach_pain", "burning_micturition", "spotting_urination"]}},
               ],
               attributes={"icd10": "T88.7"}),

    # Peptic ulcer disease
    TargetRule("Peptic Ulcer Disease", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["vomiting", "indigestion", "abdominal_pain", "passage_of_gases", "internal_itching"]}},
               ],
               attributes={"icd10": "K25.9"}),

    # AIDS
    TargetRule("AIDS", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["muscle_wasting", "patches_in_throat", "high_fever", "extra_marital_contacts"]}},
               ],
               attributes={"icd10": "B20"}),

    # Diabetes
    TargetRule("Diabetes", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["fatigue", "weight_loss", "restlessness", "lethargy", "irregular_sugar_level", "blurred_and_distorted_vision", "obesity", "excessive_hunger", "increased_appetite", "polyuria"]}},
               ],
               attributes={"icd10": "E11.9"}),

    # Gastroenteritis
    TargetRule("Gastroenteritis", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["vomiting", "sunken_eyes", "dehydration", "diarrhoea"]}},
               ],
               attributes={"icd10": "A09"}),

    # Bronchial Asthma
    TargetRule("Bronchial Asthma", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["fatigue", "cough", "high_fever", "breathlessness", "family_history", "mucoid_sputum"]}},
               ],
               attributes={"icd10": "J45"}),

    # Hypertension
    TargetRule("Hypertension", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["headache", "chest_pain", "dizziness", "loss_of_balance", "lack_of_concentration"]}},
               ],
               attributes={"icd10": "I10"}),

    # Migraine
    TargetRule("Migraine", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["acidity", "indigestion", "headache", "blurred_and_distorted_vision", "excessive_hunger", "stiff_neck", "depression", "irritability", "visual_disturbances"]}},
               ],
               attributes={"icd10": "G43.9"}),

    # Cervical Spondylosis
    TargetRule("Cervical Spondylosis", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["back_pain", "weakness_in_limbs", "neck_pain", "dizziness", "loss_of_balance"]}},
               ],
               attributes={"icd10": "M47.812"}),

    # Paralysis (Brain Hemorrhage)
    TargetRule("Paralysis (Brain Hemorrhage)", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["vomiting", "headache", "weakness_of_one_body_side", "altered_sensorium"]}},
               ],
               attributes={"icd10": "I61"}),

    # Jaundice
    TargetRule("Jaundice", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["itching", "vomiting", "fatigue", "weight_loss", "high_fever", "yellowish_skin", "dark_urine", "abdominal_pain"]}},
               ],
               attributes={"icd10": "K71.9"}),

    # Malaria
    TargetRule("Malaria", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["chills", "vomiting", "high_fever", "sweating", "headache", "nausea", "muscle_pain", "diarrhoea"]}},
               ],
               attributes={"icd10": "B54"}),

    # Chickenpox
    TargetRule("Chickenpox", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["itching", "skin_rash", "fatigue", "lethargy", "high_fever", "headache", "loss_of_appetite", "mild_fever", "swelled_lymph_nodes", "malaise", "red_spots_over_body"]}},
               ],
               attributes={"icd10": "B01.9"}),

    # Dengue
    TargetRule("Dengue", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["skin_rash", "chills", "joint_pain", "vomiting", "fatigue", "high_fever", "headache", "nausea", "loss_of_appetite", "pain_behind_the_eyes", "back_pain", "muscle_pain", "red_spots_over_body"]}},
               ],
               attributes={"icd10": "A90"}),

    # Typhoid
    TargetRule("Typhoid", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["high_fever", "abdominal_pain", "muscle_pain", "malaise", "diarrhoea", "constipation", "headache"]}},
               ],
               attributes={"icd10": "A01.0"}),

    # Hepatitis B
    TargetRule("Hepatitis B", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["itching", "vomiting", "fatigue", "yellowish_skin", "dark_urine", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes", "fluid_overload"]}},
               ],
               attributes={"icd10": "B16.9"}),

    # Hepatitis C
    TargetRule("Hepatitis C", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["fatigue", "yellowish_skin", "dark_urine", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes", "swelling_of_stomach", "distention_of_abdomen", "fluid_overload"]}},
               ],
               attributes={"icd10": "B18.2"}),

    # Hepatitis D
    TargetRule("Hepatitis D", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["fatigue", "yellowish_skin", "dark_urine", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes", "swelling_of_stomach", "distention_of_abdomen", "fluid_overload"]}},
               ],
               attributes={"icd10": "B18.1"}),

    # Hepatitis E
    TargetRule("Hepatitis E", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["fatigue", "yellowish_skin", "dark_urine", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes", "swelling_of_stomach", "distention_of_abdomen", "fluid_overload"]}},
               ],
               attributes={"icd10": "B17.1"}),

    # Alcoholic hepatitis
    TargetRule("Alcoholic Hepatitis", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["vomiting", "yellowish_skin", "dark_urine", "abdominal_pain", "yellowing_of_eyes", "fluid_overload", "swelling_of_stomach", "distention_of_abdomen"]}},
               ],
               attributes={"icd10": "K70.30"}),

    # Tuberculosis
    TargetRule("Tuberculosis", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["chills", "vomiting", "fatigue", "cough", "high_fever", "breathlessness", "sweating", "weight_loss", "malaise", "phlegm", "chest_pain"]}},
               ],
               attributes={"icd10": "A15.9"}),

    # Common Cold
    TargetRule("Common Cold", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["continuous_sneezing", "chills", "fatigue", "cough", "high_fever", "headache", "sweating", "throat_irritation", "malaise", "phlegm", "chest_pain"]}},
               ],
               attributes={"icd10": "J00"}),

    # Pneumonia
    TargetRule("Pneumonia", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["chills", "fatigue", "cough", "high_fever", "breathlessness", "sweating", "phlegm", "chest_pain", "malaise"]}},
               ],
               attributes={"icd10": "J18.9"}),

    # Arthritis
    TargetRule("Arthritis", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["swelling_joints", "pain_in_joints", "stiffness_in_joints", "swelling_in_joints", "movement_stiffness", "pain_in_joints", "knee_swelling", "hip_joint_pain"]}},
               ],
               attributes={"icd10": "M13.9"}),

    # Hyperthyroidism
    TargetRule("Hyperthyroidism", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["fatigue", "restlessness", "sweating", "sudden_weight_loss", "nervousness", "muscle_weakness", "excessive_hunger", "irritability", "abnormal_menstruation"]}},
               ],
               attributes={"icd10": "E05.90"}),

    # Hypothyroidism
    TargetRule("Hypothyroidism", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["fatigue", "weight_gain", "cold_hands_and_feets", "mood_swings", "weight_loss", "restlessness", "lethargy", "dizziness", "irregular_menstruation", "brittle_nails", "swollen_extremeties"]}},
               ],
               attributes={"icd10": "E03.9"}),

    # Hypercholesterolemia
    TargetRule("Hypercholesterolemia", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["vomiting", "fatigue", "nausea", "pain_in_the_arms", "sweating", "dizziness", "chest_pain"]}},
               ],
               attributes={"icd10": "E78.00"}),

    # Hypoglycemia
    TargetRule("Hypoglycemia", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["fatigue", "anxiety", "sweating", "cold_sweats", "mood_swings", "headache", "nausea", "vomiting", "palpitations", "tachycardia", "irritability", "blurred_and_distorted_vision"]}},
               ],
               attributes={"icd10": "E16.2"}),

    # Osteoarthristis
    TargetRule("Osteoarthristis", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["swelling_joints", "pain_in_joints", "stiffness_in_joints", "swelling_in_joints", "movement_stiffness", "pain_in_joints", "knee_swelling", "hip_joint_pain"]}},
               ],
               attributes={"icd10": "M15.9"}),

    # (vertigo) Paroymsal Positional Vertigo
    TargetRule("(Vertigo) Paroxysmal Positional Vertigo", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["vomiting", "headache", "nausea", "spinning_movements", "loss_of_balance", "unsteadiness"]}},
               ],
               attributes={"icd10": "H81.391"}),

    # Hypoglycemia
    TargetRule("Hypoglycemia", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["fatigue", "anxiety", "sweating", "cold_sweats", "mood_swings", "headache", "nausea", "vomiting", "palpitations", "tachycardia", "irritability", "blurred_and_distorted_vision"]}},
               ],
               attributes={"icd10": "E16.2"}),

    # Acne
    TargetRule("Acne", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["skin_rash", "pus_filled_pimples", "blackheads", "scurring"]}},
               ],
               attributes={"icd10": "L70.0"}),

    # Urinary tract infection
    TargetRule("Urinary tract infection", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["burning_micturition", "continuous_feel_of_urine", "passage_of_gases", "internal_itching", "toxic_look_(typhos)", "depression", "irritability", "muscle_pain", "altered_sensorium", "red_spots_over_body"]}},
               ],
               attributes={"icd10": "N39.0"}),

    # Psoriasis
    TargetRule("Psoriasis", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["skin_rash", "joint_pain", "skin_peeling", "silver_like_dusting", "small_dents_in_nails", "inflammatory_nails"]}},
               ],
               attributes={"icd10": "L40.9"}),

    # Impetigo
    TargetRule("Impetigo", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["skin_rash", "high_fever", "yellowish_skin", "painful_red_lump", "irritation_of_eyes"]}},
               ],
               attributes={"icd10": "L01.0"}),

    # GERD
    TargetRule("GERD", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["stomach_pain", "acidity", "ulcers_on_tongue", "vomiting", "cough", "chest_pain"]}},
               ],
               attributes={"icd10": "K21.9"}),

    # Bronchial Asthma
    TargetRule("Bronchial Asthma", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["fatigue", "cough", "high_fever", "breathlessness", "family_history", "mucoid_sputum"]}},
               ],
               attributes={"icd10": "J45"}),

    # Diabetes
    TargetRule("Diabetes", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["fatigue", "weight_loss", "restlessness", "lethargy", "irregular_sugar_level", "blurred_and_distorted_vision", "obesity", "excessive_hunger", "increased_appetite", "polyuria"]}},
               ],
               attributes={"icd10": "E11.9"}),

    # Gastroenteritis
    TargetRule("Gastroenteritis", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["vomiting", "sunken_eyes", "dehydration", "diarrhoea"]}},
               ],
               attributes={"icd10": "A09"}),

    # Drug Reaction
    TargetRule("Drug Reaction", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["itching", "skin_rash", "stomach_pain", "burning_micturition", "spotting_urination"]}},
               ],
               attributes={"icd10": "T88.7"}),

    # Peptic ulcer disease
    TargetRule("Peptic Ulcer Disease", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["vomiting", "indigestion", "abdominal_pain", "passage_of_gases", "internal_itching"]}},
               ],
               attributes={"icd10": "K25.9"}),

    # AIDS
    TargetRule("AIDS", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["muscle_wasting", "patches_in_throat", "high_fever", "extra_marital_contacts"]}},
               ],
               attributes={"icd10": "B20"}),

    # Diabetes
    TargetRule("Diabetes", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["fatigue", "weight_loss", "restlessness", "lethargy", "irregular_sugar_level", "blurred_and_distorted_vision", "obesity", "excessive_hunger", "increased_appetite", "polyuria"]}},
               ],
               attributes={"icd10": "E11.9"}),

    # Gastroenteritis
    TargetRule("Gastroenteritis", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["vomiting", "sunken_eyes", "dehydration", "diarrhoea"]}},
               ],
               attributes={"icd10": "A09"}),

    # Drug Reaction
    TargetRule("Drug Reaction", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["itching", "skin_rash", "stomach_pain", "burning_micturition", "spotting_urination"]}},
               ],
               attributes={"icd10": "T88.7"}),

    # Peptic ulcer disease
    TargetRule("Peptic Ulcer Disease", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["vomiting", "indigestion", "abdominal_pain", "passage_of_gases", "internal_itching"]}},
               ],
               attributes={"icd10": "K25.9"}),

    # AIDS
    TargetRule("AIDS", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["muscle_wasting", "patches_in_throat", "high_fever", "extra_marital_contacts"]}},
               ],
               attributes={"icd10": "B20"}),

    # Diabetes
    TargetRule("Diabetes", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["fatigue", "weight_loss", "restlessness", "lethargy", "irregular_sugar_level", "blurred_and_distorted_vision", "obesity", "excessive_hunger", "increased_appetite", "polyuria"]}},
               ],
               attributes={"icd10": "E11.9"}),

    # Gastroenteritis
    TargetRule("Gastroenteritis", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["vomiting", "sunken_eyes", "dehydration", "diarrhoea"]}},
               ],
               attributes={"icd10": "A09"}),

    # Drug Reaction
    TargetRule("Drug Reaction", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["itching", "skin_rash", "stomach_pain", "burning_micturition", "spotting_urination"]}},
               ],
               attributes={"icd10": "T88.7"}),

    # Peptic ulcer disease
    TargetRule("Peptic Ulcer Disease", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["vomiting", "indigestion", "abdominal_pain", "passage_of_gases", "internal_itching"]}},
               ],
               attributes={"icd10": "K25.9"}),

    # AIDS
    TargetRule("AIDS", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["muscle_wasting", "patches_in_throat", "high_fever", "extra_marital_contacts"]}},
               ],
               attributes={"icd10": "B20"}),

    # Diabetes
    TargetRule("Diabetes", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["fatigue", "weight_loss", "restlessness", "lethargy", "irregular_sugar_level", "blurred_and_distorted_vision", "obesity", "excessive_hunger", "increased_appetite", "polyuria"]}},
               ],
               attributes={"icd10": "E11.9"}),

    # Gastroenteritis
    TargetRule("Gastroenteritis", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["vomiting", "sunken_eyes", "dehydration", "diarrhoea"]}},
               ],
               attributes={"icd10": "A09"}),

    # Drug Reaction
    TargetRule("Drug Reaction", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["itching", "skin_rash", "stomach_pain", "burning_micturition", "spotting_urination"]}},
               ],
               attributes={"icd10": "T88.7"}),

    # Peptic ulcer disease
    TargetRule("Peptic Ulcer Disease", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["vomiting", "indigestion", "abdominal_pain", "passage_of_gases", "internal_itching"]}},
               ],
               attributes={"icd10": "K25.9"}),

    # AIDS
    TargetRule("AIDS", category="PROBLEM",
               pattern=[
                   {"LOWER": {"IN": ["muscle_wasting", "patches_in_throat", "high_fever", "extra_marital_contacts"]}},
               ],
               attributes={"icd10": "B20"}),
    # New rule for symptom descriptions related to atrial fibrillation
    TargetRule("symptom_af", category="SYMPTOM",
               pattern=[
                   {"LOWER": {"IN": ["irregular", "rapid", "fluttering"]}},
                   {"LOWER": {"IN": ["heartbeat", "heart", "rhythm", "rate"]}}
               ])
]


target_matcher.add(target_rules)

# Example text
chat = "I don’t have heart disease or high blood pressure, but my dad did have diabetes. I have an irregular and often very rapid heart rhythm."

doc = nlp(chat)

# Visualization
from spacy import displacy
displacy.serve(doc, style="ent")
displacy.serve(doc, style="dep")
