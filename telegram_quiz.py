from telegram import Bot
from telegram.error import RetryAfter, BadRequest, TimedOut, NetworkError
import time

# =========================
# CONFIG
# =========================

TOKEN = ""
CHAT_ID = "@EnglishQuizzesCS"

BASE_DELAY = 3.0


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
                is_anonymous=True
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
# QUESTIONS (55)
# English is primary + Arabic short helper
# =========================
questions = [

     {
        "q": "I ___ a headache this morning, but now I feel better.",
        "opts": ["had", "have", "am"],
        "correct": 0
    },
    {
        "q": "She ___ a very intelligent student.",
        "opts": ["is", "are", "has"],
        "correct": 0
    },
    {
        "q": "They ___ a big party last weekend.",
        "opts": ["had", "have", "were"],
        "correct": 0
    },
    {
        "q": "We ___ so happy to see you yesterday!",
        "opts": ["were", "are", "had"],
        "correct": 0
    },
    {
        "q": "He ___ three siblings who live in Canada.",
        "opts": ["has", "have", "is"],
        "correct": 0
    },
    {
        "q": "You ___ in the library when I called you.",
        "opts": ["were", "are", "had"],
        "correct": 0
    },
    {
        "q": "The house ___ a beautiful garden in the backyard.",
        "opts": ["has", "had", "is"],
        "correct": 0
    },
    {
        "q": "I ___ not sure if they will come tonight.",
        "opts": ["am", "is", "have"],
        "correct": 0
    },
    {
        "q": "She ___ an important meeting tomorrow morning.",
        "opts": ["has", "had", "is"],
        "correct": 0
    },
    {
        "q": "They ___ very friendly and helpful neighbors.",
        "opts": ["are", "is", "have"],
        "correct": 0
    },
    {
        "q": "He usually ___ economics, but this semester he is working in administration.",
        "opts": ["teaches", "is teaching"],
        "correct": 0
    },
    {
        "q": "I ___ the explanation is clear enough.",
        "opts": ["don't think", "am not thinking"],
        "correct": 0
    },
    {
        "q": "At this time last week, we ___ the final project.",
        "opts": ["discussed", "were discussing"],
        "correct": 1
    },
    {
        "q": "She ___ the mistake until the results were published.",
        "opts": ["didn't notice", "wasn't noticing"],
        "correct": 0
    },
    {
        "q": "While the manager ___, everyone listened carefully.",
        "opts": ["was talking", "talked"],
        "correct": 0
    },
    {
        "q": "More students ___ online courses these days.",
        "opts": ["are preferring", "prefer"],
        "correct": 1
    },
    {
        "q": "What ___ when the system suddenly crashed?",
        "opts": ["did you do", "were you doing"],
        "correct": 1
    },
    {
        "q": "He ___ at a university for five years before he changed jobs.",
        "opts": ["worked", "was working"],
        "correct": 0
    },
    {
        "q": "I ___ an old friend while I was shopping.",
        "opts": ["met", "was meeting"],
        "correct": 0
    },
    {
        "q": "When I entered the office, they ___ about the budget.",
        "opts": ["argued", "were arguing"],
        "correct": 1
    },
        # =========================
    # SECTION C: Past Simple vs Past Continuous (PDF)
    # =========================

    {
        "q": "I ___ TV when the electricity went out.",
        "opts": ["was watching", "watched"],
        "correct": 0
    },
    {
        "q": "While she ___ dinner, the phone rang.",
        "opts": ["was cooking", "cooked"],
        "correct": 0
    },
    {
        "q": "They ___ football when it started to rain.",
        "opts": ["were playing", "played"],
        "correct": 0
    },
    {
        "q": "He ___ his keys while he was walking to the office.",
        "opts": ["lost", "was losing"],
        "correct": 0
    },
    {
        "q": "We ___ about the problem when the teacher arrived.",
        "opts": ["were talking", "talked"],
        "correct": 0
    },
    {
        "q": "What ___ when I called you last night?",
        "opts": ["were you doing", "did you do"],
        "correct": 0
    },
    {
        "q": "She ___ a book when she heard a strange noise.",
        "opts": ["was reading", "read"],
        "correct": 0
    },
    {
        "q": "While the students ___ the exam, the fire alarm rang.",
        "opts": ["were taking", "took"],
        "correct": 0
    },
    {
        "q": "I ___ asleep while I was listening to the lecture.",
        "opts": ["fell", "was falling"],
        "correct": 0
    },
    {
        "q": "They ___ in the park when they saw the accident.",
        "opts": ["were walking", "walked"],
        "correct": 0
    },
        # =========================
    # SECTION D: Mixed Grammar Revision (PDF)
    # =========================

    {
        "q": "She usually ___ to university by bus, but today she walked.",
        "opts": ["goes", "is going"],
        "correct": 0
    },
    {
        "q": "We ___ the report yesterday, so it is ready now.",
        "opts": ["finished", "were finishing"],
        "correct": 0
    },
    {
        "q": "I ___ him before, but I don't remember his name.",
        "opts": ["have met", "met"],
        "correct": 0
    },
    {
        "q": "While I ___ for the exam, my friends were watching TV.",
        "opts": ["was studying", "studied"],
        "correct": 0
    },
    {
        "q": "They ___ live near the campus, so they rent an apartment.",
        "opts": ["don't", "aren't"],
        "correct": 0
    },
    {
        "q": "He ___ very tired last night after the long trip.",
        "opts": ["was", "is"],
        "correct": 0
    },
    {
        "q": "She ___ her homework yet, so she cannot go out.",
        "opts": ["hasn't finished", "didn't finish"],
        "correct": 0
    },
    {
        "q": "When the teacher entered the class, the students ___ quietly.",
        "opts": ["were sitting", "sat"],
        "correct": 0
    },
    {
        "q": "I ___ English for three years before I joined the university.",
        "opts": ["had studied", "was studying"],
        "correct": 0
    },
    {
        "q": "He ___ speak French, but he understands it well.",
        "opts": ["can't", "isn't"],
        "correct": 0
    },

]


# =========================
# SEND ALL QUESTIONS
# =========================
print(f"Sending {len(questions)} questions...")

for idx, q in enumerate(questions, start=1):
    numbered_question = f"{idx}- {q['q']}"

    send_quiz(
        numbered_question,
        q["opts"],
        q["correct"]
    )
    time.sleep(BASE_DELAY)

print("All questions sent successfully ✅")