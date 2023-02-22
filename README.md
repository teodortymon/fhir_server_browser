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

<video src="https://user-images.githubusercontent.com/8824670/220599814-93dd838b-4771-41f5-a932-f2bacec8fbce.mov" data-canonical-src="https://user-images.githubusercontent.com/8824670/220599814-93dd838b-4771-41f5-a932-f2bacec8fbce.mov" controls="controls" muted="muted" class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px; min-height: 200px">
</video>



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
