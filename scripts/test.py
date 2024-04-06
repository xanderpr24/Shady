import medspacy
from medspacy.ner import TargetMatcher, TargetRule
from spacy.tokens import Span

def out(input: str) -> str:
    nlp = medspacy.load()

    target_matcher = nlp.get_pipe("medspacy_target_matcher")

    # ICD Compatibility
    Span.set_extension("icd10", default="", force=True)

    # Target rules for medical conditions
    target_rules = [
        TargetRule("Diabetes", category="PROBLEM", 
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
        TargetRule("Fungal Infection", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["itching", "skin_rash", "nodal_skin_eruptions", "dischromic_patches"]}},
                ],
                attributes={"icd10": "B49"}),
        TargetRule("Allergy", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["continuous_sneezing", "shivering", "chills", "watering_from_eyes"]}},
                ],
                attributes={"icd10": "T78.4"}),
        TargetRule("GERD", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["stomach_pain", "acidity", "ulcers_on_tongue", "vomiting", "cough", "chest_pain"]}},
                ],
                attributes={"icd10": "K21.9"}),
        TargetRule("Chronic Cholestasis", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["itching", "vomiting", "yellowish_skin", "nausea", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes"]}},
                ],
                attributes={"icd10": "K74.60"}),
        TargetRule("Drug Reaction", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["itching", "skin_rash", "stomach_pain", "burning_micturition", "spotting_urination"]}},
                ],
                attributes={"icd10": "T88.7"}),
        TargetRule("Peptic Ulcer Disease", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["vomiting", "indigestion", "abdominal_pain", "passage_of_gases", "internal_itching"]}},
                ],
                attributes={"icd10": "K25.9"}),
        TargetRule("AIDS", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["muscle_wasting", "patches_in_throat", "high_fever", "extra_marital_contacts"]}},
                ],
                attributes={"icd10": "B20"}),
        TargetRule("Malaria", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["chills", "vomiting", "high_fever", "sweating", "headache", "nausea", "muscle_pain", "diarrhoea"]}},
                ],
                attributes={"icd10": "B54"}),
        TargetRule("Chickenpox", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["itching", "skin_rash", "fatigue", "lethargy", "high_fever", "headache", "loss_of_appetite", "mild_fever", "swelled_lymph_nodes", "malaise", "red_spots_over_body"]}},
                ],
                attributes={"icd10": "B01.9"}),
        TargetRule("Dengue", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["skin_rash", "chills", "joint_pain", "vomiting", "fatigue", "high_fever", "headache", "nausea", "loss_of_appetite", "pain_behind_the_eyes", "back_pain", "muscle_pain", "red_spots_over_body"]}},
                ],
                attributes={"icd10": "A90"}),
        TargetRule("Typhoid", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["high_fever", "abdominal_pain", "muscle_pain", "malaise", "diarrhoea", "constipation", "headache"]}},
                ],
                attributes={"icd10": "A01.0"}),
        TargetRule("Hepatitis B", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["itching", "vomiting", "fatigue", "yellowish_skin", "dark_urine", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes", "fluid_overload"]}},
                ],
                attributes={"icd10": "B16.9"}),
        TargetRule("Hepatitis C", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["fatigue", "yellowish_skin", "dark_urine", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes", "swelling_of_stomach", "distention_of_abdomen", "fluid_overload"]}},
                ],
                attributes={"icd10": "B18.2"}),
        TargetRule("Hepatitis D", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["fatigue", "yellowish_skin", "dark_urine", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes", "swelling_of_stomach", "distention_of_abdomen", "fluid_overload"]}},
                ],
                attributes={"icd10": "B18.1"}),
        TargetRule("Hepatitis E", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["fatigue", "yellowish_skin", "dark_urine", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes", "swelling_of_stomach", "distention_of_abdomen", "fluid_overload"]}},
                ],
                attributes={"icd10": "B17.1"}),
        TargetRule("Alcoholic Hepatitis", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["vomiting", "yellowish_skin", "dark_urine", "abdominal_pain", "yellowing_of_eyes", "fluid_overload", "swelling_of_stomach", "distention_of_abdomen"]}},
                ],
                attributes={"icd10": "K70.30"}),
        TargetRule("Tuberculosis", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["coughing_up_blood", "chest_pain", "fatigue", "weight_loss", "chills", "malaise", "sweat"]}},
                ],
                attributes={"icd10": "A15"}),
        TargetRule("Common Cold", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["continuous_sneezing", "chills", "fatigue", "cough", "high_fever", "sweating", "headache", "nausea", "throat_irritation"]}},
                ],
                attributes={"icd10": "J00"}),
        TargetRule("Pneumonia", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["chills", "cough", "fatigue", "high_fever", "sweating", "chest_pain", "breathing_difficulty", "fast_heart_rate", "rapid_breathing", "sputum", "phlegm"]}},
                ],
                attributes={"icd10": "J18.9"}),
        TargetRule("Dimorphic Hemmorhoids(piles)", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["pain_during_bowel_movements", "bloody_stool", "irritation_in_anus", "pain_in_anus", "lumps_in_anus", "painful_bowel_movements", "pain_in_anal_region"]}},
                ],
                attributes={"icd10": "K64.9"}),
        TargetRule("Heart Attack", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["chest_pain", "pressure_in_chest", "shortness_of_breath", "dizziness", "fainting", "heavy_feeling_in_chest", "sweating"]}},
                ],
                attributes={"icd10": "I21.9"}),
        TargetRule("Varicose Veins", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["swollen_veins", "bruising", "bleeding", "itching", "painful_legs", "painful_walk", "edema"]}},
                ],
                attributes={"icd10": "I83.90"}),
        TargetRule("Hypothyroidism", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["fatigue", "weight_gain", "cold_hands_and_feets", "mood_swings", "depression", "irritability", "abnormal_menstruation", "swollen_legs", "swollen_joints", "brittle_nails", "swollen_extremeties"]}},
                ],
                attributes={"icd10": "E03.9"}),
        TargetRule("Hyperthyroidism", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["fatigue", "weight_loss", "restlessness", "mood_swings", "irritability", "abnormal_menstruation", "swollen_legs", "swollen_joints", "brittle_nails", "swollen_extremeties"]}},
                ],
                attributes={"icd10": "E05.90"}),
        TargetRule("Hypoglycemia", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["fatigue", "anxiety", "sweating", "palpitations", "headache", "dizziness", "loss_of_consciousness", "irritability", "blurred_and_distorted_vision", "slurred_speech", "drowsiness", "confusion", "unsteadiness"]}},
                ],
                attributes={"icd10": "E16.2"}),
        TargetRule("Osteoarthristis", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["joint_pain", "neck_pain", "knee_pain", "hip_joint_pain", "swelling_joints", "movement_stiffness", "painful_walking"]}},
                ],
                attributes={"icd10": "M15.9"}),
        TargetRule("Arthritis", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["pain_in_joints", "swelling_joints", "movement_stiffness", "painful_walking"]}},
                ],
                attributes={"icd10": "M19"}),
        TargetRule("Gastroenteritis", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["vomiting", "diarrhea", "dehydration", "nausea", "stomach_pain", "fever", "bloody_stool"]}},
                ],
                attributes={"icd10": "A09"}),
        TargetRule("Bronchial Asthma", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["breathlessness", "continuous_coughing", "wheezing", "chest_pain", "fatigue", "high_fever"]}},
                ],
                attributes={"icd10": "J45.909"}),
        TargetRule("Hypertension", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["headache", "nausea", "chest_pain", "dizziness", "blurred_vision"]}},
                ],
                attributes={"icd10": "I10"}),
        TargetRule("Migraine", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["acidity", "indigestion", "headache", "blurred_vision", "excessive_hunger", "nausea", "muscle_weakness", "stiff_neck"]}},
                ],
                attributes={"icd10": "G43.9"}),
        TargetRule("Cervical Spondylosis", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["back_pain", "weakness_in_limbs", "neck_pain", "dizziness", "loss_of_balance", "stiffness_in_neck"]}},
                ],
                attributes={"icd10": "M47.814"}),
        TargetRule("Paralysis (brain hemorrhage)", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["headache", "vomiting", "weakness_of_one_body_side", "altered_sensorium", "unconsciousness", "internal_itching", "palpitations"]}},
                ],
                attributes={"icd10": "I64"}),
        TargetRule("Jaundice", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["itching", "fatigue", "yellowish_skin", "dark_urine", "nausea", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes"]}},
                ],
                attributes={"icd10": "R17"}),
        TargetRule("Malaria", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["chills", "vomiting", "high_fever", "sweating", "headache", "nausea", "muscle_pain", "diarrhoea"]}},
                ],
                attributes={"icd10": "B54"}),
        TargetRule("Chicken pox", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["itching", "skin_rash", "fatigue", "lethargy", "high_fever", "headache", "loss_of_appetite", "mild_fever", "swelled_lymph_nodes", "malaise", "red_spots_over_body"]}},
                ],
                attributes={"icd10": "B01.9"}),
        TargetRule("Dengue", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["skin_rash", "chills", "joint_pain", "vomiting", "fatigue", "high_fever", "headache", "nausea", "loss_of_appetite", "pain_behind_the_eyes", "back_pain", "muscle_pain", "red_spots_over_body"]}},
                ],
                attributes={"icd10": "A90"}),
        TargetRule("Typhoid", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["high_fever", "abdominal_pain", "muscle_pain", "malaise", "diarrhoea", "constipation", "headache"]}},
                ],
                attributes={"icd10": "A01.0"}),
        TargetRule("Hepatitis A", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["fatigue", "yellowish_skin", "dark_urine", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes", "swelling_of_stomach", "distention_of_abdomen", "fluid_overload"]}},
                ],
                attributes={"icd10": "B15.9"}),
        TargetRule("Hepatitis B", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["itching", "vomiting", "fatigue", "yellowish_skin", "dark_urine", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes", "fluid_overload"]}},
                ],
                attributes={"icd10": "B16.9"}),
        TargetRule("Hepatitis C", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["fatigue", "yellowish_skin", "dark_urine", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes", "swelling_of_stomach", "distention_of_abdomen", "fluid_overload"]}},
                ],
                attributes={"icd10": "B18.2"}),
        TargetRule("Hepatitis D", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["fatigue", "yellowish_skin", "dark_urine", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes", "swelling_of_stomach", "distention_of_abdomen", "fluid_overload"]}},
                ],
                attributes={"icd10": "B18.1"}),
        TargetRule("Hepatitis E", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["fatigue", "yellowish_skin", "dark_urine", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes", "swelling_of_stomach", "distention_of_abdomen", "fluid_overload"]}},
                ],
                attributes={"icd10": "B17.1"}),
        TargetRule("Alcoholic hepatitis", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["vomiting", "yellowish_skin", "dark_urine", "abdominal_pain", "yellowing_of_eyes", "fluid_overload", "swelling_of_stomach", "distention_of_abdomen"]}},
                ],
                attributes={"icd10": "K70.30"}),
        TargetRule("Tuberculosis", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["coughing_up_blood", "chest_pain", "fatigue", "weight_loss", "chills", "malaise", "sweat"]}},
                ],
                attributes={"icd10": "A15"}),
        TargetRule("Common Cold", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["continuous_sneezing", "chills", "fatigue", "cough", "high_fever", "sweating", "headache", "nausea", "throat_irritation"]}},
                ],
                attributes={"icd10": "J00"}),
        TargetRule("Pneumonia", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["chills", "cough", "fatigue", "high_fever", "sweating", "chest_pain", "breathing_difficulty", "fast_heart_rate", "rapid_breathing", "sputum", "phlegm"]}},
                ],
                attributes={"icd10": "J18.9"}),
        TargetRule("Dimorphic hemmorhoids(piles)", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["pain_during_bowel_movements", "bloody_stool", "irritation_in_anus", "pain_in_anus", "lumps_in_anus", "painful_bowel_movements", "pain_in_anal_region"]}},
                ],
                attributes={"icd10": "K64.9"}),
        TargetRule("Heart attack", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["chest_pain", "pressure_in_chest", "shortness_of_breath", "dizziness", "fainting", "heavy_feeling_in_chest", "sweating"]}},
                ],
                attributes={"icd10": "I21.9"}),
        TargetRule("Varicose veins", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["swollen_veins", "bruising", "bleeding", "itching", "painful_legs", "painful_walk", "edema"]}},
                ],
                attributes={"icd10": "I83.90"}),
        TargetRule("Hypothyroidism", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["fatigue", "weight_gain", "cold_hands_and_feets", "mood_swings", "depression", "irritability", "abnormal_menstruation", "swollen_legs", "swollen_joints", "brittle_nails", "swollen_extremeties"]}},
                ],
                attributes={"icd10": "E03.9"}),
        TargetRule("Hyperthyroidism", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["fatigue", "weight_loss", "restlessness", "mood_swings", "irritability", "abnormal_menstruation", "swollen_legs", "swollen_joints", "brittle_nails", "swollen_extremeties"]}},
                ],
                attributes={"icd10": "E05.90"}),
        TargetRule("Hypoglycemia", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["fatigue", "anxiety", "sweating", "palpitations", "headache", "dizziness", "loss_of_consciousness", "irritability", "blurred_and_distorted_vision", "slurred_speech", "drowsiness", "confusion", "unsteadiness"]}},
                ],
                attributes={"icd10": "E16.2"}),
        TargetRule("Osteoarthristis", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["joint_pain", "neck_pain", "knee_pain", "hip_joint_pain", "swelling_joints", "movement_stiffness", "painful_walking"]}},
                ],
                attributes={"icd10": "M15.9"}),
        TargetRule("Arthritis", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["pain_in_joints", "swelling_joints", "movement_stiffness", "painful_walking"]}},
                ],
                attributes={"icd10": "M19"}),
        TargetRule("Gastroenteritis", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["vomiting", "diarrhea", "dehydration", "nausea", "stomach_pain", "fever", "bloody_stool"]}},
                ],
                attributes={"icd10": "A09"}),
        TargetRule("Bronchial Asthma", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["breathlessness", "continuous_coughing", "wheezing", "chest_pain", "fatigue", "high_fever"]}},
                ],
                attributes={"icd10": "J45.909"}),
        TargetRule("Hypertension", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["headache", "nausea", "chest_pain", "dizziness", "blurred_vision"]}},
                ],
                attributes={"icd10": "I10"}),
        TargetRule("Migraine", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["acidity", "indigestion", "headache", "blurred_vision", "excessive_hunger", "nausea", "muscle_weakness", "stiff_neck"]}},
                ],
                attributes={"icd10": "G43.9"}),
        TargetRule("Cervical spondylosis", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["back_pain", "weakness_in_limbs", "neck_pain", "dizziness", "loss_of_balance", "stiffness_in_neck"]}},
                ],
                attributes={"icd10": "M47.814"}),
        TargetRule("Paralysis (brain hemorrhage)", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["headache", "vomiting", "weakness_of_one_body_side", "altered_sensorium", "unconsciousness", "internal_itching", "palpitations"]}},
                ],
                attributes={"icd10": "I64"}),
        TargetRule("Jaundice", category="PROBLEM",
                pattern=[
                    {"LOWER": {"IN": ["itching", "fatigue", "yellowish_skin", "dark_urine", "nausea", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes"]}},
                ],
                attributes={"icd10": "R17"}),
    ]

    target_matcher.add(target_rules)

    # Process the text
    # text = "I have continuous sneezing, shivering, chills, and watering from eyes."
    text = input
    doc = nlp(text)

    # Visualization
    from spacy import displacy
    # displacy.serve(doc, style="ent")
    # displacy.serve(doc, style="dep")

    # Add entities to identified_problems
    identified_problems = []
    for ent in doc.ents:
        identified_problems.append(ent.text)


    # Analysis
    import csv


    with open("C:\\Users\\shant\\Documents\\GitHub\\Shady\\scripts\\dataset.csv", 'r') as file:
        csv_reader = csv.reader(file)
        
        next(csv_reader)
        
        potential_diagnoses = {}
        for row in csv_reader:
            matched = 0
            symptoms = row[1:]
            for problem in identified_problems:
                for symptom in symptoms:
                    problemClean = problem.strip()
                    symptomClean = symptom.strip()
                    if problemClean == symptomClean:
                        matched += 1
            if matched > 0:

                potential_diagnoses[row[0]] = matched


    diagnosesOutput = "Based on the doctor's note inputted, some medical symptoms you may be experiencing are "
    for count, problem in enumerate(identified_problems):
        diagnosesOutput += problem
        if count != len(identified_problems) - 2: diagnosesOutput += ", "
        if count == len(identified_problems) - 2: diagnosesOutput += "and "
    diagnosesOutput += "\n"
    for key, value in potential_diagnoses.items():
        percentage = (value / len(potential_diagnoses)) * 100
        diagnosesOutput += "Your symptoms are {:.2f}% consistent with {}.\n".format(percentage, key)

    #potential_diagnoses = list(set(potential_diagnoses))
    # print("Potential Diagnoses:")
    # for diagnosis in potential_diagnoses:
    #     print(diagnosis)
    print(diagnosesOutput)
    return diagnosesOutput
