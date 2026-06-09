import streamlit as st

pg = st.navigation({
    "Home" : [
        st.Page("pages/home.py", title = "Home"),
    ],

    "Maya Tiwari" : [
        st.Page("pages/m_enter.py", title = "Enter data"),
        st.Page("pages/m_observations.py", title = "Observations"),
        st.Page("pages/m_comments.py", title = "Comments")
    ],

    "Ratan Lal Tiwari": [
        st.Page("pages/r_enter.py", title="Enter Data"),
        st.Page("pages/r_observations.py", title="Observations"),
        st.Page("pages/r_comments.py", title="Comments"),
    ],
})

pg.run()

