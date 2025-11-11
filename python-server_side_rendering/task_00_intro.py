#!/usr/bin/python3
"""
Task 0: Creating a Simple Templating Program
"""


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Invalid input type: template must be a string, "
              f"got {type(template).__name__}")
        return

    if not isinstance(attendees, list):
        print(f"Invalid input type: attendees must be a list, "
              f"got {type(attendees).__name__}")
        return

    if not all(isinstance(item, dict) for item in attendees):
        item_type = (type(attendees[0]).__name__
                     if attendees else 'non-dict items')
        print(f"Invalid input type: attendees must be a list of dictionaries, "
              f"got list containing {item_type}")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        personalized_template = template

        personalized_template = personalized_template.replace(
            "{name}", attendee.get("name", "N/A"))
        personalized_template = personalized_template.replace(
            "{event_title}", attendee.get("event_title", "N/A"))
        personalized_template = personalized_template.replace(
            "{event_date}",
            "N/A" if attendee.get("event_date") is None
            else attendee.get("event_date", "N/A"))
        personalized_template = personalized_template.replace(
            "{event_location}", attendee.get("event_location", "N/A"))

        output_filename = f"output_{i}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(personalized_template)

        print(f"Generated invitation for {attendee.get('name', 'N/A')} "
              f"in {output_filename}")
