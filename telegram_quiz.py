from telegram import Bot
from telegram.error import RetryAfter, BadRequest, TimedOut, NetworkError
import time
import random
import csv
import os

# =========================
# CONFIG
# =========================

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = "@ComputerStructureQuizzesCSUoK"
CSV_FILE = "computer_structure_questions.csv"
BASE_DELAY = 3.0

bot = Bot(token=TOKEN)

# =========================
# SEND QUIZ FUNCTION
# =========================

def send_quiz(question_text, options, correct_index):
    while True:
        try:
            bot.send_poll(
                chat_id=CHAT_ID,
                question=question_text,
                options=options,
                type="quiz",
                correct_option_id=correct_index,
                is_anonymous=True,
                disable_notification=True,
            )
            return

        except RetryAfter as e:
            wait_time = int(getattr(e, "retry_after", 5)) + 1
            time.sleep(wait_time)

        except (TimedOut, NetworkError):
            time.sleep(5)

        except BadRequest as e:
            print("BadRequest:", e)
            raise


# =========================
# LOAD QUESTIONS FROM CSV
# =========================

def load_questions_from_csv(path):
    questions = []

    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        # print("CSV columns:", reader.fieldnames)

        for row in reader:
            # ---------- options ----------
            options = []
            for i in range(1, 5):
                value = row.get(f"option_{i}")
                if value:
                    value = value.strip()
                    if value:
                        options.append(value)

            if len(options) < 2:
                continue  # تجاهل السؤال غير الصالح

            # ---------- correct option ----------
            correct_option_name = (
                row.get("correct_option")
                or row.get("correct")
                or row.get("answer")
            )

            if not correct_option_name:
                continue

            correct_option_name = correct_option_name.strip()

            try:
                correct_index = int(correct_option_name.split("_")[1]) - 1
            except:
                continue

            # ---------- question ----------
            question_text = row.get("question") or row.get("q")
            if not question_text:
                continue

            question_text = question_text.strip()

            questions.append({
                "q": question_text,
                "opts": options,
                "correct": correct_index,
                "topic": row.get("topic", "").strip(),
            })

    return questions


# =========================
# SHUFFLE OPTIONS
# =========================

def shuffle_options(options, correct_index):
    paired = [
        (opt, i == correct_index)
        for i, opt in enumerate(options)
    ]

    random.shuffle(paired)

    shuffled_options = [opt for opt, _ in paired]
    new_correct_index = next(
        i for i, (_, is_correct) in enumerate(paired) if is_correct
    )

    return shuffled_options, new_correct_index


# =========================
# MAIN
# =========================

questions = load_questions_from_csv(CSV_FILE)

print(f"Loaded {len(questions)} questions from CSV")

for idx, q in enumerate(questions, start=1):
    numbered_question = f"{idx}- {q['q']}"

    shuffled_opts, new_correct = shuffle_options(
        q["opts"], q["correct"]
    )

    send_quiz(numbered_question, shuffled_opts, new_correct)

    time.sleep(BASE_DELAY)

print("All questions sent successfully ✅")