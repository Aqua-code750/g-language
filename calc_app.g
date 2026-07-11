say "=========================="
say "   ADVANCED G CALCULATOR  "
say "=========================="

define add(a, b) do
    return a + b
end

define subtract(a, b) do
    return a - b
end

define multiply(a, b) do
    return a * b
end

define divide(a, b) do
    if b is 0 then
        say "Error: Division by zero!"
        return 0
    else
        return a / b
    end
end

set running to 1

while running is 1 do
    say ""
    say "Options:"
    say "1. Add"
    say "2. Subtract"
    say "3. Multiply"
    say "4. Divide"
    say "5. History"
    say "6. Exit"
    
    set choice to input("Select an option (1-6): ")
    
    if choice is "6" then
        say "Goodbye!"
        set running to 0
    else
        if choice is "5" then
            say "Reading history..."
            read "calc_history.txt" into history
            say history
        else
            set num1 to int(input("Enter first number: "))
            set num2 to int(input("Enter second number: "))
            set res to 0
            
            if choice is "1" then
                set res to add(num1, num2)
            end
            if choice is "2" then
                set res to subtract(num1, num2)
            end
            if choice is "3" then
                set res to multiply(num1, num2)
            end
            if choice is "4" then
                set res to divide(num1, num2)
            end
            
            say "Result: " + str(res)
            
            # Save to history
            read "calc_history.txt" into old_history
            set new_history to old_history + str(num1) + " op " + str(num2) + " = " + str(res) + "  |  "
            write new_history to "calc_history.txt"
        end
    end
end
