from typing import List

# Characters that demark a word.
WORD_DELIM = " -.\t!?;:"
HYPHEN = "-"
WHITESPACE = " \t"


class MicroTextWrapper:
    """
    A text wrapping class function that wraps the text to the next line at the specified maximum width.
    The 'textwrap' standard module cannot be used in MicroPython due to these open issues:
        https://github.com/micropython/micropython/issues/9346
        https://github.com/micropython/micropython-lib/issues/318

    """

    def wrap_text(self, unwrapped_text: str, max_line_chars:int) -> List[str]:
        """
        Takes a unwrapped_text and word wraps it to fit within the specified space.

        Arguments:

        unwrapped_text -- The text to wrap.
        max_line_chars -- The maximum number of characters that are allowed in a word.

        Returns a list of lines that have been word-wrapped.

        """
        wrapped = []
                
        more = True
        fragment = unwrapped_text
        while(more):
            if (len(fragment) <= max_line_chars):
                wrapped.append(fragment)
                more = False
            elif (fragment[max_line_chars] in WHITESPACE):
                # we are breaking at whitespace.
                pos = max_line_chars
                line = fragment[0:pos]
                wrapped.append(line)
                fragment = fragment[pos+1:len(fragment)]
                if (fragment.strip == ""):
                    more = False
            else:
                # need to find the last word delimiter and break there.
                pos = self._find_word_break(fragment[0:max_line_chars])
                if (pos == max_line_chars):
                    # we did not find a word break. Force a hyphen and move on.
                    line = fragment[0:max_line_chars - 1] + HYPHEN
                    wrapped.append(line)
                    fragment = fragment[max_line_chars - 1:len(fragment)]
                else:
                    if not (fragment[pos] in WHITESPACE):
                        line = fragment[0:pos+1]
                        wrapped.append(line)
                        fragment = fragment[pos+1:len(fragment)]
                    else:
                        line = fragment[0:pos]

                        wrapped.append(line)
                        fragment = fragment[pos+1:len(fragment)]
                        
                    if (fragment.strip == ""):
                        more = False
        return wrapped

    def _find_word_break(self, sentence: str) -> int:
        """
        Find the position of the last word break in the input string.  If a word break is not found,
        the length of the input string is returned.
        """
        for i in range(len(sentence) - 1, -1, -1):
            if sentence[i] in WORD_DELIM:
                return i
        # if we got this far, a word delimiter was not found, return end of the input string.
        return len(sentence)