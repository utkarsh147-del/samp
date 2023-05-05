import streamlit as st
import av
import aiortc
#e
from streamlit_webrtc import (
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer,
)

class StunVideoProcessor(VideoProcessorBase):
    async def process_video(self, frame: av.VideoFrame) -> av.VideoFrame:
        # Process video frames here if needed
        return frame

    async def setup(self):
        # Configure STUN and TURN servers
        
        ice_servers=[
         {"urls": "stun:bn-turn1.xirsys.com"},
            {
            "urls": [
                "turn:bn-turn1.xirsys.com:80?transport=udp",
                "turn:bn-turn1.xirsys.com:3478?transport=udp",
                "turn:bn-turn1.xirsys.com:80?transport=tcp",
                "turn:bn-turn1.xirsys.com:3478?transport=tcp",
                "turns:bn-turn1.xirsys.com:443?transport=tcp",
                "turns:bn-turn1.xirsys.com:5349?transport=tcp"
            ],
            "username": "TBPiEMw7tX24LLZvFW8ymeB-DwRFYTzQ8eVh1B3yroLEeERJ4lBh7HQKQXXD6gJaAAAAAGRUyXJ1dGthcnNoMzU2",
            "credential": "87bac70a-eb25-11ed-b31b-0242ac140004
        }
    ]
        configuration = aiortc.RTCConfiguration(iceServers=ice_servers)

    # Create WebRTC connection
        self.webrtc_ctx = self._create_webrtc_context(
        configuration=configuration
    )

# Run the WebRTC streamer
webrtc_streamer(
    key="eutkarsh",
    mode=WebRtcMode.SENDRECV,
    video_processor_factory=StunVideoProcessor,
)
