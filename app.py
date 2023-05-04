import cv2
import streamlit as st
import numpy as np

def main():
    st.title("Live Camera Feed")
    st.write("Click the button below to open the camera:")
    for i in range(6):
        print(i)
    # Try to open the camera with different index values
    if st.button("Open Camera"):
        cap = None
        for i in range(6):
            print(i)
            cap = cv2.VideoCapture(i)
            print(i)
            if cap.isOpened():
                break

        if cap is None or not cap.isOpened():
            st.error("Failed to open camera.")
            return

        # Set the resolution to 640x480
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Create a placeholder for displaying the video
        video_placeholder = st.empty()

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to capture frame from camera.")
                break

            # Convert the frame from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Display the resulting frame
            video_placeholder.image(frame, channels="RGB")

            # Check if the user has stopped the camera
            

        # Release the capture and close the window
        cap.release()

if __name__ == "__main__":
    main()
