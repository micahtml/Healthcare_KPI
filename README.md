
# 🏥 Healthcare KPI Tracker

This project is a simple and interactive dashboard for tracking key performance indicators (KPIs) across hospital departments. It is built with **Python**, **Streamlit**, and **SQLite** and is designed to demonstrate core skills in data analysis, database management, and dashboard development — specifically in a healthcare setting.

---

## 📊 Features

- Interactive KPI selection:
  - Average Wait Time
  - Infection Rate
  - Average Cost per Patient
  - Readmission Rate
- Department filtering
- Time-series visualization using Plotly
- Raw data preview
- Built using mock data to simulate real-world hospital KPIs

---

## 🗂️ Data

The dataset is a mock simulation of monthly KPIs across five hospital departments for the year 2023. It includes:

- `date`
- `department`
- `avg_wait_time_minutes`
- `infection_rate_percent`
- `avg_cost_per_patient_usd`
- `readmission_rate_percent`

---

## 🛠️ Technologies Used

- Python
- Pandas
- SQLite
- Streamlit
- Plotly Express

---

## 🚀 How to Run Locally

1. Clone the repo or download the files.
2. Ensure you have Python installed and install dependencies:
    ```bash
    pip install streamlit pandas plotly
    ```
3. Run the Streamlit app:
    ```bash
    streamlit run healthcare_kpi_app.py
    ```

---

## 🌐 Deploying to Streamlit Cloud

1. Push your code and database file (`healthcare_kpi_app.py` and `healthcare_kpi.db`) to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Click **"New app"** and link your GitHub repository.
4. Set the main file path to `healthcare_kpi_app.py`.
5. Deploy and share your live app link!

---

## 📌 Notes

This project is designed to showcase practical database skills, KPI tracking, and dashboard development — aligned with roles such as **Database Analyst** and **Data Analyst** in the healthcare sector.

---

## 📧 Contact

Built by [Your Name] | [Your Portfolio or LinkedIn URL]
