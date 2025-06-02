import streamlit as st

st.set_page_config(page_title="About", layout="centered")

st.markdown("""
<style>
h1 {
    text-align: center;
    font-size: 2.5em;
    color: #f4c430;
}
h5 {
    text-align: center;
}
p {
    font-size: 1.1em;
    text-align: justify;
}
.highlight {
    color: #f4c430;
    font-weight: bold;
}
.box {
    background-color: #1e1e1e;
    padding: 1.2em;
    border-radius: 10px;
    color: #f0f0f0;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<h1>About This Project</h1>", unsafe_allow_html=True)
st.markdown("""
<div class="box">
<p>
This project aims to shed light on the subtle and overt ways individuals might experience <span class="highlight">racism or bias</span> based on personal characteristics such as skin tone, accent, nationality, and more.
</p>

<p>
Using machine learning, we've developed a predictive model that estimates an individual's likelihood of facing discrimination. The goal is not to promote division, but to <span class="highlight">raise awareness</span> and provoke thoughtful discussion about unconscious bias and systemic inequities.
</p>

<p>
The dataset was crafted with <span class="highlight">genuine research and careful consideration</span>. It does not include fabricated or biased data points. The model reflects trends—not moral truths—and should not be used to label individuals or make real-world decisions about people.
</p>

<p>
<span class="highlight">⚠️ This is a delicate topic.</span> We urge all users to approach this tool with empathy and understanding. Our intention is to educate, not stereotype.
</p>

<p>
Key aspects of this model:
<ul>
<li>Skin tone, nationality, and accent are the strongest influencing factors</li>
<li>Other features like BMI, fashion style, and gender presentation were included based on sociological studies</li>
<li>No personal or sensitive real-user data was used—this is a <span class="highlight">simulated environment</span> built for educational use</li>
</ul>
</p>
</div>
""", unsafe_allow_html=True)
st.markdown('---')
st.markdown("<h1>⚙️ Working of the Project</h1>", unsafe_allow_html=True)
st.markdown("""
<div class="box">
<p>
The model is built using a supervised machine learning approach. Here's a high-level overview of the steps followed:
</p>

<ul>
<li><span class="highlight">Feature Preparation:</span> All user traits (like skin tone, accent, etc.) were encoded into numerical values using Label Encoding.</li>
<li><span class="highlight">Splitting:</span> The data was split into training and testing sets using an 80-20 ratio.</li>
<li><span class="highlight">Model Comparison:</span> Various regression models were compared using the <code>LazyRegressor</code> library to find the best performing model quickly.</li>
<li><span class="highlight">Final Model:</span> <code>LightGBM Regressor</code> (LGBM) was chosen for its strong accuracy and performance with tabular data.</li>
<li><span class="highlight">Evaluation:</span> Model performance was measured using RMSE (5.87), MSE (34.56), and R² Score (0.89).</li>
<li><span class="highlight">Persistence:</span> The trained model and encoders were saved using <code>joblib</code> so they can be used in the Streamlit web app.</li>
</ul>

<p>
The model outputs a percentage likelihood of experiencing racism, purely based on statistical patterns found in the data—not absolute predictions.
</p>

<p>
Ultimately, we hope this tool inspires introspection and helps advocate for a fairer, more inclusive world.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown('---')
st.markdown("""
    <h5>Created by <code>Syed Ashtar Ali Zaidi</code> & <code>Muhammad Arham Tahir</code></h5>
""", unsafe_allow_html=True)


