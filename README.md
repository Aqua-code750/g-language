# G Language

Welcome to **G**, a powerful, easy-to-learn programming language that evolved from a simple script runner into a full-fledged ecosystem! Built from the ground up, G is designed to be highly readable while offering powerful capabilities for everything from CLI tools to GUI applications and 2D games.

## 🚀 Features

* **Readable Syntax**: Intuitive, English-like syntax using keywords like `set`, `say`, and `listen`.
* **Native GUI Apps**: Built-in support for desktop applications via the `app` module (powered by CustomTkinter).
* **Native 2D Games**: Create games effortlessly using the `game` module (powered by Pygame).
* **Standalone Executable**: Run G scripts anywhere using the compiled `g.exe` binary.
* **VS Code Integration**: A dedicated VS Code extension for full syntax highlighting.

## 🛠️ Installation & Setup

1. **Download the binary**: Download `g.exe` from the [Releases](https://github.com/Aqua-code750/g-language/releases) tab.
2. **Add to PATH**: Place `g.exe` in a directory and add it to your system's PATH, or set up a PowerShell alias:
   ```powershell
   Add-Content -Path $PROFILE -Value 'Set-Alias -Name g -Value "C:\path\to\your\g.exe"'
   ```
3. **Install the VS Code Extension**: Download the `g-language-1.1.0.vsix` file from the releases and install it in VS Code to get syntax highlighting for `.g` files!

## 📖 Syntax Quickstart

Here are a few quick examples of what G code looks like.

### Hello World & Variables
```ruby
say "Hello, World!"
set name to "Developer"
say "Welcome, " + name
```

### User Input & Logic
```ruby
say "What is your age?"
listen age
if int(age) > 18 then
    say "You are an adult!"
else
    say "You are young!"
end
```

### Loops
```ruby
set counter to 0
while counter < 5 do
    say counter
    set counter to counter + 1
end
```

## 🎨 Building Apps

G makes it incredibly simple to build beautiful, modern GUI applications using the `app` module:

```ruby
import app

app.init_window(400, 300, "My G App")
app.add_label("Welcome to G Apps!", 100, 50)
app.add_button("Click Me!", "on_click", 150, 150)

function on_click() do
    say "The button was clicked!"
end

app.run()
```

## 🎮 Building Games

You can even build interactive 2D games using the `game` module!

```ruby
import game
game.init_window(800, 600, "My Game")

set px to 400
set py to 300

while game.is_running() is 1 do
    if game.get_key("left") is 1 then set px to px - 5 end
    if game.get_key("right") is 1 then set px to px + 5 end
    
    game.fill(20, 20, 40) 
    game.draw_rect(0, 255, 0, px, py, 50, 50)
    game.update()
end
```

## 🏗️ Building the Source

If you want to contribute or build `g.exe` from source:
1. Ensure you have Python 3.12+ installed.
2. Install dependencies (e.g. pygame, customtkinter, pyinstaller).
3. Run the automated build script:
   ```powershell
   ./update_release.ps1
   ```
   This will compile the interpreter into `dist/g.exe`, package the VS Code extension, and prepare a GitHub release.

## 🌟 Evolution

G started as a simple concept (codenamed *holo-constrictor*) and has been continuously upgraded into the robust ecosystem it is today!

---
*Happy coding in G!*
