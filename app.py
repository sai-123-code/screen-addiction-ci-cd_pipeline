from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# ✅ Load pickled files
model = pickle.load(open("logistic_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))

# ✅ Define input feature order
FEATURES = ['Age', 'Gender', 'Daily_Usage_Hours', 'Sleep_Hours', 'Academic_Performance',
            'Social_Interactions', 'Exercise_Hours', 'Anxiety_Level', 'Depression_Level',
            'Self_Esteem', 'Parental_Control', 'Screen_Time_Before_Bed', 'Phone_Checks_Per_Day',
            'Apps_Used_Daily', 'Time_on_Social_Media', 'Time_on_Gaming', 'Time_on_Education',
            'Phone_Usage_Purpose', 'Family_Communication', 'Weekend_Usage_Hours']

# ✅ Prediction Route
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # ✅ Collect form data
            input_data = {feature: request.form[feature] for feature in FEATURES}

            # ✅ Convert to DataFrame
            df_input = pd.DataFrame([input_data])

            # ✅ Convert numeric types
            for col in df_input.columns:
                if col not in label_encoders:
                    df_input[col] = pd.to_numeric(df_input[col])

            # ✅ Encode categorical columns
            for col in label_encoders:
                df_input[col] = label_encoders[col].transform(df_input[col])

            # ✅ Scale features
            scaled_input = scaler.transform(df_input)

            # ✅ Predict
            pred_class = model.predict(scaled_input)[0]
            label_map = {0: "Low", 1: "Medium", 2: "High"}
            prediction = label_map.get(int(pred_class), "Unknown")

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction)

# ✅ Run the app
if __name__ == "__main__":
    app.run(debug=True)
