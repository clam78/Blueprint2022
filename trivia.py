#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 20:25:16 2022

@author: clairemao
"""

def trivia():
  trivia_points = 0
  print("Take a break and play some trivia! Please input answer as A, B, C, or D. Enjoy!")
  import random
  from random import randint
  questions = ["What is the capital of China? A) Beijing B) Shanghai C) Guangzhou D) Suzhou  ", "Who was Barack Obama's Vice President? A) Hillary Clinton B) Mitt Romney C) Joe Biden D) Paul Ryan  ", "What color is the Hulk? A) yellow B) green C) red D) rainbow  ", "How many languages are written from right to left? A) 11 B) 12 C) 13 D) 14  ", "What planet is closest to the Sun? A) Venus B) Neptune C) Mars D) Mercury  ", "Who was the first woman to win a Nobel Prize? A) Jane Addams B) Bertha von Suttner C) Marie Curie D) Grazia Deledda   ", "What's the rarest M&M color? A) brown B) orange C) purple D) green  ", "What was the first soft drink in space? A) Sprite B) root beer C) Fanta D) Coca Cola  ", "Which country hasn't missed any Olympics? A) USA B) Italy C) Australia D) France  ", "What US state is Area 51 in? A) California B) Nevada C) Arizona D) New Mexico  ", "How many hearts does an octopus have? A) 3 B) 5 C) 4 D) 6  ", "What country has a unicorn as its national animal? A) Ireland B) Switzerland C) New Zealand D) Scotland  ", "What is the hottest planet in the solar system? A) Mars B) Mercury C) Venus D) Jupiter  ", "Who invented the word 'vomit'? A) Emily Dickinson B) William Shakespeare C) Lord Byron D) Me  ", "Who painted 'Girl with a Pearl Earring'? A) Johannes Vermeer B) Edgar Degas C) Jan van Goyen D) Beyonce  "]
  correct_answers = ["A", "C", "B", "B", "D", "C", "A", "D", "C", "B", "A", "D", "C", "B", "A"]

  x=5
  used_questions=[]
  while x>0:
    i = randint(0, 14)
    if i in used_questions:
      i = randint(0, 14)
    used_questions.append(i)
    random_question = questions[i]
    answer = input(random_question)
  
    if answer != correct_answers[i]:
      print("Sorry, incorrect! The correct answer is ", correct_answers[i])
      print("Total points = ", trivia_points)

    else:
      print("Correct! +1 point.")
      trivia_points +=1
      print("Total points = ", trivia_points)
    x-=1

  print("Thanks for playing!")

