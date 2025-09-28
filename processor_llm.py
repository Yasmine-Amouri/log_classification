from dotenv import load_dotenv
from groq import Groq

load_dotenv()

groq = Groq()

def classify_with_llm(log_message):

    prompt = f'''Classify the log message into one of these categories:
    (1) Workflow Error , (2) Deprecation Warning.
    If you can't figure out a category, return "Unknown".
    Only return the category name. No preamble.
    Log_message: {log_message}'''

    chat_completion = groq.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [
            {
                "role" : "user",
                "content" : prompt,
            }
        ])

    return (chat_completion.choices[0].message.content)

if __name__ == "__main__":
    print(classify_with_llm("Hello World"))
    print(classify_with_llm("Task assignment for TeamID 3425 could not complete due to invalid priority level."))
    print(classify_with_llm("User User123 logged in."))
    print(classify_with_llm("The 'ExportToCSV' feature is outdated. Please migrate to 'ExportToXLSX' by the end of Q3."))