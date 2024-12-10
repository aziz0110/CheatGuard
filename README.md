CheatGuard: AI-Powered Cheating Detection System
CheatGuard is an innovative project that leverages artificial intelligence and computer vision to detect and prevent cheating during exams. This solution automates the monitoring process, enhancing the integrity of academic evaluations.

🚀 Features
Real-Time Detection: Identifies behaviors such as unusual hand movements or suspicious facial expressions.
Web Interface: User-friendly interface for uploading exam footage and visualizing detection results.
YOLO Model Integration: Trained with custom datasets for optimized performance.
Scalable Deployment: Compatible with local systems or cloud environments.
🧠 How It Works
Input: Upload an exam image.
Detection: The trained YOLO model processes the image to identify suspicious activities.
Output: Displays bounding boxes around detected activities, classifies them, and provides real-time feedback.
🛠️ Installation
Prerequisites
Python 3.10+
Flask
Ultralytics YOLOv5
Torch
Setup
bash
Copier le code
# Clone the repository  
git clone https://github.com/YourUsername/CheatGuard.git  

# Navigate to the project directory  
cd CheatGuard  

# Install dependencies  
pip install -r requirements.txt  

# Run the Flask app  
python app.py  
📝 Usage
Launch the web app by navigating to http://127.0.0.1:5000.
Upload an image for analysis.
View the detection results with bounding boxes highlighting the identified activities.
📂 Project Structure
plaintext
Copier le code
CheatGuard/  
│  
├── app.py                 # Flask web application  
├── yolov5_trained_model.pt # Pre-trained YOLOv5 model  
├── templates/             # HTML templates for the web interface  
├── static/                # Static files (CSS, JS, images)  
│   ├── uploads/           # Uploaded images  
│   └── outputs/           # Processed images with detections  
├── requirements.txt       # Python dependencies  
└── README.md              # Project documentation  
🤝 Contribution
Contributions are welcome! Feel free to fork this repository, make improvements, and create pull requests.

📜 License
This project is licensed under the MIT License.

🌟 Acknowledgments
Ultralytics for the YOLOv5 model.
Open-source tools and libraries that made this project possible.
