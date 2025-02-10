from gtts import gTTS


def text_to_speech(text):
    save_path = "./static/audio/voice.mp3"
    tts = gTTS(text=text, lang='uk')
    tts.save(savefile=save_path)
    return save_path