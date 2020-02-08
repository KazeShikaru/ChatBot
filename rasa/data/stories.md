## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## greet with name
  * greet{"user": "name"}
  - utter_greet

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## Sales Path 1
* greet
   - utter_greet
* desire_potato
   - utter_potato_fact
   - utter_sale_pitch

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## interactive_story_1
* greet
    - utter_greet
* learn_bot
    - persona_response

## interactive_story_1
* greet
    - utter_greet
* learn_nature{"subject": "potatoes"}
    - utter_potato_fact
    - utter_sale_pitch
* affirm
    - utter_complete_sale
