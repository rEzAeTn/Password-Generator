# Password Generator
![Banner](image/banner2.png)


## Project Overview

The 'Password Generator Dashboard' is an interactive web application built with Python and Streamlit. It allows users to generate different types of passwords quickly and randomly, including:
- Pin Code
- Random Password
- Memorable Password


## Directory Structure

```
Password-Generator/
|-- src/
| |-- main.py
| |-- dashboard.py/
|-- image/
| |-- banner.png
|-- README.md
|-- requirements.txt
```

## Project Structure

- `main.py`:A Python module containing the password generators classes; `RandomPasswordGenerator`, `MemorablePasswordGenerator`, `PinCodeGenerator`.

- `dashboard.py`: A Python script using Streamlit to create a web app interface for the password generators.  The user can select the type of password and the options for generating the password.



## Prerequisites

- Python 3.6 or later
- Streamlit
- NLTK (Natural Language Toolkit)

To install NLTK, use pip:

```bash
pip install nltk
```

After installing NLTK, you need to download the 'words' corpus. Run Python and type these commands:

```python
import nltk
nltk.download('words')
```

Then install Streamlit using pip:

```bash
pip install streamlit
```

You can install all the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```


## How To Run
### Run To Local System
- Clone the repository to your local system.
- Open your command line and navigate to the `Password-Generator` project directory.
- install necessary dependencies and **Prerequisites**.
- Add the current directory to the `PYTHONPATH`.
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
```
- Run `Password Generator` script.
```bash
python main.py
```
- Run `Dashboard`.
```bash
streamlit run dashboard.py
```

### Run To Google Colab

- How TO Run Streamlit in Google Colab

    1- **Install Streamlit library:**
    ```python
    !pip install -q streamlit
    !pip freeze | grep streamlit
    ```

    2- **Run the Streamlit app in the background:**
    ```python
    !streamlit run app.py &>/dev/null&
    or
    !streamlit run app.py --server.port 8502 &>/dev/null&
    ```

    3- **Install LocalTunnel:**
    ```python
    !npm install localtunnel
    ```

    4- **Get public IP:**
    ```python
    !curl -s http://whatismyip.akamai.com/
    ```
    5- **Run LocalTunnel in the background:**
    ```python
    !npx localtunnel --port 8502
    or
    !nohup npx localtunnel --port 8502 &
    !cat nohup.out
    ```

- Add the current directory to the `PYTHONPATH`. add tis cod to Script
```bash
import sys
sys.path.append('Script Path')
```

## License

This project is licensed under the terms of the MIT license.




