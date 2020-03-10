class Pet:
    
    def __init__(self, vocalization,
                 happiness_communicator,
                    natural_enemy = 'human'):
        
        self.vocalization = vocalization
        self.happiness_communicator = happiness_communicator
        self.natural_enemy = natural_enemy
        
    def vocalize(self):
        print(self.vocalization)
        
    def express_happiness(self):
        print(self.happiness_communicator)
        
    def feelings(self):
        print(f"I hate {self.natural_enemy}")
    