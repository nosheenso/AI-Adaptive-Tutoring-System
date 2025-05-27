from crewai import Crew, Process
from adaptive_tutoring_system_py.config.agents import agents
from adaptive_tutoring_system_py.config.tasks import tasks


crew = Crew(
    agents=[
        agents["learning_style_analyst"],
        agents["curriculum_planner"],
        agents["interactive_tutor"],
        agents["progress_evaluator"]
    ],
    tasks=[
        tasks["analyze_student_profile"],
        tasks["design_adaptive_curriculum"],
        tasks["conduct_tutoring_session"],
        tasks["evaluate_learning_progress"]
    ],
    process=Process.sequential
)
