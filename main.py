import streamlit as st
from dotenv import load_dotenv
from crew import BlogCrew
from tasks import MediumTasks
from utils.file_reader import read_blog_from_file
import agentops
import os
from crewai.tasks import TaskOutput

load_dotenv()

agentops.init(os.environ.get("AGENTOPS_API_KEY"))


def create_task_callback(steps_container, steps_list):
    def task_callback(output: TaskOutput):
        task_name = output.name
        print(f"Task Name : {task_name}")

        # Update the steps in the list
        for i, step in enumerate(steps_list):
            if step.startswith(f"- {task_name}:"):
                steps_list[i] = f"- {task_name}: <span style='color:green'>✅ Completed</span>"
                break

        # Render the updated steps in the container
        steps_container.markdown("\n".join(steps_list), unsafe_allow_html=True)
        print("\n\nTask Completed")
        print(f"Task: {output.description}")
        print(f"Context: {output.raw}\n\n")

    return task_callback


def main():
    st.set_page_config(page_title="Blog Crew", page_icon="📝", layout="wide")

    st.title("Welcome to Medium Blog Assistant 🚀")
    st.markdown("---")

    left_column, right_column = st.columns([1, 1])

    with left_column:
        blog_url = st.text_input(
            "Enter the URL of the Medium blog article you want to improve (Member Only blogs are not supported) :",
            placeholder="https://medium.com/..."
        )

        steps = [
            "Prepare Introduction",
            "Prepare Conclusion",
            "Check Grammar and Spellings",
            "Convert to Markdown",
            "Generate SEO Details"
        ]

        steps_list = [f"- {step}: Pending" for step in steps]

        steps_container = st.empty()

        if st.button("Improve Blog"):
            if blog_url:
                with st.spinner("Improving blog content..."):
                    try:
                        blog_content = read_blog_from_file(blog_url)

                        steps_container.markdown("\n".join(steps_list), unsafe_allow_html=True)
                        custom_callback = create_task_callback(steps_container, steps_list)

                        blog_crew = BlogCrew(blog_content)
                        blog_crew.tasks = MediumTasks(callback=custom_callback)

                        result = blog_crew.run()

                        st.session_state.improved_content = result.raw
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

    with right_column:
        if 'improved_content' in st.session_state:
            st.subheader("Improved Blog Content")
            st.markdown(st.session_state.improved_content)
        else:
            st.info("Improved blog content will appear here after processing.")


if __name__ == "__main__":
    main()
