import streamlit as st

st.title("About BENEDICT👦")



st.title("🖼️Self Gallery")


image_paths = ["./pic/p5.jpg", "./pic/p4.jpg",]


cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)


st.header("👨‍🎓 BELENCION, BENEDICT A.")



# Personal Information
st.header("Personal Information")
st.write("**Name:** BENEDICT BELENCION")
st.write("**Age:** 22 years old")
st.write("**Education:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY")
st.write("**Year:** 3rd year Bachelor of Science in Information Systems Student")
st.write("**Location:** Barangay cinco Silay City")

st.header("Personal Hobbies")

image_paths = ["./pic/p3.jpg", "./pic/p3.jpg", "./pic/p3.jpg"]
st.write("** My hobbies include playing basketball and experimenting with new recipes in the kitchen, combining my love for sports and culinary creativity.")
  

cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)
import streamlit as st

st.header("What makes me happy")
st.expander("")
st.markdown("""       
            Sweat drips down my face as I bounce the basketball, the sound of my shoes squeaking on the gym floor. The gym is full of energy, with my friends cheering and the other team trying to block me. I move past defenders, focused on the hoop, my heart racing with excitement. As I get to the three-point line, I feel the excitement building. I throw the ball, watching it fly through the air and land perfectly in the net. The cheers from my friends fill me with happiness and pride.
            
           """, unsafe_allow_html=True)




# import streamlit as st


# images = [
#     {"path": "./pic/us1.jpg", "caption": "Throughout my academic journey, the invaluable support of my classmates has been instrumental in shaping my growth and success. As I reflect on the myriad experiences shared with these individuals, it becomes evident that their contributions have enriched my learning, inspired me to persevere through challenges, and fostered a sense of camaraderie that transcends the classroom."},
#     {"path": "./pic/us2.jpg", "caption": "First and foremost, my classmates have served as pillars of knowledge and insight, offering diverse perspectives that have broadened my understanding of complex subjects. Whether through lively classroom discussions, collaborative projects, or late-night study sessions, their unique viewpoints have challenged my assumptions and sparked new ideas. In this dynamic exchange of thoughts and opinions, I have gained a deeper appreciation for the multifaceted nature of learning and the power of collective intelligence."},
#     {"path": "./pic/us3.jpg", "caption": "the support of my classmates has been an indispensable aspect of my academic journey, shaping my growth, inspiring my perseverance, and enriching my experience in countless ways. Together, we have navigated the challenges of academia, celebrated the joys of learning, and forged lifelong friendships that will endure far beyond the confines of the classroom. As I continue on my path, I am grateful for the privilege of learning alongside such remarkable individuals, whose kindness, generosity, and friendship have made all the difference in my journey."}
# ]


# st.title("🖼️Gallery")


# for image in images:
#     st.image(image["path"], caption=image["caption"])



st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        padding: 2em;
    }
    h1, h2 {
        color: #4CAF50;
    }
    .stText {
        font-size: 1.2em;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer or additional sections (optional)
st.write("### Thank you for visiting my profile!")
st.write("Feel free to connect and reach out if you share similar interests or have any questions.")