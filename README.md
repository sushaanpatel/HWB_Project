# HWB_Project
Introducing Project for Hack Without Borders 2025: VERBATIM.

## Inspiration
We were inspired by the idea of creating a tool that bridges the gap between the visual and auditory worlds — a lightweight assistant that can see and speak.
From helping visually impaired users to simply reading some text aloud, the idea of combining OCR (Optical Character Recognition) with text-to-speech felt both useful and achievable.

## What it does
Verbatim captures live video using the user's webcam, extracts an image every 3 seconds, uses EasyOCR to recognize any text in the image, and then reads the text aloud using a built-in voice assistant (pyttsx3).

## How we built it
- Python: core language for scripting
- OpenCV: to capture webcam frames
- Easy OCR: to perform text recognition (OCR)
- pyttsx3: to convert recognized text into speech
- pyspellchecker: to correct the spellings of recognized words
- VS Code and PyCharm: our development environment

## Challenges we ran into
- Getting Easy OCR to work consistently across systems (especially on macOS)
- Dealing with image noise and poor lighting that reduced OCR accuracy
- Finding the ideal probability threshold to accept as valid words
- Keeping the code modular and clean while adding new features quickly

## Accomplishments that we're proud of
- We built a full working pipeline from image capture → text recognition → voice output
- Our system runs fully offline
- It’s beginner-friendly and requires minimal setup

## What we learned
- How to integrate computer vision and text-to-speech in real-time
- Dealing with cross-platform dependencies and performance bottlenecks (lack of GPU)
- The importance of efficient file handling and memory management in live-streamed apps

## What's next for Verbatim
- Add translation support (e.g. English → French)
- Integrate with mobile devices using a lightweight app or API
- Export spoken content to audio files
- Better text recognition models
