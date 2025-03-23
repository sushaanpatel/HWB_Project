# HWB_Project
Introducing Project for Hack Without Borders 2025: VERBATIM.

**Inspiration:**

We were inspired by the idea of creating a tool that bridges the gap between the visual and auditory worlds — a lightweight assistant that can see and speak. From helping visually impaired users to simply reading a handwritten note aloud, the idea of combining OCR (Optical Character Recognition) with text-to-speech felt both useful and achievable within a beginner hackathon.

**What it does:**

Verbatim captures live video using the user's webcam, extracts an image every 2 seconds, uses Easy OCR to recognize any text in the image, and then reads the text aloud using a built-in voice assistant (pyttsx3). It avoids reading the same text multiple times by storing previously spoken content, and automatically deletes processed images to keep the system tidy.

**How we built it:**

* Python: core language for scriptinG
* OpenCV: to capture webcam frames
* Easy OCR: to perform text recognition (OCR)
* pyttsx3: to convert recognized text into speech
* VS Code: our development environment
We also used file I/O to track previously spoken text and ensure no duplicates were read.

**Challenges we ran into:**

* Getting Easy OCR to work consistently across systems (especially on macOS)
* Dealing with image noise and poor lighting that reduced OCR accuracy
* Finding the ideal probability threshold to accept as valid words
* Making sure text-to-speech was clear, real-time, and non-blocking
* Keeping the code modular and clean while adding new features quickly

**Accomplishments that we're proud of:**

* We built a full working pipeline from image capture → text recognition → voice output
* Our system runs fully offline
* It’s beginner-friendly and requires minimal setup
* We made it modular enough to be expandable in the future
* We kept the project simple, practical, and focused

**What we learned:**

* How to integrate computer vision and text-to-speech in real-time
* Dealing with cross-platform dependencies and performance bottlenecks (lack of GPU)
* The importance of efficient file handling and memory management in live-streamed apps
* How much small automations can help people in accessibility use cases
* That even simple tools can be powerful when built with purpose


**What's next for Verbatim:**

* Add translation support (e.g. English → French)
* Integrate with mobile devices using a lightweight app or API
* Export spoken content to audio files
