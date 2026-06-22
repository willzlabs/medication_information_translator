class Medication:
    def __init__(self, name: str, usage: str, warnings: str, side_effects: str, instructions: str):
        self.name = name
        self.usage = usage
        self.warnings = warnings
        self.side_effects = side_effects
        self.instructions = instructions