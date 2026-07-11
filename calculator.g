say "====================="
say "    G CALCULATOR     "
say "====================="

set running to 1

while running is 1 do
    say ""
    say "1. Add"
    say "2. Subtract"
    say "3. Multiply"
    say "4. Divide"
    say "5. Exit"
    
    set choice to input("Select an option (1-5): ")
    
    if choice is "5" then
        say "Goodbye!"
        set running to 0
    else
        set num1 to int(input("Enter first number: "))
        set num2 to int(input("Enter second number: "))
        
        if choice is "1" then
            set res to num1 + num2
            say "Result: " + str(res)
        end
        if choice is "2" then
            set res to num1 - num2
            say "Result: " + str(res)
        end
        if choice is "3" then
            set res to num1 * num2
            say "Result: " + str(res)
        end
        if choice is "4" then
            if num2 is 0 then
                say "Error: Division by zero!"
            else
                set res to num1 / num2
                say "Result: " + str(res)
            end
        end
    end
end
