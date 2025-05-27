from crewai import Task
from .agents import agents

analyze_student_profile = Task(
    description=(
        "Review student profile information including prior knowledge, preferred formats "
        "(video, reading, hands-on), and motivation. Your goal is to extract the student's "
        "learning style and strengths."
    ),
    expected_output="A brief profile summary including learning style, strengths, and recommended strategies.",
    agent=agents["learning_style_analyst"]
)

design_adaptive_curriculum = Task(
    description=(
        "Use the student profile to create a tailored curriculum plan including topics, sequence, "
        "and delivery format. Justify why each piece was chosen."
    ),
    expected_output="A structured list of lessons with explanations for their order and format.",
    agent=agents["curriculum_planner"]
)

conduct_tutoring_session = Task(
    description=(
        "Deliver a short tutoring session based on the curriculum plan. Adjust tone and method "
        "dynamically based on style."
    ),
    expected_output="A transcript of the tutoring session and a confidence score (0-100) indicating student understanding.",
    agent=agents["interactive_tutor"]
)

evaluate_learning_progress = Task(
    description=(
        "Analyze student interactions, test responses, and engagement metrics. Determine if they "
        "are on track or if the plan should change."
    ),
    expected_output="A report with recommended changes or confirmation of sufficient progress.",
    agent=agents["progress_evaluator"]
)

tasks = {
    "analyze_student_profile": analyze_student_profile,
    "design_adaptive_curriculum": design_adaptive_curriculum,
    "conduct_tutoring_session": conduct_tutoring_session,
    "evaluate_learning_progress": evaluate_learning_progress
}
