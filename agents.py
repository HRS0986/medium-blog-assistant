from crewai import Agent
from langchain_openai import ChatOpenAI
from textwrap import dedent


class MediumAgents:
    def __init__(self):
        self.openai_gpt4o = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

    def expert_content_writer_agent(self) -> Agent:
        return Agent(
            role="Expert Content Writer",
            goal="Write a medium blog article on the given topic",
            backstory=dedent(
                """
                Expert in writing blog articles. Knowledgeable in how to structure a blog post properly.
                Many experience in writing blog articles that people can understand easily.
                """
            ),
            verbose=True,
            llm=self.openai_gpt4o,
            tools=[]
        )

    def grammar_checker_agent(self) -> Agent:
        return Agent(
            role="Grammar And Spell Checker",
            goal="Check the content for spellings, grammar mistakes and correct them",
            backstory="Expert in English language. Knowledgeable in English grammar and word spellings.",
            verbose=True,
            llm=self.openai_gpt4o,
            tools=[]
        )

    def conclusion_writer_agent(self) -> Agent:
        return Agent(
            role="Conclusion Writer",
            goal="Write a proper conclusion for the medium blog article",
            backstory=dedent(
                """
                Expert in writing conclusions for blog articles. Knowledgeable in summarizing the content.
                Many experience in writing proper conclusions.
                """
            ),
            verbose=True,
            llm=self.openai_gpt4o,
            tools=[]
        )

    def introduction_writer_agent(self) -> Agent:
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
            verbose=True,
            llm=self.openai_gpt4o,
            tools=[]
        )

    def subject_expert_agent(self, subject: str) -> Agent:
        return Agent(
            role=f"Expert in {subject}",
            goal="Check and correct the content for accuracy and correctness",
            backstory=dedent(
                f"""
                Has an expert knowledge about {subject} with tons of practical experiences.
                """
            ),
            verbose=True,
            llm=self.openai_gpt4o,
            tools=[]
        )

    def topic_modeling_agent(self) -> Agent:
        return Agent(
            role="Topic Modeling Agent",
            goal="Analyze the blog article and identify the main topic or subject area",
            backstory=dedent(
                """
                Expert in topic modeling and analyzing text data to identify the main topic and subject areas.
                """
            ),
            verbose=True,
            llm=self.openai_gpt4o,
            tools=[]
        )