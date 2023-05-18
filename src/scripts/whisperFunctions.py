import whisper
from whisper.utils import WriteSRT
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
            main_body = segment['text']
            # text.append(f"{start},:,{end}, - , {segment['text']}")
            text.append([start, end, main_body])
        
        return text

    def save_as_srt(self, transcribed, file_path):
        with open(file_path, "w") as file:
            cnt = 0
            for index in range(transcribed.count()):
                item = transcribed.item(index).text()

                if cnt == 0:
                    # Index
                    file.write(f"{item}\n")
                    cnt+=1
                elif cnt == 1:
                    # Time
                    file.write(f"{item}\n")
                    cnt+=1
                elif cnt == 2:
                    # Text
                    file.write(f"{item}\n\n")
                    cnt = 0

            # for i, line in enumerate(transcribed, start=1):
            #     start = line[0]
            #     end = line[1]
            #     text = line[2]

            #     file.write(f"{i}\n")
            #     file.write(f"{start} --> {end}\n")
            #     file.write(f"{text}\n\n")
        
        print(f"Transcribed text file saved as .srt to: {file_path}")

