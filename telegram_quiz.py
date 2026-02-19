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
CHAT_ID = "@ProgrammingQuizzesCSUOK"
CSV_FILE = "programming_quizzes_with_arabic-gemeni.csv"
BASE_DELAY = 5.0  # Increased delay to prevent Telegram rate limits

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
            return True

        except RetryAfter as e:
            wait_time = int(getattr(e, "retry_after", 5)) + 1
            print(f"Rate limit exceeded. Waiting for {wait_time} seconds...")
            time.sleep(wait_time)

        except (TimedOut, NetworkError) as e:
            print(f"Network error: {e}. Retrying in 5 seconds...")
            time.sleep(5)

        except BadRequest as e:
            print(f"BadRequest (Skipping question): {e}")
            return False
            
        except Exception as e:
            print(f"Unexpected error (Skipping question): {e}")
            return False


# =========================
# LOAD QUESTIONS FROM CSV
# =========================
def load_questions_from_csv(path):
    questions = []
    
    try:
        with open(path, newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)

            for row in reader:
                # ---------- options ----------
                options = []
                for i in range(1, 5):
                    value = row.get(f"option_{i}")
                    if value and value.strip():
                        options.append(value.strip())

                if len(options) < 2:
                    continue  # Skip invalid questions

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
                if not question_text or not question_text.strip():
                    continue

                questions.append({
                    "q": question_text.strip(),
                    "opts": options,
                    "correct": correct_index,
                })
                
    except Exception as e:
        print(f"Error reading CSV: {e}")

    return questions


# =========================
# SHUFFLE OPTIONS
# =========================
def shuffle_options(options, correct_index):
    # Safety check to prevent index out of bounds
    if correct_index >= len(options) or correct_index < 0:
        print("Warning: Correct index out of range! Defaulting to 0.")
        return options, 0

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
def main():
    if not TOKEN:
        print("Error: BOT_TOKEN is missing. Please check your environment variables.")
        return

    questions = load_questions_from_csv(CSV_FILE)
    print(f"Loaded {len(questions)} questions from CSV.")

    if not questions:
        print("No valid questions found to send. Exiting.")
        return

    for idx, q in enumerate(questions, start=1):
        print(f"Sending question {idx}/{len(questions)}...", end=" ")

        shuffled_opts, new_correct = shuffle_options(
            q["opts"], q["correct"]
        )

        # Sending the question without any numbering
        success = send_quiz(q["q"], shuffled_opts, new_correct)

        if success:
            print("[SUCCESS]")
        else:
            print("[FAILED - SKIPPED]")

        time.sleep(BASE_DELAY)

    print("All questions processed successfully.")


if __name__ == "__main__":
    main()