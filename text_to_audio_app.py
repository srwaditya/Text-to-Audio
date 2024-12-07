from gtts import gTTS
import streamlit as st
from pydub import AudioSegment
from pydub.playback import play
import os

# Function to convert text to speech
def text_to_audio(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    output_file = "output_audio.mp3"
    tts.save(output_file)
    return output_file

# Main Streamlit app
def main():
    st.title("AI Text-to-Audio Generator")
    st.markdown("Convert your text into speech using AI-powered TTS.")

    # Text input from user
    text_input = st.text_area("Enter the text you want to convert into speech:")
    
    # Language selection
    language = st.selectbox("Select Language:", ["en", "hi", "es", "fr", "de", "zh"])

    # Button to generate audio
    if st.button("Generate Audio"):
        if not text_input.strip():
            st.error("Please enter some text to generate audio!")
        else:
            st.info("Generating audio...")
            output_file = text_to_audio(text_input, language)
            st.audio(output_file, format="audio/mp3")
            st.success("Audio generated successfully!")
            
            # Option to download the audio file
            with open(output_file, "rb") as file:
                st.download_button(
                    label="Download Audio",
                    data=file,
                    file_name="generated_audio.mp3",
                    mime="audio/mp3"
                )

# Run the app
if __name__ == "__main__":
    main()
