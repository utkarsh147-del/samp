import cv2
import streamlit as st

def main():
    st.title("Camera App")

    # Open the camera and set the resolution
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Create a placeholder for the video stream
    video_placeholder = st.empty()

    while True:
        ret, frame = cap.read()

        if not ret:
            st.error("Failed to capture frame from camera")
            break

        # Convert the frame to RGB color space and display it in the app
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_placeholder.image(frame)

    # Release the camera and close the app
    cap.release()

if __name__ == '__main__':
    main()
