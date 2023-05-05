import streamlit as st
from streamlit.components.v1 import html

def main():
    st.title("Camera App")

    # Define the HTML code for the video element
    html_code = """
    <video id="video" width="640" height="100" autoplay></video>
    <script>
    const video = document.getElementById('video');
    navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(error => {
        console.error(error);
    });
    </script>
    """

    # Display the video element in the app
    html(html_code)

if __name__ == '__main__':
    main()
