import streamlit as st
import random
import string

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Check for special characters
    special_chars = "!@#$%^&*"
    if any(char in special_chars for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (!@#$%^&*).")

    # Determine strength level
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback, score

# Function to generate a strong password
def generate_strong_password():
    length = 12
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit App
def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")
    st.title("Password Strength Meter 🔒")
    st.markdown("Check the strength of your password and get feedback to improve it.")

    # Input field for password
    password = st.text_input("Enter your password:", type="password", placeholder="Type your password here...")

    if password:
        # Check password strength
        strength, feedback, score = check_password_strength(password)

        # Display strength with a progress bar
        st.subheader("Password Strength:")
        if strength == "Weak":
            st.error(f"Weak (Score: {score}/5)")
            st.progress(score / 5)
        elif strength == "Moderate":
            st.warning(f"Moderate (Score: {score}/5)")
            st.progress(score / 5)
        else:
            st.success(f"Strong (Score: {score}/5)")
            st.progress(score / 5)

        # Display feedback in an expander
        if feedback:
            with st.expander("🔍 Feedback to Improve:"):
                for item in feedback:
                    st.write(f"- {item}")
        else:
            st.success("✅ Your password meets all the criteria for a strong password!")

    # Password Generator in the sidebar
    st.sidebar.title("Password Generator")
    st.sidebar.markdown("Generate a strong password with the click of a button.")
    if st.sidebar.button("Generate Strong Password 🔑"):
        strong_password = generate_strong_password()
        st.sidebar.markdown("**Generated Password:**")
        st.sidebar.code(strong_password)

# Run the app
if __name__ == "__main__":
    main()