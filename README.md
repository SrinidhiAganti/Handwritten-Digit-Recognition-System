# Handwritten Digit Recognition System

A web-based application that recognizes handwritten digits (0–9) in real-time using a deep learning model trained on the MNIST dataset and deployed with Streamlit.

---

## 🚀 Features

* 🖌️ Draw digits (0–9) using interactive canvas
* 🧠 Real-time prediction using trained neural network
* ⚡ Fast and accurate digit recognition
* 🌐 Web-based UI using Streamlit

---

## 🧠 Tech Stack

* Python
* TensorFlow (Keras)
* Streamlit
* NumPy
* OpenCV
* Streamlit Drawable Canvas

---

## 📂 Project Structure

digit-recognizer-streamlit/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Dependencies
├── runtime.txt         # Python version for deployment
├── README.md           # Documentation

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

git clone https://github.com/yourusername/digit-recognizer-streamlit.git
cd digit-recognizer-streamlit

### 2️⃣ Install Dependencies

pip install -r requirements.txt

---

## ▶️ Run the Application

streamlit run app.py

👉 Open in browser: http://localhost:8501

---

## 🌐 Live Demo

👉 https://yourapp.streamlit.app

---

## 📊 How It Works

1. User draws a digit on the canvas
2. Image is converted to grayscale and resized (28×28)
3. Pixel values are normalized
4. Model predicts digit using neural network
5. Output displayed with confidence score

---

## 📸 Output

* Predicted digit (0–9)
* Confidence score
* Processed input image

---

## 💼 Use Cases

* Handwritten digit recognition
* Educational AI demos
* Machine learning projects
* Image classification systems

---

## 🚀 Future Enhancements

* Multi-digit recognition
* Letter (A–Z) recognition
* Mobile-friendly UI
* Model optimization for faster inference

---

## 👨‍💻 Author

Aganti Srinidhi

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
