import streamlit as st
import av
import numpy as np
from streamlit_webrtc import webrtc_streamer

def main():
    st.header("WebRTC camera demo")
    webrtc_streamer(key="camera")

if __name__ == "__main__":
    main()
