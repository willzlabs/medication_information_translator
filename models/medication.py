class Medication:
    def __init__(self, name, usage, warnings, side_effects, instructions):
        self.name = name
        self.usage = usage
        self.warnings = warnings
        self.side_effects = side_effects
        self.instructions = instructions

    def display_info(self):
        return f"""Medication: {self.name}\n\nUsage:\n{self.usage}\n\nWarnings:\n{self.warnings}\n\nSide Effects:\n{self.side_effects}\n\nInstructions:\n{self.instructions}"""