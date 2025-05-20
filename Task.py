import os
import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt_tab")
nltk.download("punkt")
nltk.download("stopwords")


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


def clean_and_tokenize(messages):
    all_text = " ".join(messages).lower()
    all_text = all_text.translate(str.maketrans("", "", string.punctuation))
    words = word_tokenize(all_text)
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words


def get_top_keywords(words, n=5):
    word_counts = Counter(words)
    return word_counts.most_common(n)


def generate_summary(user_messages, ai_messages):
    total_messages = len(user_messages) + len(ai_messages)
    keywords = clean_and_tokenize(user_messages + ai_messages)
    top_keywords = get_top_keywords(keywords)

    print("\n--- Chat Summary ---")
    print(f"Total messages exchanged: {total_messages}")
    print(f"User messages: {len(user_messages)}")
    print(f"AI messages: {len(ai_messages)}")
    print("Most common keywords:", ", ".join([word for word, _ in top_keywords]))

    print("\nSample Summary:")
    print(f"- The conversation had {total_messages} exchanges.")
    print(f"- Most common keywords: {', '.join([word for word, _ in top_keywords])}.")


if __name__ == "__main__":
    file_path = "chat.txt"  # You can modify this to accept from user or command-line
    if os.path.exists(file_path):
        user_msgs, ai_msgs = parse_chat(file_path)
        generate_summary(user_msgs, ai_msgs)
    else:
        print(f"{file_path} not found.")
