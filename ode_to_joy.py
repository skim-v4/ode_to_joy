from mido import Message, MidiFile, MidiTrack, MetaMessage

mid = MidiFile(ticks_per_beat=480)

# Track 0: Violin
violin = MidiTrack()
mid.tracks.append(violin)
violin.append(MetaMessage('set_tempo', tempo=500000))
violin.append(Message('program_change', program=40, channel=0, time=0))

# Track 1: Organ
organ = MidiTrack()
mid.tracks.append(organ)
organ.append(Message('program_change', program=19, channel=1, time=0))

# Track 2: Celesta
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
flute.append(Message('program_change', program=73, channel=5, time=0))

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
witness.append(Message('program_change', program=95, channel=10, time=0))

# Track 10: Glory
glory = MidiTrack()
mid.tracks.append(glory)
glory.append(Message('program_change', program=60, channel=11, time=0))

# Track 11: Counter-Melody
counter = MidiTrack()
mid.tracks.append(counter)
counter.append(Message('program_change', program=68, channel=12, time=0))

# Melody
notes_with_durations = [
    (64, 1), (64, 1), (65, 1), (67, 1),
    (67, 1), (65, 1), (64, 1), (62, 1),
    (60, 1), (60, 1), (62, 1), (64, 1),
    (64, 1.5), (62, 0.5), (62, 2),
    (64, 1), (64, 1), (65, 1), (67, 1),
    (67, 1), (65, 1), (64, 1), (62, 1),
    (60, 1), (60, 1), (62, 1), (64, 1),
    (62, 1.5), (60, 0.5), (60, 2)
]

# Chords
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

# Witness Swell Line
witness_line = [
    (55, 2), (57, 2), (59, 2), (60, 2),  # rising as melody descends
    (59, 1), (60, 1), (62, 2), (64, 2),  # gentle lift
    (62, 2), (60, 2), (59, 2), (57, 2),  # now descending
    (55, 2), (57, 1), (59, 1), (60, 2)   # settle back in
]

# Counter-Melody
counter_melody = [
    (72, 0.5), (74, 0.5), (76, 1),        # quick run
    (76, 1), (77, 1),                     # gentle rise
    (76, 0.5), (74, 0.5), (72, 1),        # fall back
    (74, 1.5), (76, 0.5),                 # syncopated lift
    (77, 1), (79, 1),                     # lyrical interval
    (77, 1), (76, 1), (74, 1),            # cascade
    (72, 1), (72, 1), (71, 1), (72, 1),   # slow descent
    (74, 2), (72, 2)                      # resolution
]

# Violin
total_beats_elapsed = 0
for note, duration_beats in notes_with_durations:
    duration_ticks = int(duration_beats * mid.ticks_per_beat)
    violin.append(Message('note_on', note=note, velocity=30, channel=0, time=0))
    violin.append(Message('note_off', note=note, velocity=30, channel=0, time=duration_ticks))
    total_beats_elapsed += duration_beats

# Organ
current_organ_time = 0
for start_beat, chord_notes, duration_beats in chords:
    chord_start_tick = start_beat * mid.ticks_per_beat
    delta_ticks = max(0, chord_start_tick - current_organ_time)
    duration_ticks = duration_beats * mid.ticks_per_beat
    for j, note in enumerate(chord_notes):
        organ.append(Message('note_on', note=note, velocity=30, channel=1, time=delta_ticks if j == 0 else 0))
    for j, note in enumerate(chord_notes):
        organ.append(Message('note_off', note=note, velocity=30, channel=1, time=duration_ticks if j == 0 else 0))
    current_organ_time = chord_start_tick + duration_ticks

# French Horn
for note, duration_beats in notes_with_durations:
    shimmer_note = note - 12
    duration_ticks = int(duration_beats * mid.ticks_per_beat)
    celesta.append(Message('note_on', note=shimmer_note, velocity=55, channel=2, time=0))
    celesta.append(Message('note_off', note=shimmer_note, velocity=55, channel=2, time=duration_ticks))

# Bass
current_bass_time = 0
for start_beat, chord_notes, duration_beats in chords:
    root_note = chord_notes[0] - 12
    start_tick = start_beat * mid.ticks_per_beat
    delta_ticks = max(0, start_tick - current_bass_time)
    duration_ticks = duration_beats * mid.ticks_per_beat
    bass.append(Message('note_on', note=root_note, velocity=35, channel=3, time=delta_ticks))
    bass.append(Message('note_off', note=root_note, velocity=35, channel=3, time=duration_ticks))
    current_bass_time = start_tick + duration_ticks

# Choir
melody_end_tick = 30720
current_choir_time = 0
for start_beat, chord_notes, duration_beats in chords:
    chord = [note +24 for note in chord_notes]
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

for note, duration_beats in notes_with_durations:
    start_tick = int(beat_position * mid.ticks_per_beat)
    duration_ticks = int(duration_beats * mid.ticks_per_beat)
    triplet_spacing = int(mid.ticks_per_beat / 3)
    num_triplets = int(duration_ticks // triplet_spacing)

    for i in range(num_triplets):
        triplet_note = note - i
        tick_offset = start_tick + i * triplet_spacing
        delta_ticks = max(0, tick_offset - current_flute_time)

        flute.append(Message('note_on', note=triplet_note, velocity=35, channel=5, time=delta_ticks))
        flute.append(Message('note_off', note=triplet_note, velocity=35, channel=5, time=triplet_spacing))

        current_flute_time = tick_offset + triplet_spacing

    beat_position += duration_beats


# Timpani
current_timpani_time = 0
for start_beat, _, duration_beats in chords:
    tick = start_beat * mid.ticks_per_beat
    delta_ticks = max(0, tick - current_timpani_time)
    duration_ticks = int(duration_beats * mid.ticks_per_beat * 0.8)
    timpani.append(Message('note_on', note=35, velocity=55, channel=6, time=delta_ticks))
    timpani.append(Message('note_off', note=35, velocity=55, channel=6, time=duration_ticks))
    current_timpani_time = tick + duration_ticks

# Harp
current_harp_time = 0
for start_beat, chord_notes, duration_beats in chords:
    start_tick = start_beat * mid.ticks_per_beat
    delta_ticks = max(0, start_tick - current_harp_time)

    sorted_notes = sorted(chord_notes)
    root, third, fifth = sorted_notes
    arp_notes = [root + 12, fifth + 12, third + 12, root + 24]

    duration_ticks = int(duration_beats * mid.ticks_per_beat)
    note_duration = int(mid.ticks_per_beat * 0.25)
    time_in_chord = 0
    first = True
    i = 0

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

# Strings
current_strings_time = 0
for start_beat, chord_notes, duration_beats in chords:
    for i in range(duration_beats * 2):
        if i % 2 == 1:
            beat_offset = start_beat + (i * 0.5)
            start_tick = int(beat_offset * mid.ticks_per_beat)
            delta_ticks = max(0, start_tick - current_strings_time)
            duration_ticks = int(mid.ticks_per_beat * 0.25)

            for j, note in enumerate(chord_notes):
                strings.append(Message('note_on', note=note, velocity=60, channel=7,
                                       time=delta_ticks if j == 0 else 0))
            for j, note in enumerate(chord_notes):
                strings.append(Message('note_off', note=note, velocity=60, channel=7,
                                       time=duration_ticks if j == 0 else 0))
            current_strings_time = start_tick + duration_ticks

# Witness
current_witness_time = 0
beat_position = 0

for note, duration_beats in witness_line:
    start_tick = int(beat_position * mid.ticks_per_beat)
    duration_ticks = int(duration_beats * mid.ticks_per_beat)
    delta_ticks = max(0, start_tick - current_witness_time)

    witness.append(Message('note_on', note=note, velocity=40, channel=9, time=delta_ticks))
    witness.append(Message('note_off', note=note, velocity=40, channel=9, time=duration_ticks))

    current_witness_time = start_tick + duration_ticks
    beat_position += duration_beats

# French Horn
current_glory_time = 0
beat_position = 0

for note, duration_beats in notes_with_durations:
    start_tick = int(beat_position * mid.ticks_per_beat)
    duration_ticks = int(duration_beats * mid.ticks_per_beat)
    delta_ticks = max(0, start_tick - current_glory_time)

    soaring_note = note + 12

    glory.append(Message('note_on', note=soaring_note, velocity=50, channel=10, time=delta_ticks))
    glory.append(Message('note_off', note=soaring_note, velocity=50, channel=10, time=duration_ticks))

    current_glory_time = start_tick + duration_ticks
    beat_position += duration_beats

# Oboe
current_counter_time = 0
beat_position = 0

for note, duration_beats in counter_melody:
    start_tick = int(beat_position * mid.ticks_per_beat)
    duration_ticks = int(duration_beats * mid.ticks_per_beat)
    delta_ticks = max(0, start_tick - current_counter_time)

    counter.append(Message('note_on', note=note, velocity=65, channel=11, time=delta_ticks))
    counter.append(Message('note_off', note=note, velocity=65, channel=11, time=duration_ticks))

    current_counter_time = start_tick + duration_ticks
    beat_position += duration_beats

# Save the file
mid.save("ode_to_joy.mid")
print("🎶 Created MIDI file: ode_to_joy.mid")