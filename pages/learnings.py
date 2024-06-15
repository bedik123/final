import streamlit as st
st.set_page_config(layout="wide", page_title="Learnings")

st.title("👨‍🏫 My Learnings.")
st.header('💫Quantitative Analysis')

st.image("pic/ml1.png")

st.markdown("""
#
                
Learnings from Quantitative Methods: Building Foundations for the Future

Quantitative Methods has provided me with a thorough understanding of the essential skills and procedures necessary to evaluate and interpret data.
             This course has equipped me with the capabilities needed for various applications, ranging from fundamental data analysis to more complex tasks such as 
            image classification and sentiment analysis. The knowledge and skills I acquired from this subject are certain to serve as a foundation for my future ambitions..           
            """, unsafe_allow_html=True)

with st.expander("🔧Application Learnings"):
    st.markdown("""
    
    #
                Image Classification:

One of the exciting applications of the skills learned in Quantitative Methods is image classification. By understanding how to preprocess data, train machine
                 learning models, and evaluate their performance, I can develop systems that accurately classify images. For instance, creating an image classification 
                model for identifying different types of flowers—such as roses, sunflowers, lilies, lavenders, and daisies—demonstrates how theoretical knowledge can be
                 applied to real-world problems.
                
                Sentiment Analysis:

Another practical application of the skills learned in Quantitative Methods is sentiment analysis, which involves analyzing text data to determine the sentiment behind 
                it—whether it is positive, negative, or neutral. The ability to build sentiment analyzers is immensely useful in areas like market research, customer feedback analysis,
                 and social media monitoring. By combining data analysis techniques with natural language processing (NLP), I can develop tools that help businesses understand customer 
                emotions and improve their products and services accordingly.
    """, unsafe_allow_html=True)