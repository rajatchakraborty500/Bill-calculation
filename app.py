import streamlit as st

# Menu
menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 100,
    "Coffee": 10
}

# Title
st.title("🍽️ Welcome to Rajat Restro")

# Display menu
st.subheader("Menu")

for item, price in menu.items():
    st.write(f"{item} - Rs{price}")

# First order
item1 = st.selectbox(
    "Select the item you want to order:",
    list(menu.keys())
)

# Second order option
another_order = st.radio(
    "Do you want to order another item?",
    ["No", "Yes"]
)

item2 = None

if another_order == "Yes":
    item2 = st.selectbox(
        "Select your second item:",
        list(menu.keys())
    )

# Calculate order
if st.button("Place Order"):

    order_total = menu[item1]

    st.success(f"{item1} has been added to your order.")

    if item2:
        order_total += menu[item2]
        st.success(f"{item2} has been added to your order.")

    st.subheader(f"Total Order Amount: Rs{order_total}")