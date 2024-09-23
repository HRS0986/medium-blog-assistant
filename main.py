import streamlit as st
from textwrap import dedent
from dotenv import load_dotenv
from crew import BlogCrew
from utils.file_reader import read_blog_from_file
import agentops
import litellm
import os

# Load environment variables
load_dotenv()

# Initialize AgentOps and LiteLLM
agentops.init(os.environ.get("AGENTOPS_API_KEY"))
litellm.set_verbose = True

def main():
    st.set_page_config(page_title="Blog Crew", page_icon="📝")

    st.title("Welcome to Blog Crew")
    st.markdown("---")

    # Input for blog URL
    blog_url = st.text_input(
        "Enter the URL of the Medium blog article you want to improve:",
        placeholder="https://medium.com/..."
    )

    if st.button("Improve Blog"):
        if blog_url:
            with st.spinner("Improving blog content..."):
                try:
                    # Read blog content
                    blog_content = read_blog_from_file(blog_url)

                    # Create BlogCrew instance and run improvement
                    blog_crew = BlogCrew(blog_content)
                    result = blog_crew.run()

                    # Display improved content
                    st.subheader("Improved Blog Content")
                    st.markdown(result.raw)

                    # Option to download improved content
                    st.download_button(
                        label="Download Improved Content",
                        data=result.raw,
                        file_name="improved_blog.md",
                        mime="text/markdown"
                    )
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a valid blog URL.")

if __name__ == "__main__":
    main()