# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:59:38 2015

@author: Duda
"""

import random

sheldon_score= (0)
user_score=(0)

while sheldon_score < 3 and user_score<3:
            sheldon_choice= random.choice(["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"])
            user_choice=input("Qual opção deseja?\nPedra?\nPapel?\nTesoura?\nLagarto?\nSpock?\n")
            
            if user_choice == sheldon_choice:
                print("Empatou")
                print("Sheldon escolheu: ", sheldon_choice)
            
            if user_choice == "Pedra" and sheldon_choice == "Papel":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Papel cobre pedra!")
                print("Você perdeu!")
                sheldon_score +=1
                user_score = 0
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Pedra" and sheldon_choice == "Lagarto":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Pedra esmaga lagarto!")
                print("Você ganhou!")
                sheldon_score = 0
                user_score +=1
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Pedra" and sheldon_choice == "Spock":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Spock vaporiza pedra!")
                print("Você perdeu!")
                sheldon_score += 1
                user_score = 0
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Pedra" and sheldon_choice == "Tesoura":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Pedra quebra tesoura!")
                print("Você ganhou!")
                sheldon_score = 0
                user_score +=1
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
                
            if user_choice == "Lagarto" and sheldon_choice == "Spock":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Lagarto envenena Spock!")
                print("Você ganhou!")
                sheldon_score = 0
                user_score += 1
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Lagarto" and sheldon_choice == "Tesoura":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Tesoura decapita lagarto!")
                print("Você perdeu!")
                user_score = 0
                sheldon_score += 1
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Lagarto" and sheldon_choice == "Papel":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Lagarto come papel!")
                print("Você ganhou!")
                user_score += 1
                sheldon_score = 0
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Lagarto" and sheldon_choice == "Pedra":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Pedra esmaga lagarto!")
                print("Você perdeu!")
                user_score = 0
                sheldon_score +=1
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
        
            if user_choice == "Spock" and sheldon_choice == "Tesoura":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Spock esmaga tesoura!")
                print("Você ganhou!")
                user_score +=1
                sheldon_score = 0
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Spock" and sheldon_choice == "Papel":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Papel refuta Spock!")
                print("Você perdeu!")
                user_score = 0
                sheldon_score +=1
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Spock" and sheldon_score == "Pedra":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Spock vaporiza pedra!")
                print("Você ganhou!")
                user_score +=1
                sheldon_score = 0
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Spock" and sheldon_choice == "Lagarto":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Lagarto envenena Spock!")
                print("Você perdeu!")
                user_score = 0
                sheldon_score +=1
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            
            if user_choice == "Tesoura" and sheldon_choice == "Papel":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Tesoura corta papel!")
                print("Você ganhou!")
                user_score +=1
                sheldon_score=0
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Tesoura" and sheldon_choice == "Pedra":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Pedra quebra tesoura!")
                print("Você perdeu!")
                user_score = 0
                sheldon_score += 1
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Tesoura" and sheldon_choice == "Lagarto":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Tesoura decapita lagarto!")
                print("Você ganhou!")
                user_score+=1
                sheldon_score = 0
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Tesoura" and sheldon_choice == "Spock":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Spock esmaga tesoura!")
                print("Você perdeu!")
                user_score = 0
                sheldon_score +=1
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
                
            if user_choice == "Papel" and sheldon_choice== "Pedra":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Papel cobre pedra")
                print("Você ganhou!")
                user_score += 1
                sheldon_score = 0
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Papel" and sheldon_choice == "Lagarto":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Lagarto come papel!")
                print("Você perdeu!")
                user_score =0
                sheldon_score +=1
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Papel" and sheldon_choice == "Spock":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Papel refuta Spock!")
                print("Você ganhou!")
                user_score +=1
                sheldon_score = 0
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
            if user_choice == "Papel" and sheldon_choice == "Tesoura":
                print("Sheldon escolheu: ", sheldon_choice)
                print("Tesoura corta papel!")
                print("Você perdeu!")
                user_score = 0
                sheldon_score +=1
                print("Sua pontuação é: ", user_score)
                print("A pontuação de Sheldon é: ", sheldon_score)
        
if sheldon_score == 3:
    print("Bazinga! Sheldon ganhou!")
    
if user_score == 3:
    print("Parabéns! Você ganhou!")