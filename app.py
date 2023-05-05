import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration, VideoProcessorBase

# Set up the RTCConfiguration with your TURN server details
rtc_configuration = RTCConfiguration(
    {
        "iceServers": [
            {
                "urls": ["turn:bn-turn1.xirsys.com:80?transport=udp",
       "turn:bn-turn1.xirsys.com:3478?transport=udp",
       "turn:bn-turn1.xirsys.com:80?transport=tcp",
       "turn:bn-turn1.xirsys.com:3478?transport=tcp",
       "turns:bn-turn1.xirsys.com:443?transport=tcp",
       "turns:bn-turn1.xirsys.com:5349?transport=tcp"],
                "username": "TBPiEMw7tX24LLZvFW8ymeB-DwRFYTzQ8eVh1B3yroLEeERJ4lBh7HQKQXXD6gJaAAAAAGRUyXJ1dGthcnNoMzU2",
                "credential": "87bac70a-eb25-11ed-b31b-0242ac140004",
            }
        ]
    }
)

# Create a custom VideoProcessor class to use with the WebRTC component
class VideoProcessor(VideoProcessorBase):
    pass

# Use the webrtc_streamer function with the custom rtc_configuration and VideoProcessor
webrtc_streamer(
    key="example",
    rtc_configuration=rtc_configuration,
    video_processor_factory=VideoProcessor,
)
