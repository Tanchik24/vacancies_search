from abc import abstractmethod
import streamlit as st


class TabView:
    def __init__(self, header=None):
        st.header(header)

    @abstractmethod
    def get_text_info(self):
        pass

    @abstractmethod
    def get_text_info_visualization(self):
        pass

    @abstractmethod
    def get_candidates(self):
        pass
