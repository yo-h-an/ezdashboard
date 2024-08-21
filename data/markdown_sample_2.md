
# Content produced from Markdown

[Markdown](https://en.wikipedia.org/wiki/Markdown) is simple yet powerful formatting language, used in [github](https://github.com/) [README](https://en.wikipedia.org/wiki/README) files.  
Typically a lot easier to write than HTML or RST.  
Maybe not as flexible but enough most of the time.  
The type of markdown supported here is GFM i.e. Github Flavored Markdown.  
It is the language used in github/gitlab README files and the Jupyter notebook.  
Which make is particularly convenient to write.  
You can also use online renders like the editors by [Dillinger](https://dillinger.io/) or [StackEdit](https://stackedit.io/editor).  

For a quick overview of what you can do check out the [cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).  

To view this page source markdown, see [the raw file](https://gitlab.com/oscar6echo/ezdashboard/raw/master/data/markdown_overview.md).

Here we just show the main features:

+ Headers from level 1 down to 6
+ Emphasis (bold, italics, strike-through) 
+ Links
+ Latex expressions (rendered by [MathJax](https://www.mathjax.org/))
+ Horizontal separators
+ Colors
+ Lists (unordered and ordered)
+ Tables
+ Block quotes
+ Images
+ Youtube videos

-----------------------------------------------------------------------------

## Headers

6 levels are available.  

# Level 1
## Level 2
### Level 3
#### Level 4
##### Level 5
###### Level 6



# Emphasis

Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.

Combined emphasis with **asterisks and _underscores_**.

Strikethrough uses two tildes. ~~Scratch this.~~


# Links

[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com


## Latex

Courtesy of [MathJax](https://www.mathjax.org/).  
You can include mathematical expressions both inline: $ e^{i\pi} + 1 = 0 $ and displayed as block:

$$ e^x=\sum_{i=0}^\infty \frac{x^i}{i!} $$

To practise your Latex I recommend the [codecogs latex equation online editor](https://www.codecogs.com/latex/eqneditor.php).  


## Horizontal separators

Three or more...

---

Hyphens

***

Asterisks

___

Underscores


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



## Block quotes


> Block quotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote. 


## Images

Here's our logo (hover to see the title text):

Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Reference-style: 
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"


## Youtube videos

They can't be added directly but you can add an image with a link to the video like this:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=wKimU8jy2a8
" target="_blank"><img src="http://img.youtube.com/vi/wKimU8jy2a8/0.jpg" 
alt="Video" width="240" height="180" border="10" /></a>

Or, in pure Markdown, but losing the image sizing and border:

[![Video](http://img.youtube.com/vi/wKimU8jy2a8/0.jpg)](http://www.youtube.com/watch?v=wKimU8jy2a8)

