import streamlit as st
from dotenv import load_dotenv
from crew import BlogCrew
from tasks import MediumTasks
from utils.markdown_convertor import medium_to_markdown
from langtrace_python_sdk import langtrace
from crewai.tasks import TaskOutput


load_dotenv()
langtrace.init()


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
        # Input for blog URL
        blog_url = st.text_input(
            "Enter the URL of the Medium blog article you want to improve (Member Only blogs are not supported) :",
            placeholder="https://medium.com/..."
        )

        # Input for pasting blog content
        blog_content_input = st.text_area(
            "Or paste the blog content directly below:",
            placeholder="Paste blog content here..."
        )

        steps = [
            "Prepare Introduction",
            "Prepare Conclusion",
            "Check Grammar and Spellings",
            "Convert to Markdown",
            "Generate SEO Details"
        ]

        # Initialize steps list
        steps_list = [f"- {step}: Pending" for step in steps]

        # Container for displaying task steps
        steps_container = st.empty()

        if st.button("Improve Blog"):
            if blog_url:
                # If URL is provided, run funcURL
                with st.spinner("Improving blog content from URL..."):
                    try:
                        blog_content = medium_to_markdown(blog_url)

                        # Display steps
                        steps_container.markdown("\n".join(steps_list), unsafe_allow_html=True)
                        custom_callback = create_task_callback(steps_container, steps_list)

                        # Create BlogCrew instance and run tasks
                        blog_crew = BlogCrew(blog_content)
                        blog_crew.tasks = MediumTasks(callback=custom_callback)

                        result = blog_crew.run()

                        # Store improved content in session state
                        st.session_state.improved_content = result.raw

                        # Provide download option
                        st.download_button(
                            label="Download Improved Content",
                            data=result.raw,
                            file_name="improved_blog.md",
                            mime="text/markdown"
                        )
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")

            elif blog_content_input:
                # If blog content is pasted, run funcBlog
                with st.spinner("Improving pasted blog content..."):
                    try:
                        blog_content = blog_content_input

                        # Display steps
                        steps_container.markdown("\n".join(steps_list), unsafe_allow_html=True)
                        custom_callback = create_task_callback(steps_container, steps_list)

                        # Create BlogCrew instance and run tasks
                        blog_crew = BlogCrew(blog_content)
                        blog_crew.tasks = MediumTasks(callback=custom_callback)

                        result = blog_crew.run()

                        # Store improved content in session state
                        st.session_state.improved_content = result.raw

                        # Provide download option
                        st.download_button(
                            label="Download Improved Content",
                            data=result.raw,
                            file_name="improved_blog.md",
                            mime="text/markdown"
                        )
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")

            else:
                st.warning("Please enter either a blog URL or paste the blog content.")

    with right_column:
        # Display improved blog content after processing
        if 'improved_content' in st.session_state:
            st.subheader("Improved Blog Content")
            st.markdown(st.session_state.improved_content)
        else:
            st.info("Improved blog content will appear here after processing.")


if __name__ == "__main__":
    main()
