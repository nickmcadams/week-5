import streamlit as st

from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

st.write(
    """
    How did survival rates differ by passenger class, sex, and age group?
    """
)
# Generate and display the figure
fig1 = visualize_demographic()
st.plotly_chart(fig1, use_container_width=True)

st.write(
    """
    How does average ticket fare change with family size across passenger classes?
    """
)

st.write(
    """
    The last-name counts do not perfectly agree with the family-size results.
    Passengers with the same last name are not always part of the same
    immediate family, and some family members may have different last names.
    """
)
# Generate and display the figure
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)

st.write(
'''
# Titanic Visualization Bonus
'''
)
# Generate and display the figure
fig3 = visualize_family_size()
st.plotly_chart(fig3, use_container_width=True)