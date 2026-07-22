def generate_schedule(duration, carbs_per_hour):

    events = []

    total_minutes = int(duration * 60)

    interval = 45

    current = interval

    while current < total_minutes:

        if len(events) % 3 == 0:

            food = "gel"

            carbs = 25

        elif len(events) % 3 == 1:

            food = "boisson glucidique"

            carbs = 30

        else:

            food = "pâte de fruit"

            carbs = 25

        hours = current // 60

        minutes = current % 60

        events.append(
            {"time": f"{hours:02d}:{minutes:02d}", "type": food, "carbs": carbs}
        )

        current += interval

    return events
