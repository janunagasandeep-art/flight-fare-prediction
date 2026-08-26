import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("flight_fare_random_forest.pkl")

st.title("✈️ Flight Fare Prediction")
st.write("Enter the flight details to predict the ticket price.")

# User inputs
airline = st.selectbox(
    "Airline",
    [
        "Air India",
        "GoAir",
        "IndiGo",
        "Jet Airways",
        "Jet Airways Business",
        "Multiple carriers",
        "Multiple carriers Premium economy",
        "SpiceJet",
        "Trujet",
        "Vistara",
        "Vistara Premium economy"
    ]
)

source = st.selectbox(
    "Source",
    ["Chennai", "Delhi", "Kolkata", "Mumbai"]
)

destination = st.selectbox(
    "Destination",
    ["Cochin", "Delhi", "Hyderabad", "Kolkata", "New Delhi"]
)

additional_info = st.selectbox(
    "Additional Information",
    [
        "1 Short layover",
        "2 Long layover",
        "Business class",
        "Change airports",
        "In-flight meal not included",
        "No Info",
        "No check-in baggage included",
        "No info",
        "Red-eye flight"
    ]
)

total_stops = st.number_input(
    "Total Stops",
    min_value=0,
    max_value=4,
    value=0,
    step=1
)

journey_day = st.number_input(
    "Journey Day",
    min_value=1,
    max_value=31,
    value=1,
    step=1
)

journey_month = st.number_input(
    "Journey Month",
    min_value=1,
    max_value=12,
    value=1,
    step=1
)

dep_hour = st.number_input(
    "Departure Hour",
    min_value=0,
    max_value=23,
    value=10,
    step=1
)

dep_minute = st.number_input(
    "Departure Minute",
    min_value=0,
    max_value=59,
    value=0,
    step=1
)

arrival_hour = st.number_input(
    "Arrival Hour",
    min_value=0,
    max_value=23,
    value=12,
    step=1
)

arrival_minute = st.number_input(
    "Arrival Minute",
    min_value=0,
    max_value=59,
    value=0,
    step=1
)

duration_minutes = st.number_input(
    "Duration (Minutes)",
    min_value=1,
    max_value=2000,
    value=120,
    step=1
)

# Prediction button
if st.button("Predict Flight Price"):

    # Create all 37 model features
    data = {
        "Total_Stops": total_stops,
        "Journey_Day": journey_day,
        "Journey_Month": journey_month,
        "Dep_Hour": dep_hour,
        "Dep_Minute": dep_minute,
        "Arrival_Hour": arrival_hour,
        "Arrival_Minute": arrival_minute,
        "Duration_Minutes": duration_minutes
    }

    # Airline columns
    for col in [
        "Airline_Air India",
        "Airline_GoAir",
        "Airline_IndiGo",
        "Airline_Jet Airways",
        "Airline_Jet Airways Business",
        "Airline_Multiple carriers",
        "Airline_Multiple carriers Premium economy",
        "Airline_SpiceJet",
        "Airline_Trujet",
        "Airline_Vistara",
        "Airline_Vistara Premium economy"
    ]:
        data[col] = 1 if col == "Airline_" + airline else 0

    # Source columns
    for col in [
        "Source_Chennai",
        "Source_Delhi",
        "Source_Kolkata",
        "Source_Mumbai"
    ]:
        data[col] = 1 if col == "Source_" + source else 0

    # Destination columns
    for col in [
        "Destination_Cochin",
        "Destination_Delhi",
        "Destination_Hyderabad",
        "Destination_Kolkata",
        "Destination_New Delhi"
    ]:
        data[col] = 1 if col == "Destination_" + destination else 0

    # Additional information columns
    for col in [
        "Additional_Info_1 Short layover",
        "Additional_Info_2 Long layover",
        "Additional_Info_Business class",
        "Additional_Info_Change airports",
        "Additional_Info_In-flight meal not included",
        "Additional_Info_No Info",
        "Additional_Info_No check-in baggage included",
        "Additional_Info_No info",
        "Additional_Info_Red-eye flight"
    ]:
        data[col] = 1 if col == "Additional_Info_" + additional_info else 0

    # Convert to DataFrame
    input_data = pd.DataFrame([data])

    # Make sure columns are in exactly the same order
    input_data = input_data[model.feature_names_in_]

    # Predict
    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted Flight Price: ₹{prediction:,.2f}"
    )