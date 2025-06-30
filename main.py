from gtts import gTTS
import whisper
from pydub import AudioSegment
import os

def text_to_mp3(text: str, mp3_path: str):
    tts = gTTS(text=text, lang='ru')
    tts.save(mp3_path)
    print(f"[✓] MP3 сохранён: {mp3_path}")

def transcribe_mp3(mp3_path: str, txt_output_path: str):
    wav_path = mp3_path.replace('.mp3', '.wav')
    AudioSegment.from_mp3(mp3_path).export(wav_path, format="wav")
    print(f"[✓] MP3 → WAV: {wav_path}")

    model = whisper.load_model("base")
    result = model.transcribe(wav_path)

    with open(txt_output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print(f"[✓] Транскрипция сохранена в: {txt_output_path}")

if __name__ == "__main__":
    text = "Привет, мир! Это пример преобразования текста в речь и обратно в текст."
    mp3_file = "example.mp3"
    txt_file = "result.txt"

    text_to_mp3(text, mp3_file)
    transcribe_mp3(mp3_file, txt_file)
