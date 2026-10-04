import streamlit as st
import pandas as pd
import pickle


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="NEO Hazard Prediction",
    page_icon="🌍",
    layout="wide"
)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    with open("model_pipe (1).pkl", "rb") as file:
        model = pickle.load(file)

    return model


try:

    model = load_model()

except Exception as e:

    st.error("❌ Error loading model")
    st.error(str(e))
    st.stop()


# =========================================================
# TITLE
# =========================================================

st.title("🌍 NEO Hazard Prediction System")

st.write(
    "Machine Learning based Near-Earth Object Hazard Prediction"
)

st.divider()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("About the Project")

    st.write(
        """
        This application predicts whether a
        Near-Earth Object (NEO) is potentially
        hazardous using a Random Forest Classifier.
        """
    )

    st.write("### Model")
    st.write("Random Forest Classifier")

    st.write("### Prediction Classes")
    st.write("🟢 Not Hazardous")
    st.write("🔴 Hazardous")


# =========================================================
# INPUT SECTION
# =========================================================

st.header("🛰️ Enter NEO Information")


col1, col2 = st.columns(2)


# =========================================================
# INPUTS
# =========================================================

with col1:

    est_diameter_min = st.number_input(
        "Minimum Estimated Diameter (km)",
        min_value=0.0,
        value=0.16,
        step=0.01
    )

    relative_velocity = st.number_input(
        "Relative Velocity (km/s)",
        min_value=0.0,
        value=15.00,
        step=0.1
    )

    miss_distance = st.number_input(
        "Miss Distance (km)",
        min_value=0.0,
        value=1000000.0,
        step=1000.0
    )


with col2:

    est_diameter_max = st.number_input(
        "Maximum Estimated Diameter (km)",
        min_value=0.0,
        value=0.50,
        step=0.01
    )

    orbiting_body = st.selectbox(
        "Orbiting Body",
        ["Earth"]
    )


# =========================================================
# ORBITING BODY ENCODING
# =========================================================

# Earth was encoded as 0 during training

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

st.header("ℹ️ Additional Information")

st.info(
    """
    The model uses the original NEO measurements
    together with engineered features.

    • Average Diameter
    • Diameter Ratio
    • Proximity Score
    • Size × Miss Distance
    • Size × Velocity
    """
)


# =========================================================
# INPUT SUMMARY
# =========================================================

st.header("📋 Input Summary")

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

st.header("📊 Key Measurements")

m1, m2, m3 = st.columns(3)

with m1:

    st.metric(
        "Average Diameter",
        f"{avg_diameter:.4f} km"
    )

with m2:

    st.metric(
        "Diameter Ratio",
        f"{diameter_ratio:.4f}"
    )

with m3:

    st.metric(
        "Proximity Score",
        f"{proximity_score:.8f}"
    )


# =========================================================
# CREATE MODEL INPUT
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

    feature_columns = list(
        model.feature_names_in_
    )

elif (
    hasattr(model, "best_estimator_")
    and hasattr(
        model.best_estimator_,
        "feature_names_in_"
    )
):

    feature_columns = list(
        model.best_estimator_.feature_names_in_
    )

else:

    feature_columns = [
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
# REORDER INPUT FEATURES
# =========================================================

input_data = input_data[
    feature_columns
]


# =========================================================
# SHOW MODEL INPUT
# =========================================================

with st.expander("🔍 View Data Sent to Model"):

    st.dataframe(
        input_data,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# PREDICTION
# =========================================================

st.header("🔮 Prediction")


if st.button(
    "🚀 Predict Hazard",
    use_container_width=True
):

    try:

        prediction = model.predict(
            input_data
        )[0]


        # =============================================
        # RESULT
        # =============================================

        if prediction == True:

            st.error(
                "🔴 HAZARDOUS NEO"
            )

            st.warning(
                "The model predicts that this "
                "Near-Earth Object is potentially hazardous."
            )

        else:

            st.success(
                "🟢 NOT HAZARDOUS"
            )

            st.info(
                "The model predicts that this "
                "Near-Earth Object is not hazardous."
            )


        # =============================================
        # PROBABILITY
        # =============================================

        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(
                input_data
            )[0]


            st.subheader("📈 Prediction Probability")


            p1, p2 = st.columns(2)


            with p1:

                st.metric(
                    "Not Hazardous",
                    f"{probabilities[0] * 100:.2f}%"
                )


            with p2:

                st.metric(
                    "Hazardous",
                    f"{probabilities[1] * 100:.2f}%"
                )


            probability_df = pd.DataFrame({

                "Class": [
                    "Not Hazardous",
                    "Hazardous"
                ],

                "Probability (%)": [
                    round(probabilities[0] * 100, 2),
                    round(probabilities[1] * 100, 2)
                ]

            })


            st.dataframe(
                probability_df,
                use_container_width=True,
                hide_index=True
            )


    except Exception as e:

        st.error("❌ Prediction Error")

        st.write(str(e))


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🌍 NEO Hazard Prediction System | "
    "Random Forest Classifier"
)
