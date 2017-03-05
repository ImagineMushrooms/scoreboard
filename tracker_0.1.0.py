#!/usr/bin/python
import numpy as np
import csv
print "Score tracker"
player = "Player 1"
player = raw_input("Enter player name: ")
score = 50
endgame=0
n = 1
while endgame == 0:
    print "Turn ", str(n), "Score: ", str(score)
    input111 = 0
    while input111 ==0:
        delta_score = raw_input("Change in score: ")
        if "q" in delta_score:
            endgame = 1
            input111 = 1
        try:
            int(delta_score)
            delta_score = int(delta_score)
            score = score + delta_score
            print "end of turn ", str(n)
            #print "score: ", str(score)
            n = n+1
            if score < 1:
                endgame = 1
            input111 = 1
        except:
            pass
lose = 0
if score < 1:
    lose = 1
    print player, "loses, final score: ", str(score)
if lose == 0:
    print "end of game, final score: ", str(score)
