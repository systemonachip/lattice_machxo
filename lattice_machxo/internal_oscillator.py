import bisect

from nmigen import Const, Elaboratable, Instance, Signal

class InternalOscillator(Elaboratable):
    # Diamond will complain that the frequency of the oscillator doesn't match
    # if it doesn't match one of the below frequencies. Since we tend to deal
    # with periods in nanoseconds, choose the closest frequency (in MHz)
    # within +/-5%. These numbers were extracted from
    # "MachXO2 sysCLOCK PLL Design and Usage Guide"
    supported_freqs = [
        2.08, 2.15, 2.22, 2.29, 2.38, 2.46, 2.56, 2.66, 2.77, 2.89,
        3.02, 3.17, 3.33, 3.50, 3.69, 3.91, 4.16, 4.29, 4.43, 4.59,
        4.75, 4.93, 5.12, 5.32, 5.54, 5.78, 6.05, 6.33, 6.65, 7.00,
        7.39, 7.82, 8.31, 8.58, 8.87, 9.17, 9.50, 9.85, 10.23, 10.64,
        11.08, 11.57, 12.09, 12.67, 13.30, 14.00, 14.78, 15.65, 15.65, 16.63,
        17.73, 19.00, 20.46, 22.17, 24.18, 26.60, 29.56, 33.25, 38.00, 44.33,
        53.20, 66.50, 88.67, 133.00
    ]

    def __init__(self, *, period=None, frequency=None):
        if frequency and frequency not in supported_freqs:
            raise ValueError("Unsupported frequency")
        if period and not frequency:
            frequency = self.nearest_freq(period)
        if frequency is None:
            frequency = 3.02
        self._freq_str = "{:.2f}".format(frequency)
        self.out = Signal()
        """Clock signal out."""

    def nearest_freq(self, period):
        target_freq = 1000.0/period

        # A None match is defined to not be in range. Handles special cases
        # described below.
        def in_range(actual, err=0.05):
            return abs((target_freq - actual)/target_freq) <= err if actual else False

        # Agreed-upon algorithm:
        # https://github.com/m-labs/migen/pull/111#discussion_r189687411
        i = bisect.bisect_right(self.supported_freqs, target_freq)

        # Special case: desired freq was < 2.08, but could still within +5%
        lo_match = self.supported_freqs[i-1] if i else None

        # Special case: desired freq was > 133.00, but could still within -5%
        hi_match = self.supported_freqs[i] if i < len(self.supported_freqs) else None

        if in_range(lo_match):
            selected_freq = lo_match
        elif in_range(hi_match):
            selected_freq = hi_match
        else:
            raise ValueError("Clock period out of range (-/+5%) for internal oscillator.")

        return selected_freq

    def elaborate(self, platform):
        m = Instance("OSCH",
                     p_NOM_FREQ=self._freq_str,
                     i_STDBY=Const(0),
                     o_OSC=self.out
                     )
        return m
