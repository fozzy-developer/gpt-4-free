import g4f
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

print("""
[1] > Ask a question
[2] > Exit
""")

choice = input("Enter option: ")

if choice == "1":
    user_input = input("Enter your query: ")
    print("Processing...")

    try:
        response = g4f.ChatCompletion.create(
            model='gpt-4',
            messages=[{'role': 'user', 'content': user_input}]
        )
        print(f"Answer: {response}")
    except Exception as e:
        print(f"Error: {e}")

elif choice == "2":
    exit()

else:
    print("Wrong choice")