from crewai import Crew, Process
from dotenv import load_dotenv

from agents import MediumAgents
from tasks import MediumTasks


load_dotenv()


class BlogCrew:
    def __init__(self, blog: str):
        self.blog = blog
        self.verbose = True
        self.agents = MediumAgents(verbose=self.verbose)
        self.tasks = MediumTasks()

    def run(self):

        prepare_introduction = self.tasks.prepare_introduction(
            self.agents.introduction_writer_agent(),
            self.blog
        )

        prepare_conclusion = self.tasks.prepare_conclusion(
            self.agents.conclusion_writer_agent(),
            self.blog
        )

        check_grammar_and_spellings = self.tasks.check_grammar_and_spellings(
            self.agents.grammar_checker_agent(),
            [prepare_conclusion, prepare_introduction]
        )

        crew = Crew(
            agents=[
                self.agents.introduction_writer_agent(),
                self.agents.conclusion_writer_agent(),
                self.agents.grammar_checker_agent()
            ],
            tasks=[
                prepare_introduction,
                prepare_conclusion,
                check_grammar_and_spellings,
            ],
            verbose=self.verbose,
            manager_llm=self.agents.openai_gpt4o,
            manager_agent=self.agents.expert_project_manager_agent(),
            process=Process.hierarchical
        )

        result = crew.kickoff()
        return result
