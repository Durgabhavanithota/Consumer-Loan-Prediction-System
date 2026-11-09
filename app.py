# ==========================================
# CONSUMER LOAN APPROVAL PREDICTION SYSTEM
# ==========================================

# STEP 1: Import required libraries

from flask import Flask, render_template, request
import joblib
import numpy as np
import os
from pathlib import Path


# STEP 2: Create Flask application

app = Flask(__name__)


# STEP 3: Set project directory

BASE_DIR = Path(__file__).resolve().parent


# STEP 4: Load trained Machine Learning model and scaler

model = joblib.load(BASE_DIR / "loan_model.pkl")
scaler = joblib.load(BASE_DIR / "scaler.pkl")


# STEP 5: Display home page

@app.route("/")
def home():
    return render_template("loan_app.html")


# STEP 6: Receive applicant details and predict

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get applicant information

        age = int(request.form["age"])

        years_experience = float(
            request.form["years_experience"]
        )

        family_size = int(
            request.form["family_size"]
        )

        annual_income = float(
            request.form["annual_income"]
        )

        avg_spending = float(
            request.form["avg_spending"]
        )

        education_level = int(
            request.form["education_level"]
        )

        mortgage = float(
            request.form["mortgage"]
        )

        securities_account = int(
            request.form["securities_account"]
        )

        cd_account = int(
            request.form["cd_account"]
        )

        online_banking = int(
            request.form["online_banking"]
        )

        credit_card = int(
            request.form["credit_card"]
        )


        # Arrange features in training order

        input_data = np.array([[
            age,
            years_experience,
            family_size,
            annual_income,
            avg_spending,
            education_level,
            mortgage,
            securities_account,
            cd_account,
            online_banking,
            credit_card
        ]])


        # Apply feature scaling

        input_scaled = scaler.transform(input_data)


        # Generate prediction probability

        prediction_proba = model.predict_proba(input_scaled)

        prob = prediction_proba[0][1]


        # Apply existing 30% threshold

        if prob >= 0.30:

            result = (
                f"Loan Approved ✅ "
                f"({prob * 100:.2f}% chance)"
            )

        else:

            result = (
                f"Loan Not Approved ❌ "
                f"({prob * 100:.2f}% chance)"
            )


        # Display prediction result

        return render_template(
            "result.html",
            prediction=result
        )


    except (ValueError, TypeError, KeyError):

        return "Invalid application details. Please check your inputs.", 400

    except Exception as error:

        app.logger.exception("Prediction failed")

        return "Unable to process your application. Please try again.", 500


# STEP 7: Run application

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )