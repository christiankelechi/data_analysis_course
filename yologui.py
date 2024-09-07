import sys
import cv2
import requests
import numpy as np
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QTimer
import cv2

import sys
import cv2
import requests
import numpy as np
import pyttsx4
import base64
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QGridLayout, QWidget, QPushButton
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QTimer, QThread, pyqtSignal
import time

class AudioThread(QThread):
    text_to_speak = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.engine = pyttsx4.init()
        self.queue = []
        self.running = True

    def run(self):
        while self.running:
            if self.queue:
                text = self.queue.pop(0)
                self.engine.say(text)
                self.engine.runAndWait()
            time.sleep(0.1)  # Avoid busy-waiting
    
    def add_to_queue(self, text):
        self.queue.append(text)

    def stop(self):
        self.running = False
        self.wait()

class WebcamStream(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Webcam Stream")
        self.setGeometry(0, 20, 1400, 700)  # Set fullscreen dimensions

        # Setup UI
        self.intake_label = QLabel(self)
        self.result_label = QLabel(self)
        self.detect_button = QPushButton("Detect Now", self)
        # self.intake_label.setGeometry(0)
        # Initialize webcam
        self.cap = cv2.VideoCapture(0)
        
        # Initialize audio thread
        self.audio_thread = AudioThread()
        self.audio_thread.start()
        
        # Connect button to detection method
        self.detect_button.clicked.connect(self.detect_objects)

        # Initialize detection flag
        self.detecting = False
        
        # Setup timer for updating frames
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update every 30 ms for ~33 FPS

        # Store the current frame for detection
        self.current_frame = None

        # Layout setup
        self.layout = QGridLayout()
        self.layout.addWidget(self.intake_label, 0, 0)
        self.layout.addWidget(self.result_label, 0, 1)
        self.layout.addWidget(self.detect_button, 1, 0, 1, 1)
        self.setLayout(self.layout)
        self.show()
    def detect_objects(self):
        if self.current_frame is not None:
            # Stream current frame to backend
            _, img_encoded = cv2.imencode('.jpg', self.current_frame)
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                data=img_encoded.tobytes(),
                headers={'Content-Type': 'image/jpeg'}
            )
            
            if response.status_code == 200:
                data = response.json()
                img_data = data['image']
                detected_objects = data['detected_objects']

                # Read the response image
                nparr = np.frombuffer(base64.b64decode(img_data.split(',')[1]), np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                
                if img is not None:
                    # Convert frame to RGB format
                    rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    
                    # Convert to QImage
                    h, w, ch = rgb_frame.shape
                    bytes_per_line = ch * w
                    qimg = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
                    
                    # Set the image to the result label
                    self.result_label.setPixmap(QPixmap.fromImage(qimg))

                    # Announce detected objects if they are new or changed
                    for obj in detected_objects:
                        text = f"Detected {obj['class_name']} with confidence {obj['confidence']:.2f}"
                        self.audio_thread.add_to_queue(text)
                else:
                    print("Failed to decode image from backend response.")
            else:
                print(f"Invalid response from backend: {response.status_code}, content length: {len(response.content)}")

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Store the current frame for later use
            self.current_frame = frame

            # Convert frame to RGB format
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Convert to QImage
            h, w, ch = rgb_frame.shape
            bytes_per_line = ch * w
            qimg = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            
            # Set the image to the intake label
            self.intake_label.setPixmap(QPixmap.fromImage(qimg))

    def closeEvent(self, event):
        self.cap.release()
        self.audio_thread.stop()
        super().closeEvent(event)

app = QApplication(sys.argv)
window = WebcamStream()
# Set fullscreen mode
sys.exit(app.exec())



# class WebcamStream(QWidget):
#     def __init__(self):
#         super().__init__()
        
#         # Setup UI
#         self.setWindowTitle("Webcam Stream")
#         self.image_label = QLabel(self)
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.image_label)
#         self.setLayout(self.layout)
        
#         # Initialize webcam
#         self.cap = cv2.VideoCapture(0)
        
#         # Setup timer for updating frames
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(30)  # 30 ms for ~33 FPS
        
#     def update_frame(self):
#         ret, frame = self.cap.read()
#         if ret:
#             # Stream frame to backend
#             _, img_encoded = cv2.imencode('.jpg', frame)
#             response = requests.post(
#                 "http://127.0.0.1:8000/predict",
#                 data=img_encoded.tobytes(),
#                 headers={'Content-Type': 'image/jpeg'}
#             )
            
#             if response.status_code == 200 and response.content:
#                 # Read the response image
#                 nparr = np.frombuffer(response.content, np.uint8)
#                 img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                
#                 if img is not None:
#                     # Convert frame to RGB format
#                     rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    
#                     # Convert to QImage
#                     h, w, ch = rgb_frame.shape
#                     bytes_per_line = ch * w
#                     qimg = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
                    
#                     # Set the image to the label
#                     self.image_label.setPixmap(QPixmap.fromImage(qimg))
#                 else:
#                     print("Failed to decode image from backend response.")
#             else:
#                 print(f"Invalid response from backend: {response.status_code}, content length: {len(response.content)}")

    
#     def closeEvent(self, event):
#         self.cap.release()
#         super().closeEvent(event)

# app = QApplication(sys.argv)
# window = WebcamStream()
# window.show()
# sys.exit(app.exec())
