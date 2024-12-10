# CheatGuard: AI-Powered Cheating Detection System

CheatGuard is an advanced solution that combines artificial intelligence and computer vision to enhance the integrity of academic evaluations. By automating the monitoring process during exams, CheatGuard ensures real-time detection and prevention of cheating behaviors.

---

## 🚀 Features

- **Real-Time Detection**: Detects suspicious behaviors such as unusual hand movements or facial expressions.
- **User-Friendly Interface**: Easily upload exam footage and visualize detection results through an intuitive web interface.
- **YOLO Model Integration**: Utilizes a custom-trained YOLOv5 model for high-performance object detection.
- **Scalable Deployment**: Works seamlessly on both local systems and cloud environments.

---

## 🧠 How It Works

1. **Input**: Upload an image of the exam room.  
2. **Detection**: The YOLOv5 model processes the image to identify and highlight suspicious activities.  
3. **Output**: View the results with bounding boxes around detected activities and receive real-time feedback.

---

## 🛠️ Installation

### Prerequisites

- Python 3.10+  
- Flask  
- Ultralytics YOLOv5  
- Torch  

### Setup

```bash
# Clone the repository
git clone https://github.com/YourUsername/CheatGuard.git

# Navigate to the project directory
cd CheatGuard

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py

---
         # Project documentation  

