# Streamlit python FHIR server and patient browser

- [Streamlit python FHIR server and patient browser](#streamlit-python-fhir-server-and-patient-browser)
  - [DEMO](#demo)
  - [Quick overview](#quick-overview)
    - [Code structure](#code-structure)
    - [Running](#running)

## DEMO
[https://fhir-patients.streamlit.app/](https://fhir-patients.streamlit.app/)

## Quick overview

To spin up the streamlit up run:

```sh
git clone git@github.com:teodortymon/fhir_server_browser.git
cd fhir_server_browser
make install
make run
```

Then open [http://localhost:8501/](http://localhost:8501/) to see the patients on chosen FHIR server

<p align='center'>
<img src='https://gist.githubusercontent.com/teodortymon/ca06a50eaf7f58b6316bed5477a21ee6/raw/fe4b6c2b5a2709fa827fd34c4d5b1bd789cbb458/NBIS_cast.svg' width='600' alt='make run-dev'>
</p>



### Code structure

```
.
├── README.md
├── makefile
├── poetry.lock
├── pyproject.toml
├── python_client
│   ├── __init__.py
│   └── app.py
└── tests
    └── __init__.py
```

### Running

There is a `makefile` that contains commands for interacting with the server.

```
run: # Run the app
	poetry run streamlit run python_client/app.py

install: # Install dependencies, requries poetry
	poetry install
```