from crewai import Agent
from langchain_openai import ChatOpenAI
from textwrap import dedent


class MediumAgents:
    def __init__(self, verbose: bool = False):
        self.openai_gpt4o = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
        self.verbose = verbose

    def expert_project_manager_agent(self, verbose: bool = None) -> Agent:
        return Agent(
            role="Expert Project Manager",
            goal="Efficiently manage the crew and ensure high-quality task completion",
            backstory=dedent(
                """
                Experienced project manager, skilled in overseeing complex projects and guiding teams to success. You
                have many experiences in content writing. You are familiar with the process of creating blog articles.
                Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on
                time and to the highest standard.
                """
            ),
            verbose=verbose if verbose is not None else self.verbose,
            llm=self.openai_gpt4o,
            allow_delegation=True,
        )

    def grammar_checker_agent(self, verbose: bool = None) -> Agent:
        return Agent(
            role="Grammar And Spell Checker",
            goal="Check the content for spellings, grammar mistakes and correct them",
            backstory="Expert in English language. Knowledgeable in English grammar and word spellings.",
            verbose=verbose if verbose is not None else self.verbose,
            llm=self.openai_gpt4o
        )

    def markdown_converter_agent(self, verbose: bool = None) -> Agent:
        return Agent(
            role="Markdown Converter",
            goal="Convert the medium blog article to markdown format",
            backstory=dedent(
                """
                Expert in converting HTML or text content to markdown format. Knowledgeable in markdown syntax.
                Many experience in converting various types of content to markdown format using suitable styles.
                """
            ),
            verbose=verbose if verbose is not None else self.verbose,
            llm=self.openai_gpt4o
        )

    def conclusion_writer_agent(self, verbose: bool = None) -> Agent:
        return Agent(
            role="Conclusion Writer",
            goal="Write a proper conclusion for the medium blog article",
            backstory=dedent(
                """
                Expert in writing conclusions for blog articles. Knowledgeable in summarizing the content.
                Many experience in writing proper conclusions and summarizing contents.
                """
            ),
            verbose=verbose if verbose is not None else self.verbose,
            llm=self.openai_gpt4o
        )

    def introduction_writer_agent(self, verbose: bool = None) -> Agent:
        return Agent(
            role="Introduction/Lead Paragraph Writer",
            goal="Write a proper introduction/lead paragraph for the medium blog article",
            backstory=dedent(
                """
                Expert in writing introductions/lead paragraphs for blog articles.
                Knowledgeable in introducing the contents in creatively.
                Many experience in writing proper introductions.
                """
            ),
            verbose=verbose if verbose is not None else self.verbose,
            llm=self.openai_gpt4o
        )

    def subject_expert_agent(self, verbose: bool = None) -> Agent:
        return Agent(
            role=f"Subject Matter Expert",
            goal="Check and correct the content for accuracy and correctness",
            backstory=dedent(
                """
                Has expert knowledge about the identified subject area with tons of practical experiences.
                Able to adapt to various subjects and provide accurate information and corrections.
                """
            ),
            verbose=verbose if verbose is not None else self.verbose,
            llm=self.openai_gpt4o
        )

    def topic_modeling_agent(self, verbose: bool = None) -> Agent:
        return Agent(
            role="Topic Modeling Agent",
            goal="Analyze the blog article and identify the main topic or subject area",
            backstory=dedent(
                """
                Expert in topic modeling and analyzing text data to identify the main topic and subject areas.
                """
            ),
            verbose=verbose if verbose is not None else self.verbose,
            llm=self.openai_gpt4o
        )
