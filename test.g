import game

say "Starting game module test..."
game.init_window(800, 600, "My G Game")

while game.is_running() do
    game.fill(50, 50, 150)
    game.update()
end

say "Game closed"
