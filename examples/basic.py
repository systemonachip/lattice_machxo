import itertools

from nmigen import Cat, ClockDomain, ClockSignal, Elaboratable, Module, Signal
from nmigen.build import Attrs, Pins, Resource, ResourceError
from nmigen_boards.machxo3_sk import MachXO3SKPlatform

from lattice_machxo.internal_oscillator import InternalOscillator
from lattice_machxo.embedded_function_block import EmbeddedFunctionBlock

class Blinky(Elaboratable):
    def __init__(self, clock_frequency, leds, switches=()):
        self._leds = leds
        self._switches = switches
        self._clock_frequency = clock_frequency

    def elaborate(self, platform):
        m = Module()
        inverts  = [0 for _ in self._leds]
        for index, switch in zip(itertools.cycle(range(len(inverts))), self._switches):
            inverts[index] ^= switch

        clk_freq = self._clock_frequency
        timer = Signal(range(int(clk_freq//4)), reset=int(clk_freq//4) - 1)
        flops = Signal(len(self._leds))

        m.d.comb += Cat(self._leds).eq(flops ^ Cat(inverts))
        with m.If(timer == 0):
            m.d.sync += timer.eq(timer.reset)
            m.d.sync += flops.eq(~flops)
        with m.Else():
            m.d.sync += timer.eq(timer - 1)

        return m

class BaseMach(Elaboratable):
    def __init__(self, scl, sda, scl2, sda2, clock=None):
        if clock:
            self._clock = clock
        else:
            self._clock = InternalOscillator()
        self.efb = EmbeddedFunctionBlock(clock=self._clock.out, scl=scl, sda=sda, scl2=scl2, sda2=sda2)

    def elaborate(self, platform):
        m = Module()
        m.submodules.clock = self._clock
        m.submodules.efb = self.efb
        m.domains += ClockDomain("sync")
        m.d.comb += ClockSignal("sync").eq(self._clock.out)
        return m

class BlinkySystem(BaseMach):
    def __init__(self, leds, switches, scl, sda, scl2, sda2):
        super().__init__(scl, sda, scl2, sda2)

        self.blinky = Blinky(3020000, leds, switches)

    def elaborate(self, platform):
        m = super().elaborate(platform)
        # We can do this automatically.
        m.submodules.blinky = self.blinky
        return m


if __name__ == "__main__":
    platform = MachXO3SKPlatform()
    def get_all_resources(name):
        resources = []
        for number in itertools.count():
            try:
                resources.append(platform.request(name, number))
            except ResourceError:
                break
        return resources

    leds     = [res.o for res in get_all_resources("led")]

    # Treat each part of the RGB LEDs separately.
    rgb_leds = [res for res in get_all_resources("rgb_led")]
    leds.extend([led.r.o for led in rgb_leds])
    leds.extend([led.g.o for led in rgb_leds])
    leds.extend([led.b.o for led in rgb_leds])

    switches = [res.i for res in get_all_resources("switch")]
    switches.extend((res.i for res in get_all_resources("button")))

    # c = platform.request("j", 3)
    # print(c)

    platform.add_resources([Resource("sda", 0, Pins("C9", dir="io"), Attrs(IO_TYPE="LVCMOS33"))])
    platform.add_resources([Resource("scl", 0, Pins("A9", dir="io"), Attrs(IO_TYPE="LVCMOS33"))])
    sda = platform.request("sda")
    scl = platform.request("scl")

    platform.add_resources([Resource("sda2", 0, Pins("B4", dir="io"), Attrs(IO_TYPE="LVCMOS33"))])
    platform.add_resources([Resource("scl2", 0, Pins("B5", dir="io"), Attrs(IO_TYPE="LVCMOS33"))])
    sda2 = platform.request("sda2")
    scl2 = platform.request("scl2")
    b = BlinkySystem(leds[:4], switches, scl, sda, scl2, sda2)
    platform.build(b)
