from crewai import Task, Agent
from textwrap import dedent


class MediumTasks:
    def __tip_section(self) -> str:
        return dedent(
            """
            If you do your best work, you will be given a $10,000 commission.
            If not, you will not get the commission.
            """
        )

    def make_better_blog_article(self, agent: Agent, blog: str) -> Task:
        return Task(
            description=dedent(
                f"""
                Task: Make the medium blog article better.
                Description: Study the given blog article. Improve the blog post in a creative way. Add more details,
                correct any mistakes, and make the blog post more engaging. And make blog article crystal clear to the
                audience. Output should be the blog article with improvements.
                Parameters (parameter values are delimited in triple backticks):
                    - Blog (in markdown format): ```{blog}```
                Notes: {self.__tip_section()}
                """
            ),
            agent=agent
        )

    def prepare_introduction(self, agent: Agent, blog: str) -> Task:
        return Task(
            decription=dedent(
                f"""
                Task: Write or rewrite the introduction/lead paragraph for the medium blog article.
                Description: Study the given blog article. Check if the blog post already have an introduction.
                If yes, read the introduction and improve that in more creative manner.
                If it does not have an introduction, write a proper introduction in creative way. But don't be dramatic.
                Write a natural one. It should more close to the writing style of the current blog post. Should not
                change anything not related to introduction. Output should be the blog article with improved introduction.
                Parameters (parameter values are delimited in triple backticks):
                    - Blog (in markdown format): ```{blog}```
                Notes: {self.__tip_section()}
                """
            ),
            agent=agent
        )

    def prepare_conclusion(self, agent: Agent, blog: str) -> Task:
        return Task(
            description=dedent(
                f"""
                Task: Write or rewrite the conclusion for the medium blog article.
                Description: Study the given blog article. Check if the blog post already have a conclusion. If yes
                read the conclusion and improve that in more creative manner. If the conclusion contain unnecessary
                information, remove them. Then add relevant details to the conclusion. If it does not have a conclusion,
                write a proper conclusion in creative way. But don't be dramatic. Write a natural one. It should more
                close to the writing style of the current blog post. Should not change anything not related to
                conclusion. Output should be the blog article with improved conclusion.
                Parameters (parameter values are delimited in triple backticks):
                    - Blog (in markdown format): ```{blog}```
                Notes: {self.__tip_section()}
                """
            ),
            agent=agent
        )

    def check_grammar_and_spellings(self, agent: Agent, blog: str) -> Task:
        return Task(
            description=dedent(
                f"""
                Task: Check the grammar and spelling mistakes in the medium blog article.
                Description: Study the given blog article. Check the grammar and spelling mistakes in the blog post.
                Correct the mistakes and make the blog post error free. If there are no mistakes do nothing.
                Output should be the blog article with corrected grammar and spelling mistakes.
                Parameters (parameter values are delimited in triple backticks):
                    - Blog (in markdown format): ```{blog}```
                Notes: {self.__tip_section()}
                """
            ),
            agent=agent
        )

    def analyze_for_subject_area(self, agent: Agent, blog: str) -> Task:
        return Task(
            description=dedent(
                f"""
                Task: Analyze the given medium blog article and find the subject area.
                Description: Study the given blog article. Find the most suitable subject areas of the blog post.
                The output should be an string contain the subject area or areas of the blog post.
                Parameters (parameter values are delimited in triple backticks):
                    - blog (in markdown format): ````{blog}```
                Notes: {self.__tip_section()}
                """
            ),
            agent=agent
        )

    def check_for_content_accuracy(self, agent: Agent, blog: str, subject: str) -> Task:
        return Task(
            description=dedent(
                f"""
                Task: Check the content accuracy of the medium blog article.
                Description: Study the given blog article. Check the content accuracy of the blog post.
                If there are any inaccurate information, correct them. If there are no mistakes do nothing.
                Output should be the blog article with corrected content accuracy.
                Parameters (parameter values are delimited in triple backticks):
                    - Blog (in markdown format): ```{blog}```
                    - Subject Area: ```{subject}```
                Notes: {self.__tip_section()}
                """
            ),
            agent=agent
        )
