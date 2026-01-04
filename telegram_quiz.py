from telegram import Bot
import time


TOKEN = "8255957753:AAFnaI7St8vi1DsE5m3Y3POxYsL7GBa3z20"
CHAT_ID = "@MCQCompStructureUOK"

bot = Bot(token=TOKEN)

questions = [

# 1
{
"q": "CPU stands for?\nماذا تعني CPU؟",
"opts": [
"Central Program Unit (وحدة برنامج)",
"Central Processing Unit (وحدة المعالجة)",
"Computer Unit (وحدة الحاسوب)",
"Control Unit (وحدة التحكم)"
],
"correct": 1
},

# 2
{
"q": "What is the main role of the CPU?\nما الوظيفة الرئيسية للمعالج؟",
"opts": [
"Store data permanently (تخزين دائم)",
"Display output (عرض النتائج)",
"Process data into information (معالجة البيانات)",
"Connect devices (ربط الأجهزة)"
],
"correct": 2
},

# 3
{
"q": "Which unit controls all CPU operations?\nأي وحدة تتحكم بعمل المعالج؟",
"opts": [
"ALU (وحدة الحساب)",
"Register (سجل)",
"Control Unit (وحدة التحكم)",
"Bus (ناقل)"
],
"correct": 2
},

# 4
{
"q": "Which unit performs arithmetic operations?\nأي وحدة تنفذ العمليات الحسابية؟",
"opts": [
"CU (وحدة التحكم)",
"ALU (الحساب والمنطق)",
"Register (سجل)",
"Memory (ذاكرة)"
],
"correct": 1
},

# 5
{
"q": "Which is NOT part of the CPU?\nأي مما يلي ليس جزءًا من المعالج؟",
"opts": [
"ALU (الحساب والمنطق)",
"Control Unit (وحدة التحكم)",
"Registers (السجلات)",
"Printer (الطابعة)"
],
"correct": 3
},

# 6
{
"q": "Registers are:\nالسجلات هي:",
"opts": [
"Slow storage (تخزين بطيء)",
"Permanent storage (تخزين دائم)",
"High-speed temporary storage (تخزين سريع مؤقت)",
"Input devices (أجهزة إدخال)"
],
"correct": 2
},

# 7
{
"q": "What does ALU stand for?\nماذا تعني ALU؟",
"opts": [
"Arithmetic Logic Unit (الحساب والمنطق)",
"Advanced Logic Unit (منطق متقدم)",
"Access Logic Unit (وحدة وصول)",
"Arithmetic Load Unit (تحميل حسابي)"
],
"correct": 0
},

# 8
{
"q": "Which register holds the next instruction address?\nأي سجل يحمل عنوان التعليمة التالية؟",
"opts": [
"IR (سجل التعليمة)",
"PC (عداد البرنامج)",
"MAR (سجل العناوين)",
"Accumulator (المجمع)"
],
"correct": 1
},

# 9
{
"q": "Which register holds the current instruction?\nأي سجل يحمل التعليمة الحالية؟",
"opts": [
"PC (عداد البرنامج)",
"IR (سجل التعليمة)",
"MAR (سجل العناوين)",
"ACC (المجمع)"
],
"correct": 1
},

# 10
{
"q": "Which register stores operation results?\nأي سجل يخزن نتائج العمليات؟",
"opts": [
"PC (عداد البرنامج)",
"IR (سجل التعليمة)",
"Accumulator (المجمع)",
"MAR (سجل العناوين)"
],
"correct": 2
},

# 11
{
"q": "What is the first step in machine cycle?\nما أول خطوة في دورة الآلة؟",
"opts": [
"Execute (تنفيذ)",
"Decode (فك الترميز)",
"Fetch (جلب التعليمة)",
"Store (تخزين)"
],
"correct": 2
},

# 12
{
"q": "Which step decodes the instruction?\nأي خطوة تفك ترميز التعليمة؟",
"opts": [
"Fetch (جلب)",
"Decode (فك الترميز)",
"Execute (تنفيذ)",
"Store (تخزين)"
],
"correct": 1
},

# 13
{
"q": "Which step executes the instruction?\nأي خطوة تنفذ التعليمة؟",
"opts": [
"Fetch (جلب)",
"Decode (فك)",
"Execute (تنفيذ)",
"Store (تخزين)"
],
"correct": 2
},

# 14
{
"q": "What does MAR stand for?\nماذا تعني MAR؟",
"opts": [
"Memory Access Register (وصول)",
"Memory Address Register (عنوان الذاكرة)",
"Main Address Register (عنوان رئيسي)",
"Machine Address Register (عنوان آلة)"
],
"correct": 1
},

# 15
{
"q": "What is a bus?\nما هو الناقل (Bus)؟",
"opts": [
"Storage unit (وحدة تخزين)",
"Electronic pathway (مسار إلكتروني)",
"Input device (إدخال)",
"Processing unit (معالجة)"
],
"correct": 1
},

# 16
{
"q": "Which bus carries data?\nأي ناقل ينقل البيانات؟",
"opts": [
"Address bus (العناوين)",
"Control bus (التحكم)",
"Data bus (البيانات)",
"System bus (النظام)"
],
"correct": 2
},

# 17
{
"q": "Which bus carries addresses?\nأي ناقل يحمل العناوين؟",
"opts": [
"Data bus (البيانات)",
"Control bus (التحكم)",
"Address bus (العناوين)",
"Expansion bus (توسعة)"
],
"correct": 2
},

# 18
{
"q": "Which bus carries control signals?\nأي ناقل يحمل إشارات التحكم؟",
"opts": [
"Data bus (بيانات)",
"Address bus (عناوين)",
"Control bus (تحكم)",
"System bus (نظام)"
],
"correct": 2
},

# 19
{
"q": "Binary system uses:\nالنظام الثنائي يستخدم:",
"opts": [
"0 and 1 (صفر وواحد)",
"0 to 9 (أرقام عشرية)",
"A and B (حروف)",
"True only (صح فقط)"
],
"correct": 0
},

# 20
{
"q": "Decimal system has how many digits?\nكم عدد أرقام النظام العشري؟",
"opts": [
"2 digits",
"8 digits",
"10 digits",
"16 digits"
],
"correct": 2
},

# 21
{
"q": "Binary system has how many digits?\nكم عدد أرقام النظام الثنائي؟",
"opts": [
"2 digits",
"8 digits",
"10 digits",
"16 digits"
],
"correct": 0
},

# 22
{
"q": "What does ASCII stand for?\nماذا تعني ASCII؟",
"opts": [
"American Standard Code for Information Interchange",
"Advanced System Code",
"Automatic Symbol Code",
"Applied System Code"
],
"correct": 0
},

# 23
{
"q": "ASCII uses how many bits?\nكم عدد البتات في ASCII؟",
"opts": [
"4 bits",
"8 bits",
"16 bits",
"32 bits"
],
"correct": 1
},

# 24
{
"q": "Unicode uses how many bits?\nكم عدد البتات في Unicode؟",
"opts": [
"8 bits",
"16 bits",
"32 bits",
"64 bits"
],
"correct": 1
},

# 25
{
"q": "Unicode can represent:\nUnicode يستطيع تمثيل:",
"opts": [
"English only",
"Numbers only",
"Most world languages",
"Binary only"
],
"correct": 2
},

# 26
{
"q": "Which coding is used in mainframes?\nأي ترميز يُستخدم في الحواسيب الكبيرة؟",
"opts": [
"ASCII",
"EBCDIC",
"Unicode",
"Binary"
],
"correct": 1
},

# 27
{
"q": "PC register stores:\nعداد البرنامج يخزن:",
"opts": [
"Current instruction",
"Next instruction address",
"Data value",
"Result"
],
"correct": 1
},

# 28
{
"q": "IR register stores:\nسجل التعليمة يخزن:",
"opts": [
"Next instruction",
"Memory address",
"Current instruction",
"Results"
],
"correct": 2
},

# 29
{
"q": "Accumulator is used for:\nالمجمع يُستخدم لـ:",
"opts": [
"Addressing",
"Storing results",
"Fetching instructions",
"Decoding"
],
"correct": 1
},

# 30
{
"q": "Bus width affects:\nعرض الناقل يؤثر على:",
"opts": [
"Storage size",
"Processing speed",
"Data transfer speed",
"Power usage"
],
"correct": 2
},

# 31
{
"q": "ALU performs logic operations like:\nالعمليات المنطقية مثل:",
"opts": [
"Add only",
"Subtract only",
"Compare values",
"Store data"
],
"correct": 2
},

# 32
{
"q": "Which is temporary storage?\nأي تخزين مؤقت؟",
"opts": [
"Hard disk",
"SSD",
"Registers",
"Flash drive"
],
"correct": 2
},

# 33
{
"q": "Which component interprets instructions?\nأي مكون يفسر التعليمات؟",
"opts": [
"ALU",
"CU",
"Register",
"Bus"
],
"correct": 1
},

# 34
{
"q": "Machine cycle has how many steps?\nكم عدد خطوات دورة الآلة؟",
"opts": [
"2",
"3",
"4",
"5"
],
"correct": 2
},

# 35
{
"q": "Which step stores result?\nأي خطوة تخزن النتيجة؟",
"opts": [
"Fetch",
"Decode",
"Execute",
"Store"
],
"correct": 3
},

# 36
{
"q": "Binary 1 means:\nالرقم 1 يعني:",
"opts": [
"Off",
"On",
"Error",
"Null"
],
"correct": 1
},

# 37
{
"q": "Binary 0 means:\nالرقم 0 يعني:",
"opts": [
"On",
"Off",
"True",
"Signal"
],
"correct": 1
},

# 38
{
"q": "CPU works with:\nالمعالج يعمل مع:",
"opts": [
"Keyboard",
"Mouse",
"Main memory",
"Monitor"
],
"correct": 2
},

# 39
{
"q": "Which is output device?\nأي جهاز إخراج؟",
"opts": [
"Keyboard",
"Mouse",
"Monitor",
"Scanner"
],
"correct": 2
},

# 40
{
"q": "Main function of bus:\nالوظيفة الرئيسية للناقل:",
"opts": [
"Store data",
"Process data",
"Transfer data",
"Display data"
],
"correct": 2
}

]

for item in questions:
    bot.send_poll(
        chat_id=CHAT_ID,
        question=item["q"],
        options=item["opts"],
        correct_option_id=item["correct"],
        type="quiz",
        is_anonymous=True
    )
    time.sleep(1)
