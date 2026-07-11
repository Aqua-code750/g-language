import game

say "Starting Catch the Square game!"

game.init_window(800, 600, "Catch the Square!")

# Player Position
set px to 400
set py to 500
set p_speed to 8

# Falling Square Position
set tx to 400
set ty to 0
set t_speed to 5

set score to 0

while game.is_running() is 1 do
    # Player Input
    if game.get_key("left") is 1 then set px to px - p_speed end
    if game.get_key("right") is 1 then set px to px + p_speed end

    # Boundaries for player
    if px < 0 then set px to 0 end
    if px > 750 then set px to 750 end

    # Update Target (Falling square)
    set ty to ty + t_speed

    # Check collision (simple bounding box logic)
    set hit to 0
    if ty > 450 then
        if ty < 550 then
            # target is at player's y level. Check X
            if tx + 50 > px then
                if tx < px + 50 then
                    set hit to 1
                end
            end
        end
    end

    if hit is 1 then
        set score to score + 1
        say "Score: " + str(score)
        
        # Reset target
        set ty to 0
        
        # Pseudo-random horizontal placement based on score
        set tx to 100 + (score * 150)
        
        # Wrap tx if it gets too large
        while tx > 700 do
            set tx to tx - 600
        end
        
        # increase speed slightly
        set t_speed to t_speed + 1
    end

    # Check miss
    if ty > 600 then
        say "You missed! Final Score: " + str(score)
        # Reset game
        set ty to 0
        set tx to 400
        set score to 0
        set t_speed to 5
    end

    # Render
    game.fill(20, 20, 40) 
    
    # Draw Target (Red Square)
    game.draw_rect(255, 50, 50, tx, ty, 50, 50)

    # Draw Player (Green Square)
    game.draw_rect(0, 255, 0, px, py, 50, 50)
    
    game.update()
end

say "Game Closed."
