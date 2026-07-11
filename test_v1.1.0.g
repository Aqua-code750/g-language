say "Testing v1.1.0..."

define square(x) do
    return x * x
end

set result to square(5)
say "Square of 5 is:"
say result

say "Testing File I/O..."
write "Hello from G v1.1.0!" to "hello.txt"
read "hello.txt" into content
say content

say "Testing Lists and Dicts..."
set mylist to [1, 2, 3]
say mylist[0]
set mydict to {"name": "G", "version": "1.1.0"}
say mydict["name"]

say "All tests passed!"
