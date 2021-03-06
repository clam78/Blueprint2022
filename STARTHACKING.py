#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 17:29:13 2022

@author: clairemao
"""

from datetime import date
from threading import Thread
import time
import datetime


def strike(text):
    i = 0
    new_text = ''
    while i < len(text):
        new_text = new_text + (text[i] + u'\u0336')
        i = i + 1
    return(new_text)

class assignment:
  def __init__(self, name, due_date, course_in):
    self.name = name
    self.checked = False
    self.due_date = due_date
    self.course_in = course_in
    self.on_time = None


  def on_time(due_date):
    #next line checks if was done by due date
    if date(due_date) < date.today():
        return True
    else:
        return False

  def check_off_list(self):
    self.checked = True
    if self.on_time(due_date):
      self.on_time = True
      #self = strike(self)  
    else:
      self.on_time = False
      #self = strike(self)
      
  def uncheck_item(self):
    self.checked = False
    #next line figure out how to unstrikethrough something
    #self.assignments[item]=



class course:
  def __init__(self, course_name):
    self.course_name = course_name
    self.assignments = []
    self.uncompleted_assignments = []
    self.completed_assignments = []
  
  def add_item(self, item):
    self.assignments.append(item)
    self.uncompleted_assignments.append(item)
    self.checked = False
    self.by_due_date = None
  

  def complete_item(self, item):
    self.completed_assignments.append(item)
    self.uncompleted_assignments.remove(item)


  def uncomplete_item(self, item):
    self.uncompleted_assignments.append(item)
    self.completed_assignments.remove(item)
  

  def view_to_dos(self):
      print(course.assignments_under_course)

  


courses = []
all_assignments=[]
all_completed_assignemnts = []
all_uncompleted_assignments = []



def add_course():
  new_course = course(input("What course would you like to add?   "))
  courses.append(new_course)

def add_assignment():
  new_assignment = assignment(input("What is the assignment?   "), input("What is the due date for this assignment? yyyy/mm/dd?   "), input("What course is this under?  " ))
  if (new_assignment.course_in in courses):
    for course in courses:
      if new_assignment.course_in == course.course_name:
        course.add_item(new_assignment)
        break
  '''else:
    courses.append(new_assignment.course_in)
    print(new_assignment.course_in)
    print(new_assignment)
    (new_assignment.course_in).add_item(new_assignment)'''
  
  all_assignments.append(new_assignment)
  all_uncompleted_assignments.append(new_assignment)


def check_item(item):
  course.complete_item(item.course_in, item)
  item.check_off_list()
  all_uncompleted_assignments.remove(item)
  all_completed_assignments.append(item)
  if item.on_time == True:
    print("Nice work completing this assignment on time! Here are your upcoming assignments: ", uncompleted_assignments)  
  if item.on_time == False:
    print("Looks like the due date has passed! Good job completing the assignment anyway.")

def uncheck_item(item):
  course.uncomplete_item(item.course_in)
  item.uncheck_item(item)
  all_uncompleted_assignments.append(item)
  

def view_all():
  print(all_assignments)

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








print("Hi user! Let's begin.")
while 0 == 0:
  def eventadder(due_date, assignment):
    
    due_year, due_month, due_day = due_date.split("/")

    new_thread = Thread(target=Timeleft, args=[
                        due_day, due_month, due_year, assignment])
    new_thread.start()


    
  def Timeleft(due_day, due_month, due_year, subject):
    init_clock = datetime.datetime.now()
    init_year = init_clock.strftime("%Y")
    init_month = init_clock.strftime("%m")
    init_day = init_clock.strftime("%d")

    init_date = datetime.date(int(init_year),   int(init_month), int(init_day))

    final_date = datetime.date(int(due_year), int(due_month), int(due_day))

    timeleft = final_date - init_date
    daysleft = int(timeleft.days)

    while daysleft > 1:
        clock = datetime.datetime.now()
        date = clock.date()
        # print(date)
        if(date == init_date):
            # time.sleep(246060-int(init_hour))
            time.sleep(3)
            daysleft = daysleft - 1
        else:
            time.sleep(24*60*60)
            daysleft = daysleft - 1

    print("one day left until " + subject + "!!!")
  
  for i in all_uncompleted_assignments:
    eventadder(i.due_date, i.name)
    
  
  
  
  current_input = None
  next_action = input("""What is your desired next action? The choices are 
  A. Add course
  B. Add Assignment
  C. Check Assignment off to-do list
  D. Uncheck a checked assignment
  E. Play a game of trivia!
  Please enter a letter.    """)

  if next_action == "A":
    add_course()
  if next_action == "B":
    add_assignment()
  if next_action == "C":
    uncheck_item(input("Which item would you like to check off? "))
  if next_action == "D":
    print("Here are all of you checked items: ", all_completed_assignments)
    uncheck_item(input("Which item would you like to uncheck?  "))
  if next_action == "E":
    trivia()
    