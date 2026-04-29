<h1 align="center"> Insurance Premium Prediction </h1>

<p align="center">
  <b>FastAPI + Machine Learning + Scikit-learn</b><br>
  Predict insurance premium categories with confidence scores.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python">
  <img src="https://img.shields.io/badge/FastAPI-0.129-green?logo=fastapi">
  <img src="https://img.shields.io/badge/ML-Scikit--Learn-orange">
  <img src="https://img.shields.io/badge/Status-Production Ready-success">
</p>

<hr>

<h2>⚡ Overview</h2>

<p>
A real-time <b>Insurance Premium Prediction API</b> built using FastAPI and Machine Learning.
It takes user details and predicts the insurance premium category along with confidence scores.
</p>

<p><i>Validate → Transform → Predict → Respond</i></p>

<hr>

<h2>📁 Project Structure</h2>

<pre>
.
├── app.py
├── models/
│   └── rc_model.pkl
├── schema/
│   ├── user_input.py
│   └── response.py
├── config/
│   └── city_tier.py
├── requirements.txt
</pre>

<hr>

<h2>✅ Features</h2>

<ul>
  <li>✔ FastAPI REST API</li>
  <li>✔ Input validation using Pydantic</li>
  <li>✔ Automatic feature engineering (BMI, risk, age group)</li>
  <li>✔ ML model prediction with probability scores</li>
  <li>✔ Clean JSON responses</li>
  <li>✔ Health check endpoint</li>
</ul>

<hr>

<h2>🧠 Input Processing</h2>

<p>Derived features automatically computed:</p>

<ul>
  <li><b>BMI</b> = weight / height²</li>
  <li><b>Lifestyle Risk</b> (Low / Medium / High)</li>
  <li><b>Age Group</b> (Young / Adult / Middle Age / Senior)</li>
  <li><b>City Tier</b> (1 / 2 / 3)</li>
</ul>

<hr>

<h2>📦 Requirements</h2>

<ul>
  <li>Python 3.x</li>
  <li>FastAPI</li>
  <li>Uvicorn</li>
  <li>Scikit-learn</li>
  <li>Pandas & NumPy</li>
</ul>

<hr>

<h2>⚙️ Installation</h2>

<pre>
git clone https://github.com/your-username/your-repo.git
cd your-repo

pip install -r requirements.txt
</pre>

<hr>

<h2>🚀 Run the API</h2>

<pre>
uvicorn app:app --reload
</pre>

<p>Open in browser:</p>

<ul>
  <li>Swagger UI → http://127.0.0.1:8000/docs</li>
  <li>Health Check → http://127.0.0.1:8000/health</li>
</ul>

<hr>

<h2>🔌 API Endpoints</h2>

<h3>GET /</h3>
<p>Welcome message</p>

<h3>GET /health</h3>
<p>Check API and model status</p>

<h3>POST /predict</h3>
<p>Predict insurance premium category</p>

<hr>

<h2>📥 Sample Request</h2>

<pre>
{
  "age": 30,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 10,
  "smoker": false,
  "city": "Kolkata",
  "occupation": "private_job"
}
</pre>

<hr>

<h2>📤 Sample Response</h2>

<pre>
{
  "predicted_category": "Medium",
  "confidence": 0.87,
  "class_probabilities": {
    "Low": 0.05,
    "Medium": 0.87,
    "High": 0.08
  }
}
</pre>

<hr>

<h2>🧩 Tech Stack</h2>

<ul>
  <li>FastAPI</li>
  <li>Pydantic</li>
  <li>Scikit-learn</li>
  <li>Pandas</li>
</ul>

<hr>

<h2>📌 Notes</h2>

<ul>
  <li>Model loaded using pickle</li>
  <li>Version controlled (MODEL_VERSION)</li>
  <li>Feature engineering handled in schema layer</li>
</ul>

<hr>

<h2 align="center">💡 Future Improvements</h2>

<ul>
  <li>Docker support</li>
  <li>Frontend UI (Streamlit/React)</li>
  <li>Model monitoring (MLflow)</li>
</ul>

<hr>

<p align="center">
  ⭐ Star this repo if you found it useful!
</p>
