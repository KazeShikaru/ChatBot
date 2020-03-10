## rasputin
* rasputin
  - utter_rasputin

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

## barter potato
* greet{"user": "name"}
   - utter_greet
* learn_nature{"subject": "potatoes"}
   - utter_potato_fact
* show_product_interest
   - utter_sale_pitch
* barter_price
   - utter_adjusted_pitch
* affirm
   - utter_complete_sale

## greet and learn
* greet
    - utter_greet
* learn_bot
    - persona_response

## greet learn and buy
* greet
    - utter_greet
* learn_nature{"subject": "potatoes"}
    - utter_potato_fact
    - utter_sale_pitch
* affirm
    - utter_complete_sale

## greet, learn, show interet, barter, buy
* greet{"user": "Kevin"}
    - slot{"user": "Kevin"}
    - utter_greet
* learn_nature{"subject": "potato"}
    - utter_potato_fact
* show_product_interest
    - utter_sale_pitch
* barter_price
    - utter_adjusted_pitch
* show_product_interest
    - utter_complete_sale

## greet, learn, barter, buy
* greet{"user": "Lord_Johnathan"}
    - slot{"user": "Lord_Johnathan"}
    - utter_greet
* learn_nature{"subject": "potatoes"}
    - utter_potato_fact
    - utter_sale_pitch
* barter_price
    - utter_adjusted_pitch
* affirm
    - utter_complete_sale

## greet back
* greet
    - utter_greet

## learn future
* learn_future
    - utter_philosophy
    
## goodbye
* goodbye
    - utter_goodbye
