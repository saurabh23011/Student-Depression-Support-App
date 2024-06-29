import streamlit as st
import requests
import random


# Function to fetch quotes from an API
def get_motivational_quote():
    response = requests.get("https://type.fit/api/quotes")
    quotes = response.json()
    quote = random.choice(quotes)
    return f'"{quote["text"]}" - {quote["author"]}'

# Function to fetch mindfulness exercises from a static list or an API
import random

def get_mindfulness_exercise():
    exercises = [
        "1. Take deep breaths. Inhale through your nose for 4 seconds, hold for 4 seconds, and exhale through your mouth for 4 seconds. Repeat 5 times.",
        "2. Close your eyes and imagine a peaceful place. Spend a few minutes there in your mind.",
        "3. Take a moment to focus on the sounds around you. What can you hear?",
        "4. Practice gratitude. Write down three things you are grateful for today.",
        "5. Do a body scan. Starting from your toes, slowly bring your attention to each part of your body, up to your head."
    ]
    return random.choice(exercises)


# Streamlit App
st.title("Student Depression Support App")
st.header("Welcome to the Student Depression Support App")
st.write("This app is here to help you through tough times. Below are some resources and exercises that may help.")

# Section for Motivational Quotes
st.subheader("Motivational Quote")
quote = get_motivational_quote()
st.write(f"**{quote}**")

# Section for Mindfulness Exercises
st.subheader("Mindfulness Exercise")
exercise = get_mindfulness_exercise()
st.write(exercise)

# Section for Tips
st.subheader("Tips for Managing Depression")
tips = [
    "Talk to someone you trust about how you're feeling.",
    "Maintain a regular sleep schedule.",
    "Exercise regularly, even if it's just a short walk.",
    "Eat a balanced diet and stay hydrated.",
    "Take breaks and do activities you enjoy.",
    "Seek professional help if you need it."
]
st.write("\n".join(tips))

# Section for Students to Express Their Feelings
st.subheader("Express Your Feelings")
feeling = st.text_area("How are you feeling today?", "")
if st.button("Submit"):
    st.write("Thank you for sharing. Remember, it's okay to feel this way, and you are not alone.")

# Section for Multimedia Resources
st.subheader("Mindfulness Videos 1")
st.video("https://www.youtube.com/watch?v=inpok4MKVLM")

st.subheader("Mindfulness Videos 2")
st.video("https://youtu.be/VDLfVwMSbJ8?si=hNp4NUZsxWZs_s8X")

st.subheader("Mindfulness Videos 3")
st.video("https://youtu.be/GjkwrVi_Lj0?si=iw3u98gQl-tA5Vok")




st.subheader("Mindfulness Audio ")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")




# Contact Information for Professional Help
st.subheader("Professional Help")
st.write("If you need to talk to a professional, here are some resources you can contact:")
#contacts_foregn = {
    #"National Suicide Prevention Lifeline (US)": "1-800-273-8255",
   # "Crisis Text Line": "Text HOME to 741741",
    #"Samaritans (UK and Ireland)": "116 123",
   # "Lifeline (Australia)": "13 11 14"

contacts_india = {
    "National":
        "National Institute of Mental Health and Neurosciences (NIMHANS)" "080-46110007",
        "Vandrevala Foundation": "9999666555"
    
    "Delhi"
        "Samaritans Mumbai" "91-8422984528",
        "Delhi Psychiatry Centre": "9811006930"
    
    "Mumbai"
        "AASRA" "91-9820466726",
        "ICALL (Tata Institute of Social Sciences)": "9152987821"
    
    "Bangalore"
        "Sahai Helpline" "080-25497777",
        "Parivarthan": "7676602602"
    
    "Chennai" 
        "Snehi" "91-44-24640050",
        "Roshni Trust": "040-66202000"
    }

st.table(list(contacts_india.items()))

# Integration with Live Chat Support using a hypothetical service
#st.subheader("Live Chat Support")
#if st.button("Connect to a Counselor"):
   # st.write("Connecting you to a live counselor...")
import time


st.subheader("Live Chat Support")

if st.button("Connect to a Counselor"):
    st.write("Connecting you to a live counselor...")
    
    # Simulate connecting process
    with st.spinner('Connecting...'):
        time.sleep(3)  # Simulate a delay for connection
        
    st.success("Connected! You are now chatting with a counselor.")
    st.write("Counselor: Welcome! How can I assist you today?")
    
    

