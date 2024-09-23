from crewai import Crew, Process
from agents import MediumAgents
from tasks import MediumTasks


class BlogCrew:
    def __init__(self, blog: str):
        self.blog = blog
        self.verbose = False
        self.agents = MediumAgents(verbose=self.verbose)
        self.tasks = MediumTasks()
        self.max_rpm = 3

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

        markdown_conversion = self.tasks.convert_to_markdown(
            self.agents.markdown_converter_agent(),
            [check_grammar_and_spellings]
        )

        seo_title_generation = self.tasks.seo_title_generate(
            self.agents.seo_specialist_agent(),
            [markdown_conversion]
        )

        crew = Crew(
            agents=[
                self.agents.introduction_writer_agent(),
                self.agents.conclusion_writer_agent(),
                self.agents.grammar_checker_agent(),
                self.agents.markdown_converter_agent(),
                self.agents.seo_specialist_agent()
            ],
            tasks=[
                prepare_introduction,
                prepare_conclusion,
                check_grammar_and_spellings,
                markdown_conversion,
                seo_title_generation
            ],
            verbose=self.verbose,
            # manager_llm=self.agents.openai_gpt4o,
            manager_agent=self.agents.expert_project_manager_agent(),
            process=Process.hierarchical,
            max_rpm=self.max_rpm
        )

        result = crew.kickoff()
        return result
