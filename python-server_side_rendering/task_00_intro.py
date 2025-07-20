#!/usr/bin/python3
import os
"""
    Generate invitations based on a template and a list of attendees.
      Args:
        template (str): The invitation template.
        attendees (list): A list of attendee dictionaries.    Raises:
        ValueError: If the template is not a string, if the attendees
                    list is empty, or if the attendees list is not a
                    list of dictionaries.
"""


def generate_invitations(template, attendees):    # Many checks
    try:
        if not isinstance(template, str):
            raise ValueError("[ERROR] The template must be a string.")

        if not template.strip():
            raise ValueError("[ERROR] The template must not be empty.")

        if not isinstance(attendees, list):
            raise ValueError("[ERROR] Attendees must be a list.")

        if not attendees:
            raise ValueError("[ERROR] Attendees list must not be empty.")

        for item in attendees:
            if not isinstance(item, dict):
                raise ValueError(
                    "[ERROR] Attendees list must be a list of dictionaries."
                )

        template_content = template
        if not template_content.strip():
            print("Template is empty, no output files generated.")
            return

    except ValueError as err:
        print(err)
        return
    # If missing keys in the attendees list and update them with N/A
    for item in attendees:
        if not item.get('name'):
            item.update({'name': 'N/A'})

        if not item.get('event_title'):
            item.update({'event_title': 'N/A'})

        if not item.get('event_date'):
            item.update({'event_date': 'N/A'})

        if not item.get('event_location'):
            item.update({'event_location': 'N/A'})

    # Generate the invitations
    for item in attendees:
        invitation = template_content
        invitation = invitation.replace('{{name}}', item['name'])
        invitation = invitation.replace('{{event_title}}', item['event_title'])
        invitation = invitation.replace('{{event_date}}', item['event_date'])
        invitation = invitation.replace(
            '{{event_location}}', item['event_location']
        )

        # Save the invitation in a file
        filename = f"{item['name']}.html"
        with open(filename, "w") as file:
            file.write(invitation)
        print(f"Invitation for {item['name']} saved in {filename}")
        