def generate_plan(duration, carbs_per_hour):

    events = []

    interval = 45

    time = interval

    while time < duration * 60:

        events.append({"time": time, "carbs_target": carbs_per_hour})

        time += interval

    return events
