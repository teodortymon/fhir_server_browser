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

    st.write("Capability statement:")
    with st.spinner("Loading"):
        st.write(smart.server.capabilityStatement.as_json())


def main():
    st.set_page_config(layout="wide")

    # url_default_value = "http://localhost:8080"
    url_default_value = "http://localhost:8080"

    url = st.text_input("FHIR server url", url_default_value)

    settings = {"app_id": "my_web_app", "api_base": url}
    smart = client.FHIRClient(settings=settings)

    if st.button("Reload"):
        get_patients(smart)
    else:
        get_patients(smart)


# ny
# https://spark.incendi.no/fhir/

if __name__ == "__main__":
    main()
