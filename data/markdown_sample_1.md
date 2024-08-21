
# Written in Markdown

## Latex

Courtesy of [MathJax](https://www.mathjax.org/).  
You can include mathematical expressions both inline: $ e^{i\pi} + 1 = 0 $ and displayed as block:

$$ e^x=\sum_{i=0}^\infty \frac{x^i}{i!} $$

To practise your Latex I recommend the [codecogs latex equation online editor](https://www.codecogs.com/latex/eqneditor.php).



## Colors

Sometimes you need to use colors to draw attention.

<span style="color:blue">Hey *This is Blue italic.* text</span>

<span style="color:red">Hey **This is Red Bold.** text</span>

## Lists

1. First ordered list item
2. Another item
    * Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
    1. Ordered sub-list
    1. Ordered sub-list other item
4. And another item.

    You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

    To have a line break without a paragraph, you will need to use two trailing spaces.  
    Note that this line is separate, but within the same paragraph.  
    (This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks
- Or minuses
+ Or pluses

## Tables

Tables aren't part of the core Markdown spec, but they are part of GFM and Markdown Here supports them. They are an easy way of adding tables to your email -- a task that would otherwise require copy-pasting from another application.

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3
