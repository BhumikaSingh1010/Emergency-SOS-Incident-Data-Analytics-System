import streamlit as st
import pyodbc
from datetime import datetime

st.set_page_config(
    page_title="Emergency SOS System",
    page_icon="🚨",
    layout="centered"
)

# Initialize page
if "page" not in st.session_state:
    st.session_state.page = 1


# ================= PAGE 1 =================

if st.session_state.page == 1:

    st.title("🚨 Emergency SOS System")
    st.subheader("Your Safety. Our Priority.")

    st.write("Welcome to the Emergency SOS System.")
    st.write(
        "This system allows you to quickly submit "
        "an emergency report and request assistance."
    )

    st.divider()

    st.warning("⚠️ Use this system only for genuine emergencies.")

    if st.button("🆘 START SOS", use_container_width=True):
        st.session_state.page = 2
        st.rerun()


# ================= PAGE 2 =================

elif st.session_state.page == 2:

    st.title("📝 Emergency Information")
    st.write("Please enter the following information.")

    user_name = st.text_input("👤 Your Name")
    phone = st.text_input("📞 Phone Number")

    emergency_type = st.selectbox(
        "🚨 Emergency Type",
        ["Medical", "Fire", "Accident", "Crime", "Other"]
    )

    location = st.text_input("📍 Location")

    latitude = st.number_input(
        "🌐 Latitude",
        format="%.6f"
    )

    longitude = st.number_input(
        "🌐 Longitude",
        format="%.6f"
    )

    description = st.text_area(
        "📝 Describe the Emergency"
    )

    priority = st.selectbox(
        "⚠️ Priority",
        ["Low", "Medium", "High", "Critical"]
    )

    if st.button("➡️ Continue", use_container_width=True):

        st.session_state.update({
            "user_name": user_name,
            "phone": phone,
            "emergency_type": emergency_type,
            "location": location,
            "latitude": latitude,
            "longitude": longitude,
            "description": description,
            "priority": priority
        })

        st.session_state.page = 3
        st.rerun()


# ================= PAGE 3 =================

elif st.session_state.page == 3:

    st.title("🚨 SOS READY TO SEND")

    st.warning(
        "⚠️ Please review your emergency information "
        "before sending."
    )

    st.subheader("📋 Emergency Details")

    fields = {
        "👤 Name": "user_name",
        "📞 Phone": "phone",
        "🚨 Emergency Type": "emergency_type",
        "📍 Location": "location",
        "🌐 Latitude": "latitude",
        "🌐 Longitude": "longitude",
        "📝 Description": "description",
        "⚠️ Priority": "priority"
    }

    for label, key in fields.items():
        st.write(f"**{label}:**", st.session_state[key])

    st.divider()


    # SEND SOS
    if st.button("🔴 SEND SOS", use_container_width=True):

        try:

            connection = pyodbc.connect(
                r"DRIVER={ODBC Driver 17 for SQL Server};"
                r"SERVER=.\SQLEXPRESS;"
                r"DATABASE=EmergencySOS;"
                r"Trusted_Connection=yes;"
            )

            cursor = connection.cursor()

            query = """
            INSERT INTO SOS_Reports
            (
                Report_Date_Time,
                User_Name,
                Phone_Number,
                Emergency_Type,
                Location,
                Latitude,
                Longitude,
                Description,
                Priority,
                Status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            values = (
                datetime.now(),
                st.session_state.user_name,
                st.session_state.phone,
                st.session_state.emergency_type,
                st.session_state.location,
                st.session_state.latitude,
                st.session_state.longitude,
                st.session_state.description,
                st.session_state.priority,
                "Active"
            )

            cursor.execute(query, values)
            connection.commit()

            cursor.close()
            connection.close()

            st.success(
                "✅ SOS request successfully saved to the database!"
            )

            st.balloons()

        except Exception as e:

            st.error(f"❌ Error while saving SOS: {e}")


    # GO BACK
    if st.button("⬅️ Go Back", use_container_width=True):

        st.session_state.page = 2
        st.rerun()