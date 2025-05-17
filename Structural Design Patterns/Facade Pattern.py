

class TV:
    def switch_on(self):
        print("TV Started")
        
    def switch_off(self):
        print("TV Switched Off")
        
    def volume_up(self):
        print("Volume Increased")
        
    def volume_down(self):
        print("Volume Decreased")

class SoundSystem:
    def turn_on(self):
        print("Sound System Turned On")
        
    def Connect(self):
        print("Sound System connected to TV")
    def turn_off(self):
        print("Sound System Turned Off")

class Lights:
    def turn_on(self):
        print("Lights On")
    
    def turn_off(self):
        print("Lights Turned off.")

        

class StreamMovie:
    def __init__(self,streaming_platform = None):
        self.streaming_platform = streaming_platform
        
    def select_ott(self,streaming_platform):
        self.streaming_platform = streaming_platform
        print(f"Opening {self.streaming_platform}")
        
    def surf_movie(self):
        print(f"Surfing Movie on {self.streaming_platform}")
        
    def start_movie(self):
        print("Playing Movie")


        
        
class HomeTheaterFacade:
    def __init__(self,streaming_platform = None):
        self.tv = TV()
        self.sound_system = SoundSystem()
        self.lights = Lights()
        self.stream_movie = StreamMovie(streaming_platform)
        
    def watch_movie(self,streaming_platform):
        self.tv.switch_on()
        self.sound_system.turn_on()
        self.sound_system.Connect()
        self.lights.turn_off()
        self.stream_movie.select_ott(streaming_platform)
        self.stream_movie.surf_movie()
        self.stream_movie.start_movie()
    
    def end_movie(self):
        self.tv.switch_off()
        self.sound_system.turn_off()
        self.lights.turn_on()
        print("Movie Ended")
        
        
facade = HomeTheaterFacade()
facade.watch_movie("Netflix")
        

