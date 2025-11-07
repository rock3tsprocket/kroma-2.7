from .enums import ANSIColors, StyleType, TextFormat
from .utils import _get_ansi_color_code, _apply_text_formatting, _get_ansi_color_code_with_formatting


def style(
    text, # type: str
    foreground = None, # type: ANSIColors | None
    background = None, # type: ANSIColors | None
    bold = False, # type: bool
    italic = False, # type: bool
    underline = False, # type: bool
    strikethrough = False, # type: bool
):
    # type: (...) -> str
    formats = []
    if bold:
        formats.append(TextFormat.BOLD)
    if italic:
        formats.append(TextFormat.ITALIC)
    if underline:
        formats.append(TextFormat.UNDERLINE)
    if strikethrough:
        formats.append(TextFormat.STRIKETHROUGH)

    if foreground is None and background is None:
        if formats:
            return _apply_text_formatting(text, formats)
        else:
            return text
    elif foreground is not None and background is None:
        if formats:
            return _get_ansi_color_code_with_formatting(text, foreground, StyleType.FOREGROUND, formats)
        else:
            return _get_ansi_color_code(text, foreground, StyleType.FOREGROUND)
    elif foreground is None and background is not None:
        if formats:
            return _get_ansi_color_code_with_formatting(text, background, StyleType.BACKGROUND, formats)
        else:
            return _get_ansi_color_code(text, background, StyleType.BACKGROUND)
    else:
        assert foreground is not None and background is not None
        if formats:
            fg_formatted = _get_ansi_color_code_with_formatting(text, foreground, StyleType.FOREGROUND, formats)
            return _get_ansi_color_code_with_formatting(fg_formatted, background, StyleType.BACKGROUND, None)
        else:
            return _get_ansi_color_code(_get_ansi_color_code(text, foreground, StyleType.FOREGROUND), background, StyleType.BACKGROUND)
