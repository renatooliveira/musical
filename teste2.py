import os


def shift_wav(wavfile, output, shifts, verbose=False):
    """
    Makes new sounds by shifting the pitch of a sound.
    Requires soundstrech installed.

    Args:
        wavfile : Name of the file containing the original sound
        output: name to use as a prefix for the output files and for
                the output folder name
        shifts (list of int): specifies of how many half-tones the pitch
                shifts should be. For instance [-2,-1,1,2] will produce
                4 files containing the sound 2 half-tones lower, one
                halftone lower, one halftone higher and two halftones
                higher.
    """

    folder = os.path.dirname(output)

    if not os.path.exists(folder):

        os.makedirs(folder)

    for i, s in enumerate(shifts):

        outputfile = '%s%02d.wav' % (output, i)

        command = 'soundstretch %s %s -pitch=%d' % (wavfile, outputfile, s)
        if verbose:
            print command
        os.system(command)
