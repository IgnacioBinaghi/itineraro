import os
import openai
from bardapi import Bard

token = 'WQgjAEFxXf7nAKcL1qVgEh8TLtLQCkROSlcTSEIIjHIkqg-fPkT0wSUBSxJKMXBKaeX5Aw.'
bard = Bard(token = token)

org_id = 'org-Mc54issDcu91GLgI5wR8b1EJ'
# Load your API key from an environment variable or secret management service

openai.api_key = ('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')
model_id = 'gpt-3.5-turbo'

def convo(plans):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You're itineraro, a travel planner for individuals and friends that can also accomodate for special needs. You will recieve a place,"
                                                      +" time, number of users, their interests, hobbiers, dietary restrictions, and specific requests. If they allergic ensure that places dont have cross contamination "
                                                       +"Ensure that all users will be satisfied and generate a comprehensive itinerary for these users for"
                                                       +" each day and be specific. If users want to be busy give their schedule lots to do and if they dont they make their schedule with much more time between activities. Ensure to include prices next to each reccomendation and ensure to put a final price for everything at the bottom that satisfies the budget"
                                                        +"Divide into sections for each day with a header <h1>, and give them each their own correspionding emoji within the html next to the day that relates to the plans for that day."
                                                         +"make sure you mention their travel accomodations and how they will get to each place and give hotel reccomendations. Provide links for everything."
                                                         +"Make sure it is in html with each header to be with an <h1> tag and the rest with <p>!!! You will give a day to day schedule for each day."
                                                         +"Make sure you start with the days rather than introducing yourself. Then at the end show all the costs and the total spent"},
            {"role": "user", "content": plans},
        ])

    message = response.choices[0]['message']
    response = "{}: {}".format(message['role'], message['content'])[10:]
    if 'openai' in response:
        response = "Our systems either failed or detected inappropriate prompts, please try again"

    text_file = open("sample.txt", "w")
    n = text_file.write(response)
    text_file.close()

    return response


def convoBard(plans):
    response = bard.get_answer("You're itineraro, a travel planner for individuals and friends that can also accomodate for special needs. You will recieve a place,"
                                                          +" time, number of users, their interests, hobbiers, dietary restrictions, and specific requests. If they allergic ensure that places dont have cross contamination "
                                                           +"Ensure that all users will be satisfied and generate a comprehensive itinerary for these users for"
                                                           +" each day and be specific. If users want to be busy give their schedule lots to do and if they dont they make their schedule with much more time between activities. Ensure to include prices next to each reccomendation and put a final price at the bottom that satisfies the budget"
                                                            +"Divide into sections for each day with a header written with '**' on the outside of the title to make the characters bold and give them each their own correspionding emoji within the html next to the day that relates to the plans for that day."
                                                             +"make sure you mention their travel accomodations and how they will get to each place and give hotel reccomendations. Provide links for everything."
                                                             +"I want it in html with each header to be with an <h1> tag and the rest with <p>. You will give a day to day schedule for each day. I dont want it in HTML format but just with the titles within the <h1> tag with their respective emojis and the rest in <p> or <a> if they are links, no more html is required than that please."
                                                             +"For my personalized planner I want: "+plans)['content']
    if 'unable' in response or 'not able' in response or "can't" in response or "don't" in response:
        response = "Sorry, we weren't able to satisfy your request, please try again"
    return response