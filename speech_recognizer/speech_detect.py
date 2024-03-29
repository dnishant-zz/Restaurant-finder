class SpeechDetector:
    def __init__(self):
        # Microphone stream config.
        self.CHUNK = 1024  # CHUNKS of bytes to read each time from mic
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000
        
        self.SILENCE_LIMIT = 1  # Silence limit in seconds. The max ammount of seconds where
        # only silence is recorded. When this time passes the
        # recording finishes and the file is decoded
        
        self.PREV_AUDIO = 0.5  # Previous audio (in seconds) to prepend. When noise
        # is detected, how much of previously recorded audio is
        # prepended. This helps to prevent chopping the beginning
        # of the phrase.
        
        self.THRESHOLD = 4500
        self.num_phrases = -1
        
        # These will need to be modified according to where the pocketsphinx folder is
        MODELDIR = ""
        
        # Create a decoder with certain model
        config = Decoder.default_config()
        config.set_string('-hmm', os.path.join(MODELDIR, 'en-us'))
        config.set_string('-lm', os.path.join(MODELDIR, 'anish.lm.bin'))
        config.set_string('-dict', os.path.join(MODELDIR, 'cmudict-en-us.dict'))
        
        # Decode streaming data.
        self.decoder = Decoder(config)
    


    def detect(self, input):
        self.decoder.start_utt()
        stream = open(input, "rb")
        while True:
            buffer = stream.read(1024)
            if buffer:
                self.decoder.process_raw(buffer, False, False)
            else:
                break
                self.decoder.end_utt()
        words = [][words.append(seg.word) for seg in self.decoder.seg()]
        return words

