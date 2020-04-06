
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
    - utter_enjoy_equal

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

## rasputin path
* rasputin
    - utter_speak_rasputin

## 30 long path
* greet
  - utter_greet
* question_state
  - utter_state
* question_favorite_color
  - utter_favorite_color
* question_bot_purpose
  - utter_purpose
* question_potato_stock
  - utter_stock
* question_best_potato
  - utter_user_needs
* inform_user_needs
  - action_decide
* question_price
  - utter_potato_price
* barter_price
  - utter_denial
* barter_price
  - utter_new_price
* affirm
  - utter_complete_sale
  - utter_additional_request_check
* affirm
  - utter_question_intent
* question_functions
  - utter_functions
* question_flower_event_death
  - utter_flower_death
* question_flower_event_wedding
  - utter_flower_wedding
* goodbye
  - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* question_state
    - utter_state
* question_favorite_color
    - utter_favorite_color
* question_bot_purpose
    - utter_purpose
* question_potato_stock
    - utter_stock
* question_best_potato
    - utter_user_needs
* inform_user_needs
    - action_decide
* question_price
    - utter_potato_price
* barter_price
    - utter_denial
* barter_price
    - utter_new_price
* affirm
    - utter_complete_sale
    - utter_additional_request_check
* question_functions
    - utter_functions
* question_flower_event_death
    - utter_flower_death
* question_flower_event_wedding
    - utter_flower_wedding
* goodbye

## interactive_story_1
* question_best_potato{"subject": "potato"}
    - utter_user_needs
* inform_user_needs
    - action_decide

## interactive_story_1
* question_state
    - utter_state
* question_potato_stock
    - utter_stock
* question_favorite_potato
    - utter_favorite_potato
* unsatisfied_answer
    - utter_appology

## interactive_story_1
* rasputin
    - utter_speak_rasputin
* question_potato_stock
    - utter_stock
* question_best_potato
    - utter_favorite_potato
* learn_bot
    - utter_favorite_color
* mood_unhappy{"subject": "sad"}
    - utter_cheer_up
    - utter_did_that_help
* mood_great
    - utter_happy
* ask_philosophy
    - utter_philosophy
* inform_user_needs
    - utter_question_intent
* learn_nature
    - utter_potato_fact
* learn_nature
    - utter_potato_fact
* bot_challenge
    - utter_appology
* mood_unhappy
    - utter_state
* desire_potato{"subject": "potato"}
    - utter_potato_price
* barter_price
    - utter_adjusted_pitch
    - utter_new_price
* barter_price
    - utter_adjusted_pitch
* affirm{"subject": "Ok"}
    - utter_complete_sale
* affirm
    - utter_additional_request_check
* deny
    - utter_goodbye
* goodbye
    - /back
* stop

## interactive_story_1
* greet
    - utter_greet
* question_state
    - utter_state
* question_potato_stock
    - utter_stock
* barter_price
    - utter_potato_price
* show_product_interest
    - utter_complete_sale
* rasputin
    - utter_speak_rasputin
* goodbye
    - utter_goodbye
* stop
    - utter_greet
* stop

## interactive_story_1
* greet
    - utter_greet
* learn_bot{"trait": "colour"}
    - utter_enjoy_equal

## interactive_story_1
* greet
    - utter_greet
* question_best_potato
    - utter_favorite_potato
* learn_bot
    - utter_favorite_color
* mood_great
    - utter_iamabot
* greet{"name": "Will"}
    - utter_greet
* learn_bot
    - utter_stock

## interactive_story_2
* greet
    - utter_greet
* state_name{"name": "Will"}
    - utter_greet

## interactive_story_1
* greet{"user": "will"}
    - slot{"user": "will"}
    - utter_greet
* learn_bot
    - utter_iamabot
* ask_philosophy{"subject": "life"}
    - utter_philosophy
* affirm
    - utter_sale_pitch
* deny{"subject": "potatoes"}
    - utter_adjusted_product
* deny
    - utter_adjusted_price
* learn_bot
    - utter_functions
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* question_current_bot_action
    - utter_greet
    - utter_current_bot_action
* question_current_bot_action
    - utter_current_bot_action
* question_weather
    - utter_optimism

## interactive_story_1
* greet
    - utter_greet
* learn_bot
    - utter_enjoy_equal
* question_bot_purpose
    - utter_purpose
* show_product_interest
    - utter_sale_pitch
* affirm
    - utter_user_needs
* inform_user_needs
    - action_decide
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* learn_bot{"subject": "music"}
    - utter_purpose
* affirm
    - utter_sale_pitch
* show_product_interest
    - utter_complete_sale
* ask_philosophy
    - utter_philosophy
* ask_philosophy
    - utter_what_potato
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet


## interactive_story_1
* question_flower{"sentiment": "love"}
    - action_flower_recommendation
* question_flower{"sentiment": "death"}
    - action_flower_recommendation

## interactive_story_1
* question_flower{"sentiment": "hatred"}
    - action_flower_recommendation

## interactive_story_1
* question_flower{"sentiment": "death"}
    - action_flower_recommendation

## interactive_story_1
* question_flower{"sentiment": "love"}
    - action_flower_recommendation

## interactive_story_1
* question_flower
    - action_flower_recommendation

## interactive_story_1
* question_flower
    - action_flower_recommendation
* question_flower
    - action_flower_recommendation

## interactive_story_1
* question_music
    - action_music_recommendation
## interactive_story_1
* question_music{"sentiment": "chill"}
    - action_music_recommendation

## interactive_story_1
* question_music{"sentiment": "chill"}
    - action_music_recommendation

## interactive_story_1
* question_music{"sentiment": "chill"}
    - action_music_recommendation
* question_music
    - action_music_recommendation
* question_music{"sentiment": "happy"}
    - action_music_recommendation
* question_music{"sentiment": "rainy"}
    - action_music_recommendation
* question_music{"sentiment": "rainy"}
    - action_music_recommendation

## interactive_story_1
* question_music
    - action_music_recommendation
* question_music{"sentiment": "sad"}
    - action_music_recommendation

## interactive_story_2
* question_music{"sentiment": "sad"}
    - action_music_recommendation

## interactive_story_1
* question_music{"sentiment": "bittersweet"}
    - action_music_recommendation
* question_music{"sentiment": "lonely"}
    - action_music_recommendation
