class Player(object):
    def __init__(self, name, position, avgMinutesPlayed, avgPoints, avgRebounds, starter):
        self.name = name
        self.position = position
        self.avgMinutesPlayed = avgMinutesPlayed
        self.avgPoints = avgPoints
        self.avgRebounds = avgRebounds
        self.starter = starter
