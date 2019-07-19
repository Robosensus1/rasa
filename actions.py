# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)


class ActionAIBenefits(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_ai_benefits"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        #joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message("•Machines don't need breaks like humans.\n\n" +
		                         "•They do repetitive jobs without any complaints.\n\n" +
								 "•Helps us in reducing the error and increases the chance of reaching accuracy.\n\n" +
								 "•specially known for multitasking.\n\n" +
								 "•can use in daily applications and also as digital assistants. ")
        return []
		
		
class ActionAIToCompany(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_ai_to_company"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        #joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message("•use chatbots in any customer service.\n\n" +
		                         "•customize the user preferences while providing services.\n\n" +
								 "•Turn to AI to improve your security.\n\n" +
								 "•Get an AI expert help.\n\n" +
								 "•read and research about AI solutions to your business ")
        return []
		
		
class ActionAIBenefits(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_ai_benefits"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        #joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message("•Machines don't need breaks like humans.\n\n" +
		                         "•They do repetitive jobs without any complaints.\n\n" +
								 "•Helps us in reducing the error and increases the chance of reaching accuracy.\n\n" +
								 "•specially known for multitasking.\n\n" +
								 "•can use in daily applications and also as digital assistants. ")
        return []
		
		
class ActionChatbotUses(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_chatbot_uses"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        #joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message("•chatbots are being able to reach a broad audience on messenger apps, as well as the ability to automate personalized messages.\n\n" +
		                         "•They can also improve efficiency by taking over tasks for which humans are not essential and also for 24/7 .\n\n" +
								 "•The purpose of chatbots is to support and scale business teams in their relations with customers. By doing this, it can help businesses to save a lot of money and time. ")
        return []
		
		
class ActionEnd(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_end"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        #joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message("Thanks for knowing the information about RoboSensus")
        return []
		
		
class ActionLocation(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_location"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        #joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message("Plot No 910 - E, Road no - 46, Near Ambedkar Open University Back Gate,\n\n" +
		                         "Plot TA No 173 of the Jubilee Hills, Co-Operative House Building Society Ltd,\n\n" +  
								 "Beside Durgam Cheruvu Entrance, Masthan Nagar, CBI Colony, Jubilee Hills ,\n\n" +
								 "Hyderabad, Telangana 500033, India. ")
        return [] 
		
		
class ActionBye(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_bye"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        #joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message("Have a nice time")
        return []
		
		
class ActionMeetings(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_meetings"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        #joke = request['value']  # extract a joke from returned json response
        message = tracker.latest_message.get('text')
        dispatcher.utter_message(message)
        dispatcher.utter_message("Please drop an  email {}  to contact@robosensus.com". format(message))
        return []
		
		
class ActionServices(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_services"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        #joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message("•Machines can interact with customers like humans.This helps in elimination repetitive and mundane tasks.\n\n" +
		                         "•We can get to know more about the customer and their profile information.\n\n" +
								 "•We can provide information by adding data visualizations where needed. This can help in taking strategic business decision during the meeting with the Business stakeholders.\n\n" +
								 "•We can perform various actions similar to computer tasks.\n\n" +
								 "•We can extract users interest and emotions through conversations and take appropriate actions to improve business and customer satisfaction.")
        return []
		
		
class ActionBlockchain(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_blockchain"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        #joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message("A blockchain is a digitized, decentralized, public ledger of all cryptocurrency transactions, and here ledger is nothing but record of all transactions.\n\n" +
		                         "Blockchain keeps a record of all transactions, every verified transaction is added to the ledger as a block. It utilizes a distributed system to verify each transaction. ")
        return []
		
		
class ActionWelcome(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_welcome"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        #request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        #joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message("Welcome To Robosensus,")
        dispatcher.utter_message("How can I help you?")
        return []
		
		

		
		

		
	
		
		
		
		
		
		
