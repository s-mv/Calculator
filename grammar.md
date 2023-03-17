This might not be perfect
```
calculation -> value ("+" | "-" term)*
term        -> (function | value ("*" | "/" | "%" value))*
function    -> identifier\((value | identifier ",")*\)
value       => (0-9)+(\.(0-9)*)? | identifier
```
Some examples:
```
1 + 2
15 * sin(12) - 12
12 * pi - 33
```