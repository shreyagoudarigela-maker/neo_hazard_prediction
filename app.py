import streamlit as st
import pandas as pd
import pickle


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="NEO Hazard Prediction",
    page_icon="🌍",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =========================
   MAIN BACKGROUND
   ========================= */

.stApp {
    background: linear-gradient(
        135deg,
        #dff3ff 0%,
        #eef7ff 50%,
        #ffffff 100%
    );
}


/* =========================
   MAIN TITLE
   ========================= */

.main-title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    color: #083b66 !important;
    margin-top: 10px;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    font-weight: 500;
    color: #34495e !important;
    margin-bottom: 30px;
}


/* =========================
   ALL NORMAL TEXT
   ========================= */

.stApp p,
.stApp span,
.stApp label,
.stApp div {
    color: #1f2937;
}


/* =========================
   SECTION HEADINGS
   ========================= */

.section-title {
    font-size: 25px;
    font-weight: 800;
    color: #083b66 !important;
    margin-top: 25px;
    margin-bottom: 15px;
}


/* =========================
   INPUT BOX
   ========================= */

div[data-baseweb="input"] {
    background-color: #ffffff !important;
    border: 2px solid #b7d7f0 !important;
    border-radius: 10px !important;
}


/* Input value */

div[data-baseweb="input"] input {
    color: #111111 !important;
    background-color: #ffffff !important;
    font-weight: 600 !important;
}


/* Placeholder */

div[data-baseweb="input"] input::placeholder {
    color: #777777 !important;
}


/* =========================
   SELECT BOX
   ========================= */

div[data-baseweb="select"] {
    background-color: #ffffff !important;
    border: 2px solid #b7d7f0 !important;
    border-radius: 10px !important;
}


/* Selectbox selected value */

div[data-baseweb="select"] span {
    color: #111111 !important;
}


/* Dropdown text */

ul[role="listbox"] {
    background-color: #ffffff !important;
}

ul[role="listbox"] li {
    color: #111111 !important;
}


/* =========================
   INPUT LABELS
   ========================= */

.stNumberInput label,
.stSelectbox label {
    color: #12344d !important;
    font-size: 16px !important;
    font-weight: 700 !important;
}


/* =========================
   BUTTON
   ========================= */

.stButton > button {
    width: 100%;
    background: linear-gradient(
        90deg,
        #0b3d91,
        #1976d2
    ) !important;

    color: white !important;

    font-size: 20px !important;
    font-weight: 700 !important;

    border-radius: 12px !important;
    padding: 12px !important;

    border: none !important;

    box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
}


/* Button text */

.stButton > button p {
    color: white !important;
}


/* Button hover */

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #1976d2,
        #0b3d91
    ) !important;

    color: white !important;
}


/* =========================
   INFO BOX
   ========================= */

div[data-testid="stAlert"] {
    background-color: #e8f4ff !important;
    border-radius: 12px !important;
    border-left: 5px solid #1976d2 !important;
}


/* Text inside info box */

div[data-testid="stAlert"] p,
div[data-testid="stAlert"] span {
    color: #12344d !important;
}


/* =========================
   DATAFRAME / TABLE
   ========================= */

div[data-testid="stDataFrame"] {
    background-color: white !important;
    border-radius: 10px !important;
}


/* =========================
   METRIC BOXES
   ========================= */

div[data-testid="stMetric"] {
    background-color: white !important;

    padding: 18px !important;

    border-radius: 12px !important;

    border: 1px solid #c7dff2 !important;

    box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
}


/* Metric label */

div[data-testid="stMetric"] label {
    color: #456 !important;
}


/* Metric value */

div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
    color: #083b66 !important;
}


/* Metric delta */

div[data-testid="stMetric"] div[data-testid="stMetricDelta"] {
    color: #333333 !important;
}


/* =========================
   EXPANDER
   ========================= */

div[data-testid="stExpander"] {
    background-color: #ffffff !important;
    border: 1px solid #b7d7f0 !important;
    border-radius: 10px !important;
}


/* Expander title */

div[data-testid="stExpander"] summary {
    color: #083b66 !important;
    font-weight: 700 !important;
}


/* =========================
   SIDEBAR
   ========================= */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #dff3ff,
        #ffffff
    ) !important;
}


/* Sidebar text */

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label {
    color: #1f2937 !important;
}


/* Sidebar headings */

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #083b66 !important;
}


/* =========================
   SUCCESS MESSAGE
   ========================= */

div[data-testid="stAlert"][kind="success"] {
    background-color: #e9f8ef !important;
}

div[data-testid="stAlert"][kind="success"] p,
div[data-testid="stAlert"][kind="success"] span {
    color: #146c2e !important;
    font-weight: 600 !important;
}


/* =========================
   ERROR MESSAGE
   ========================= */

div[data-testid="stAlert"][kind="error"] {
    background-color: #fff0f0 !important;
}

div[data-testid="stAlert"][kind="error"] p,
div[data-testid="stAlert"][kind="error"] span {
    color: #a00000 !important;
    font-weight: 600 !important;
}


/* =========================
   FOOTER
   ========================= */

.footer {
    text-align: center;
    color: #555555 !important;
    font-size: 14px;
    margin-top: 20px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MODEL
# =========================================================

try:

    with open("model_pipe (1).pkl", "rb") as file:
        model = pickle.load(file)

except Exception as e:

    st.error("❌ Error loading model")
    st.error(str(e))
    st.stop()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🌍 NEO Hazard Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Machine Learning Based Near-Earth Object Hazard Prediction</div>',
    unsafe_allow_html=True
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("🌌 About the Project")

    st.write(
        """
        This application predicts whether a
        Near-Earth Object (NEO) is potentially
        hazardous using a Machine Learning model.
        """
    )

    st.markdown("---")

    st.subheader("🤖 Model")

    st.write("Random Forest Classifier")

    st.markdown("---")

    st.subheader("🎯 Prediction")

    st.write("🟢 Not Hazardous")
    st.write("🔴 Hazardous")

    st.markdown("---")

    st.info(
        "Enter the NEO measurements and click "
        "'Predict Hazard' to get the result."
    )


# =========================================================
# INPUT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">🛰️ Enter NEO Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


# =========================================================
# LEFT COLUMN
# =========================================================

with col1:

    est_diameter_min = st.number_input(
        "Minimum Estimated Diameter (km)",
        min_value=0.0,
        value=0.16,
        step=0.01,
        format="%.4f"
    )

    relative_velocity = st.number_input(
        "Relative Velocity (km/s)",
        min_value=0.0,
        value=15.00,
        step=0.1,
        format="%.4f"
    )

    miss_distance = st.number_input(
        "Miss Distance (km)",
        min_value=0.0,
        value=1000000.0,
        step=1000.0,
        format="%.2f"
    )


# =========================================================
# RIGHT COLUMN
# =========================================================

with col2:

    est_diameter_max = st.number_input(
        "Maximum Estimated Diameter (km)",
        min_value=0.0,
        value=0.50,
        step=0.01,
        format="%.4f"
    )

    orbiting_body = st.selectbox(
        "Orbiting Body",
        ["Earth"]
    )


# =========================================================
# ORBITING BODY ENCODING
# =========================================================

# During training, Earth was encoded numerically.
# Assuming Earth = 0.

orbiting_body_encoded = 0


# =========================================================
# FEATURE ENGINEERING
# =========================================================

avg_diameter = (
    est_diameter_min + est_diameter_max
) / 2


diameter_ratio = (
    est_diameter_max /
    (est_diameter_min + 1e-10)
)


proximity_score = (
    1 / (miss_distance + 1)
)


size_miss_distance = (
    avg_diameter * miss_distance
)


size_velocity = (
    avg_diameter * relative_velocity
)


# =========================================================
# ADDITIONAL INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">ℹ️ Additional Information</div>',
    unsafe_allow_html=True
)

st.info(
    """
    **The model uses both original and engineered features.**

    • Average Diameter = Mean of minimum and maximum diameter

    • Diameter Ratio = Maximum Diameter / Minimum Diameter

    • Proximity Score = 1 / (Miss Distance + 1)

    • Size × Miss Distance = Average Diameter × Miss Distance

    • Size × Velocity = Average Diameter × Relative Velocity
    """
)


# =========================================================
# INPUT SUMMARY
# =========================================================

st.markdown(
    '<div class="section-title">📋 Input Summary</div>',
    unsafe_allow_html=True
)

summary_df = pd.DataFrame({

    "Feature": [
        "Minimum Diameter",
        "Maximum Diameter",
        "Relative Velocity",
        "Miss Distance",
        "Orbiting Body"
    ],

    "Value": [
        est_diameter_min,
        est_diameter_max,
        relative_velocity,
        miss_distance,
        orbiting_body
    ]
})


st.dataframe(
    summary_df,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# KEY MEASUREMENTS
# =========================================================

st.markdown(
    '<div class="section-title">📊 Key Measurements</div>',
    unsafe_allow_html=True
)

metric1, metric2, metric3 = st.columns(3)


with metric1:

    st.metric(
        "Average Diameter",
        f"{avg_diameter:.4f} km"
    )


with metric2:

    st.metric(
        "Diameter Ratio",
        f"{diameter_ratio:.4f}"
    )


with metric3:

    st.metric(
        "Proximity Score",
        f"{proximity_score:.8f}"
    )


# =========================================================
# CREATE INPUT DATA
# =========================================================

input_data = pd.DataFrame({

    "est_diameter_min": [
        est_diameter_min
    ],

    "est_diameter_max": [
        est_diameter_max
    ],

    "relative_velocity": [
        relative_velocity
    ],

    "miss_distance": [
        miss_distance
    ],

    "orbiting_body": [
        orbiting_body_encoded
    ],

    "avg_diameter": [
        avg_diameter
    ],

    "diameter_ratio": [
        diameter_ratio
    ],

    "proximity_score": [
        proximity_score
    ],

    "size_miss_distance": [
        size_miss_distance
    ],

    "size_velocity": [
        size_velocity
    ]
})


# =========================================================
# GET MODEL FEATURE ORDER
# =========================================================

if hasattr(model, "feature_names_in_"):

    FEATURE_COLUMNS = list(
        model.feature_names_in_
    )

elif (
    hasattr(model, "best_estimator_")
    and hasattr(
        model.best_estimator_,
        "feature_names_in_"
    )
):

    FEATURE_COLUMNS = list(
        model.best_estimator_.feature_names_in_
    )

else:

    FEATURE_COLUMNS = [
        "est_diameter_min",
        "est_diameter_max",
        "relative_velocity",
        "miss_distance",
        "orbiting_body",
        "avg_diameter",
        "diameter_ratio",
        "proximity_score",
        "size_miss_distance",
        "size_velocity"
    ]


# =========================================================
# REORDER FEATURES
# =========================================================

try:

    input_data = input_data[FEATURE_COLUMNS]

except Exception as e:

    st.error("❌ Feature matching error")

    st.write("Model expects:")

    st.write(FEATURE_COLUMNS)

    st.write("Application created:")

    st.write(input_data.columns.tolist())

    st.stop()


# =========================================================
# VIEW DATA SENT TO MODEL
# =========================================================

with st.expander("🔍 View Data Sent to the Model"):

    st.dataframe(
        input_data,
        use_container_width=True
    )


# =========================================================
# PREDICTION SECTION
# =========================================================

st.markdown(
    '<div class="section-title">🔮 Prediction</div>',
    unsafe_allow_html=True
)


if st.button("🚀 Predict Hazard"):

    try:

        # Make prediction
        prediction = model.predict(
            input_data
        )[0]


        # =================================================
        # RESULT
        # =================================================

        if prediction:

            st.error(
                "🔴 HAZARDOUS NEO"
            )

            st.markdown(
                """
                ### ⚠️ Prediction Result

                The model predicts that this
                Near-Earth Object is **potentially hazardous**.
                """
            )

        else:

            st.success(
                "🟢 NOT HAZARDOUS"
            )

            st.markdown(
                """
                ### ✅ Prediction Result

                The model predicts that this
                Near-Earth Object is **not hazardous**.
                """
            )


        # =================================================
        # PREDICTION PROBABILITY
        # =================================================

        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(
                input_data
            )[0]


            st.markdown(
                "### 📈 Prediction Probability"
            )


            probability_df = pd.DataFrame({

                "Class": [
                    "Not Hazardous",
                    "Hazardous"
                ],

                "Probability": [
                    probabilities[0] * 100,
                    probabilities[1] * 100
                ]

            })


            probability_df["Probability"] = (
                probability_df["Probability"].round(2)
            )


            st.dataframe(
                probability_df,
                use_container_width=True,
                hide_index=True
            )


            # =================================================
            # PROBABILITY METRICS
            # =================================================

            prob1, prob2 = st.columns(2)


            with prob1:

                st.metric(
                    "🟢 Not Hazardous",
                    f"{probabilities[0] * 100:.2f}%"
                )


            with prob2:

                st.metric(
                    "🔴 Hazardous",
                    f"{probabilities[1] * 100:.2f}%"
                )


    except Exception as e:

        st.error(
            "❌ Prediction Error"
        )

        st.code(
            str(e)
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    '<div class="footer">🌍 NEO Hazard Prediction System | '
    'Machine Learning Project | Random Forest Classifier</div>',
    unsafe_allow_html=True
)