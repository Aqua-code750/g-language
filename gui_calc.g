import app

say "Initializing GUI Calculator..."

# Global State
set display to "0"
set current_val to 0
set op to ""

app.init_window(350, 450, "G Calculator")

# Row 0 - Display
app.add_label("display", display, 0, 0, 4)

# Button Handlers
define btn_1() do
    if display is "0" then set display to "1" else set display to str(display) + "1" end
    app.set_label("display", display)
end

define btn_2() do
    if display is "0" then set display to "2" else set display to str(display) + "2" end
    app.set_label("display", display)
end

define btn_3() do
    if display is "0" then set display to "3" else set display to str(display) + "3" end
    app.set_label("display", display)
end

define btn_4() do
    if display is "0" then set display to "4" else set display to str(display) + "4" end
    app.set_label("display", display)
end

define btn_5() do
    if display is "0" then set display to "5" else set display to str(display) + "5" end
    app.set_label("display", display)
end

define btn_6() do
    if display is "0" then set display to "6" else set display to str(display) + "6" end
    app.set_label("display", display)
end

define btn_7() do
    if display is "0" then set display to "7" else set display to str(display) + "7" end
    app.set_label("display", display)
end

define btn_8() do
    if display is "0" then set display to "8" else set display to str(display) + "8" end
    app.set_label("display", display)
end

define btn_9() do
    if display is "0" then set display to "9" else set display to str(display) + "9" end
    app.set_label("display", display)
end

define btn_0() do
    if display is "0" then set display to "0" else set display to str(display) + "0" end
    app.set_label("display", display)
end

define btn_clear() do
    set display to "0"
    set current_val to 0
    set op to ""
    app.set_label("display", display)
end

define btn_add() do
    set current_val to int(display)
    set op to "+"
    set display to "0"
end

define btn_sub() do
    set current_val to int(display)
    set op to "-"
    set display to "0"
end

define btn_mul() do
    set current_val to int(display)
    set op to "*"
    set display to "0"
end

define btn_div() do
    set current_val to int(display)
    set op to "/"
    set display to "0"
end

define btn_eq() do
    set next_val to int(display)
    if op is "+" then
        set current_val to current_val + next_val
    end
    if op is "-" then
        set current_val to current_val - next_val
    end
    if op is "*" then
        set current_val to current_val * next_val
    end
    if op is "/" then
        if next_val is 0 then
            set current_val to 0
        else
            set current_val to current_val / next_val
        end
    end
    set display to str(current_val)
    app.set_label("display", display)
end

# Layout Buttons Grid (Row, Col, Span)
# Row 1
app.add_button("btn7", "7", "btn_7", 1, 0, 1)
app.add_button("btn8", "8", "btn_8", 1, 1, 1)
app.add_button("btn9", "9", "btn_9", 1, 2, 1)
app.add_button("btnd", "/", "btn_div", 1, 3, 1)

# Row 2
app.add_button("btn4", "4", "btn_4", 2, 0, 1)
app.add_button("btn5", "5", "btn_5", 2, 1, 1)
app.add_button("btn6", "6", "btn_6", 2, 2, 1)
app.add_button("btnm", "*", "btn_mul", 2, 3, 1)

# Row 3
app.add_button("btn1", "1", "btn_1", 3, 0, 1)
app.add_button("btn2", "2", "btn_2", 3, 1, 1)
app.add_button("btn3", "3", "btn_3", 3, 2, 1)
app.add_button("btns", "-", "btn_sub", 3, 3, 1)

# Row 4
app.add_button("btnc", "C", "btn_clear", 4, 0, 1)
app.add_button("btn0", "0", "btn_0", 4, 1, 1)
app.add_button("btne", "=", "btn_eq", 4, 2, 1)
app.add_button("btna", "+", "btn_add", 4, 3, 1)

say "Starting UI..."
app.run()
