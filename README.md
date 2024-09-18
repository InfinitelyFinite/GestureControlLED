# Gesture-Controlled Brightness Adjustment

## Overview
This project utilizes hand gesture recognition to control the brightness of a connected device. Using computer vision and machine learning techniques, the system tracks hand movements and translates them into brightness adjustments. The project integrates OpenCV and MediaPipe for hand tracking, and communicates with a device via serial communication to adjust brightness.

## Features
- **Hand Tracking**: Uses MediaPipe and OpenCV to detect and track hand gestures.
- **Brightness Control**: Adjusts the brightness of a device based on the distance between two specific hand landmarks.
- **Real-Time Processing**: Processes video input in real-time to provide immediate feedback and adjustments.
- **Serial Communication**: Communicates with a device via serial port to adjust brightness settings.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)
- PySerial (`serial`)
- Arduino IDE for device firmware

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/gesture-controlled-brightness.git
    ```
2. **Navigate to the Project Directory:**
    ```bash
    cd gesture-controlled-brightness
    ```
3. **Install Python Dependencies:**
    ```bash
    pip install opencv-python mediapipe pyserial
    ```

## How to Use

1. **Set Up Your Arduino Device:**
    - Upload the provided Arduino sketch to your Arduino board. The sketch listens for serial data to adjust the brightness.

    ```cpp
    void setup() {
      Serial.begin(9600);
      pinMode(5, OUTPUT);
    }

    void loop() {
      int x;
      if (Serial.available() > 0) {
        x = Serial.readString().toInt();
        analogWrite(5, x);
      }
    }
    ```

2. **Run the Python Script:**
    - Connect your Arduino board to your computer.
    - Update the serial port in the Python script to match your Arduino's serial port (e.g., `/dev/cu.usbserial-10`).
    - Execute the Python script:

    ```bash
    python main.py
    ```

3. **Use the System:**
    - The system will open a video feed window.
    - Adjust the distance between your thumb and index finger to change the brightness of the connected device.

## Sample Usage
When running the script, you will see a video feed with hand landmarks drawn on the screen. The distance between the tip of your thumb and index finger determines the brightness level sent to the Arduino. The system will visualize the hand landmarks and the distance between them in real-time.

## Future Improvements
- **Enhanced Gesture Recognition**: Incorporate more gestures for additional controls.
- **GUI Implementation**: Develop a graphical user interface for easier configuration and control.
- **Device Compatibility**: Extend support to control other types of devices or features.

## Troubleshooting
- **Serial Communication Issues**: Ensure that the serial port specified in the Python script matches your Arduino's port. Check for correct baud rate and connections.
- **Library Errors**: Verify that all required Python libraries are installed correctly.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- This project utilizes MediaPipe and OpenCV for hand gesture tracking.
- Special thanks to the open-source community for the development of these powerful tools.

