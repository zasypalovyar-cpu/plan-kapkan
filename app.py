"""Streamlit entry point for the Plan Kapkan invitation."""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="План капкан ♛", page_icon="♛", layout="wide")
st.markdown(
    """<style>
    [data-testid="stHeader"] {display:none;}
    [data-testid="stMainBlockContainer"] {padding:0;max-width:1180px;}
    [data-testid="stAppViewContainer"] {background:#f9e4ef;}
    iframe {border:0;display:block;}
    </style>""",
    unsafe_allow_html=True,
)

invitation = components.declare_component(
    "plan_kapkan", path=str(Path(__file__).parent)
)
# Use the actual deployed address, so shared choices never point at the iframe.
from urllib.parse import urlencode
selection = urlencode({
    key: str(st.query_params.get(key, ""))[:(100 if key == "custom" else 300)]
    for key in ("places", "mode", "custom")
})
invitation(
    app_url=st.context.url or "http://localhost:8501/",
    selection=selection,
    key="invitation",
    default=None,
)
