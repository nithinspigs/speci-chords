from music21 import *
from mingus.core.chords import *
import copy
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from os import path
from random import *


class GUI():
    def __init__(self, window):
        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 0, row = 0)

        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 0, row = 1)
        self.key_label = Label(window, text = "Key")
        self.key_label.grid(column = 1, row = 1)
        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 2, row = 1)
        self.amount_label = Label(window, text = "Amount")
        self.amount_label.grid(column = 3, row = 1)
        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 4, row = 1)
        self.octave_label = Label(window, text = "Octave")
        self.octave_label.grid(column = 5, row = 1)
        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 6, row = 1)
        self.velocity_label = Label(window, text = "Velocity")
        self.velocity_label.grid(column = 7, row = 1)

        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 0, row = 2)
        self.key = StringVar()
        self.key_option_menu = ttk.OptionMenu(window, self.key, "", "C", "c", "Db", "db", "D", "d", "Eb", "eb", "E", "e", "F", "f", "Gb", "gb", "G", "g", "Ab", "ab", "A", "a", "Bb", "bb", "B", "b")
        self.key_option_menu.grid(column = 1, row = 2)
        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 2, row = 2)
        self.amount = IntVar()
        self.amount_entry = Entry(window, width = 3, textvariable = self.amount)
        self.amount_entry.grid(column = 3, row = 2)
        self.amount.set(4)
        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 4, row = 2)
        self.octave = IntVar()
        self.octave_spinbox = Spinbox(window, from_ = -2, to = 8, width = 3, textvariable = self.octave, values = tuple(range(-2, 9)))
        self.octave_spinbox.grid(column = 5, row = 2)
        self.octave.set(2)
        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 6, row = 2)
        self.velocity = IntVar()
        self.velocity_spinbox = Spinbox(window, from_ = 0, to = 127, width = 3, textvariable = self.velocity, values = tuple(range(0, 128)))
        self.velocity_spinbox.grid(column = 7, row = 2)
        self.velocity.set(80)

        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 0, row = 3)

        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 0, row = 4)
        self.humanize_label = Label(window, text = "Humanize")
        self.humanize_label.grid(column = 1, row = 4)
        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 2, row = 4)
        self.inversions_label = Label(window, text = "Variation")
        self.inversions_label.grid(column = 3, row = 4)
        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 4, row = 4)
        #self.inversions_label = Label(window, text = "Embellish")
        #self.inversions_label.grid(column = 5, row = 4)

        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 0, row = 5)
        self.humanize = IntVar()
        self.humanize_spinbox = Spinbox(window, from_ = 0, to = 12, width = 3, textvariable = self.humanize, values = tuple(range(0, 13)))
        self.humanize_spinbox.grid(column = 1, row = 5)
        self.humanize.set(0)
        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 2, row = 5)
        self.inversions = StringVar()
        self.variation = IntVar()
        self.variation_spinbox = Spinbox(window, from_ = 0, to = 24, width = 3, textvariable = self.variation, values = tuple(range(0, 99)))
        self.variation_spinbox.grid(column = 3, row = 5)
        self.variation.set(0)

        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 0, row = 6)

        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 0, row = 7)
        self.input_file_name = None
        self.input_file_button = ttk.Button(window, text = "Input File", command = self.askopenfilename)
        self.input_file_button.grid(column = 1, row = 7)
        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 2, row = 7)
        self.input_file_name_label = Label(window)
        self.input_file_name_label.grid(column = 3, row = 7)
        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 4, row = 7)
        self.harmonize_button = ttk.Button(window, text = "Harmonize", command = self.harmonize)
        self.harmonize_button.grid(column = 5,row = 7)

        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 0, row = 8)

        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 0, row = 9)
        self.output_file_name = StringVar()
        self.output_file_name_entry = Entry(window, width = 9, textvariable = self.output_file_name)
        self.output_file_name_entry.grid(column = 1, row = 9)
        self.output_file_name.set("output.mid")
        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 2, row = 9)
        self.output_file_name_label = Label(window)
        self.output_file_name_label.grid(column = 3, row = 9)
        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 4, row = 9)
        self.play_button = ttk.Button(window, text = "Play", command = self.play)
        self.play_button.grid(column = 5,row = 9)

        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 0, row = 10)

        self.pad = Label(window, padx = 12)
        self.pad.grid(column = 0, row = 1)
        self.error_label = Label(window, fg = "red")
        self.error_label.grid(column = 1, row = 11)

        self.stream = None


    def askopenfilename(self):
        self.input_file_name = filedialog.askopenfilename()
        self.input_file_name_label.configure(text = path.basename(self.input_file_name))


    def harmonize(self):
        if self.input_file_name is None:
            self.error_label.config(text = "Missing Input File")
            return

        if not self.input_file_name.endswith("mid"):
            self.error_label.config(text = "Invalid Input File")
            return

        self.error_label.config(text = "")

        midi_file = midi.MidiFile()
        midi_file.open(self.input_file_name)
        midi_file.read()
        midi_file.close()

        self.stream = midi.translate.midiFileToStream(midi_file, quantizePost = False)
        
        # all the metadata from the melody track is copied to the harmony track
        # this fixes the issue where the input melodies would be converted to 4/4 upon output regardless of their original time signature
        self.stream.append(copy.deepcopy(self.stream.elements[0]))
        self.stream.elements[1].removeByClass('Note')
        self.stream.elements[1].removeByClass('Rest')

        i = 0
        key = self.key.get()

        last_note_time = self.stream.elements[0].highestTime

        while i < last_note_time:

            elements = self.stream.elements[0].getElementsByOffset(i, i + self.amount.get(), includeEndBoundary = False)

            # key is not taken from midi file because midi does not always make a distinction between major and minor keys (e.g. G major vs e minor)
            if key == "":
                self.error_label.config(text = "Missing Key")
                return

            notes = self.stream.elements[0].flat.notes.getElementsByOffset(i, i + self.amount.get(), includeEndBoundary = False)
            #note_names = [element.name for element in notes]

            counter = 0
            max_chord = []
            counters = []
            chords = []

            seventh_num = randint(0, 99)
            chords_from_key = sevenths(key) if seventh_num < self.variation.get() else triads(key)

            for triad in chords_from_key:
                counter = 0
                for temp in triad:
                    # mingus.chords represents flats using 'b' as in Bb
                    # music21 represents flats using '-' as in B-
                    temp = temp.replace('b', '-')
                    for current_note in notes:
                        # checks for enharmonics
                        if temp == current_note.name or temp == current_note.pitch.getEnharmonic().name:
                            # counter goes by length of note instead of number of notes so that passing notes are less of an issue
                            counter += current_note.duration.quarterLength
                counters.append(counter)
                chords.append(triad)
            
            # hierarchy of chords such that certain ones are favored over others in the event of a tie
            # order in decreasing priority: tonic, dominant, sixth, fourth (this could be changed later)
            temp = max(counters)
            max_chord_ties = zip([chords[i] for i in range(7) if counters[i] == temp], [i for i in range(7) if counters[i] == temp])
            max_chord = choice([chords[i] for i in range(7) if counters[i] == temp])
            
            for tuple in max_chord_ties:
                if tuple[1] == 0:
                    max_chord = tuple[0]
                    break
                elif tuple[1] == 4:
                    max_chord = tuple[0]
                    break
                elif tuple[1] == 5:
                    max_chord = tuple[0]
                    break
                elif tuple[1] == 3:
                    max_chord = tuple[0]
                    break

            # notes are compiled into a chord, which is then appended to the stream
            # this is so that an inversion can be applied to the entire chord
            notes_in_chord = []
            for k in range(0, len(max_chord)):
                note_to_add = max_chord[k]
                offset = 0.01 * randint(0, self.humanize.get())
                temp = note.Note(note_to_add, octave = self.octave.get()+1, quarterLength = self.amount.get() - offset - 0.01 * randint(0, self.humanize.get()))
                temp.volume.velocity = self.velocity.get() + randint(-self.humanize.get(), self.humanize.get())
                notes_in_chord.append(temp)
            
            # inversions
            inversion_num = 0
            if seventh_num < self.variation.get():
                inversion_num = choice([0, 1, 2, 3])
            else:
                if (randint(0, 99) < self.variation.get()):
                    inversion_num = choice([1, 2])
            chord_to_add = chord.Chord(notes_in_chord)
            chord_to_add.inversion(inversion_num)
            self.stream.elements[1].insert(i + offset, chord_to_add)
            
            i += self.amount.get()

            self.stream.write("midi", fp = self.output_file_name.get())
            self.output_file_name_label.config(text = self.output_file_name.get())


    def play(self):
        if self.stream is None:
            self.error_label.config(text = "Missing Output File")
            return

        self.error_label.config(text = "")
        self.stream.show()


window = Tk()
#window.title("Harmonizer")
window.geometry('600x600')
gui = GUI(window)
window.mainloop()
