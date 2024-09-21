from crewai import Task, Agent
from textwrap import dedent
from crewai.tasks import TaskOutput


class MediumTasks:

    @staticmethod
    def __task_callback(output: TaskOutput):
        print("\n\nTask Completed")
        print(f"Task: {output.description}")
        print(f"Context: {output.raw}\n\n")

    @staticmethod
    def __tip_section() -> str:
        return dedent(
            """
            If you do your best work, you will be given a $10,000 commission.
            If not, you will not get the commission.
            """
        )

    def prepare_introduction(self, agent: Agent, blog: str) -> Task:
        return Task(
            description=dedent(
                f"""
                Task: Write or rewrite the introduction/lead paragraph for the medium blog article.
                Description: Study the given blog article. Check if the blog post already have an introduction. If yes,
                read the introduction and check does it need any improvements. If it need some improvements, improve
                that in more creative manner, but don't change the wring style and the core idea of it. If the existing
                introduction does not need any improvement don't do anything to that. If it does not have an
                introduction, write a proper introduction in creative way. But don't be dramatic. Write a natural one.
                It should more close to the writing style of the current blog post. Should not change anything not
                related to introduction. Output should be the blog article with improved introduction.
                Parameters (parameter values are delimited in triple backticks):
                    - Blog (in markdown format): ```{blog}```
                Notes: {self.__tip_section()}
                """
            ),
            expected_output="Blog article with improved introduction in markdown format.",
            agent=agent,
            async_execution=True,
            callback=self.__task_callback
        )

    def prepare_conclusion(self, agent: Agent, blog: str) -> Task:
        return Task(
            description=dedent(
                f"""
                Task: Write or rewrite the conclusion for the medium blog article.
                Description: Study the given blog article. Check if the blog post already have a conclusion. If yes
                read the conclusion and check does it need any improvements. If it need some improvements, improve
                that in more creative manner, but don't change the wring style and the core idea of it. If the existing
                conclusion does not need any improvement don't do anything to that. If the conclusion contain un wanted
                information, remove them. Then add relevant details to the conclusion. If it does not have a conclusion,
                write a proper conclusion in creative way. But don't be dramatic. Write a natural one. It should more
                close to the writing style of the current blog post. Should not change anything not related to
                conclusion. Output should be the blog article with improved conclusion.
                Parameters (parameter values are delimited in triple backticks):
                    - Blog (in markdown format): ```{blog}```
                Notes: {self.__tip_section()}
                """
            ),
            expected_output="Blog article with improved conclusion in markdown format.",
            agent=agent,
            async_execution=True,
            callback=self.__task_callback
        )

    def check_grammar_and_spellings(self, agent: Agent, blog_tasks: list[Task]) -> Task:
        return Task(
            description=dedent(
                f"""
                Task: Check the grammar and spelling mistakes in the medium blog article.
                Description: Study the given blog article. Check the grammar and spelling mistakes in the blog post.
                Correct the mistakes and make the blog post error free. If there are no mistakes do nothing.
                Output should be the blog article with corrected grammar and spelling mistakes.
                Notes: {self.__tip_section()}
                """
            ),
            expected_output="Blog article with corrected grammar and spelling mistakes in markdown format.",
            agent=agent,
            context=blog_tasks,
            callback=self.__task_callback
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
            expected_output="An string contains subject area or areas of the blog post.",
            agent=agent,
            callback=self.__task_callback
        )

    def check_for_content_accuracy(self, agent: Agent, blog: str, subject: Task) -> Task:
        return Task(
            description=dedent(
                f"""
                Task: Check the content accuracy of the medium blog article.
                Description: Study the given blog article. Check the content accuracy of the blog post.
                If there are any inaccurate information, correct them. If there are no mistakes do nothing.
                Output should be the blog article with corrected content accuracy.
                Parameters (parameter values are delimited in triple backticks):
                    - Blog (in markdown format): ```{blog}```
                Notes: {self.__tip_section()}
                """
            ),
            expected_output="Blog article with corrected content accuracy in markdown format.",
            agent=agent,
            context=[subject],
            callback=self.__task_callback
        )

    def convert_to_markdown(self, agent: Agent, blog_tasks: list[Task]) -> Task:
        return Task(
            description=dedent(
                f"""
                Task: Convert the medium blog article to markdown format.
                Description: Study the given blog article. If it already in markdown format, check for syntaxes.
                If you found some mistakes only correct them. If no mistakes, do nothing. Convert the blog post
                to markdown format. If it is not in markdown format, convert it to markdown format using suitable
                styles. After formatting, the blog should be easily readable. use appropriate gaps, spacing between
                paragraphs. Use headings, lists for suitable places. DON'T INCLUDE THE FINAL CONTENT WITHIN TRIPLE
                BACKTICKS. Just give the markdown formatted content ready to render. DO NOT CHANGE ANY OF THE CONTENT.
                Output should be the blog article in markdown format. Study following example Your output should be
                like correct one. After format, remove first and last triple backticks.
                Example:
                    Incorrect:
                        ```markdown
                        # Title
                        ## Subtitle
                        Other connet...
                        ```
                    Correct:
                        # Title
                        ## Subtitle
                        Other content...
                Notes: {self.__tip_section()}
                """
            ),
            expected_output="Readable blog article in markdown format.",
            agent=agent,
            context=blog_tasks,
            callback=self.__task_callback
        )
