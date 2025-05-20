def read_chat_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line in lines:
        print(line.strip())


if __name__ == "__main__":
    file_path = "chat.txt"
    read_chat_file(file_path)
