# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:29:55 2024

@author: pjpet
"""

import items

#Data for the game store

gtaVxbox = items.XboxGame("Grand Theft Auto V (xbox)",59.99,40)
haloCollection = items.XboxGame("Halo: The Master Chief Collection",69.99,40)
halo = items.XboxGame("Halo Infinite",39.99,40)
minecraft = items.XboxGame("Minecraft",24.99,40)
forza5 = items.XboxGame("Forza Horizon 5",49.99,40)
rocket = items.XboxGame("Rocket League",24.99,40)
forza4 = items.XboxGame("Forza Horizon 4",29.99,40)
redDead = items.XboxGame("Red Dead Redemption 2",24.99,40)
sea = items.XboxGame("Sea of Thieves",29.99,40)
fallout = items.XboxGame("Fallout 4",49.99,40)
siege = items.XboxGame("Tom Clancy's Rainbow Six Siege",24.99,40)

godOfWar = items.SonyGame("God of War",44.99,40)
horizon = items.SonyGame("Horizon Zero Dawn",39.99,40)
gtaVsony = items.SonyGame("Grand Theft Auto V (PS4)",44.99,40)
spider = items.SonyGame("Marvel's Spider-Man",29.99,40)
uncharted = items.SonyGame("Uncharted 4: A Thief's End",24.99,40)
infamous = items.SonyGame("inFAMOUS Second Son",29.99,40)
cod = items.SonyGame("Call of Duty: Black Ops III",24.99,40)
lastOfUs = items.SonyGame("The Last of Us Remastered",39.99,40)
ratchNclank = items.SonyGame("Ratchet & Clank",44.99,40)
batman = items.SonyGame("Batman: Arkham Knight",19.99,40)
destiny = items.SonyGame("Destiny",29.99,40)

counterStrike = items.SteamGame("Counter-Strike",39.99,40)
teamFortress = items.SteamGame("Team Fortress Classic",29.99,40)
dayOfDefeat = items.SteamGame("Day of Defeat",29.99,40)
deathmatch = items.SteamGame("Deathmatch Classic",24.99,40)
halfLifeOF = items.SteamGame("Half-Life: Opposing Force",39.99,40)
ricochet = items.SteamGame("Ricochet",29.99,40)
halfLife = items.SteamGame("Half-Life",49.99,40)
counterStrikeCZ = items.SteamGame("Counter-Strike: Condition Zero",24.99,40)
halfLifeBS = items.SteamGame("Half-Life: Blue Shift",39.99,40)
halfLife2 = items.SteamGame("Half-Life 2",24.99,40)


pokemonLeg = items.NintendoGame("Pokémon Legends Z-A",49.99,40)
paperMario = items.NintendoGame("Paper Mario: The Thousand-Year Door",29.99,40)
endlessOcean = items.NintendoGame("Endless Ocean Luminous ",24.99,40)
prinPeach = items.NintendoGame("Princess Peach Showtime!",39.99,40)
marioVDonk = items.NintendoGame("Mario vs. Donkey Kong",29.99,40)
recollection = items.NintendoGame("Another Code: Recollection",49.99,40)
superMarioRPG = items.NintendoGame("Super Mario RPG",24.99,40)
warioWare = items.NintendoGame("WarioWare: Move It!",39.99,40)
superMarioBros = items.NintendoGame("Super Mario Bros. Wonder",24.99,40)
detPik = items.NintendoGame("Detective Pikachu Returns",29.99,40)

allGamesList = [counterStrike,teamFortress,dayOfDefeat,deathmatch,halfLifeOF,ricochet,
                halfLife,counterStrikeCZ,halfLifeBS,halfLife2,pokemonLeg,paperMario,endlessOcean,
                prinPeach,marioVDonk,recollection,superMarioRPG,warioWare,superMarioBros,
                detPik,gtaVxbox,haloCollection,halo,minecraft,forza5,rocket,forza4,redDead,
                sea,fallout,siege,godOfWar,horizon,gtaVsony,spider,uncharted,infamous,
                cod,lastOfUs,ratchNclank,batman,destiny]
