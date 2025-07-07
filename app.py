# app.py
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Safety check
if not api_key:
    st.error("🚫 OPENAI_API_KEY not found. Please check your .env file.")
    st.stop()

# LangChain & OpenAI imports
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import OpenAI
import openai

# Set up OpenAI for non-LangChain use (for auto-insights)
openai.api_key = api_key

# Streamlit UI
st.set_page_config(page_title="InsightCopilot", layout="wide")
st.title("📊 InsightCopilot")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📌 Data Preview")
    st.dataframe(df.head())

    # --- AUTO INSIGHT SECTION ---
    if st.button("🔍 Generate Auto Insights"):
        with st.spinner("Analyzing data..."):
            profile = df.describe(include='all', datetime_is_numeric=True).to_dict()
            prompt = f"Given the dataset summary: {profile}, write 5 business insights in markdown bullet points."

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a data analyst. Write concise business-style insights."},
                    {"role": "user", "content": prompt}
                ]
            )
            insights = response['choices'][0]['message']['content']
            st.markdown(insights)

    # --- CHAT WITH DATA SECTION ---
    st.subheader("💬 Chat With Your Data")
    query = st.text_input("Ask a question (e.g. What's the average revenue?)")
    if query:
        try:
            llm = OpenAI(temperature=0, openai_api_key=api_key)
            agent = create_pandas_dataframe_agent(llm, df, verbose=False, allow_dangerous_code=True)
            response = agent.run(query)
            st.success(response)
        except Exception as e:
            st.error(f"❌ Error: {e}")
    # --- INTERACTIVE CHART GENERATOR (PLOTLY + GPT SUGGESTION) ---
    st.subheader("📈 Auto Chart Generator (Interactive)")

    # Suggest a chart idea using GPT
    if st.button("💡 Suggest a Chart Idea"):
        try:
            suggestion_prompt = f"Based on this dataset schema: {df.dtypes.to_dict()}, suggest one useful chart a business analyst might want to see. Just provide the plain-English idea."
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a data analyst helping generate ideas for visualizations."},
                    {"role": "user", "content": suggestion_prompt}
                ]
            )
            chart_suggestion = response['choices'][0]['message']['content']
            st.info(f"💡 Suggested: *{chart_suggestion}*")
            st.session_state['viz_prompt'] = chart_suggestion
        except Exception as e:
            st.error(f"❌ Error suggesting chart: {e}")

    # Let user modify or enter chart prompt
    viz_prompt = st.text_input("Describe the chart you want:", value=st.session_state.get('viz_prompt', ''))

    if viz_prompt:
        try:
            from langchain_experimental.agents import create_pandas_dataframe_agent
            from langchain_openai import OpenAI
            import plotly.express as px
            import streamlit.components.v1 as components
            import io
            import contextlib

            # Create agent (code execution enabled)
            llm = OpenAI(temperature=0, openai_api_key=api_key)
            agent = create_pandas_dataframe_agent(
                llm, df, verbose=False, allow_dangerous_code=True
            )

            with st.spinner("Generating Plotly chart..."):
                # Instruct LLM to use Plotly and return the figure
                chart_code_prompt = f"""
                Write Python code using Plotly Express (as px) to create and return an interactive chart from this instruction: "{viz_prompt}". 
                Assume `df` is the DataFrame. Do not use plt.show(). Just assign the chart to a variable called `fig` and return it.
                """
                # Redirect stdout and exec generated code
                exec_buffer = {}
                result = agent.run(chart_code_prompt)

                # Try to extract and execute the code
                with contextlib.redirect_stdout(io.StringIO()):
                    exec(result, {"df": df, "px": px}, exec_buffer)

                fig = exec_buffer.get("fig")
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("⚠️ No chart was generated. Try rewording your prompt.")

                # Show LLM explanation/code
                with st.expander("🧠 Show Python code"):
                    st.code(result, language="python")

        except Exception as e:
            st.error(f"❌ Error generating chart: {e}")
