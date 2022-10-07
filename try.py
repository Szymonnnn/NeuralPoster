from gpt import Ask
ask = Ask()
text_for_gpt = "tell me something about this: CHAMPIONSHIP SUNDAY #VforVictory https://t.co/JK5cQPzivR/nRT @itachi_rl: CHAMPIONSHIP SUNDAY #RLCS #KCORP https://t.co/MnLz4ANQfZ/nRT @nidcom_gov: Israel Adesanya @stylebender beats Jared Cannonier to retain UFC Middleweight Championship! 🏆 #UFC276 on Sunday, July 3, 20…/nChampionship Sunday POGGERS #RLCS/nRT @Eversax: Si on m’avait dit il y a 3 mois qu’on allait jouer le championship Sunday durant un major j’aurais eu du mal à y croire. Ça va…"
description = ask.ask(text_for_gpt, 50, 0.9)
#print("Opis: " + description)
description = description.replace("\n", " ")
print("Opis: " + description)
#print("Dlugosc stringa: " + str(len(description + " #" + hasztag)) + " - max 280")