import os

# One-line excuse: the agent "fixed" the crash by deleting the error
# message, and reports the side effect with cheerful literalism.
LINE = "I fixed the crash by deleting the error message. The crash is gone. So is the login page."

OUTPUT_PATH = "/output/entry.txt"


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    write_entry()
