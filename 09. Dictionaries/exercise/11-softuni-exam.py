participants = {}

language_submissions = {}

while True:
    command = input()
    
    if command == "exam finished":
        break
    
    if command.endswith("-banned"):
        username = command.replace("-banned", "")

        if username in participants:
            del participants[username]
    else:
        parts = command.split("-")
        username = parts[0]
        language = parts[1]
        points = int(parts[2])
        
        if language not in language_submissions:
            language_submissions[language] = 0
        language_submissions[language] += 1
        
        if username not in participants:
            participants[username] = {}
        
        if language not in participants[username]:
            participants[username][language] = points
        else:
            participants[username][language] = max(participants[username][language], points)

participant_max_points = {}
for username, languages in participants.items():
    participant_max_points[username] = max(languages.values())

sorted_participants = sorted(participant_max_points.items(), 
                            key=lambda x: (-x[1], x[0]))

print("Results:")
for username, points in sorted_participants:
    print(f"{username} | {points}")

sorted_languages = sorted(language_submissions.items(), 
                         key=lambda x: (-x[1], x[0]))

print("Submissions:")
for language, count in sorted_languages:
    print(f"{language} - {count}")