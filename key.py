#	Johnathan Speck

class key:
    def __init__(self, id, down, just_pressed, just_released):
	    self.id = id
	    self.down = down 
	    self.just_pressed = just_pressed 
	    self.just_released = just_released

    def get_key_name(self):
	    return pygame.key.name(self.id)

    def printStatus(self):
	    print("  key: ", self.get_key_name(), " |  down: ", self.down, " |  just pressed: ", self.just_pressed, " |  just released: ", self.just_released)