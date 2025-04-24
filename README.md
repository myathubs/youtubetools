# MyatHubs YouTube Notes Generator

Generate high-quality blog-style notes from YouTube videos using OpenAI GPT-3.5. Includes 🇬🇧 English and 🇲🇲 Burmese output support. Built with Streamlit and designed for creators, students, and knowledge sharers.

## 🚀 Features

- ✨ Uses OpenAI GPT-3.5 to summarize YouTube content
- 🌐 Output in English 🇬🇧 or Burmese 🇲🇲
- 📄 Download notes as `.txt`
- 🧠 Includes AI-generated key points & mind map
- 📱 Mobile sharing tips for Messenger/Facebook
- 🎨 Simple and responsive Streamlit interface

## 🧠 Tech Stack

- Python 3.11
- Streamlit
- OpenAI GPT-3.5
- Google Translate API (for Burmese toggle)
- dotenv (.env support for API keys)

## 🖼️ Screenshot

![Application Screenshot](screenshots/sample.png)

## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/youtube-notes-generator.git
   cd youtube-notes-generator
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your OpenAI key:

   ```env
   OPENAI_API_KEY=your_openai_key_here
   ```

## 🚀 Usage

1. Run the application:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Paste a YouTube link, select language, and click "Generate Notes."

## ⭐ Support

If you find this tool helpful, give it a ⭐ on GitHub and share it with others!

## 📬 Contact

For questions, collaboration, or feedback, open an issue or reach out on social.
