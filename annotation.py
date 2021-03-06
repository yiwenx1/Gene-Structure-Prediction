import numpy as np

STATE_DICT = {
    'N': 0,
    'E': 1,
    'I': 2, # intron
    'p': 3, # first base of an intron
    'P': 4, # second base of an intron
    'Z': 5, # second to last base of an intron
    'z': 6, # last base of an intron
    's': 7, # first base of an exon
    'S': 8 # second base of an exon
}

OBS_DICT = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}

def load_state(states_filename, obs_filename):
    states = np.loadtxt(states_filename, dtype=str)[1][50000:50000+500]
    observations = np.loadtxt(obs_filename, dtype=str)[1][50000:50000+500]
    # states = "NEEpPIIZzsSE"
    # observations = "ACGTCCAACCCA"
    assert len(states) == len(observations)

    timestep = len(states)
    states_index = [0 for i in range(timestep)]
    observations_index = [0 for i in range(timestep)]
    print("timestep:", timestep)
    for i in range(timestep):
        states_index[i] = STATE_DICT[states[i]]
        observations_index[i] = OBS_DICT[observations[i]]

    # observations_index is a list of integers
    return states, observations, observations_index
