import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("simulation_results.csv")

df = load_data()

# Model Selection
st.sidebar.header("Model Comparison")
selected_models = st.sidebar.multiselect("Select models to compare", ["Without NexStratus", "With NexStratus"], default=["Without NexStratus", "With NexStratus"])

# Tabs 
tab1, tab2, tab3 = st.tabs(["Fulfilled vs Demand", "Stockouts", "Cost & Profit"])

# Fulfilled vs Demand
with tab1:
    st.subheader("Fulfilled Demand vs. Demand")
    fig, ax = plt.subplots()
    if "Without NexStratus" in selected_models:
        ax.plot(df.Day, df.Fulfilled, label='Fulfilled (Without)', linestyle='-', color='b')
        ax.plot(df.Day, df.Demand, label='Demand (Without)', linestyle='-', color='r')
    if "With NexStratus" in selected_models:
        ax.plot(df.Day, df.Fulfilled, label='Fulfilled (With)', linestyle='--', color='c')
        ax.plot(df.Day, df.Demand, label='Demand (With)', linestyle='--', color='m')
    ax.set_xlabel('Day')
    ax.set_ylabel('Quantity')
    ax.legend()
    st.pyplot(fig)

# Stockouts
with tab2:
    st.subheader("Stockouts by Day")
    fig, ax = plt.subplots()
    if "Without NexStratus" in selected_models:
        ax.plot(df.Day, df.Stockouts, label='Stockouts (Without)', linestyle='-', color='r')
    if "With NexStratus" in selected_models:
        ax.plot(df.Day, df.Stockouts, label='Stockouts (With)', linestyle='--', color='m')
    ax.set_xlabel('Day')
    ax.set_ylabel('Quantity')
    ax.legend()
    st.pyplot(fig)

# Cost & Profit
with tab3:
    st.subheader("Cumulative Profit and Costs")
    fig, ax = plt.subplots()
    if "Without NexStratus" in selected_models:
        ax.plot(df.Day, df["Supplier Cost"].cumsum(), color='r', linestyle='-', label='Supplier Cost (Without)')
        ax.plot(df.Day, df["Profit"].cumsum(), color='b', linestyle='-', label='Profit (Without)')
        ax.plot(df.Day, df["Revenue"].cumsum(), color='g', linestyle='-', label='Revenue (Without)')
    if "With NexStratus" in selected_models:
        ax.plot(df.Day, df["Supplier Cost"].cumsum(), color='r', linestyle='--', label='Supplier Cost (With)')
        ax.plot(df.Day, df["Profit"].cumsum(), color='b', linestyle='--', label='Profit (With)')
        ax.plot(df.Day, df["Revenue"].cumsum(), color='g', linestyle='--', label='Revenue (With)')
    ax.set_xlabel('Day')
    ax.set_ylabel('Dollars')
    ax.legend()
    st.pyplot(fig)

# Display Data
st.subheader("Simulation Data")
st.dataframe(df, use_container_width=True)
