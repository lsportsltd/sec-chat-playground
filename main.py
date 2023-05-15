import streamlit as st
import pandas as pd


st.title('Uber pickups in NYC')
df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 44, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 33, "is_widget": True},
    ]
)

edited_df = st.experimental_data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")