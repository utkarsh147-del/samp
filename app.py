import streamlit as st
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from streamlit_webrtc import (
    ClientSettings,
    WebRtcMode,
    webrtc_streamer,
    VideoProcessorBase,
)

class TwilioVideoProcessor(VideoProcessorBase):
    async def process_video(self, frame):
        return frame

    async def setup(self):
        # Set up Twilio access token and VideoGrant
        account_sid = "ACd75dbc4fc896ef550cf165903ea08632"
        auth_token = "0d8d76ce54524203b61fe72b55f36331"
        token = AccessToken(account_sid, auth_token, identity="user")

        video_grant = VideoGrant(room="test")
        token.add_grant(video_grant)

        # Create Twilio WebRTC connection
        self.webrtc_ctx = self._create_webrtc_context(
            settings=ClientSettings(
                rtc_configuration={"iceServers": token.ice_servers},
                media_stream_constraints={"video": True, "audio": False},
                offer_options={},
            ),
            mode=WebRtcMode.SENDRECV,
        )

webrtc_streamer(
    key="example",
    mode=WebRtcMode.SENDRECV,
    video_processor_factory=TwilioVideoProcessor,
)
