#!/usr/bin/env python3

import json
import streamlit as st
import pandas as pd
from fhirclient import client
import fhirclient.models.patient as p


def print_resource(resource, indent=None, length=1000):
    s = json.dumps(resource.as_json(), indent=indent)
    print(s[: length - 4] + " ..." if len(s) > length else s)


def get_patients(smart):
    try:
        search = p.Patient.where(struct={})
        with st.spinner("Loading"):
            patients = search.perform_resources(smart.server)
        for patient in patients:
            print_resource(patient)

        patients2 = list(map(lambda x: x.as_json(), patients))

        df = pd.DataFrame(patients2)

        st.title(f"Patients found: {len(df)}")

        print(df)

        st.write("All patients:")
        st.write(df)
    except Exception as e:
        st.write(str(e))

    try:
        st.write("Capability statement:")
        with st.spinner("Loading"):
            st.write(smart.server.capabilityStatement.as_json())
    except Exception as e:
        st.write(str(e))


def reloadApp():
    try:
        settings = {"app_id": "my_web_app", "api_base": st.session_state.url}
        smart = client.FHIRClient(settings=settings)
        get_patients(smart)
    except Exception as e:
        st.write(str(e))


def main():
    st.set_page_config(layout="wide")

    st.session_state.url = "https://server.fire.ly/"

    st.session_state.url = st.selectbox(
        "Select:FHIR Server",
        (
            "https://server.fire.ly/",
            "https://fhir.simplifier.net/TeodorTest",
            "https://34.111.55.123.nip.io/TeodorTest",
            "http://localhost:8080",
        ),
    )
    if st.button("Reload"):
        reloadApp()
    else:
        reloadApp()


# ny
# https://spark.incendi.no/fhir/

if __name__ == "__main__":
    main()
