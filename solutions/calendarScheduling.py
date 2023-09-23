# greedy approach
def schedule_lessons(lesson_requests):
    # Sort lesson requests in descending order of potential earnings
    lesson_requests.sort(key=lambda x: x['potentialEarnings'], reverse=True)

    schedule = {}

    # Initialize the available hours for each day
    available_hours = {
        'monday': 12,
        'tuesday': 12,
        'wednesday': 12,
        'thursday': 12,
        'friday': 12,
        'saturday': 12,
        'sunday': 12
    }

    # Iterate over lesson requests and schedule lessons
    for request in lesson_requests:
        duration = request['duration']
        earnings = request['potentialEarnings']
        available_days = request['availableDays']

        # Find the first available day where the lesson can fit within the available hours
        for day in available_days:
            if available_hours[day] >= duration:
                if day not in schedule:
                    schedule[day] = []
                schedule[day].append(request['lessonRequestId'])
                available_hours[day] -= duration
                break

    return schedule


# Test case
lesson_requests = [
    {
        "lessonRequestId": "LR1",
        "duration": 1,
        "potentialEarnings": 100,
        "availableDays": ["monday", "wednesday"]
    },
    {
        "lessonRequestId": "LR2",
        "duration": 2,
        "potentialEarnings": 50,
        "availableDays": ["monday"]
    },
    {
        "lessonRequestId": "LR3",
        "duration": 12,
        "potentialEarnings": 1000,
        "availableDays": ["wednesday"]
    },
    {
        "lessonRequestId": "LR4",
        "duration": 13,
        "potentialEarnings": 10000,
        "availableDays": ["friday"]
    }
]

schedule = schedule_lessons(lesson_requests)