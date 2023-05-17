import streamlit as st
from streamlit.components.v1 import html

html_string = """
<video id="camera-stream" width="640" height="480" autoplay></video>
<button id="take-photo">Take Photo</button>

<script>
  const video = document.querySelector('#camera-stream');
  const takePhotoButton = document.querySelector('#take-photo');

  navigator.mediaDevices
    .getUserMedia({ video: true })
    .then(stream => {
      video.srcObject = stream;
    })
    .catch(error => {
      console.error('Error accessing camera', error);
    });

  takePhotoButton.addEventListener('click', () => {
    // code to take a photo
  });
</script>
"""

html(html_string, width=640, height=520)
