<!-- Title and Badges -->
<h1 align="center">🎙️ Persian Medical Speech-to-Text (تشخیص گفتار نسخه پزشکی به زبان فارسی)</h1>

<p align="center">
  <b>A Deep Learning-based Persian Speech Recognition System for Medical Prescriptions</b><br>
  <b>سیستم تشخیص گفتار فارسی برای نسخه‌های پزشکی، مبتنی بر یادگیری عمیق</b>
</p>

---

## 🧠 Overview | مقدمه

**EN:**  
This project is a **deep learning-powered speech-to-text system** for **Persian medical audio**, focusing on transcribing **spoken prescriptions by doctors** into **structured and readable text**. It can be integrated into hospital systems, used for digital record-keeping, or even mobile applications for clinical dictation.

**FA:**  
این پروژه یک سیستم **تبدیل گفتار به متن برای زبان فارسی** است که به‌صورت تخصصی برای **صداهای نسخه‌خوانی پزشکی** طراحی شده است. هدف، تبدیل نسخه‌های صوتی به **متن دقیق و ساخت‌یافته** است تا در سیستم‌های بیمارستانی، پرونده الکترونیکی، و اپلیکیشن‌های سلامت قابل استفاده باشد.

---

## 🎯 Objectives | اهداف

- ✅ Recognize Persian spoken medical prescriptions  
- ✅ Extract structured drug data (name, dosage, frequency)  
- ✅ Enable speech-to-text in healthcare applications  
- ✅ قابل استفاده در نرم‌افزارهای مدیریت مطب و کلینیک  
- ✅ استخراج دقیق اطلاعات دارویی از صدای پزشک  

---

## 🧰 Technologies Used | فناوری‌های مورد استفاده

- Python 3.10+
- PyTorch & torchaudio
- HuggingFace Transformers
- Whisper / Wav2Vec2.0
- Librosa
- NumPy, pandas, tqdm
- (اختیاری) Gradio یا Streamlit برای رابط کاربری

---

## 🧱 Project Structure | ساختار پروژه


<table>
  <thead>
    <tr>
      <th>Path</th>
      <th>توضیح (فارسی)</th>
      <th>Description (English)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>data/raw/</code></td>
      <td>فایل‌های صوتی خام (ورودی اولیه)</td>
      <td>Raw audio files as input (e.g., .wav)</td>
    </tr>
    <tr>
      <td><code>data/processed/</code></td>
      <td>داده‌های تمیز و برچسب‌خورده (آمادهٔ آموزش)</td>
      <td>Cleaned and labeled data for training</td>
    </tr>
    <tr>
      <td><code>models/</code></td>
      <td>مدل‌های آموزش‌دیده و Checkpointها</td>
      <td>Trained model checkpoints</td>
    </tr>
    <tr>
      <td><code>notebooks/</code></td>
      <td>دفترچه‌های Jupyter برای تحلیل یا نمونه‌سازی</td>
      <td>Jupyter notebooks for analysis and prototyping</td>
    </tr>
    <tr>
      <td><code>src/preprocessing.py</code></td>
      <td>اسکریپت پیش‌پردازش صدا و داده</td>
      <td>Audio preprocessing, noise removal, feature extraction</td>
    </tr>
    <tr>
      <td><code>src/train.py</code></td>
      <td>آموزش مدل یادگیری ماشین</td>
      <td>Model training script (e.g., Whisper, Wav2Vec)</td>
    </tr>
    <tr>
      <td><code>src/inference.py</code></td>
      <td>استنتاج: تبدیل صدا به متن</td>
      <td>Run inference to convert audio to text</td>
    </tr>
    <tr>
      <td><code>src/utils.py</code></td>
      <td>توابع کمکی برای پردازش، لاگ و تنظیمات</td>
      <td>Helper utilities: configs, logging, loaders, etc.</td>
    </tr>
    <tr>
      <td><code>configs/</code></td>
      <td>فایل‌های پیکربندی YAML یا JSON</td>
      <td>YAML/JSON configuration files</td>
    </tr>
    <tr>
      <td><code>requirements.txt</code></td>
      <td>لیست کتابخانه‌های پایتون موردنیاز</td>
      <td>List of required Python packages</td>
    </tr>
    <tr>
      <td><code>README.md</code></td>
      <td>مستندات کلی پروژه</td>
      <td>Project overview and documentation</td>
    </tr>
    <tr>
      <td><code>HELP.md</code></td>
      <td>سؤالات رایج و راهنمای رفع اشکال</td>
      <td>FAQ and troubleshooting guide</td>
    </tr>
    <tr>
      <td><code>.gitignore</code></td>
      <td>نادیده‌گرفتن فایل‌های غیرضروری توسط Git</td>
      <td>Exclude unnecessary files from Git tracking</td>
    </tr>
  </tbody>
</table>

---

## 🚀 Installation & Setup | نصب و راه‌اندازی

### 📌 Prerequisites | پیش‌نیازها

- Python 3.10 or higher  
- pip or conda  
- Git  
- (Optional) CUDA for GPU acceleration  

### 🔧 Install Dependencies | نصب کتابخانه‌ها

```bash
git clone https://github.com/YOUR_USERNAME/speech-to-text-medical-fa.git
cd speech-to-text-medical-fa
pip install -r requirements.txt


🎙️ How to Use | نحوه استفاده
🔹 1. Run Inference | اجرای تشخیص گفتار
bash
Copy
Edit
python src/inference.py --input_audio data/raw/sample.wav
This will output transcription of the medical audio into a .txt file.

🔹 2. Train Custom Model | آموزش مدل شخصی‌سازی‌شده
bash
Copy
Edit
python src/train.py --config configs/train_config.yaml
Use your own medical dataset for better accuracy in prescription recognition.

🔹 3. Preprocess Your Audio | پیش‌پردازش فایل صوتی
bash
Copy
Edit
python src/preprocessing.py --input_folder data/raw --output_folder data/processed
Includes noise reduction, resampling, segmentation, etc.

💬 Example Output | نمونه خروجی
Input audio:
"قرص استامینوفن ۵۰۰ هر ۸ ساعت یک عدد مصرف شود."

Transcribed text:

makefile
Copy
Edit
دارو: استامینوفن ۵۰۰  
دوز مصرف: ۱ عدد  
فاصله زمانی: هر ۸ ساعت
🗂️ Dataset Guidelines | ساخت دیتاست
If you want to build your own dataset:

Collect audio samples of doctors reading prescriptions (preferably 16kHz mono .wav)

Label them manually in .txt format

Organize as:

kotlin
Copy
Edit
data/
  raw/
    001.wav
    002.wav
  processed/
    001.txt
    002.txt
⚙️ Customization Tips | نکات توسعه
You can fine-tune the model with your own domain-specific data

Add a custom dictionary for Persian drug names (پیشنهاد می‌شود)

Integrate with an NLP pipeline to extract dosage, frequency, and drug name

🧪 Evaluation | ارزیابی مدل
WER (Word Error Rate)

CER (Character Error Rate)

Accuracy on drug extraction

Performance in noisy environments

🙋 FAQ / سؤالات متداول
آیا این سیستم آنلاین کار می‌کند؟
در حال حاضر فقط به‌صورت آفلاین روی سیستم اجرا می‌شود. در آینده نسخه API ارائه می‌شود.

آیا نسخه موبایل یا وب دارد؟
خیر، اما می‌توانید با ابزارهایی مثل Gradio یا Streamlit یک نسخه وب تستی بسازید.

چطور دقت را بالا ببریم؟
با جمع‌آوری داده‌های تخصصی‌تر، افزایش حجم دیتاست، و آموزش مدل بر داده‌های پزشکی

🤝 Contribution | مشارکت
We welcome contributions from the open-source community.
برای مشارکت، لطفاً ابتدا یک Issue باز کنید یا از طریق Pull Request مشارکت داشته باشید.

📄 License | مجوز
MIT License

📬 Contact | ارتباط با ما
For questions, suggestions, or collaboration:
جهت ارتباط با تیم توسعه:

github:
https://github.com/MRTahasaadat
https://github.com/Aliakbar-omidi

Email:
mrtahasaadat@gmail.com
aliakbaromidyy@gmail.com

