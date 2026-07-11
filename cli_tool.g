say "================================="
say "   Welcome to the Math Master    "
say "================================="

set score to 0

set name to input("What is your name? ")
say "Hello " + name + "! Let's play a game."

say ""
say "Question 1: What is 5 * 12?"
set ans to input("Answer: ")

if ans is "60" then
    say "Correct!"
    set score to score + 1
else
    say "Wrong! It was 60."
end

say ""
say "Question 2: What is 100 / 4?"
set ans to input("Answer: ")

if ans is "25" then
    say "Correct!"
    set score to score + 1
else
    say "Wrong! It was 25."
end

say ""
say "================================="
say "Game Over! You scored " + str(score) + " points."

if score is 2 then
    say "You are a Math Master!"
else
    say "Better luck next time!"
end
