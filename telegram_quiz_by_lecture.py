import csv
import time
import json
import os
from telegram import Bot
from telegram.error import RetryAfter, BadRequest, NetworkError

# ================== CONFIG ==================
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = "@EnglishQuizzesCSUoK"
CSV_FILE = "english_exam_sections_FINAL.csv"
PROGRESS_FILE = "progress.json"

BASE_DELAY = 2.5
LECTURE_DELAY = 6.0
COOLDOWN_AFTER_LECTURE = 10
# ============================================

bot = Bot(token=BOT_TOKEN)


# ---------- Progress ----------
def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"lecture": None, "question": 0}


def save_progress(lecture, question):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump({"lecture": lecture, "question": question}, f)


# ---------- CSV ----------
def load_questions_grouped_by_lecture(csv_path):
    lectures = {}

    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for row in reader:
            lec_num = (row.get("lecture_number") or "").strip()
            lec_name = (row.get("lecture_name") or "").strip()

            if not lec_num:
                continue

            if lec_num not in lectures:
                lectures[lec_num] = {"name": lec_name, "questions": []}

            question = (row.get("question") or "").strip()
            if not question:
                continue

            options = []
            for i in range(1, 5):
                opt = row.get(f"option_{i}")
                if opt and opt.strip():
                    options.append(opt.strip())

            if len(options) < 2:
                continue

            correct_raw = row.get("correct_option", "option_1")
            try:
                correct_index = int(correct_raw.split("_")[1]) - 1
            except:
                correct_index = 0

            lectures[lec_num]["questions"].append(
                {"q": question, "opts": options, "correct": correct_index}
            )

    return lectures


# ---------- Utils ----------
def shuffle_options(options, correct_index):
    import random

    indexed = list(enumerate(options))
    random.shuffle(indexed)

    new_correct = next(i for i, (idx, _) in enumerate(indexed) if idx == correct_index)
    return [opt for _, opt in indexed], new_correct


# ---------- Safe Send ----------
def safe_send_message(text):
    while True:
        try:
            bot.send_message(chat_id=CHAT_ID, text=text)
            return
        except RetryAfter as e:
            wait = int(e.retry_after) + 2
            print(f"Flood (message). Waiting {wait}s...")
            time.sleep(wait)


def send_quiz(question_text, options, correct_index):
    while True:
        try:
            bot.send_poll(
                chat_id=CHAT_ID,
                question=question_text[:300],
                options=options,
                type="quiz",
                correct_option_id=correct_index,
                is_anonymous=True,
                disable_notification=True,
            )
            return
        except RetryAfter as e:
            wait = int(e.retry_after) + 2
            print(f"Flood (quiz). Waiting {wait}s...")
            time.sleep(wait)
        except NetworkError:
            time.sleep(5)
        except BadRequest as e:
            print("BadRequest:", e)
            return


# ---------- Main ----------
def main():
    lectures = load_questions_grouped_by_lecture(CSV_FILE)
    progress = load_progress()

    total = sum(len(v["questions"]) for v in lectures.values())
    print(f"Loaded {total} questions from CSV")

    start_lecture = progress["lecture"]
    start_question = progress["question"]

    for lec_num in sorted(lectures, key=int):
        if start_lecture and int(lec_num) < int(start_lecture):
            continue

        lec_name = lectures[lec_num]["name"]

        safe_send_message(f"✏️ Grammar Quiz – Section {lec_num}\n" f"{lec_name}")
        time.sleep(LECTURE_DELAY)

        questions = lectures[lec_num]["questions"]

        for idx, q in enumerate(questions, start=1):
            if start_lecture == lec_num and idx <= start_question:
                continue

            save_progress(lec_num, idx)

            numbered_question = f"{idx}) {q['q']}"
            shuffled_opts, new_correct = shuffle_options(q["opts"], q["correct"])
            send_quiz(numbered_question, shuffled_opts, new_correct)

            time.sleep(BASE_DELAY)

        save_progress(lec_num, 0)
        print("Lecture sent. Cooling down...")
        time.sleep(COOLDOWN_AFTER_LECTURE)

    if os.path.exists(PROGRESS_FILE):
        os.remove(PROGRESS_FILE)

    print("All lectures sent successfully ✅")


if __name__ == "__main__":
    main()
