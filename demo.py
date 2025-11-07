# flake8: noqa

# ! kroma demonstration


# ? HTML colors and HEX codes
from kroma import html_color, HTMLColors

# example for blue-violet text with a maroon background
print(html_color.style("\nThis is blue-violet text on a maroon background.", background=HTMLColors.MAROON, foreground=HTMLColors.BLUEVIOLET))

# you can leave out either the background or foreground argument to only set one of them, for example:
print(html_color.style("This is normal text with a chartreuse background.", background=HTMLColors.CHARTREUSE))

# and for only foreground color:
print(html_color.style("This is aquamarine text on a normal background.", foreground=HTMLColors.AQUAMARINE))

# the html_color.style function also accepts HEX color codes, for example:
print(html_color.style("This is text with a custom background and foreground.\n", background="#000094", foreground="#8CFF7F"))


# ? ANSI colors
# you may want to use these if you want color support on terminals that do not support True Color.
# True Color is a newer standard utilized in html_color.style that allows for millions of colors instead of a limited palette of 16 or 256 colors.

from kroma import ansi_color, ANSIColors

# example for bright blue text with a red background
print(ansi_color.style("This is bright blue text on a red background.\n", background=ANSIColors.RED, foreground=ANSIColors.BRIGHT_BLUE))

#* this function works the same way as html_color.style, except it uses ANSI colors instead of HTML colors.
#* so, that means you can also leave out either the background or foreground argument to only set one of them.


# ? Text formatting
# In addition to colors, you can also apply bold, italic, underline, and strikethrough text formatting to your styled text.
# This works for both html_color.style and ansi_color.style functions.

# Examples:
print(html_color.style("This is bold, italic, underlined, and strikethrough text.", bold=True, italic=True, underline=True, strikethrough=True))
print(ansi_color.style("This is bold text.", bold=True))
print(html_color.style("This is underlined text.", underline=True))
print(html_color.style("This is italic and strikethrough text.", italic=True, strikethrough=True))
# As you can see, you can combine multiple formatting options in a single call.

# You can also combine text formatting with colors:
print(ansi_color.style("This is bold and italic text with colors.\n", foreground=ANSIColors.MAGENTA, bold=True, italic=True))


# ! Enjoy the module!
