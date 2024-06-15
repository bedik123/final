import streamlit as st
import pickle

# Load the trained NaiveBayesClassifier from the saved file
filename = 'pages/diabetes.sav'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

st.title("Diabetes Predictor 🩺")
st.subheader("Enter patient details to predict diabetes status:")

# User inputs for patient details
age_input = st.number_input("Age:", min_value=1, max_value=120, step=1, value=30)
gender_input = st.selectbox("Gender:", ["Male", "Female"])
bmi_input = st.slider("Body Mass Index (BMI):", min_value=10.0, max_value=50.0, step=0.1, value=25.0)
hypertension_input = st.checkbox("Hypertension (Yes/No)")
heart_disease_input = st.checkbox("Heart Disease (Yes/No)")
smoking_history_input = st.selectbox("Smoking History:", ["Non-Smoker", "Ex-Smoker", "Current Smoker"])
hba1c_input = st.slider("HbA1c Level:", min_value=4.0, max_value=12.0, step=0.1, value=5.5)
blood_glucose_input = st.slider("Blood Glucose Level (mg/dL):", min_value=50, max_value=300, step=1, value=100)

# Function to make a prediction
def predict_diabetes_status(age, gender, bmi, hypertension, heart_disease, smoking_history, hba1c, blood_glucose):
    def diabetes_features(age, gender, bmi, hypertension, heart_disease, smoking_history, hba1c, blood_glucose):
        gender_binary = 1 if gender == "Male" else 0  # Encode gender as binary feature
        smoking_history_map = {"Non-Smoker": 0, "Ex-Smoker": 1, "Current Smoker": 2}  # Map smoking history to numerical values
        return {
            'age': age,
            'gender': gender_binary,
            'bmi': bmi,
            'hypertension': 1 if hypertension else 0,
            'heart_disease': 1 if heart_disease else 0,
            'smoking_history': smoking_history_map[smoking_history],
            'hba1c': hba1c,
            'blood_glucose': blood_glucose
        }

    # Apply features function to user inputs
    test_data = diabetes_features(age, gender_input, bmi, hypertension_input, heart_disease_input, smoking_history_input, hba1c, blood_glucose)

    # Use the model to get the predicted diabetes status
    prediction = loaded_model.classify(test_data)
    return prediction

# Display button and result
if st.button('Predict'):
    predicted_status = predict_diabetes_status(age_input, gender_input, bmi_input, hypertension_input, heart_disease_input, smoking_history_input, hba1c_input, blood_glucose_input)
    st.text("The predicted diabetes status based on the given patient details is:")
    st.text_area(label="", value=str(predicted_status), height=100)