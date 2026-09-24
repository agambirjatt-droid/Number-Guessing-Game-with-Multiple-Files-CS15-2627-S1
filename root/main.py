import utils
import score

secret_number = utils.generate_secret_number()
player_score = 100
# you start at 100,and lose 10 points if its incorrect.

while True:
    if utils.check_user_guess(secret_number):
        print(f"Your final score :{player_score}")
        print(f"Rating: {score.get_rating(player_score)}")
        break
# if its correct, you get a rating and final score, if not you go to else where they give you a penalty for getting it incorrect.
    else:
        player_score = score.update_score(player_score)
# imports utils and sets the secret number to whatever number the generator makes.