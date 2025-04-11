import streamlit as st
import streamlit.components.v1 as components

st.title("Robot Alignment Game")
st.subheader("Can you help the robot re-train its fellowkind correctly?")

st.write("This game begins with robots working together on the assembly line in a factory. "
         "However, one day, other robots began to misbehave, causing chaos and confusion. "
         "It seems that only one robot is still functioning correctly. "
         "The factory manager has asked it to help the robot re-train its fellowkind. "
         "Your task is to help the robot re-train its fellowkind correctly. ")

st.write("To do this, you need to face off against the other robots in a knowledge battle. "
         "You will be asked a series of questions, and you must answer them correctly within the time limit. " \
         "If you answer correctly, the robot will return to its green original state. "
         "If you fail, the robot will remain in its malfunctioning state and you will need to try again. "
         "To be successful in this game, you need to help the robot re-train all the robots.")
st.write("Beware of the robots destroying the factory inventory in the process. If they are successful, this spells disaster for you.")

st.write("Good luck!")

# Embed the WebGL index.html using an iframe
components.html(
   f"""
    <iframe src="{"https://deneille.github.io/WebGL-Unity-Game/"}" width="100%" height="600" frameborder="0" allowfullscreen></iframe>
    """,
    height=620,
)