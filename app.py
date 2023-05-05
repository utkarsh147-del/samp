import asyncio
import streamlit as st
import av
import aiortc



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
        iceServers: [{urls: [ "stun:bn-turn1.xirsys.com" ]}, {username: "TBPiEMw7tX24LLZvFW8ymeB-DwRFYTzQ8eVh1B3yroLEeERJ4lBh7HQKQXXD6gJaAAAAAGRUyXJ1dGthcnNoMzU2", credential: "87bac70a-eb25-11ed-b31b-0242ac140004",urls: ["turn:bn-turn1.xirsys.com:80?transport=udp","turn:bn-turn1.xirsys.com:3478?transport=udp","turn:bn-turn1.xirsys.com:80?transport=tcp","turn:bn-turn1.xirsys.com:3478?transport=tcp","turns:bn-turn1.xirsys.com:443?transport=tcp","turns:bn-turn1.xirsys.com:5349?transport=tcp"]}]
        configuration = aiortc.RTCConfiguration(iceServers=ice_servers)





    # Create WebRTC connection
        self.webrtc_ctx = self._create_webrtc_context(
        configuration=configuration
    )

async def main():
    # Run the WebRTC streamer
    webrtc_ctx = webrtc_streamer(
        key="example",
        mode=WebRtcMode.SENDRECV,
        video_processor_factory=StunVideoProcessor,
    )

if __name__ == "__main__":
    asyncio.run(main())
