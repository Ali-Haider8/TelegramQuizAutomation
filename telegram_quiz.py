from telegram import Bot
from telegram.error import RetryAfter, BadRequest, TimedOut, NetworkError
import time

# =========================
# CONFIG
# =========================
TOKEN = "8255957753:AAFnaI7St8vi1DsE5m3Y3POxYsL7GBa3z20"
CHAT_ID = "@MCQCompStructureUOK2" # channel username (must start with @)

bot = Bot(token=TOKEN)

# لتقليل Flood control (جرّب 2.5 إلى 4 ثواني حسب القناة)
BASE_DELAY = 2.8

def send_quiz(q_text, options, correct_index):
    """
    Sends a Telegram Quiz poll (anonymous - required for channels).
    Handles flood control with RetryAfter.
    """
    while True:
        try:
            bot.send_poll(
                chat_id=CHAT_ID,
                question=q_text,
                options=options,
                correct_option_id=correct_index,
                type="quiz",
                # IMPORTANT for channels: keep it anonymous
                is_anonymous=True,
            )
            return

        except RetryAfter as e:
            #The Telegram asked us to slow down
            sleep_for = int(getattr(e, "retry_after", 5)) + 1
            print(f"[RetryAfter] Sleeping {sleep_for}s ...")
            time.sleep(sleep_for)

        except (TimedOut, NetworkError) as e:
            print(f"[Network] {e} -> retry in 5s")
            time.sleep(5)

        except BadRequest as e:
            # Most common reasons:
            # - bot not admin in channel
            # - channel username wrong
            # - question/options too long
            print(f"[BadRequest] {e}")
            raise

# =========================
# QUESTIONS (55)
# English is primary + Arabic short helper
# =========================
questions = [

    # -------------------------
    # EASY (1-10)
    # -------------------------
    {
        "q": "1) CPU stands for?\n(ما معنى CPU؟)",
        "opts": [
            "Central Program Unit (وحدة برنامج مركزية)",
            "Central Processing Unit (وحدة المعالجة المركزية)",
            "Computer Processing Utility (أداة معالجة)",
            "Control Processing Unit (وحدة تحكم ومعالجة)"
        ],
        "correct": 1
    },
    {
        "q": "2) ALU is responsible for:\n(ALU مسؤولة عن؟)",
        "opts": [
            "Storing files (خزن الملفات)",
            "Arithmetic & logic operations (عمليات حسابية ومنطقية)",
            "Displaying output (عرض النتائج)",
            "Connecting network (ربط الشبكة)"
        ],
        "correct": 1
    },
    {
        "q": "3) RAM is:\n(RAM هي؟)",
        "opts": [
            "Non-volatile memory (لا تفقد البيانات)",
            "Volatile memory (تفقد البيانات بانقطاع الكهرباء)",
            "Secondary storage (خزن ثانوي)",
            "Input device (جهاز إدخال)"
        ],
        "correct": 1
    },
    {
        "q": "4) ROM is typically:\n(ROM عادةً تكون؟)",
        "opts": [
            "Volatile (متطايرة)",
            "Non-volatile (غير متطايرة)",
            "A bus (ناقل بيانات)",
            "An output device (إخراج)"
        ],
        "correct": 1
    },
    {
        "q": "5) Which is an input device?\n(أي جهاز إدخال؟)",
        "opts": [
            "Monitor (شاشة)",
            "Printer (طابعة)",
            "Keyboard (لوحة مفاتيح)",
            "Speaker (سماعة)"
        ],
        "correct": 2
    },
    {
        "q": "6) Which is an output device?\n(أي جهاز إخراج؟)",
        "opts": [
            "Mouse (فأرة)",
            "Scanner (ماسح ضوئي)",
            "Monitor (شاشة)",
            "Microphone (مايك)"
        ],
        "correct": 2
    },
    {
        "q": "7) Cache memory is usually:\n(الـ Cache عادةً تكون؟)",
        "opts": [
            "Slower than RAM (أبطأ من RAM)",
            "Faster than RAM (أسرع من RAM)",
            "Same as HDD (مثل القرص)",
            "Outside CPU only (خارج المعالج فقط)"
        ],
        "correct": 1
    },
    {
        "q": "8) 1 Byte equals:\n(1 بايت يساوي؟)",
        "opts": [
            "4 bits (4 بت)",
            "8 bits (8 بت)",
            "16 bits (16 بت)",
            "32 bits (32 بت)"
        ],
        "correct": 1
    },
    {
        "q": "9) Hard disk is:\n(القرص الصلب هو؟)",
        "opts": [
            "Primary memory (ذاكرة أولية)",
            "Secondary storage (خزن ثانوي)",
            "Register (مسجل)",
            "ALU (وحدة حساب)"
        ],
        "correct": 1
    },
    {
        "q": "10) Bus is best described as:\n(الـ Bus هو؟)",
        "opts": [
            "A storage unit (وحدة خزن)",
            "A data transfer path (مسار نقل بيانات)",
            "A program (برنامج)",
            "A monitor part (جزء من الشاشة)"
        ],
        "correct": 1
    },

    # -------------------------
    # EASY+ (11-20)
    # -------------------------
    {
        "q": "11) Data bus carries:\n(ناقل البيانات ينقل؟)",
        "opts": [
            "Addresses (عناوين)",
            "Control signals (إشارات تحكم)",
            "Actual data (البيانات نفسها)",
            "Power (طاقة)"
        ],
        "correct": 2
    },
    {
        "q": "12) Address bus carries:\n(ناقل العناوين ينقل؟)",
        "opts": [
            "Data (بيانات)",
            "Addresses (عناوين)",
            "Sound (صوت)",
            "Images (صور)"
        ],
        "correct": 1
    },
    {
        "q": "13) Control Unit (CU) mainly:\n(CU وظيفتها الأساسية؟)",
        "opts": [
            "Performs arithmetic (تنفذ الحساب)",
            "Controls execution (تتحكم بتنفيذ التعليمات)",
            "Stores permanent data (تخزن دائمًا)",
            "Prints documents (تطبع)"
        ],
        "correct": 1
    },
    {
        "q": "14) Register is:\n(المسجل Register هو؟)",
        "opts": [
            "Very fast small storage (خزن صغير سريع جدًا)",
            "Slow storage (خزن بطيء)",
            "Disk storage (خزن قرص)",
            "Network device (جهاز شبكة)"
        ],
        "correct": 0
    },
    {
        "q": "15) Smallest CPU storage is:\n(أصغر خزن داخل CPU؟)",
        "opts": [
            "RAM",
            "Cache",
            "Register",
            "Hard disk"
        ],
        "correct": 2
    },
    {
        "q": "16) BIOS is stored in:\n(يُخزن BIOS في؟)",
        "opts": [
            "RAM",
            "ROM / Flash ROM (ذاكرة دائمة)",
            "Cache",
            "Register"
        ],
        "correct": 1
    },
    {
        "q": "17) Touchscreen is:\n(شاشة اللمس هي؟)",
        "opts": [
            "Input only (إدخال فقط)",
            "Output only (إخراج فقط)",
            "Input & Output (إدخال وإخراج)",
            "Storage (خزن)"
        ],
        "correct": 2
    },
    {
        "q": "18) Which is NOT hardware?\n(أي ليس عتادًا؟)",
        "opts": [
            "Keyboard (لوحة مفاتيح)",
            "Monitor (شاشة)",
            "Operating System (نظام التشغيل)",
            "CPU (المعالج)"
        ],
        "correct": 2
    },
    {
        "q": "19) Volatile memory means:\n(ذاكرة متطايرة تعني؟)",
        "opts": [
            "Keeps data without power (تحتفظ بدون كهرباء)",
            "Loses data when power off (تفقد البيانات عند انقطاع الكهرباء)",
            "Always on disk (دائمًا على القرص)",
            "Only for images (للصور فقط)"
        ],
        "correct": 1
    },
    {
        "q": "20) CPU clock speed is measured in:\n(تقاس سرعة المعالج بـ؟)",
        "opts": [
            "Bytes (بايت)",
            "Hertz (Hz) (هرتز)",
            "Volts (فولت)",
            "Inches (إنش)"
        ],
        "correct": 1
    },

    # -------------------------
    # MEDIUM (21-30)
    # Includes True/False + conversions
    # -------------------------
    {
        "q": "21) Program Counter (PC) holds:\n(PC يخزن؟)",
        "opts": [
            "The current instruction text (نص التعليمة الحالية)",
            "Address of next instruction (عنوان التعليمة القادمة)",
            "Permanent OS files (ملفات النظام الدائمة)",
            "Input data only (بيانات إدخال فقط)"
        ],
        "correct": 1
    },
    {
        "q": "22) Instruction Register (IR) stores:\n(IR يخزن؟)",
        "opts": [
            "Address bus signals (إشارات ناقل العناوين)",
            "The instruction being executed (التعليمة الحالية)",
            "Hard disk sectors (قطاعات القرص)",
            "Printer commands (أوامر الطابعة)"
        ],
        "correct": 1
    },
    {
        "q": "23) Fetch-Decode-Execute cycle starts with:\n(دورة التعليمة تبدأ بـ؟)",
        "opts": [
            "Execute (تنفيذ)",
            "Fetch (جلب)",
            "Store (خزن)",
            "Print (طباعة)"
        ],
        "correct": 1
    },
    {
        "q": "24) True/False: A bit is the smallest unit of data.\n(صح/خطأ: البِت أصغر وحدة بيانات)",
        "opts": [
            "True (صح)",
            "False (خطأ)"
        ],
        "correct": 0
    },
    {
        "q": "25) True/False: Pascal built the first computer that performs all basic operations.\n(صح/خطأ: باسكال صنع أول حاسوب ينفذ كل العمليات الأساسية)",
        "opts": [
            "True (صح)",
            "False (خطأ)"
        ],
        "correct": 1
    },
    {
        "q": "26) 1 KB equals (binary):\n(1 كيلوبايت يساوي - بالنظام الثنائي؟)",
        "opts": [
            "1000 bytes (1000 بايت)",
            "1024 bytes (1024 بايت)",
            "1024 bits (1024 بت)",
            "100 bytes (100 بايت)"
        ],
        "correct": 1
    },
    {
        "q": "27) 1 MB equals:\n(1 ميغابايت يساوي؟)",
        "opts": [
            "1024 KB (1024 كيلوبايت)",
            "1000 KB (1000 كيلوبايت)",
            "1024 bytes (1024 بايت)",
            "8 Mb (8 ميغابت)"
        ],
        "correct": 0
    },
    {
        "q": "28) 1 GB equals:\n(1 غيغابايت يساوي؟)",
        "opts": [
            "1024 MB (1024 ميغابايت)",
            "1000 MB (1000 ميغابايت)",
            "1024 KB (1024 كيلوبايت)",
            "8 Gb (8 غيغابت)"
        ],
        "correct": 0
    },
    {
        "q": "29) 1 TB equals:\n(1 تيرابايت يساوي؟)",
        "opts": [
            "1024 GB (1024 غيغابايت)",
            "1024 MB (1024 ميغابايت)",
            "1000 GB فقط (1000 GB only)",
            "1024 KB (1024 كيلوبايت)"
        ],
        "correct": 0
    },
    {
        "q": "30) Convert: 1.5 MB to bits (binary MB).\n(حوّل: 1.5 ميغابايت إلى بِت)",
        "opts": [
            "12,582,912 bits تقريبًا",
            "1,572,864 bits تقريبًا",
            "1,500,000 bits تقريبًا",
            "125,829,120 bits تقريبًا"
        ],
        "correct": 0
    },

    # -------------------------
    # HARD (31-40)
    # More conceptual / tricky conversions / architecture
    # -------------------------
    {
        "q": "31) If address bus is 16-bit, maximum addressable locations =\n(إذا ناقل العناوين 16-بت، عدد العناوين؟)",
        "opts": [
            "2^8 = 256",
            "2^16 = 65,536",
            "16^2 = 256",
            "2^32"
        ],
        "correct": 1
    },
    {
        "q": "32) If a system uses 32-bit addresses, it can address up to:\n(عناوين 32-بت تعني إمكانية عنونة حتى؟)",
        "opts": [
            "2^16 bytes",
            "2^32 bytes (≈ 4 GB)",
            "2^8 bytes",
            "32 GB exactly"
        ],
        "correct": 1
    },
    {
        "q": "33) Which is typically fastest to slowest?\n(الترتيب من الأسرع للأبطأ؟)",
        "opts": [
            "HDD > RAM > Cache > Registers",
            "Registers > Cache > RAM > HDD",
            "RAM > Registers > HDD > Cache",
            "Cache > HDD > RAM > Registers"
        ],
        "correct": 1
    },
    {
        "q": "34) True/False: Mainframe computers were historically used for large-scale processing.\n(صح/خطأ: المينفريم استُخدم للأعمال الضخمة ومعالجة كبيرة)",
        "opts": ["True (صح)", "False (خطأ)"],
        "correct": 0
    },
    {
        "q": "35) True/False: Mainframes are often called minicomputers.\n(صح/خطأ: المينفريم تُسمى ميني كمبيوتر)",
        "opts": ["True (صح)", "False (خطأ)"],
        "correct": 1
    },
    {
        "q": "36) Convert: 512 KB to bytes.\n(حوّل: 512 كيلوبايت إلى بايت)",
        "opts": [
            "512,000 bytes",
            "524,288 bytes",
            "4,096 bytes",
            "4,194,304 bytes"
        ],
        "correct": 1
    },
    {
        "q": "37) Convert: 2 GB to bytes (binary).\n(حوّل: 2 غيغابايت إلى بايت)",
        "opts": [
            "2,000,000,000 bytes",
            "2,147,483,648 bytes",
            "2,097,152 bytes",
            "17,179,869,184 bytes"
        ],
        "correct": 1
    },
    {
        "q": "38) Which register is most related to sequencing instructions?\n(أي مسجل مرتبط بتسلسل التعليمات؟)",
        "opts": [
            "PC (عداد البرنامج)",
            "MAR (مسجل عنوان الذاكرة)",
            "MDR (مسجل بيانات الذاكرة)",
            "ACC (المجمّع)"
        ],
        "correct": 0
    },
    {
        "q": "39) During FETCH, the CPU primarily uses:\n(أثناء الجلب Fetch يُستخدم غالبًا؟)",
        "opts": [
            "PC + MAR (عداد البرنامج + عنوان الذاكرة)",
            "ALU فقط",
            "Hard disk فقط",
            "Printer buffer"
        ],
        "correct": 0
    },
    {
        "q": "40) Which is correct about CU?\n(أي عبارة صحيحة عن وحدة التحكم؟)",
        "opts": [
            "Does arithmetic only (حساب فقط)",
            "Generates control signals (تولد إشارات التحكم)",
            "Stores files permanently (تخزن ملفات دائمًا)",
            "Acts as monitor (تعمل كشاشة)"
        ],
        "correct": 1
    },

    # -------------------------
    # BONUS / COVERAGE (41-55)
    # mix of topics: history, types, number systems, etc.
    # -------------------------
    {
        "q": "41) Babbage's Analytical Engine was:\n(آلة بابيج التحليلية كانت؟)",
        "opts": [
            "A modern electronic CPU (معالج إلكتروني حديث)",
            "A mechanical programmable concept (فكرة ميكانيكية قابلة للبرمجة)",
            "A GPU (معالج رسومي)",
            "An operating system (نظام تشغيل)"
        ],
        "correct": 1
    },
    {
        "q": "42) True/False: Babbage’s Analytical Engine was fully completed and widely used.\n(صح/خطأ: آلة بابيج اكتملت واستخدمت على نطاق واسع)",
        "opts": ["True (صح)", "False (خطأ)"],
        "correct": 1
    },
    {
        "q": "43) The decimal system uses digits:\n(النظام العشري يستخدم الأرقام؟)",
        "opts": [
            "0-7",
            "0-9",
            "0-1",
            "1-16"
        ],
        "correct": 1
    },
    {
        "q": "44) The binary system uses digits:\n(النظام الثنائي يستخدم؟)",
        "opts": [
            "0 and 1 (0 و 1)",
            "0 to 9",
            "0 to 7",
            "1 to 16"
        ],
        "correct": 0
    },
    {
        "q": "45) Convert: (1010)₂ to decimal.\n(حوّل: 1010 ثنائي إلى عشري)",
        "opts": [
            "8",
            "9",
            "10",
            "12"
        ],
        "correct": 2
    },
    {
        "q": "46) Convert: (15)₁₀ to binary.\n(حوّل: 15 عشري إلى ثنائي)",
        "opts": [
            "1111",
            "1011",
            "1100",
            "1001"
        ],
        "correct": 0
    },
    {
        "q": "47) Convert: (1A)₁₆ to decimal.\n(حوّل: 1A ست عشري إلى عشري)",
        "opts": [
            "16",
            "26",
            "20",
            "18"
        ],
        "correct": 1
    },
    {
        "q": "48) True/False: Hexadecimal digits include A-F.\n(صح/خطأ: النظام الست عشري يشمل A-F)",
        "opts": ["True (صح)", "False (خطأ)"],
        "correct": 0
    },
    {
        "q": "49) Which memory is closest to CPU core speed?\n(أي ذاكرة أقرب لسرعة نواة المعالج؟)",
        "opts": [
            "Registers (المسجلات)",
            "Hard disk (قرص صلب)",
            "Optical disk (قرص ضوئي)",
            "USB flash always (فلاش دائمًا)"
        ],
        "correct": 0
    },
    {
        "q": "50) Which one is primary memory?\n(أي ذاكرة أولية؟)",
        "opts": [
            "RAM (رام)",
            "Hard disk (قرص صلب)",
            "DVD (دي في دي)",
            "Cloud only (سحابة فقط)"
        ],
        "correct": 0
    },
    {
        "q": "51) Convert: 4096 bytes to KB.\n(حوّل: 4096 بايت إلى كيلوبايت)",
        "opts": [
            "2 KB",
            "4 KB",
            "8 KB",
            "16 KB"
        ],
        "correct": 1
    },
    {
        "q": "52) Convert: 3 KB to bits.\n(حوّل: 3 كيلوبايت إلى بِت)",
        "opts": [
            "24,576 bits",
            "3,072 bits",
            "2,048 bits",
            "196,608 bits"
        ],
        "correct": 0
    },
    {
        "q": "53) True/False: OS is software, not hardware.\n(صح/خطأ: نظام التشغيل برنامج وليس عتاد)",
        "opts": ["True (صح)", "False (خطأ)"],
        "correct": 0
    },
    {
        "q": "54) A computer can be defined as:\n(تعريف الحاسوب الأفضل؟)",
        "opts": [
            "Device that only stores data (يخزن فقط)",
            "Electronic device that accepts input, processes, and outputs info (إدخال/معالجة/إخراج)",
            "Machine that prints only (يطبع فقط)",
            "Device without memory (بدون ذاكرة)"
        ],
        "correct": 1
    },
    {
        "q": "55) True/False: Data and information are the same thing.\n(صح/خطأ: البيانات والمعلومات نفس الشيء)",
        "opts": ["True (صح)", "False (خطأ)"],
        "correct": 1
    },
]

# =========================
# SEND ALL
# =========================
print(f"Sending {len(questions)} quiz polls...")

for item in questions:
    send_quiz(item["q"], item["opts"], item["correct"])
    time.sleep(BASE_DELAY)

print("Done ✅")