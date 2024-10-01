import streamlit as st
import json
import os

# File to store credentials and special code
DATA_FILE = "data.json"

# Initialize the data file if it doesn't exist
def initialize_data():
    if not os.path.exists(DATA_FILE):
        data = {
            "registrar_password": "vcsec@1987",
            "special_code": None
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)

# Load data from the file
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save data to the file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def main():
    st.title("University Portal")

    initialize_data()
    data = load_data()

    # Dropdown menu for role selection
    role = st.selectbox("Choose your role", ["Select", "Student", "Registrar"])

    if role == "Registrar":
        # Ask for password when Registrar is selected
        password = st.text_input("Enter Registrar Password", type="password")

        if password:
            if password == data["registrar_password"]:
                st.success("Password verified!")
                # Ask to enter the special code and store it permanently
                new_code = st.text_input("Enter a new special code", type="default")

                if new_code:
                    if st.button("Save Special Code"):
                        data["special_code"] = new_code
                        save_data(data)
                        st.success("Special code has been updated and stored.")
            else:
                st.error("Incorrect password.")

    elif role == "Student":
        # Allow the student to enter the special code
        entered_code = st.text_input("Enter the special code", type="default")

        if entered_code:
            if st.button("Submit"):
                if data["special_code"] is None:
                    st.error("No special code has been set by the registrar.")
                elif entered_code == data["special_code"]:
                    st.success("Special code matched!")
                else:
                    st.error("Incorrect special code.")

    else:
        st.info("Please select a role to proceed.")

if __name__ == "__main__":
    main()
