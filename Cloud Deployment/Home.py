import streamlit as st
import pickle
import numpy as np

def load_model(): 
    pred_input = np.array([135.570286, 738582.0, 0, 0])
    pred_input = pred_input.reshape(1,4)
    loaded_model = pickle.load(open('pages/Models/count_model.pkl', 'rb'))
    print(loaded_model.predict(pred_input))

def deploy():

    st.title('Luxury Vehicle Rental Car Forecasting')
    st.header('Justin Abernathy, Cindy Change, Christian Hollar, & Chad Miller')
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False

    st.checkbox("Disable text input widget", key="disabled")
    st.radio(
        "Set text input label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Date:",
        "YYYY-MM-DD Format",
        key="DateInput",
    )
    st.text_input(
        "Location",
        "Mercedes-Benz Stadium, State Farm Arena, or Other",
        key="LocationInput",
    )


    # with col2:
    #     text_input = st.text_input(
    #         "Enter some text 👇",
    #         label_visibility=st.session_state.visibility,
    #         disabled=st.session_state.disabled,
    #         placeholder=st.session_state.placeholder,
    #     )

    #     if text_input:
    #         st.write("You entered: ", text_input)

if __name__ == "__main__":
    load_model()
    deploy()