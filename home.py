import streamlit as st
import joblib as jb
import numpy as np

model = jb.load('mymodel.pkl')
encoders = jb.load('myencoders.pkl')

st.set_page_config(page_title="Racism Exposure", layout="centered")
st.markdown("<h1 style='text-align: center;'>Racism Exposure Estimator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict how others may treat you based on visible and cultural traits.</p>", unsafe_allow_html=True)
st.markdown("---")

# Inputs
skin = st.selectbox('Skin Type', ['Very Fair', 'Fair', 'Medium', 'Brown', 'Dark'])
accent = st.selectbox('Accent', ['British', 'Spanish', 'African', 'Indian', 'American', 'Chinese'])
nationality = st.selectbox('Nationality', ['Nigeria', 'China', 'UK', 'Mexico', 'USA', 'India', 'Germany','Pakistan'])
origin = st.selectbox('Originated in', ['Nigeria', 'China', 'UK', 'Mexico', 'USA', 'India', 'Germany','Pakistan'])
hair_type = st.selectbox('Hair Type', ['Curly', 'Straight', 'Wavy', 'Kinky'])
bmi = st.slider('BMI', 15.0, 45.0, 20.0)

with st.expander("〽️ Don’t know your BMI?"):
    weight = st.number_input('Enter your weight (in kgs)', min_value=30.0, max_value=200.0, value=50.0)
    height = st.number_input('Enter your height (in metres)', min_value=0.5, max_value=2.5, value=1.0)
    calculated_bmi = weight / height**2
    st.warning(f'Your calculated BMI is **{calculated_bmi:.2f}**')

religious = st.radio('Wearing a Religious Symbol?', ['Yes', 'No'])
style = st.selectbox('Clothing Style', ['Casual', 'Modern', 'Streetwear', 'Traditional', 'Formal'])
gender = st.selectbox('Gender Presentation', ['Masculine', 'Feminine', 'Non-Conforming', 'Androgynous'])

# Predict
if st.button('Predict'):
    # Encode features
    skin_encoded = encoders['skin_tone'].transform([skin])[0]
    accent_encoded = encoders['accent'].transform([accent])[0]
    nationality_encoded = encoders['nationality'].transform([nationality])[0]
    origin_encoded = encoders['originated_in'].transform([origin])[0]
    hair_encoded = encoders['hair_texture'].transform([hair_type])[0]
    religious_encoded = encoders['religious_symbol_visible'].transform([religious])[0]
    style_encoded = encoders['fashion_style'].transform([style])[0]
    gender_encoded = encoders['gender_presentation'].transform([gender])[0]

    # Prepare input
    user_input = [[skin_encoded, accent_encoded, nationality_encoded, origin_encoded, hair_encoded, bmi,
                   religious_encoded, style_encoded, gender_encoded]]

    # Predict
    racism_score = model.predict(user_input)[0]
    racism_score = round(racism_score, 2)

    # Display
    st.markdown("---")
    st.warning(f"🧾 Estimated Racism Exposure: **{racism_score}%** chance")
    
    # Optional visualization
    st.progress(int(racism_score) if racism_score < 100 else 100)
