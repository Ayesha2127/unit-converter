import streamlit as st
from streamlit_extras import add_vertical_space as avs

# Page Configuration
st.set_page_config(
    page_title="Convertify",
    page_icon="📐",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for Gradient Background, Fonts, and Styling
st.markdown(
    """
    <style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(45deg,  #BCE7FC,  #C491B1 );
        background-size: 300% 300%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Stylish Fonts */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Georgia', serif;
        color: #2E4053;
    }
    
    .stButton button {
    font-family: 'Georgia', serif;
    background-color: #FF6F61; /* Button background color */
    color: white; /* Text color */
    border-radius: 10px; /* Rounded corners */
    padding: 10px 20px; /* Padding inside the button */
    font-size: 16px; /* Font size */
    border: none; /* Remove default border */
    cursor: pointer; /* Pointer cursor on hover */
    transition: background-color 0.3s ease, color 0.3s ease; /* Smooth transition */
}

.stButton button:hover {
    background-color: #FF3B2F; /* Darker background color on hover */
    color: white; /* Keep text color white on hover */
}
    }
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        font-family: 'Georgia', serif;
        border-radius: 10px;
    }

    /* Footer Styling */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #2E4053;
        color: white;
        text-align: center;
        padding: 10px;
        font-family: 'Georgia', serif;
    }

    /* Center Logo */
    .center {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Logo and Slogan
def display_header():
    st.markdown('<div class="center">', unsafe_allow_html=True)
    st.image("logo.png", width=400)  # Adjust width as needed
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("**_Convert Smarter, Not Harder!_**", unsafe_allow_html=True)

# Footer
def display_footer():
    st.markdown(
        """
        <div class="footer">
            Created by Ayesha Waseem | Powered by Streamlit
        </div>
        """,
        unsafe_allow_html=True,
    )

# Length Converter
def length_converter():
    st.header("📏 Length Converter")
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Feet", "Kilometers", "Miles"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Feet", "Kilometers", "Miles"])
    value = st.number_input("Enter value", min_value=0.0, step=0.1)

    if st.button("Convert Length", key="length_convert_button"):
        if from_unit == "Meters" and to_unit == "Feet":
            result = value * 3.28084
        elif from_unit == "Feet" and to_unit == "Meters":
            result = value / 3.28084
        elif from_unit == "Kilometers" and to_unit == "Miles":
            result = value * 0.621371
        elif from_unit == "Miles" and to_unit == "Kilometers":
            result = value / 0.621371
        else:
            result = value  # If units are the same
        st.success(f"**Converted Value:** {result:.4f} {to_unit}")

# Weight Converter
def weight_converter():
    st.header("⚖️ Weight Converter")
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Pounds", "Grams", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Pounds", "Grams", "Ounces"])
    value = st.number_input("Enter value", min_value=0.0, step=0.1)

    if st.button("Convert Weight", key="weight_convert_button"):
        if from_unit == "Kilograms" and to_unit == "Pounds":
            result = value * 2.20462
        elif from_unit == "Pounds" and to_unit == "Kilograms":
            result = value / 2.20462
        elif from_unit == "Grams" and to_unit == "Ounces":
            result = value * 0.035274
        elif from_unit == "Ounces" and to_unit == "Grams":
            result = value / 0.035274
        else:
            result = value  # If units are the same
        st.success(f"**Converted Value:** {result:.4f} {to_unit}")

# Temperature Converter
def temperature_converter():
    st.header("🌡️ Temperature Converter")
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    value = st.number_input("Enter value", min_value=-273.15, step=0.1)

    if st.button("Convert Temperature", key="temp_convert_button"):
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value  # If units are the same
        st.success(f"**Converted Value:** {result:.4f} {to_unit}")

# Volume Converter
def volume_converter():
    st.header("🧴 Volume Converter")
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", ["Liters", "Gallons", "Milliliters", "Fluid Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Liters", "Gallons", "Milliliters", "Fluid Ounces"])
    value = st.number_input("Enter value", min_value=0.0, step=0.1)

    if st.button("Convert Volume", key="volume_convert_button"):
        if from_unit == "Liters" and to_unit == "Gallons":
            result = value * 0.264172
        elif from_unit == "Gallons" and to_unit == "Liters":
            result = value / 0.264172
        elif from_unit == "Milliliters" and to_unit == "Fluid Ounces":
            result = value * 0.033814
        elif from_unit == "Fluid Ounces" and to_unit == "Milliliters":
            result = value / 0.033814
        else:
            result = value  # If units are the same
        st.success(f"**Converted Value:** {result:.4f} {to_unit}")

# Currency Converter (Using forex-python)
def currency_converter():
    st.header("💵 Currency Converter")
    col1, col2 = st.columns(2)
    with col1:
        from_currency = st.selectbox("From", ["USD", "EUR", "GBP", "INR", "JPY"])
    with col2:
        to_currency = st.selectbox("To", ["USD", "EUR", "GBP", "INR", "JPY"])
    value = st.number_input("Enter value", min_value=0.0, step=0.1)

    if st.button("Convert Currency", key="currency_convert_button"):
        try:
            from forex_python.converter import CurrencyRates
            c = CurrencyRates()
            result = c.convert(from_currency, to_currency, value)
            st.success(f"**Converted Value:** {result:.4f} {to_currency}")
        except Exception as e:
            st.error(f"Error: {e}. Please check your internet connection.")

# Home Page
def home_page():
    display_header()
    st.markdown("---")
    st.markdown(
        """
       
      ### Welcome to Convertify!

**Convertify** is your ultimate tool for quick, accurate, and hassle-free unit conversions. Whether you're a student, professional, or just someone who needs to convert units in daily life, Convertify is here to make your life easier.

**Why Choose Convertify?**
- **Comprehensive Conversions**: Convertify supports a wide range of unit conversions, including length, weight, temperature, volume, and even real-time currency conversions.
- **User-Friendly Interface**: With its intuitive design and easy-to-use features, Convertify ensures a seamless experience for users of all levels.
- **Accurate Results**: Our advanced algorithms guarantee precise conversions every time, so you can trust Convertify for all your needs.
- **Fast and Efficient**: Save time with instant conversions. No more manual calculations or searching for conversion tools online!
- **Accessible Anywhere**: Convertify is available online, so you can access it anytime, anywhere, from any device.

**Key Features:**
- **Length Converter**: Convert between meters, feet, kilometers, miles, and more.
- **Weight Converter**: Switch between kilograms, pounds, grams, ounces, and other weight units.
- **Temperature Converter**: Easily convert between Celsius, Fahrenheit, and Kelvin.
- **Volume Converter**: Convert liters, gallons, milliliters, fluid ounces, and more.
- **Currency Converter**: Get real-time currency conversion rates for USD, EUR, GBP, INR, JPY, and other major currencies.

**Who Can Benefit from Convertify?**
- **Students**: Perfect for science, engineering, and math projects.
- **Professionals**: Ideal for engineers, scientists, chefs, and travelers.
- **Everyday Users**: Great for cooking, DIY projects, and general knowledge.

**Join the Convertify Community Today!**
Experience the convenience of effortless unit conversions with Convertify. Whether you're at home, in the classroom, or on the go, Convertify is your go-to tool for all your conversion needs. Start converting smarter, not harder!

        """
    )
    avs.add_vertical_space(2)
    display_footer()

# About Page
def about_page():
    display_header()
    st.markdown("---")
    st.header("👩‍💻 About Me")
    st.markdown(
        """
        ### Hi, I'm **Ayesha Waseem**! 👋

I'm a passionate and dedicated developer with a strong love for creating innovative tools that simplify everyday tasks. My journey in the world of programming began with a curiosity to solve real-world problems, and over time, I've developed a deep interest in building user-friendly applications that make life easier for everyone.

**About Me:**
- **Tech Enthusiast**: I have a keen interest in exploring new technologies and frameworks to create efficient and scalable solutions.
- **Problem Solver**: I enjoy tackling challenges and finding creative ways to solve them through code.
- **Lifelong Learner**: I believe in continuous learning and always strive to improve my skills and knowledge.
        """
    )
    avs.add_vertical_space(2)
    display_footer()

# Contact Page
def contact_page():
    display_header()
    st.markdown("---")
    st.header("📧 Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send")
        if submit_button:
            st.success("Thank you for contacting us! We'll get back to you soon.")
    display_footer()

# FAQs Page (Accordion Style)
def faqs_page():
    display_header()
    st.markdown("---")
    st.header("❓ FAQs")
    with st.expander("How do I use Convertify?"):
        st.write("Select the unit type from the sidebar, enter the value, and click Convert.")
    with st.expander("What units can I convert?"):
        st.write("You can convert length, weight, temperature, volume, and currency!")
    with st.expander("Is Convertify free to use?"):
        st.write("Yes, Convertify is completely free!")
    display_footer()

# Main App Logic
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        ["Home", "Length Converter", "Weight Converter", "Temperature Converter", "Volume Converter", "Currency Converter", "About", "Contact", "FAQs"],
    )

    if page == "Home":
        home_page()
    elif page == "Length Converter":
        display_header()
        length_converter()
        display_footer()
    elif page == "Weight Converter":
        display_header()
        weight_converter()
        display_footer()
    elif page == "Temperature Converter":
        display_header()
        temperature_converter()
        display_footer()
    elif page == "Volume Converter":
        display_header()
        volume_converter()
        display_footer()
    elif page == "Currency Converter":
        display_header()
        currency_converter()
        display_footer()
    elif page == "About":
        about_page()
    elif page == "Contact":
        contact_page()
    elif page == "FAQs":
        faqs_page()

# Run the App
if __name__ == "__main__":
    main()