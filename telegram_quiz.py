from telegram import Bot
import time

TOKEN = "8255957753:AAFnaI7St8vi1DsE5m3Y3POxYsL7GBa3z20"
CHAT_ID = "@MCQCompStructureUOK"

bot = Bot(token=TOKEN)
questions = [

    # 1
    {
        "q": "CPU stands for?\n(ما معنى CPU؟)",
        "opts": [
            "Central Program Unit – وحدة برنامج مركزية",
            "Central Processing Unit – وحدة المعالجة المركزية",
            "Computer Unit – وحدة الحاسوب",
            "Control Unit – وحدة التحكم"
        ],
        "correct": 1
    },

    # 2
    {
        "q": "What is the main function of CPU?\n(ما الوظيفة الرئيسية للمعالج؟)",
        "opts": [
            "Store data – تخزين البيانات",
            "Process data – معالجة البيانات",
            "Display output – عرض النتائج",
            "Input data – إدخال البيانات"
        ],
        "correct": 1
    },

    # 3
    {
        "q": "Which unit performs arithmetic and logic operations?\n(أي وحدة تنفذ العمليات الحسابية والمنطقية؟)",
        "opts": [
            "CU – وحدة التحكم",
            "ALU – وحدة الحساب والمنطق",
            "RAM – الذاكرة",
            "Register – المسجل"
        ],
        "correct": 1
    },

    # 4
    {
        "q": "Which part controls CPU operations?\n(أي جزء يتحكم بعمل المعالج؟)",
        "opts": [
            "ALU – الحساب والمنطق",
            "RAM – الذاكرة",
            "CU – وحدة التحكم",
            "Cache – الذاكرة المخبأة"
        ],
        "correct": 2
    },

    # 5
    {
        "q": "What does RAM stand for?\n(ما معنى RAM؟)",
        "opts": [
            "Read Access Memory – ذاكرة قراءة",
            "Random Access Memory – ذاكرة وصول عشوائي",
            "Rapid Access Memory – ذاكرة سريعة",
            "Run Access Memory – ذاكرة تشغيل"
        ],
        "correct": 1
    },

    # 6
    {
        "q": "RAM is a:\n(ذاكرة RAM هي؟)",
        "opts": [
            "Permanent memory – دائمة",
            "Temporary memory – مؤقتة",
            "Secondary storage – ثانوية",
            "Input device – جهاز إدخال"
        ],
        "correct": 1
    },

    # 7
    {
        "q": "Which memory is non-volatile?\n(أي ذاكرة لا تفقد البيانات بانقطاع الكهرباء؟)",
        "opts": [
            "RAM – ذاكرة مؤقتة",
            "Cache – مخبأة",
            "ROM – ذاكرة دائمة",
            "Register – مسجل"
        ],
        "correct": 2
    },

    # 8
    {
        "q": "ROM is used to store:\n(تُستخدم ROM لخزن؟)",
        "opts": [
            "User files – ملفات المستخدم",
            "Operating system – النظام",
            "Boot instructions – تعليمات الإقلاع",
            "Temporary data – بيانات مؤقتة"
        ],
        "correct": 2
    },

    # 9
    {
        "q": "Cache memory is:\n(الذاكرة المخبأة هي؟)",
        "opts": [
            "Slower than RAM – أبطأ من RAM",
            "Faster than RAM – أسرع من RAM",
            "Same speed as HDD – مثل القرص",
            "External memory – خارجية"
        ],
        "correct": 1
    },

    # 10
    {
        "q": "Cache memory is located:\n(أين توجد Cache؟)",
        "opts": [
            "Inside CPU – داخل المعالج",
            "Inside hard disk – داخل القرص",
            "Inside keyboard – داخل لوحة المفاتيح",
            "Inside monitor – داخل الشاشة"
        ],
        "correct": 0
    },

    # 11
    {
        "q": "Which is an input device?\n(أي مما يلي جهاز إدخال؟)",
        "opts": [
            "Monitor – شاشة",
            "Printer – طابعة",
            "Keyboard – لوحة مفاتيح",
            "Speaker – سماعة"
        ],
        "correct": 2
    },

    # 12
    {
        "q": "Which is an output device?\n(أي مما يلي جهاز إخراج؟)",
        "opts": [
            "Mouse – فأرة",
            "Scanner – ماسح",
            "Monitor – شاشة",
            "Keyboard – لوحة مفاتيح"
        ],
        "correct": 2
    },

    # 13
    {
        "q": "Which device is both input and output?\n(أي جهاز إدخال وإخراج معًا؟)",
        "opts": [
            "Keyboard – لوحة مفاتيح",
            "Monitor – شاشة",
            "Touch screen – شاشة لمس",
            "Printer – طابعة"
        ],
        "correct": 2
    },

    # 14
    {
        "q": "Hard disk is:\n(القرص الصلب هو؟)",
        "opts": [
            "Primary memory – ذاكرة أولية",
            "Temporary memory – مؤقتة",
            "Secondary storage – خزن ثانوي",
            "Register – مسجل"
        ],
        "correct": 2
    },

    # 15
    {
        "q": "Which stores data permanently?\n(أي يخزن البيانات بشكل دائم؟)",
        "opts": [
            "RAM – ذاكرة مؤقتة",
            "Cache – مخبأة",
            "Hard disk – قرص صلب",
            "Register – مسجل"
        ],
        "correct": 2
    },

    # 16
    {
        "q": "Registers are:\n(المسجلات هي؟)",
        "opts": [
            "Very fast memory – ذاكرة فائقة السرعة",
            "Slow memory – بطيئة",
            "External memory – خارجية",
            "Secondary storage – ثانوية"
        ],
        "correct": 0
    },

    # 17
    {
        "q": "Registers are located:\n(أين توجد المسجلات؟)",
        "opts": [
            "Inside CPU – داخل المعالج",
            "Inside RAM – داخل RAM",
            "Inside hard disk – داخل القرص",
            "Outside computer – خارج الحاسوب"
        ],
        "correct": 0
    },

    # 18
    {
        "q": "Which is the smallest memory?\n(أصغر نوع ذاكرة؟)",
        "opts": [
            "RAM",
            "Cache",
            "Register",
            "Hard disk"
        ],
        "correct": 2
    },

    # 19
    {
        "q": "Main memory refers to:\n(الذاكرة الرئيسية هي؟)",
        "opts": [
            "Cache",
            "RAM",
            "Hard disk",
            "Flash memory"
        ],
        "correct": 1
    },

    # 20
    {
        "q": "What is a bus?\n(ما هو الـ Bus؟)",
        "opts": [
            "Storage unit – وحدة خزن",
            "Data transfer path – مسار نقل بيانات",
            "Input device – جهاز إدخال",
            "Output device – جهاز إخراج"
        ],
        "correct": 1
    },

    # 21
    {
        "q": "Data bus carries:\n(ناقل البيانات ينقل؟)",
        "opts": [
            "Addresses – العناوين",
            "Control signals – إشارات تحكم",
            "Actual data – البيانات",
            "Instructions only – تعليمات فقط"
        ],
        "correct": 2
    },

    # 22
    {
        "q": "Address bus carries:\n(ناقل العناوين ينقل؟)",
        "opts": [
            "Data – بيانات",
            "Addresses – عناوين",
            "Signals – إشارات",
            "Instructions – تعليمات"
        ],
        "correct": 1
    },

    # 23
    {
        "q": "Control bus carries:\n(ناقل التحكم ينقل؟)",
        "opts": [
            "Data – بيانات",
            "Addresses – عناوين",
            "Control signals – إشارات تحكم",
            "Files – ملفات"
        ],
        "correct": 2
    },

    # 24
    {
        "q": "Which is NOT hardware?\n(أي مما يلي ليس عتادًا؟)",
        "opts": [
            "Keyboard",
            "Monitor",
            "Operating System",
            "CPU"
        ],
        "correct": 2
    },

    # 25
    {
        "q": "Operating System is:\n(نظام التشغيل هو؟)",
        "opts": [
            "Hardware – عتاد",
            "Software – برنامج",
            "Input device – إدخال",
            "Output device – إخراج"
        ],
        "correct": 1
    },

    # 26
    {
        "q": "Which starts the computer?\n(ما الذي يبدأ تشغيل الحاسوب؟)",
        "opts": [
            "RAM",
            "ROM",
            "BIOS – برنامج الإقلاع",
            "CPU"
        ],
        "correct": 2
    },

    # 27
    {
        "q": "BIOS is stored in:\n(أين يُخزن BIOS؟)",
        "opts": [
            "RAM",
            "ROM",
            "Cache",
            "Hard disk"
        ],
        "correct": 1
    },

    # 28
    {
        "q": "Which memory is fastest?\n(أسرع ذاكرة؟)",
        "opts": [
            "Hard disk",
            "RAM",
            "Cache",
            "Register"
        ],
        "correct": 3
    },

    # 29
    {
        "q": "Which is volatile memory?\n(أي ذاكرة متطايرة؟)",
        "opts": [
            "ROM",
            "Hard disk",
            "RAM",
            "Flash"
        ],
        "correct": 2
    },

    # 30
    {
        "q": "Flash memory is:\n(ذاكرة الفلاش هي؟)",
        "opts": [
            "Volatile – متطايرة",
            "Non-volatile – غير متطايرة",
            "Primary memory – أولية",
            "Register – مسجل"
        ],
        "correct": 1
    },

    # 31
    {
        "q": "Which is secondary storage?\n(أي خزن ثانوي؟)",
        "opts": [
            "RAM",
            "Cache",
            "Hard disk",
            "Register"
        ],
        "correct": 2
    },

    # 32
    {
        "q": "CPU speed is measured in:\n(تقاس سرعة المعالج بـ؟)",
        "opts": [
            "Bytes",
            "Hertz (Hz)",
            "Volts",
            "Bits"
        ],
        "correct": 1
    },

    # 33
    {
        "q": "1 Byte equals:\n(البايت يساوي؟)",
        "opts": [
            "4 bits",
            "8 bits",
            "16 bits",
            "32 bits"
        ],
        "correct": 1
    },

    # 34
    {
        "q": "Which unit fetches instructions?\n(أي وحدة تجلب التعليمات؟)",
        "opts": [
            "ALU",
            "CU",
            "RAM",
            "Register"
        ],
        "correct": 1
    },

    # 35
    {
        "q": "Instruction cycle starts with:\n(دورة التعليمة تبدأ بـ؟)",
        "opts": [
            "Execute – تنفيذ",
            "Fetch – جلب",
            "Decode – فك",
            "Store – خزن"
        ],
        "correct": 1
    },

    # 36
    {
        "q": "Which memory stores currently running programs?\n(أي ذاكرة تخزن البرامج الجارية؟)",
        "opts": [
            "ROM",
            "Hard disk",
            "RAM",
            "Flash"
        ],
        "correct": 2
    },

    # 37
    {
        "q": "Output of ALU is sent to:\n(ناتج ALU يُرسل إلى؟)",
        "opts": [
            "RAM",
            "Register",
            "Cache",
            "Hard disk"
        ],
        "correct": 1
    },

    # 38
    {
        "q": "Which device converts paper to digital?\n(أي جهاز يحول الورق إلى رقمي؟)",
        "opts": [
            "Printer",
            "Scanner",
            "Monitor",
            "Speaker"
        ],
        "correct": 1
    },

    # 39
    {
        "q": "Which stores OS files?\n(أين تُخزن ملفات النظام؟)",
        "opts": [
            "RAM",
            "Cache",
            "Hard disk",
            "Register"
        ],
        "correct": 2
    },

    # 40
    {
        "q": "Computer works on:\n(الحاسوب يعمل بنظام؟)",
        "opts": [
            "Manual processing – يدوي",
            "Mechanical processing – ميكانيكي",
            "Electronic processing – إلكتروني",
            "Human processing – بشري"
        ],
        "correct": 2
    }

]

count = 1
for q in questions:
    print(f"Sending question {count}")
    
    bot.send_poll(
        chat_id=CHAT_ID,
        question=f"س{count}️⃣\n\n{q['q']}",
        options=q["opts"],
        correct_option_id=q["correct"],
        type="quiz",
        is_anonymous=True
    )
    
    count += 1
    time.sleep(3)   # ⭐ هذا السطر هو الحل

print("✅ All questions sent")