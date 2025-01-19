from abc import ABC, abstractmethod 

class State(ABC):
    @abstractmethod
    def play(self, player):
        pass
    @abstractmethod
    def pause(self, player):
        pass
    @abstractmethod
    def stop(self, player):
        pass
    
class PlayingState(State):
    def play(self, player):
        print('Already Palying')
    def pause(self, player):
        print('Pausing the player')
        player.change_state(PausedState())
    def stop(self, player):
        print('Stoppig playback.')
        player.change_state(StoppedState())

class PausedState(State):
    def play(self, player):
        print('Resume playback.')
        player.change_state(PlayingState())

    def pause(self, player):
        print('Already Paused.')

    def stop(self, player):
        print('Stopping from paused state.')
        player.change_state(StoppedState())

class StoppedState(State):
    def play(self, player):
        print('Starting playback')
        player.change_state(PlayingState())

    def pause(self, player):
        print('Cannot pause. The player is stopped.')

    def stop(self, player):
        print('Already stopped.')

class MediaPlayer:
    def __init__(self):
        self._state = StoppedState()
    
    def change_state(self, state):
        self._state = state
        
    def play(self):
        self._state.play(self)

    def pause(self):
        self._state.pause(self) 

    def stop(self):
        self._state.stop(self)

if __name__=='__main__':
    player = MediaPlayer()
    player.play()
    player.pause()
    player.play()
    player.stop()
    player.pause()
    