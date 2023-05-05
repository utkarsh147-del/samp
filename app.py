import streamlit as st
import av
import asyncio
from streamlit_webrtc import VideoProcessorBase, WebRtcMode, webrtc_streamer

class VideoProcessor(VideoProcessorBase):
    async def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        # Process the video frame here
        return frame

async def main():
    webrtc_ctx = webrtc_streamer(
        key="example",
        mode=WebRtcMode.SENDRECV,
        video_processor_factory=VideoProcessor,
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        st.error("Error: {e}")
