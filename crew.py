from textwrap import dedent
from crewai import Crew
from dotenv import load_dotenv

from agents import MediumAgents
from tasks import MediumTasks


load_dotenv()


class BlogCrew:
    def __init__(self, blog: str):
        self.blog = blog

    def run(self):
        agents = MediumAgents()
        tasks = MediumTasks()

        expert_content_writer_agent = agents.expert_content_writer_agent()
        introduction_writer_agent = agents.introduction_writer_agent()
        conclusion_writer_agent = agents.conclusion_writer_agent()
        grammar_checker_agent = agents.grammar_checker_agent()
        subject_area_checking_agent = agents.topic_modeling_agent()
        check_content_accuracy_agent = agents.subject_expert_agent()

        make_better_blog_article = tasks.make_better_blog_article(expert_content_writer_agent, self.blog)
        prepare_introduction = tasks.prepare_introduction(introduction_writer_agent, self.blog)
        prepare_conclusion = tasks.prepare_conclusion(conclusion_writer_agent, self.blog)
        check_grammar_and_spellings = tasks.check_grammar_and_spellings(grammar_checker_agent, self.blog)
        analyze_for_subject_area = tasks.analyze_for_subject_area(subject_area_checking_agent, self.blog)
        check_for_content_accuracy = tasks.check_for_content_accuracy(
            check_content_accuracy_agent,
            self.blog,
            analyze_for_subject_area
        )

        crew = Crew(
            agents=[
                expert_content_writer_agent,
                introduction_writer_agent,
                conclusion_writer_agent,
                grammar_checker_agent,
                subject_area_checking_agent,
                check_content_accuracy_agent
            ],
            tasks=[
                make_better_blog_article,
                prepare_introduction,
                prepare_conclusion,
                check_grammar_and_spellings,
                analyze_for_subject_area,
                check_for_content_accuracy
            ],
            verbose=True
        )

        result = crew.kickoff()
        return result
