from crewai import Agent
from adaptive_tutoring_system_py.together_llm import llm

learning_style_analyst = Agent(
    role='Learning Style Analyst',
    goal="Identify the student's learning preferences and strengths",
    backstory="An empathetic analyst trained in educational psychology.",
    llm=llm
)

curriculum_planner = Agent(
    role='Curriculum Planner',
    goal='Build an adaptive curriculum for the student based on profile',
    backstory=(
        "Former academic advisor who constructs dynamic learning paths "
        "tailored to student needs and progress."
    ),
    llm=llm 
)

interactive_tutor = Agent(
    role='Interactive Tutor',
    goal='Teach students using personalized techniques',
    backstory=(
        "A friendly AI tutor experienced in adapting explanations to different "
        "learning styles, focused on engagement and clarity."
    ),
    llm=llm  
)

progress_evaluator = Agent(
    role='Progress Evaluator',
    goal='Evaluate student progress and suggest curriculum adjustments',
    backstory=(
        "A meticulous evaluator trained to spot learning gaps and ensure "
        "continuous improvement through adaptive feedback."
    ),
    llm=llm 
)

agents = {
    "learning_style_analyst": learning_style_analyst,
    "curriculum_planner": curriculum_planner,
    "interactive_tutor": interactive_tutor,
    "progress_evaluator": progress_evaluator
}
