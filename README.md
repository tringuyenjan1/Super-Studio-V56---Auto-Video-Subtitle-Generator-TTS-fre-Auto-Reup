# Super-Studio-V56---Auto-Video-Subtitle-Generator-TTS-fre-Auto-Reup

# 🎬 Super Studio V56 - Auto Video & Subtitle Generator

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

**Super Studio V56** is an all-in-one, fully automated video processing tool designed to streamline content creation for platforms like YouTube Shorts, TikTok, and Facebook Reels. 

With a single click, this tool uses AI to transcribe audio, accurately detect speaker genders, translate subtitles, generate high-quality Text-to-Speech (TTS), and automatically sync everything to your original video perfectly.

---

## ✨ Key Features

*   **🤖 Smart AI Translation:** Supports integration with Gemini, ChatGPT, Claude, and DeepSeek for context-aware translations.
*   **🎙️ Precise Gender Detection:** Automatically analyzes audio pitch to assign male or female voices to the correct speaker without manual tagging.
*   **⏱️ Perfect Audio Sync (Time-Stretch):** Automatically adjusts TTS speed to ensure the generated audio fits perfectly within the original video's timeframe.
*   **📱 Multi-Platform Aspect Ratios:** Auto-crop your videos to 9:16 (TikTok/Shorts), 1:1 (Square), or 16:9 with center-focus.
*   **🛡️ Anti-Reup Filters:** Built-in video flipping and color adjustment features to avoid copyright detection.
*   **🌍 Bilingual UI:** The user interface supports both English and Vietnamese for seamless operation.
*   **📊 Real-time Progress Tracking:** Watch the progress bar update smoothly from 0% to 100% directly on the UI.

---

## 🚀 Installation

### 1. Prerequisites
Make sure you have [Python 3.12 or higher](https://www.python.org/downloads/) installed. You will also need `FFmpeg` installed and added to your system's PATH.

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME3. Install Dependencies
Bash
pip install -r requirements.txt
(Make sure to include packages like gradio, numpy, soundfile, edge_tts, librosa, whisper, deep_translator, etc., in your requirements.txt)

💻 Usage
Run the following command in your terminal to start the application:

Bash
python app.py
Once the script is running, open your web browser and navigate to the local URL provided in the terminal (usually http://127.0.0.1:7860).

🔑 API Key Setup
To use the advanced AI Directors (Gemini, OpenAI, Claude, DeepSeek), you will need to input your API keys directly into the UI under the Translation Engine section.

🛠️ Workflows
1-Click Auto Video: Upload your raw video, select your preferred voices, set the aspect ratio (e.g., 9:16 for TikTok), and click run. The tool handles extraction, translation, TTS, mixing, and rendering automatically.

Manual Extraction: Extract .srt files using Whisper AI and manually translate them using Google Translate.

Voice Management: Add custom cloned voices (.wav or .mp3) to the voices/ folder for personalized TTS output.
