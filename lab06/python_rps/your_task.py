def hello_world():
    return "Hello world!"


def rps(hand1, hand2):
    # finish this code:
    if hand1 == "rock" and hand2 == "paper" or hand1 == "paper" and hand2 == "rock":
        return "Paper wins!"
    if hand1 == "paper" and hand2 == "scissor" or hand1 == "scissor" and hand2 == "paper":
    
        return "Scissor wins!"
    if hand1 == "scissor" and hand2 == "rock" or hand1 == "rock" and hand2 == "scissor":
        return "Rock wins!"
    if hand1 == hand2:
        return "Tie!"
    else:
        return "Invalid"
