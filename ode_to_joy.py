from mido import Message, MidiFile, MidiTrack, MetaMessage

# 480 ticks per quarter note
mid = MidiFile(ticks_per_beat=480)

# 16 (0-15) total available tracks in MIDI

# Track 0: Violin
violin = MidiTrack()
mid.tracks.append(violin)
# only needs to be set once, 500k microseconds per beat = 120 bpm
violin.append(MetaMessage('set_tempo', tempo=500000))
violin.append(Message('program_change', program=40, channel=0, time=0))

# Track 1: Organ
organ = MidiTrack()
mid.tracks.append(organ)
organ.append(Message('program_change', program=19, channel=1, time=0))
# disable reverb, chorus, and sustain just for organ
organ.append(Message('control_change', control=91, value=0, channel=1, time=0))  # Reverb
organ.append(Message('control_change', control=93, value=0, channel=1, time=0))  # Chorus
organ.append(Message('control_change', control=64, value=0, channel=1, time=0))  # Sustain

# Track 2: Brass
celesta = MidiTrack()
mid.tracks.append(celesta)
celesta.append(Message('program_change', program=61, channel=2, time=0))

# Track 3: Acoustic Bass
bass = MidiTrack()
mid.tracks.append(bass)
bass.append(Message('program_change', program=32, channel=3, time=0))

# Track 4: Choir
choir = MidiTrack()
mid.tracks.append(choir)
choir.append(Message('program_change', program=52, channel=4, time=0))

# Track 5: Flute
flute = MidiTrack()
mid.tracks.append(flute)
flute.append(Message('program_change', program=82, channel=5, time=0))

# Track 6: Timpani
timpani = MidiTrack()
mid.tracks.append(timpani)
timpani.append(Message('program_change', program=48, channel=6, time=0))

# Track 7: Harp
harp = MidiTrack()
mid.tracks.append(harp)
harp.append(Message('program_change', program=46, channel=7, time=0))

# Track 8: Strings
strings = MidiTrack()
mid.tracks.append(strings)
strings.append(Message('program_change', program=48, channel=8, time=0))

# Track 9: Witness
witness = MidiTrack()
mid.tracks.append(witness)
# do not use channel 9, reserved in hardware for drums. using 14 instead
witness.append(Message('program_change', program=95, channel=14, time=0))

# Track 10: Glory
glory = MidiTrack()
mid.tracks.append(glory)
glory.append(Message('program_change', program=60, channel=11, time=0))

# Track 11: Counter-Melody
counter = MidiTrack()
mid.tracks.append(counter)
counter.append(Message('program_change', program=51, channel=12, time=0))

# Track 12: Caveman Power Chords
guitar = MidiTrack()
mid.tracks.append(guitar)
guitar.append(Message('program_change', program=30, channel=13, time=0))

# Melody
notes_with_durations = [
    (64, 1), (64, 1), (65, 1), (67, 1), # tuples (pitch, time)
    (67, 1), (65, 1), (64, 1), (62, 1),
    (60, 1), (60, 1), (62, 1), (64, 1),
    (64, 1.5), (62, 0.5), (62, 2),
    (64, 1), (64, 1), (65, 1), (67, 1),
    (67, 1), (65, 1), (64, 1), (62, 1),
    (60, 1), (60, 1), (62, 1), (64, 1),
    (62, 1.5), (60, 0.5), (60, 2)
]

# Best Melody
horn_melody = [
    (64, 1), (64, 1), (65, 1), (67, 1),
    (67, 1), (65, 1), (64, 1), (65, 0.5), (62, 0.5),  # F D variation
    (60, 1), (60, 1), (62, 1), (64, 1),
    (64, 1.5), (62, 0.5), (67, 2),  # G variation at end of phrase
    (64, 1), (64, 1), (65, 1), (67, 1),
    (67, 1), (65, 1), (64, 1), (62, 1),
    (60, 1), (60, 1), (62, 1), (64, 1),
    (62, 1), (67, 1), (72, 2)  # G and high C variation
]

# Triads
chords = [
    (0, [48, 52, 55], 4),  # C major
    (4, [43, 47, 50], 4),  # G major
    (8, [41, 45, 48], 4),  # F major
    (12, [48, 52, 55], 2),  # C major
    (14, [43, 47, 50], 2),  # G major
    (16, [48, 52, 55], 2),  # C major
    (18, [43, 47, 50], 2),  # G major
    (20, [45, 48, 52], 2),  # A minor
    (22, [43, 47, 50], 2),  # G major
    (24, [48, 52, 55], 2),  # C major
    (26, [41, 45, 48], 2),  # F major
    (28, [43, 47, 50], 2),  # G major
    (30, [48, 52, 55], 2),  # C major
]

# Power Chords
power_chords = [
    (0, [36, 43], 4),
    (4, [38, 45], 4),
    (8, [41, 48], 4),
    (12, [43, 50], 2),
    (14, [31, 38], 2),
    (16, [36, 43], 2),
    (18, [38, 45], 2),
    (20, [41, 48], 2),
    (22, [43, 50], 2),
    (24, [31, 38], 2),
    (26, [36, 43], 2),
    (28, [38, 45], 2),
    (30, [41, 48], 2),
]

# Witness Swell
witness_line = [
    (55, 2), (57, 2), (59, 2), (60, 2),  # rising as melody descends
    (59, 1), (60, 1), (62, 2), (64, 2),  # gentle lift
    (62, 2), (60, 2), (59, 2), (57, 2),  # now descending
    (55, 2), (57, 1), (59, 1), (60, 2)  # settle back in
]

# Counter-Melody
counter_melody = [
    (72, 0.5), (74, 0.5), (76, 1),
    (76, 1), (77, 1),
    (76, 0.5), (74, 0.5), (72, 1),
    (74, 1.5), (76, 0.5),
    (77, 1), (79, 1),
    (77, 1), (76, 1), (74, 1),
    (72, 1), (72, 1), (71, 1), (72, 1),
    (74, 2), (72, 2),  # original resolution (total ~21 beats)
    # NEW ascending line (~11 beats) to fill 8 bars = 32 total
    (74, 1), (76, 1), (77, 1), (79, 1),
    (81, 1), (83, 1), (84, 1.5), (83, 0.5),
    (84, 1), (86, 2)
]

# Cescendos and Diminuendo
base_velocity = 5
crescendo_velocities = [base_velocity + i * 3 for i in range(8)]  # gradually increases

# Violin
for i, (note, duration_beats) in enumerate(notes_with_durations):
    # modulo to create repeating patterns of increasing/decreasing velocity
    velocity = base_velocity + 10 * (i % 4)
    # converts beat duration into MIDI ticks
    duration_ticks = int(duration_beats * mid.ticks_per_beat)
    # start playing at time = 0
    violin.append(Message('note_on', note=note, velocity=velocity, channel=0, time=0))
    # stop playing at time = current beat * 480
    violin.append(Message('note_off', note=note, velocity=velocity, channel=0, time=duration_ticks))

# Organ
current_organ_time = 0
for start_beat, chord_notes, duration_beats in chords:
    chord_start_tick = start_beat * mid.ticks_per_beat
    # how much time has passed since the last event
    delta_ticks = max(0, chord_start_tick - current_organ_time)
    # how long to hold the chords
    duration_ticks = duration_beats * mid.ticks_per_beat

    # add sustain pedal right before the notes start
    if delta_ticks > 0:
        organ.append(Message('control_change', control=64, value=127, channel=1, time=delta_ticks))
        # Reset delta_ticks since we used it for pedal
        delta_ticks = 0
    else:
        # if no available delta time, add pedal down with time = 0
        organ.append(Message('control_change', control=64, value=127, channel=1, time=0))

    for j, note in enumerate(chord_notes):
        organ.append(Message('note_on', note=note, velocity=30, channel=1, time=0))

    for j, note in enumerate(chord_notes):
        # only the first note_off gets duration time
        organ.append(Message('note_off', note=note, velocity=30, channel=1, time=duration_ticks if j == 0 else 0))

    # release sustain pedal after the notes end
    organ.append(Message('control_change', control=64, value=0, channel=1, time=0))

    current_organ_time = chord_start_tick + duration_ticks

# Brass
# featuring phrasing, dynamics, breathing, and vibrato :D
current_horn_time = 0
beat_position = 0

for i, (note, duration_beats) in enumerate(notes_with_durations):
    # octave lower for sonic balance
    shimmer_note = note - 12

    start_tick = int(beat_position * mid.ticks_per_beat)
    duration_ticks = int(duration_beats * mid.ticks_per_beat)
    delta_ticks = max(0, start_tick - current_horn_time)

    # dynamic contrast phrasing
    phrase_position = i % 8  # takes place within a 8-note phrase
    if phrase_position < 4:  # first half of phrase is crescendo
        velocity = 60 + (phrase_position * 5)  # 60, 65, 70, 75
    else:  # second half of phrase is diminuendo
        velocity = 75 - ((phrase_position - 4) * 5)  # 75, 65, 60, 55

    if duration_beats > 1:  # longer notes get louder, common in horns
        velocity += 10

    # simulate breath control with celesta layer, kind of works
    celesta.append(Message('control_change', control=2, value=100, channel=2, time=delta_ticks))

    # legato between notes
    if i > 0:
        celesta.append(Message('control_change', control=84, value=30, channel=2, time=0))

    celesta.append(Message('note_on', note=shimmer_note, velocity=velocity, channel=2, time=0))

    # add vibrato in the middle of long notes only
    if duration_ticks > mid.ticks_per_beat:
        # pitch bend for vibrato
        vibrato_start = duration_ticks // 4
        celesta.append(Message('pitchwheel', pitch=0, channel=2, time=vibrato_start))
        celesta.append(Message('pitchwheel', pitch=100, channel=2, time=duration_ticks // 16))
        celesta.append(Message('pitchwheel', pitch=-100, channel=2, time=duration_ticks // 16))
        celesta.append(Message('pitchwheel', pitch=50, channel=2, time=duration_ticks // 16))
        celesta.append(Message('pitchwheel', pitch=-50, channel=2, time=duration_ticks // 16))
        celesta.append(Message('pitchwheel', pitch=0, channel=2, time=duration_ticks // 16))

        # remaining time after vibrato
        remaining_duration = duration_ticks - vibrato_start - (duration_ticks // 16 * 5)
    else:
        remaining_duration = duration_ticks

    celesta.append(Message('note_off', note=shimmer_note, velocity=velocity, channel=2, time=remaining_duration))

    # reset legato for next note
    celesta.append(Message('control_change', control=84, value=0, channel=2, time=0))

    current_horn_time = start_tick + duration_ticks
    beat_position += duration_beats

# Bass
current_bass_time = 0
for start_beat, chord_notes, duration_beats in chords:
    # extract root note from chords, then drop by one octave
    root_note = chord_notes[0]
    start_tick = start_beat * mid.ticks_per_beat
    delta_ticks = max(0, start_tick - current_bass_time)
    duration_ticks = duration_beats * mid.ticks_per_beat
    bass.append(Message('note_on', note=root_note, velocity=35, channel=3, time=delta_ticks))
    bass.append(Message('note_off', note=root_note, velocity=35, channel=3, time=duration_ticks))
    current_bass_time = start_tick + duration_ticks

# Power Hour
current_guitar_time = 0

# root fifth power chords
for i, (start_beat, [root, fifth], duration_beats) in enumerate(power_chords):
    start_tick = start_beat * mid.ticks_per_beat
    delta_ticks = max(0, start_tick - current_guitar_time)
    duration_ticks = duration_beats * mid.ticks_per_beat

    guitar.append(Message('note_on', note=root+12, velocity=60, channel=13, time=delta_ticks))
    guitar.append(Message('note_on', note=fifth+12, velocity=60, channel=13, time=0))
    guitar.append(Message('note_off', note=root+12, velocity=34, channel=13, time=duration_ticks))
    guitar.append(Message('note_off', note=fifth+12, velocity=34, channel=13, time=0))

    current_guitar_time = start_tick + duration_ticks

# Choir
melody_end_tick = 30720     # defined melody end to cutoff overlap
current_choir_time = 0
for start_beat, chord_notes, duration_beats in chords:
    chord = [note + 24 for note in chord_notes[1:]]  # only third and fifth, skip first
    start_tick = start_beat * mid.ticks_per_beat
    delta_ticks = max(0, start_tick - current_choir_time)
    duration_ticks = duration_beats * mid.ticks_per_beat
    max_duration = melody_end_tick - start_tick
    if duration_ticks > max_duration:
        duration_ticks = max_duration
    for i, note in enumerate(chord):
        choir.append(Message('note_on', note=note, velocity=55, channel=4, time=delta_ticks if i == 0 else 0))
    for i, note in enumerate(chord):
        choir.append(Message('note_off', note=note, velocity=55, channel=4, time=duration_ticks if i == 0 else 0))
    current_choir_time = start_tick + duration_ticks

# Flute
current_flute_time = 0
beat_position = 0

# glorious triplets that dance above melody
for note, duration_beats in notes_with_durations:
    start_tick = int(beat_position * mid.ticks_per_beat)
    duration_ticks = int(duration_beats * mid.ticks_per_beat)
    triplet_spacing = int(mid.ticks_per_beat / 3)
    # not every note can fit a full triplet somehow
    num_triplets = int(duration_ticks // triplet_spacing)

    triplet_intervals = [12, 16, 19]  # octave, major third, perfect fifth
    triplet_notes = [(note + 12 + interval) for interval in triplet_intervals]

    for i in range(min(num_triplets, len(triplet_notes))):
        triplet_note = triplet_notes[i]
        tick_offset = start_tick + i * triplet_spacing
        delta_ticks = max(0, tick_offset - current_flute_time)
        # soft and airy
        flute.append(Message('note_on', note=triplet_note, velocity=20, channel=5, time=delta_ticks))
        flute.append(Message('note_off', note=triplet_note, velocity=20, channel=5, time=triplet_spacing))

        current_flute_time = tick_offset + triplet_spacing

    beat_position += duration_beats

# Timpani because I can
current_timpani_time = 0
for start_beat, _, duration_beats in chords:
    tick = start_beat * mid.ticks_per_beat
    delta_ticks = max(0, tick - current_timpani_time)
    duration_ticks = int(duration_beats * mid.ticks_per_beat * 0.8)
    timpani.append(Message('note_on', note=35, velocity=55, channel=6, time=delta_ticks))
    timpani.append(Message('note_off', note=35, velocity=55, channel=6, time=duration_ticks))
    current_timpani_time = tick + duration_ticks

# Harp for Harmony
current_harp_time = 0
for start_beat, chord_notes, duration_beats in chords:
    start_tick = start_beat * mid.ticks_per_beat
    delta_ticks = max(0, start_tick - current_harp_time)

    # arpeggio pattern
    sorted_notes = sorted(chord_notes)
    root, third, fifth = sorted_notes
    arp_notes = [root + 12, fifth + 12, third + 12, root + 24]

    duration_ticks = int(duration_beats * mid.ticks_per_beat)
    note_duration = int(mid.ticks_per_beat * 0.25)
    time_in_chord = 0
    first = True
    i = 0

    # glissando
    while time_in_chord + note_duration <= duration_ticks:
        note = arp_notes[i % len(arp_notes)]

        harp.append(Message('note_on', note=note, velocity=40, channel=7,
                            time=delta_ticks if first else 0))
        harp.append(Message('note_off', note=note, velocity=40, channel=7,
                            time=note_duration))

        delta_ticks = 0
        first = False
        time_in_chord += note_duration
        i += 1

    current_harp_time = start_tick + duration_ticks

# Strings w/ short 16th stabs on upbeat
current_strings_time = 0
for start_beat, chord_notes, duration_beats in chords:
    root = sorted(chord_notes)[0]
    for i in range(duration_beats * 2):
        if i % 2 == 1:
            beat_offset = start_beat + (i * 0.5)
            start_tick = int(beat_offset * mid.ticks_per_beat)
            delta_ticks = max(0, start_tick - current_strings_time)
            duration_ticks = int(mid.ticks_per_beat * 0.25)

            # cycle through root root+5 root+3
            if (i // 2) % 3 == 0:
                note = root
            elif (i // 2) % 3 == 1:
                note = root + 5
            else:
                note = root + 3

            velocity = 55 + (i % 3) * 5  # 55, 60, 65 cycling

            strings.append(Message('note_on', note=note, velocity=velocity, channel=8, time=delta_ticks))
            strings.append(Message('note_off', note=note, velocity=velocity, channel=8, time=duration_ticks))

            current_strings_time = start_tick + duration_ticks

# Witness the Swell
current_witness_time = 0
beat_position = 0

for note, duration_beats in witness_line:
    start_tick = int(beat_position * mid.ticks_per_beat)
    duration_ticks = int(duration_beats * mid.ticks_per_beat)
    delta_ticks = max(0, start_tick - current_witness_time)

    # pitch wheel at center
    witness.append(Message('pitchwheel', pitch=0, channel=14, time=delta_ticks))

    # add note_on time = 0
    witness.append(Message('note_on', note=note, velocity=40, channel=14, time=0))

    # add pitch bend up after 1/4 of note duration
    witness.append(Message('pitchwheel', pitch=200, channel=14, time=duration_ticks // 4))

    # return to center after another 1/4 of note duration
    witness.append(Message('pitchwheel', pitch=0, channel=14, time=duration_ticks // 4))

    # note_off after remaining duration
    witness.append(Message('note_off', note=note, velocity=40, channel=14, time=duration_ticks // 2))

    current_witness_time = start_tick + duration_ticks
    beat_position += duration_beats

# French Horn
current_glory_time = 0
beat_position = 0

# reverb
glory.append(Message('control_change', control=91, value=65, channel=11, time=0))

for i, (note, duration_beats) in enumerate(horn_melody):
    start_tick = int(beat_position * mid.ticks_per_beat)
    duration_ticks = int(duration_beats * mid.ticks_per_beat)
    delta_ticks = max(0, start_tick - current_glory_time)

    soaring_note = note

    # breath controller for expression
    breath_value = 80 if i % 8 == 0 else 70
    glory.append(Message('control_change', control=2, value=breath_value, channel=11, time=delta_ticks))

    # subtle expression controller
    glory.append(Message('control_change', control=11, value=75, channel=11, time=0))

    glory.append(Message('note_on', note=soaring_note, velocity=70, channel=11, time=0))

    # add gentle vibrato for longer notes
    if duration_ticks > mid.ticks_per_beat:
        vibrato_start = duration_ticks // 4
        vibrato_cycle = duration_ticks // 10

        # let vibrato sing
        glory.append(Message('pitchwheel', pitch=0, channel=11, time=vibrato_start))
        glory.append(Message('pitchwheel', pitch=50, channel=11, time=vibrato_cycle))
        glory.append(Message('pitchwheel', pitch=-30, channel=11, time=vibrato_cycle))
        glory.append(Message('pitchwheel', pitch=20, channel=11, time=vibrato_cycle))
        glory.append(Message('pitchwheel', pitch=-10, channel=11, time=vibrato_cycle))
        glory.append(Message('pitchwheel', pitch=0, channel=11, time=vibrato_cycle))

        remaining = duration_ticks - vibrato_start - (vibrato_cycle * 5)
    else:
        remaining = duration_ticks

    glory.append(Message('note_off', note=soaring_note, velocity=60, channel=11, time=remaining))

    current_glory_time = start_tick + duration_ticks
    beat_position += duration_beats

# Oboe the Solo Maestro
current_counter_time = 0
beat_position = 0

for note, duration_beats in counter_melody:
    start_tick = int(beat_position * mid.ticks_per_beat)
    duration_ticks = int(duration_beats * mid.ticks_per_beat)
    delta_ticks = max(0, start_tick - current_counter_time)

    counter.append(Message('note_on', note=note+12, velocity=15, channel=12, time=delta_ticks))
    counter.append(Message('note_off', note=note+12, velocity=15, channel=12, time=duration_ticks))

    current_counter_time = start_tick + duration_ticks
    beat_position += duration_beats

# Track 13: Drums
drums = MidiTrack()
mid.tracks.append(drums)

DRUM_VOLUME_BOOST = 30
last_tick = 0

def drum_hit(note, velocity, start_beat, length_beats=0.25):

    global last_tick
    on_tick = int(start_beat * mid.ticks_per_beat)
    off_tick = int((start_beat + length_beats) * mid.ticks_per_beat)
    delta = max(0, on_tick - last_tick)
    v = min(velocity + DRUM_VOLUME_BOOST, 127)  # boost velocity
    # Note on
    drums.append(Message('note_on', note=note, velocity=v, channel=9, time=delta))
    # Note off
    drums.append(Message('note_off', note=note, velocity=0, channel=9, time=off_tick - on_tick))
    last_tick = off_tick

# 8 bars * 4 beats each = 32 beats total

# 1) Bars 0-1 (beats 0-8): vibing
for b in range(0, 8):
    if b % 2 == 0:
        drum_hit(41, 100, b)  # Tom
    else:
        drum_hit(38, 110, b)  # Snare

# 2) Bars 2-3 (beats 8-16): gradually add hi-hat
for b in range(8, 16):
    if b % 2 == 0:
        drum_hit(36, 110, b)  # Bass drum
    else:
        drum_hit(38, 115, b)  # Snare
    drum_hit(42, 60, b + 0.5)  # Closed hi-hat

# 3) Bars 4-6 (beats 16-28): technical frenzy
for b in range(16, 28):
    if b % 2 == 0:
        drum_hit(36, 120, b)
    else:
        drum_hit(38, 120, b)
    for p in [0.25, 0.5, 0.75]:  # 16th-note tom runs
        tom_note = 41 + ((b + int(p*4)) % 4) * 2  # cycles 41,43,45,47
        drum_hit(tom_note, 90, b + p, 0.25)

# 4) Bar 7 (beats 28-32): euphoric explosion
for b in range(28, 32):
    drum_hit(49, 127, b)      # Crash
    drum_hit(38, 120, b + 0.5)  # Snare

# epic final fill
drum_hit(41, 110, 25, 0.125)
drum_hit(43, 115, 25.2, 0.125)
drum_hit(45, 120, 25.4, 0.125)
drum_hit(47, 127, 25.6, 0.125)

# save midi file
mid.save("ode_to_joy.mid")
print("Created MIDI file: ode_to_joy.mid")