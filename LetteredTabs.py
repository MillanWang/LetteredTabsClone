def main(input_string):

    #Opening original tab and creating a new text file for the lettered tab
    lettered = str()  #The returned string

    #Putting all lines of text into a list so that multiple lines can be analyzed at once
    list_of_lines = input_string.split("\n")
    for i in range(len(list_of_lines)):
        list_of_lines[i] += ("\n")
    list_of_lines.append("\n")
    #Attaches empty line to end so that it will never end on a tab line

    bars = list()
    for i in range(len(list_of_lines)):
        if is_line_tab(list_of_lines[i]):
            #current line is tab. Append to bars so that they can all be handled similtaneously
            bars.append(list(list_of_lines[i]))

        else:  #Finished a bar section. Handle it and
            print("Current")
            print(lettered)
            if len(bars):  #Only when bars is not empty
                lettered += handle_bars(bars)
                bars = list()  # resets bars to move on the next bar section
            lettered += list_of_lines[i]
    return lettered


def is_line_tab(line):
    """
    True if current line is of tab format. False otherwise
    
    :type note: string
    :rtype: bool
    """
    if len(line) < 3:
        #Tab lines are never shorter than 3 characters. Prevents index from being out of range
        return False
    if line[1] == "|" or line[2] == "|":
        #This character is used to separate the string note from the tab.
        return True
    else:
        return False


def get_offset(note):
    """
    returns the note offset for the current string.
    
    :type note: string
    :rtype: int
    """
    #Constant tuples of notes with indexes representing offset
    sharp_notes = ("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G",
                   "G#")
    flat_notes = ("A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G",
                  "Ab")

    lowercase_notes_flat = ("a", "bb", "b", "c", "db", "d", "eb", "e", "f",
                            "gb", "g", "ab")
    lowercase_notes_sharp = ("a", "a#", "b", "c", "c#", "d", "d#", "e", "f",
                             "f#", "g", "g#")
    #Often used for high E string. Accomadates different tunings

    if note in sharp_notes:
        return sharp_notes.index(note)
    elif note in flat_notes:
        return flat_notes.index(note)
    elif note in lowercase_notes_flat:
        return lowercase_notes_flat.index(note)
    elif note in lowercase_notes_sharp:
        return lowercase_notes_sharp.index(note)
    else:
        return 0


def get_letter(fret, offset):
    """
    returns the note of the fret with the string corresponding to the tuning
    
    :bars: int
    :offset: int
    :rtype: string
    """

    #Switch the accidentals to suit your preference.
    #I personally like a combination of flats and sharps but it is good practice
    #to periodically switch it up
    #It cycles through the notes twice because not doing so can make the offset look for an invalid index
    notes = ("A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab",
             "A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab")
    if fret >= 12:
        fret -= 12
    return notes[fret + offset]


def handle_bars(bars):
    """
    writes lettered tabs to writing_location
    
    :bars: list of lists of characters
    :rtype: None
    """
    numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    offsets = list()

    #Getting combining two digit numbers into a single string and getting the offsets
    for line in bars:

        #Two digit combination
        i = 0
        while i < len(
                line
        ) - 1:  #Minus one so that the indexes are right. The last characters are assumed to be "\n"
            if line[i] in numbers and line[
                    i +
                    1] in numbers:  #This combines the two digit frets to be read individually
                line[i] = line[i] + line[i + 1]
                line[i + 1] = ""  #Not removed to preserve constant length
                i += 2  #So that the second digit is not evaluated again
            else:
                i += 1

        #Offsets
        if line[1] == "|":  #Guitar string is a natural note
            offsets.append(get_offset(line[0]))
        else:  #Guitar string is an accidental note
            offsets.append(get_offset(line[:1]))

    #Lettering
    #This is done shifting over one character at a time, evaluating
    i = 0
    while i < len(
            bars[0]
    ) - 2:  #In properly formatted tabs, all of these lines will have the same length
        string_number = 0
        while string_number < len(bars):
            if bars[string_number][i] != "":

                if bars[string_number][i][
                        0] in numbers:  #the [0] at the end looks at the first character.

                    single_digit = len(bars[string_number][i]) == 1

                    #Setting to letter
                    bars[string_number][i] = get_letter(
                        int(bars[string_number][i]), offsets[string_number])

                    #When the fret was one digit and the note is accidental
                    #an extra "-" must be inserted to ensure that the bars stay aligned
                    if single_digit and len(bars[string_number][i]) == 2:
                        for curr in range(len(bars)):
                            if curr != string_number:
                                bars[curr].insert(i + 1, "-")

                            else:
                                bars[curr].insert(i + 1, "")

                    #In the case where the fret is 2 digit and the note is one letter
                    elif not single_digit and len(bars[string_number][i]) == 1:
                        bars[string_number][i] += "-"

            string_number += 1
        i += 1
    writing_location = ""
    #Writing all the lines to the file
    for line in bars:
        writing_location += ("".join(line))
        #The \n is not included because it is already a part of the string
    return writing_location
