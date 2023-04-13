# add the layout of the homepage with a photo
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
import time

def home():
    img = Image.open("cover.jpeg")
    st.image(img,width=450,use_column_width=True)
    audio_file = open('bg_song.mp3', 'rb')
    # audio_bytes = audio_file.read()
    st.text("Can Play audio")
    st.audio(audio_file)

    st.subheader("A Boys Hostel tour by our frind Ganesh Revanth : ")
    st.video("https://www.youtube.com/watch?v=1OVI1TlGEho")
    # components.html(
    #     """
    #     <div>
    #     <audio controls autoplay>
    #     <source src="bg_song.mp3" type="audio/mpeg">
    #     Your browser does not support the audio tag.
    #     </audio>
    #     </div>
    #     """
    # )