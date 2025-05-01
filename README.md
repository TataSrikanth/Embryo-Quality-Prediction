
# 🧬 Embryo Quality Prediction Web App

This project is a web-based application that allows users to upload embryo images and receive predictions of embryo quality using a trained YOLO model.

## 📌 Features

- Upload multiple embryo images in `.jpg`, `.jpeg`, or `.png` formats.
- View real-time predictions of embryo quality.
- User-friendly interface built with Streamlit.
- Uses a custom-trained YOLO model for classification.

## 🧠 Model

The application uses a YOLO-based model (`best_Embryo_model.pt`) trained for classifying embryo quality into categories such as **Grade A**, **Grade B**, and **Grade C** across developmental stages (Cleavage, Morula, Blastocyst).

## 🚀 How to Run

### Prerequisites

- Python 3.8+
- Install required libraries:

```bash
pip install streamlit ultralytics torch Pillow
```

### Launch the App

Make sure `best_Embryo_model.pt` is in the same directory or update the path in the script.

Run the app with:

```bash
streamlit run Deployment.py
```

## 📁 Files

- `Deployment.py` — Streamlit app script for image classification.
- `best_Embryo_model.pt` — Trained YOLO model file (not included here).

## 🧪 Example

1. Open the app.
2. Upload embryo images.
3. View predicted quality and confidence score.

## 📷 Screenshot

*(You can add a screenshot of the app here.)*

## 🔒 Notes

- Make sure the model file path is correctly set.
- Model must support classification and return `probs` attribute.

## 📬 Contact

For queries or contributions, feel free to open an issue or contact the maintainer.
