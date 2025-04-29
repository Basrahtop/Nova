def generate_lesson(subject: str) -> str:
    # Placeholder logic — actual model coming in later iterations
    lessons = {
        "math": "Today’s lesson is about multiplication tables up to 12.",
        "english": "Let’s learn about nouns and verbs with easy examples.",
        "science": "We’re exploring living and non-living things today!"
    }
    return lessons.get(subject.lower(), "No lesson available for that subject.")
