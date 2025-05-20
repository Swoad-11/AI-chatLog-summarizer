def parse_chat(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    user_messages = []
    ai_messages = []

    for line in lines:
        line = line.strip()
        if line.startswith("User:"):
            user_messages.append(line.replace("User:", "").strip())
        elif line.startswith("AI:"):
            ai_messages.append(line.replace("AI:", "").strip())

    return user_messages, ai_messages


if __name__ == "__main__":
    file_path = "chat.txt"
    user_msgs, ai_msgs = parse_chat(file_path)
    print("User Messages:", user_msgs)
    print("AI Messages:", ai_msgs)
