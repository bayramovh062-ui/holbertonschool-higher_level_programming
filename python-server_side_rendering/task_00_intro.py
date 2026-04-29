#!/usr/bin/pyhton3
"""
this code  is an example of server side rendering
"""


import os

def generate_invitations(template, attendees):
    """
    this function is using for define template and
    attends and create a template with using these
    information
    """
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        processed_content = template
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            processed_content = processed_content.replace(f"{{{key}}}", str(value))

        filename = f"output_{index}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(processed_content)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")

