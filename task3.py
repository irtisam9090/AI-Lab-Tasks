#simple reflex agent
class SimpleReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature 

    def perceive(self, current_temperature):
        return current_temperature

    def act(self, current_temperature):
        if current_temperature < self.desired_temperature:
            action = "Turn on heater"
        else:
            action = "Turn off heater"
        return action

rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}
desired_temperature = 22
agent = SimpleReflexAgent(desired_temperature)

for room, temperature in rooms.items():
    action = agent.act(temperature)
    print(f"{room}: Current temperature = {temperature}°C. {action}.")

#model base reflex agent
class ModelBasedReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
        self.heater_state = None  

    def perceive(self, current_temperature):
        return current_temperature

    def act(self, current_temperature):
        
        if current_temperature < self.desired_temperature:
            action = "Turn on heater"
            self.heater_state = "on"
        elif current_temperature >= self.desired_temperature:
            action = "Turn off heater"
            self.heater_state = "off"
        else:
            action = "No action"
        
        return action

rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}
desired_temperature = 22
agent = ModelBasedReflexAgent(desired_temperature)

for room, temperature in rooms.items():
    action = agent.act(temperature)
    print(f"{room}: Current temperature = {temperature}°C. {action}.")
