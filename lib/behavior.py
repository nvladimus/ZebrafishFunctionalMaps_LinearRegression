# -*- coding: utf-8 -*-
"""
functions for processing behavior files
"""
import numpy as np
SAMPLING_FREQ_HZ = 6000


def import10ch(filename):
    """ Imports *.10ch or *.10chFlt file and parses it into structure-like arrays: data['t'][:], etc.
    Parameters
    ----------
    filename: str
        Full path to the binary file containing behavior data (.10ch or .10chFlt format)

    Returns
    -------
    parsed_data, structure-like numpy array with named fields: 't', 'ch0', 'ch1', 'fltCh0', 'fltCh1', 'camTrigger', '2pTrigger',
        'drift', 'speed', 'gain'. For example, data['drift'][:] contains all visual stimulus drift speed at all
        time points.
    """
    with open(filename, 'rb') as f:
        raw = np.fromfile(f, np.float32).reshape((-1, 10)).T
# there are two alternative file formats used in the lab, *.10ch or *.10chFlt, with different order of data fields.
    if filename[-5:] == '.10ch':
        parsed_data = np.zeros(np.size(raw, axis=1), dtype=[
                                            ('t', np.float32),
                                            ('ch0', np.float32),
                                            ('ch1', np.float32),
                                            ('fltCh0', np.float32),
                                            ('fltCh1', np.float32),
                                            ('camTrigger', np.float32),
                                            ('2pTrigger', np.float32),
                                            ('drift', np.float32),
                                            ('speed', np.float32),
                                            ('gain', np.float32)])
        parsed_data['gain'][:] = raw[4,:]
        parsed_data['drift'][:] = raw[5,:]
        parsed_data['speed'][:] = raw[6,:]
        parsed_data['camTrigger'][:] = raw[7,:]
        parsed_data['2pTrigger'][:] = raw[8,:]
    elif filename[-5:] == 'chFlt':
        parsed_data = np.zeros( np.size(raw, axis=1), dtype=[
                                            ('t', np.float32),
                                            ('ch0', np.float32),
                                            ('ch1', np.float32),
                                            ('fltCh0', np.float32),
                                            ('fltCh1', np.float32),
                                            ('camTrigger', np.float32),
                                            ('drift', np.float32),
                                            ('gain', np.float32)])
        parsed_data['camTrigger'][:] = raw[2,:]
        parsed_data['drift'][:] = raw[6,:]
        parsed_data['gain'][:] = raw[9,:]
    else:
        raise ValueError("Unknown file format")
    filter_kernel = np.exp(-np.r_[-60:61:1] ** 2 / (2 * 20 ** 2.))
    filter_kernel = filter_kernel / filter_kernel.sum()
    ch1 = raw[0,:]
    ch2 = raw[1,:]
    smoothed_channel1 = np.convolve(ch1, filter_kernel, mode='same')
    smoothed_channel2 = np.convolve(ch2, filter_kernel, mode='same')
    squared_deviation_ch1 = (ch1 - smoothed_channel1)**2
    squared_deviation_ch2 = (ch2 - smoothed_channel2)**2
    parsed_data['ch0'][:] = ch1
    parsed_data['ch1'][:] = ch2
    parsed_data['fltCh0'][:] = np.convolve(squared_deviation_ch1,filter_kernel,mode='same')
    parsed_data['fltCh1'][:] = np.convolve(squared_deviation_ch2,filter_kernel,mode='same')
    parsed_data['t'][:] = np.linspace(1, np.size(raw[0,:]),np.size(raw[0,:]))/SAMPLING_FREQ_HZ

    return parsed_data


def stack_onsets(parsed_data, threshold=3.8):
    """ finds stack onset indices in ephys data
    """
    stack_inits = np.where(parsed_data['camTrigger'][:] > threshold)[0]
    init_diffs = np.where(np.diff(stack_inits) > 1)[0]
    init_diffs = np.concatenate(([0], init_diffs + 1))
    stack_inits = stack_inits[init_diffs]
    return stack_inits


def conv2exp(x, tau1, tau):
    """ Convolution with double-exponent kernel, time in stacks """
    ker_window = 50
    r = np.linspace(0, ker_window)
    ker2exp = np.r_[np.zeros(ker_window - 1), np.exp(-r / tau) - np.exp(-r / tau1)]
    y = np.convolve(ker2exp / ker2exp.sum(), x, mode='same')
    return y

