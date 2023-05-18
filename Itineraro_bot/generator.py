import os
import openai

org_id = 'org-Mc54issDcu91GLgI5wR8b1EJ'
# Load your API key from an environment variable or secret management service

openai.api_key = ('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')
model_id = 'gpt-3.5-turbo'

def convo(plans):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You're itineraro, a discord travel planner for friends. You will recieve a place,"
                                                      +" time, number of users, their interests, hobbiers, dietary restrictions, and specific requests. If they allergic ensure that places dont have cross contamination "
                                                       +"Ensure that all users will be satisfied and generate a comprehensive itinerary for these users for"
                                                       +" each day and be specific. If users want to be busy give their schedule lots to do and if they dont they make their schedule with much more time between activities. "
                                                        +"Divide into sections for each day with a header written with '**' on the outside of the title to make the characters bold and a calendar emoji 📅."
                                                         +"make sure you mention their travel accomodations and how they will get to each place and give hotel reccomendations. Provide links for everything. You have a hard limit of 2000 characters."},
            {"role": "user", "content": plans},
        ])

    message = response.choices[0]['message']
    response = "{}: {}".format(message['role'], message['content'])[10:]

    return response
