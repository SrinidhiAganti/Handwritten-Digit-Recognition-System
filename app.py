import streamlit as st
from streamlit_drawable_canvas import st_canvas
import tensorflow as tf
import numpy as np
import cv2

st.set_page_config(page_title="Digit Recognizer")
st.title("🔢 Handwritten Digit Recognizer (0–9)")

# ---------------- MODEL ----------------
@st.cache_resource
def load_model():
    (x_train, y_train), _ = tf.keras.datasets.mnist.load_data()

    x_train = x_train / 255.0

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=2, verbose=0)

    return model

model = load_model()

# ---------------- CANVAS ----------------
canvas_result = st_canvas(
    stroke_width=12,
    stroke_color="#FFFFFF",
    background_color="#000000",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

# ---------------- PREDICTION ----------------
if canvas_result.image_data is not None:
    img = canvas_result.image_data.astype('uint8')

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize to MNIST size
    resized = cv2.resize(gray, (28, 28))

    # Invert colors (IMPORTANT)
    inverted = 255 - resized

    # Normalize
    normalized = inverted / 255.0
    normalized = normalized.reshape(1, 28, 28)

    st.image(inverted, caption="Processed Digit")

    if st.button("Predict Digit"):
        pred = model.predict(normalized)
        digit = np.argmax(pred)
        confidence = np.max(pred)

        st.success(f"Predicted Digit: {digit}")
        st.write(f"Confidence: {confidence:.2%}")
