import whisper
import datetime


class WhisperFunctions():
    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe(self, audio_url):
        results = self.model.transcribe(audio_url)

        for key, val in results.items():
            print(key)

        return results
    
    def display_transcribed_text(self, transcribed, print_text=False):
        text = []
        if print_text:
            for segment in transcribed["segments"]:
                print(datetime.timedelta(seconds=segment["start"]),":",datetime.timedelta(seconds=segment["end"])," - ", segment["text"])
            return
        
        for segment in transcribed["segments"]:
            start = datetime.timedelta(seconds=segment["start"])
            end = datetime.timedelta(seconds=segment["end"])
            text.append(f"{start},:,{end}, - , {segment['text']}")
        
        return text
    
    def save_as_srt(self, transcribed, file_path):
        with open(file_path, "w") as file:
            for i, segment in enumerate(transcribed["segments"], start=1):
                start = datetime.timedelta(seconds=segment["start"])
                end = datetime.timedelta(seconds=segment["end"])
                text = segment["text"]

                file.write(f"{i}\n")
                file.write(f"{start} --> {end}\n")
                file.write(f"{text}\n\n")
        
        print(f"Transcribed text file saved as .srt to: {file_path}")
