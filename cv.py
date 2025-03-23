import cv2
import os
from ocr import ocr
import time


# Function to capture frames every 2 seconds from live video
def live_video_capture():
    cap = cv2.VideoCapture(0)  # Open the webcam (0 for default)

    last_saved_time = time.time()  # Store the current time
    count = 0

    while True:
        ret, frame = cap.read()  # Capture frame from webcam

        if not ret:
            break  # Stop if no frame is read

        # Save frame every 2 seconds
        if time.time() - last_saved_time >= 3:
            filename = f"data/frame{count}.jpg"
            cv2.imwrite(filename, frame)  # Save the frame
            ocr(filename)
            os.remove(filename)
            count += 1
            last_saved_time = time.time()  # Update time for next frame

        cv2.imshow("Live Video Feed", frame)  # Show live feed

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key press
            break

    cap.release()  # Release the webcam
    cv2.destroyAllWindows()  # Close the OpenCV window


# Driver Code
if __name__ == '__main__':
    live_video_capture()