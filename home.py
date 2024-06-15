import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "ITEQMT Machine Learning Application Portfolio", "🛠️"),
        Section("Machine Learning Project UI Application", "🤖"),
        Page("pages/aboutme.py", "🤵🏻ALL ABOUT BENEDICT", "1️⃣", in_section=True),
        Page("pages/discription.py", "🧐PROJECT ALL ABOUT", "2️⃣", in_section=True),
        Page("pages/learnings.py", "📝LEARNINGS", "3️⃣", in_section=True),
    
  
        Section("PROJECTS", "💾"),
        Page("pages/predict.py", "🔎PREDICTION", "1️⃣", in_section=True),
        Page("pages/sentiment.py", "📌SENTIMENT ANALYZER", "2️⃣", in_section=True),
        Page("pages/image.py", "🐾IMAGE CLASSIFICATION", "3️⃣", in_section=True),


         Section("SOURCE CODE", "💾"),
        Page("pages/predict_src.py", "🌐PREDICTION SRC", "1️⃣", in_section=True),
        Page("pages/sentiment_src.py", "🌐SENTIMENT ANALYZER SRC", "2️⃣", in_section=True),
        Page("pages/image_src.py", "🌐IMAGE CLASSIFICATION SRC", "3️⃣", in_section=True),
    

    ]
)

hide_pages(["Thank you"])

st.markdown("### 👨‍🔧 Project Presented by: ")
st.header("🤵🏻BELENCION, BENEDICT A. - BSIS 3B")

st.image("./pic/p2.jpg")


st.info("Visit the project [Github](https://github.com/koalatech/streamlit_web_app)")
st.info("👨‍🔧 Please take note when on streamlit.app the [Image Classification] pages are not working due to Memory Limitation of 'Free Tier' hosting of Streamlit") 
st.markdown("---")


st.markdown("""
### 👨‍🎓 Benefits of Streamlit application

##### 👨‍👦‍👦 Streamlit!

* 1. Ease of Use
Simple and Intuitive API: Streamlit allows you to create web apps with just a few lines of Python code. It has a straightforward API that doesn't require knowledge of web development.
No Frontend Experience Needed: You can build interactive web applications without having to write HTML, CSS, or JavaScript.
* 2. Rapid Development
Quick Prototyping: Streamlit enables fast development and quick iterations, which is ideal for prototyping and experimenting with data.
Real-Time Updates: The app updates in real-time as you modify your code, providing immediate feedback.
* 3. Data Visualization
Built-in Widgets: Streamlit includes a variety of widgets (like sliders, buttons, and text inputs) for building interactive user interfaces.
Seamless Integration with Python Libraries: It integrates smoothly with popular data visualization libraries such as Matplotlib, Plotly, Altair, and Bokeh, allowing you to visualize data effortlessly.
* 4. Interactivity
User Inputs: You can easily add interactive elements that allow users to input data, which can then be processed and visualized in real-time.
Dynamic Content: The app can dynamically update its content based on user interactions without requiring a page reload.
* 5. Deployment and Sharing
Easy Sharing: Streamlit apps can be easily shared with others by simply deploying them on platforms like Streamlit Cloud, Heroku, or other cloud services.
Lightweight and Fast: The apps are lightweight and load quickly, providing a smooth user experience.


##### 👨‍🔧 More Content

   Machine learning (ML) is a branch of artificial intelligence (AI) that involves the development of algorithms and statistical models that enable computers to perform tasks without explicit instructions. Instead, these systems learn and improve from experience by identifying patterns and making decisions based on data. Here are some key aspects of machine learning:

* 1. Core Concepts

Algorithms: The set of rules or procedures used to perform a task or solve a problem. In ML, these algorithms allow computers to learn from and make predictions or decisions based on data.

Models: Mathematical representations of real-world processes created by training algorithms on data. Models are used to make predictions or classifications.

* 2. Types of Machine Learning
            
Supervised Learning: Involves training a model on a labeled dataset, meaning the data comes with input-output pairs. The goal is for the model to learn to predict the output from the input. Common algorithms include linear regression, logistic regression, and support vector machines.

Unsupervised Learning: Involves training a model on data without labeled responses. The goal is to identify hidden patterns or intrinsic structures in the input data. Common algorithms include clustering (e.g., k-means) and association analysis.

Semi-Supervised Learning: Combines a small amount of labeled data with a large amount of unlabeled data during training. This approach can improve learning accuracy.

Reinforcement Learning: Involves training an agent to make a sequence of decisions by rewarding it for good decisions and penalizing it for bad ones. It’s commonly used in areas like robotics, game playing, and automated trading.

* 3. Applications of Machine Learning
            

Image and Speech Recognition: Identifying objects in images or converting spoken words into text.

Natural Language Processing (NLP): Enabling machines to understand and respond to human language, such as chatbots and translation services.

Recommendation Systems: Suggesting products, services, or content to users based on their behavior and preferences, such as in e-commerce or streaming services.

Predictive Analytics: Forecasting future events based on historical data, used in finance, healthcare, and supply chain management.

Autonomous Systems: Developing self-driving cars, drones, and robotic systems.
### 🔎 Overview""", unsafe_allow_html=True)


st.image("./pic/s1.png")


st.markdown("""
 Streamlit is a powerful tool for creating interactive web applications with ease, and the possibilities for what you can build with it are endless. This sample application demonstrates just a glimpse of what's possible. With Streamlit, you can create dynamic and engaging applications for a variety of purposes, including data visualization, machine learning demos, interactive dashboards, and more.
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
