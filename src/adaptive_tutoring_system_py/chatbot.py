from dotenv import load_dotenv
import os
from adaptive_tutoring_system_py.config.agents import agents  # ⬅️ Import your agents

load_dotenv()

# Get the interactive tutor agent
tutor = agents["interactive_tutor"]

def main():
    print("\n🤖 Welcome to the Adaptive Tutor! Ask me anything. Type 'exit' to quit.")
    while True:
        user_input = input("\n🧑 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        # Ask the CrewAI agent (uses LangChain under the hood)
        response = tutor.llm.invoke([
            {"role": "system", "content": f"{tutor.role}: {tutor.backstory}"},
            {"role": "user", "content": user_input}
        ])

        print(f"\n🤖 {tutor.role}: {response.content.strip()}\n")

if __name__ == "__main__":
    main()
