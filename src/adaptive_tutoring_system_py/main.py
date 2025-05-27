from adaptive_tutoring_system_py.crew import crew

if __name__ == "__main__":
    result = crew.kickoff(inputs={
        "student_profile": "Jane is a high school student who prefers visual learning and has a strong interest in science."
    })
    print(result)
