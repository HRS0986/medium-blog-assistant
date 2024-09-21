from textwrap import dedent

from crew import BlogCrew
from utils.markdown_convertor import medium_to_markdown
from utils.file_reader import read_blog_from_file

if __name__ == "__main__":
    print("## Welcome to Blog Crew")
    print('-------------------------------')
    blog_url = input(
        dedent("""
      What is the URL of the Medium blog article you want to improve?
    """))

    # blog_content = medium_to_markdown(blog_url)
    blog_content = read_blog_from_file(blog_url)
    blog_crew = BlogCrew(blog_content)
    result = blog_crew.run()
    print(result)
    with open("output.md", "w", encoding='utf-8') as f:
        f.write(result.raw)