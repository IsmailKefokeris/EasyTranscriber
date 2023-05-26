from faster_whisper import WhisperModel
import torch
from whisper.utils import WriteSRT
import datetime


class FasterWhisperFunctions():
    def __init__(self, model):
        torch.cuda.is_available()
        DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

        MODELS = ["tiny", "base", "small", "medium", "large-v1", "large-v2",]

        self.model = WhisperModel(MODELS[model], device=DEVICE, compute_type="float32")


    def transcribe(self, audio_url):
        segments, info = self.model.transcribe(audio_url, beam_size=5)

        return segments, info

    def format_time(self, time):
        time = datetime.timedelta(seconds=time)

        # Extract the components from the timedelta object
        hours = time // datetime.timedelta(hours=1)
        minutes = (time // datetime.timedelta(minutes=1)) % 60
        seconds = (time // datetime.timedelta(seconds=1)) % 60
        milliseconds = (time // datetime.timedelta(milliseconds=1)) % 1000

        formatted_time = "{:02d}:{:02d}:{:02d},{:03d}".format(hours, minutes, seconds, milliseconds)

        return formatted_time
    
    def display_transcribed_text(self, transcribed, print_text=False):
        text = []
        
        for segment in transcribed:
            start = self.format_time(segment.start)
            
            end = self.format_time(segment.end)

            main_body = segment.text
            # text.append(f"{start},:,{end}, - , {segment['text']}")
            text.append([start, end, main_body])
        
        return text

    def save_as_srt(self, transcribed, file_path):
        # Needs fixing must include ,000 at the end of all timestamps
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

        print(f"Transcribed text file saved as .srt to: {file_path}")

