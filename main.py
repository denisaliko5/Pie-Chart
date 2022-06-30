import turtle
t = turtle.Turtle()
while True:
  try:
    iter = int(input("Enter the number of people completing the questionnaire: "))
  except ValueError as VE:
    print(VE)
  if type(iter) == int:
    break
print("\nWhich is your favourite fruit?\n\na) Avocado\nb) Coconut\nc) Mango\nd) Pineapple")
ans_a_nr = 0
ans_b_nr = 0
ans_c_nr = 0
ans_d_nr = 0
i = 0
while i < iter:
  ans = input("Enter the letter: ")
  if ans == "a" :
    ans_a_nr += 1
  elif ans == "b":
    ans_b_nr += 1
  elif ans == "c":
    ans_c_nr += 1
  elif ans == "d":
    ans_d_nr += 1
  else:
    print("Invalid Input!")
    i -= 1
  i += 1
ang_a = ans_a_nr*360/iter
ang_b = ans_b_nr*360/iter
ang_c = ans_c_nr*360/iter
ang_d = ans_d_nr*360/iter
perc_a = round(ang_a/3.6, 1)#perc -> percentage
perc_b = round(ang_b/3.6, 1)
perc_c = round(ang_c/3.6, 1)
perc_d = round(ang_d/3.6, 1)
r = 100
p = r-20
t.speed(0)
t.ht()
t.fd(100)
t.lt(90)
for e in [["#568203", ang_a],["#79513E", ang_b],["#ff8d40", ang_c],["#fee332", ang_d]]:
  if e[1] != 0:
    t.color(e[0])
    t.begin_fill()
    t.circle(100, e[1])
    t.lt(90)
    t.fd(100)
    t.lt(180-e[1])
    t.fd(100)
    t.lt(90)
    t.end_fill()
    t.circle(100, e[1])
t.shape("square")
t.pu()
t.goto(r*1.5, p)
t.pd()
for e in [["#568203", "Avocado: ", perc_a],["#79513E", "Coconut: ", perc_b],["#ff8d40", "Mango: ", perc_c],["#fee332", "Pineapple: ", perc_d]]:
  t.color(e[0])
  t.stamp()
  t.pu()
  t.goto(r*1.5+30, p-10)
  t.pd()
  t.write(str(e[1]) + str(e[2]) + "%", font=("Segoe UI", 12, "bold"))
  p -= 30
  t.pu()
  t.goto(r*1.5, p)
  t.pd()