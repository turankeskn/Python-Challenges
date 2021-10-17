
# Kata = https://www.codewars.com/kata/569651a2d6a620b72e000059



def result(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    
    print(p1)
    print(p2)
    
    dict = {
        "rock":["scissor", "lizard"],
        "scissor":["paper", "lizard"],
        "paper":["rock", "spock"],
        "lizard":["paper", "spock"],
        "spock":["scissor", "rock"]
    }

    if p1 not in dict or p2 not in dict:
        return "Oh, Unknown Thing"
    if p1 == p2:
        return "Draw!"
    
    targets = dict[p1]
    if p2 in targets:
        return "Player 1 won!"
    else:
        return "Player 2 won!"