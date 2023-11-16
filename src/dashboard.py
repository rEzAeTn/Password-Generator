
import streamlit as st
from PIL import Image

from src.main import MemorablePasswordGenerator, PinCodesGenerator, RandomPasswordGenerator

# Add the path of your project to the system path
#   Use in Googel Colab:
#       import sys
#       sys.path.append('/content/drive/MyDrive/Colab_Notebooks/Password_Generator')


# Load the banner image
image = Image.open('/Password-Generator/image/banner.png')
st.image(image)

# Title of the app
st.markdown("<h1 style='text-align: center; color: green;'>Password Generators</h1>", unsafe_allow_html=True)

# Add a blank line for better readability
st.write("\n")

# Allow the user to select the type of password they want to generate
new_title = '<h1 style="text-align:sans-serif; color: black; font-size: 25px;">Select Password Type</h1>'
tag_radio = st.markdown(new_title, unsafe_allow_html=True)
password_type = st.radio("", ("Pin Code", "Random Password", "Memorable Password"))

# Depending on the type of password, display the appropriate options to the user
if password_type == "Pin Code":
    pin_length = st.slider("Select Length Pin Code", 4, 16)
    generator = PinCodesGenerator(length=pin_length)

elif password_type == "Random Password":
    pass_length = st.slider("Select Length Password", 4, 32)
    # Changing the layout of the page (split columns)
    col1, col2, col3, col4 = st.columns(4)
    include_lowercase = col1.toggle("Lowercase", value=True)
    include_uppercase = col2.toggle("Uppercase")
    include_punc = col3.toggle("Punctuation")
    include_number = col4.toggle("Number")

    generator = RandomPasswordGenerator(
        length=pass_length,
        include_lowercase=include_lowercase,
        include_uppercase=include_uppercase,
        include_punc=include_punc,
        include_number=include_number
    )

elif password_type == "Memorable Password":
    number_of_words = st.slider("Select  Of Words", 1, 16)
    # Changing the layout of the page (split columns)
    col1, col2, col3 = st.columns(3)
    capitalized = col1.toggle("Capitalization")
    separator = col2.toggle("Change Separator")
    vocabulary = col3.toggle("Use Your Vocabulary")
    if separator:
        separator = st.text_input("Separator", value="-")
    else:
        separator = "-"

    if vocabulary:
        vocabulary = st.text_input("Input Your Vocabularys (**Separate With `,`**)")
        vocabulary = [word.strip() for word in vocabulary.split(',')]
    else:
        vocabulary = None

    generator = MemorablePasswordGenerator(
        number_of_words=number_of_words,
        separator=separator,
        capitalized=capitalized,
        vocabulary=vocabulary,
    )

# Add a blank line for better readability
st.write("\n")

# Generate the password and display it to the user if they choose to show it
password = generator.password_generator()
show_pass = st.checkbox('Show Password')
if show_pass:
    st.write(fr"**Your Password: ``` {password} ```** ")
