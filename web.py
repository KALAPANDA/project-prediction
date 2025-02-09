import os
import pickle  # Pre-trained model
import streamlit as st  # Web app
from streamlit_option_menu import option_menu


st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon='🩺')






# Load models
diabetes_model = pickle.load(open(r"C:\Users\soura\Desktop\project\training_models\diabetes_model.sav", 'rb'))
heart_model = pickle.load(open(r"C:\Users\soura\Desktop\project\training_models\heart_model.sav", 'rb'))
park_model = pickle.load(open(r"C:\Users\soura\Desktop\project\training_models\park_model.sav", 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreak System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson’s Prediction'],
                           menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the Person')

    # Button for prediction
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [float(Pregnancies), float(Glucose), float(BloodPressure), 
                      float(SkinThickness), float(Insulin), float(BMI), 
                      float(DiabetesPedigreeFunction), float(Age)]

        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


elif selected == 'Heart Disease Prediction': 
    st.title('Heart Disease Prediction using Machine Learning')

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (1 = Male, 0 = Female)')
    with col3:
        cp = st.text_input('Chest Pain Type (0-3)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Cholesterol Level')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar (>120 mg/dl, 1 = True, 0 = False)')
    with col1:
        restecg = st.text_input('Resting ECG Results (0-2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = Yes, 0 = No)')
    with col1:
        oldpeak = st.text_input('ST Depression (oldpeak)')
    with col2:
        slope = st.text_input('Slope of Peak Exercise ST Segment (0-2)')
    with col3:
        ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy (0-4)')
    with col1:
        thal = st.text_input('Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect, 3 = Unknown)')

# Button for prediction
    diab_diagnosis = ''
    if st.button('Heart Test Result'):
        user_input = [float(age), float(sex), float(cp), 
                      float(trestbps), float(chol), float(fbs), 
                      float(restecg), float(thalach),float(exang),float(oldpeak),float(slope),float(ca),float(thal)]

        diab_prediction = heart_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person has heart disease'
        else:
            diab_diagnosis = 'The person does not have heart disease'

    st.success(diab_diagnosis)

elif selected == "Parkinson’s Prediction":
    st.title("Parkinson’s Disease Prediction using Machine Learning")

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        mdvp_fo = st.text_input("MDVP:Fo(Hz)")
        mdvp_jitter_percent = st.text_input("MDVP:Jitter(%)")
        mdvp_rap = st.text_input("MDVP:RAP")
        jitter_ddp = st.text_input("Jitter:DDP")
        shimmer_apq3 = st.text_input("Shimmer:APQ3")
        shimmer_apq5 = st.text_input("Shimmer:APQ5")
        shimmer_dda = st.text_input("Shimmer:DDA")
        nhr = st.text_input("NHR")
    
    with col2:
        mdvp_fhi = st.text_input("MDVP:Fhi(Hz)")
        mdvp_jitter_abs = st.text_input("MDVP:Jitter(Abs)")
        mdvp_ppq = st.text_input("MDVP:PPQ")
        mdvp_shimmer = st.text_input("MDVP:Shimmer")
        mdvp_apq = st.text_input("MDVP:APQ")
        mdvp_shimmer_db = st.text_input("MDVP:Shimmer(dB)")
        hnr = st.text_input("HNR")
        rpde = st.text_input("RPDE")

    with col3:
        mdvp_flo = st.text_input("MDVP:Flo(Hz)")
        spread1 = st.text_input("Spread1")
        spread2 = st.text_input("Spread2")
        dfa = st.text_input("DFA")
        d2 = st.text_input("D2")
        ppe = st.text_input("PPE")   

    # Button for prediction
    parkinson_diagnosis = ''
    if st.button('Parkinson Test Result'):
        user_input = [float(mdvp_fo), float(mdvp_fhi), float(mdvp_flo), 
                      float(mdvp_jitter_percent), float(mdvp_jitter_abs), 
                      float(mdvp_rap), float(mdvp_ppq), float(jitter_ddp), 
                      float(mdvp_shimmer), float(mdvp_shimmer_db), 
                      float(shimmer_apq3), float(shimmer_apq5), 
                      float(mdvp_apq), float(shimmer_dda), 
                      float(nhr), float(hnr), float(rpde), float(dfa), 
                      float(spread1), float(spread2), float(d2), float(ppe)
                     ]

        parkinson_prediction = park_model.predict([user_input])
        if parkinson_prediction[0] == 1:
            parkinson_diagnosis = 'The person has Parkinson’s disease'
        else:
            parkinson_diagnosis = 'The person does not have Parkinson’s disease'

    st.success(parkinson_diagnosis)
