from dice import start, game, winners

igrok1, igrok2, rounds = start()

score1, score2, wins1, wins2 = game(igrok1, igrok2, rounds)

winners(score1, score2, wins1, wins2, igrok1, igrok2)
