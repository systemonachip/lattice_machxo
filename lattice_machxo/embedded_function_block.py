"""The embedded function block (EFB for short) includes a number of hard peripherals
   connected together via an 8-bit Wishbone bus. It is available in Mach XO2, Mach XO3
   and Mach XO3d.

   Reference PDFs are here:
     * [Mach XO2](http://www.latticesemi.com/view_document?document_id=46300)
     * [Mach XO3](http://www.latticesemi.com/view_document?document_id=50512)
     * [Mach XO3D](http://www.latticesemi.com/view_document?document_id=52704)
"""

from nmigen import Elaboratable, Instance, Module, Signal
from nmigen.hdl import ir
from nmigen_soc import wishbone

class PhaseLockLoop:
    pass
#     input wire [8:0] pll0_bus_i;
#     output wire [16:0] pll0_bus_o;

class InterIntegratedCircuit:
    def __init__(self, scl=None, sda=None, address_window=None):
        print(dir(scl), type(scl))

        self.kwargs = {
            "i_I2C{}SDAI": sda.i,
            "o_I2C{}SDAO": sda.o,
            "o_I2C{}SDAOEN": sda.oe,
            "i_I2C{}SCLI": scl.i,
            "o_I2C{}SCLO": scl.o,
            "o_I2C{}SCLOEN": scl.oe,
        }

#     output wire i2c1_irqo;
#     inout wire i2c1_scl;
#     inout wire i2c1_sda;
#     wire i2c2_scli;
#     wire i2c1_sdaoen;
#     wire i2c1_sdao;
#     wire i2c1_scloen;
#     wire i2c1_sclo;
#     wire i2c1_sdai;
#     wire i2c1_scli;
#     BB BB1_sda (.I(i2c1_sdao), .T(i2c1_sdaoen), .O(i2c1_sdai), .B(i2c1_sda));

#     BB BB1_scl (.I(i2c1_sclo), .T(i2c1_scloen), .O(i2c1_scli), .B(i2c1_scl));

#     defparam EFBInst_0.I2C1_WAKEUP = "DISABLED" ;
#     defparam EFBInst_0.I2C1_GEN_CALL = "DISABLED" ;
#     defparam EFBInst_0.I2C1_CLK_DIVIDER = 125 ;
#     defparam EFBInst_0.I2C1_BUS_PERF = "100kHz" ;
#     defparam EFBInst_0.I2C1_SLAVE_ADDR = "0b1010101" ;
#     defparam EFBInst_0.I2C1_ADDRESSING = "7BIT" ;
#     defparam EFBInst_0.EFB_I2C1 = "ENABLED" ;

class SerialPeripheralInterface:
    pass
#     input wire spi_scsn;
#     inout wire spi_clk;
#     inout wire spi_miso;
#     inout wire spi_mosi;
#     wire spi_mosi_oe;
#     wire spi_mosi_o;
#     wire spi_miso_oe;
#     wire spi_miso_o;
#     wire spi_clk_oe;
#     wire spi_clk_o;
#     wire spi_mosi_i;
#     wire spi_miso_i;
#     wire spi_clk_i;
#     BB BBspi_mosi (.I(spi_mosi_o), .T(spi_mosi_oe), .O(spi_mosi_i), .B(spi_mosi));

#     BB BBspi_miso (.I(spi_miso_o), .T(spi_miso_oe), .O(spi_miso_i), .B(spi_miso));

#     BB BBspi_clk (.I(spi_clk_o), .T(spi_clk_oe), .O(spi_clk_i), .B(spi_clk));

#     defparam EFBInst_0.SPI_WAKEUP = "DISABLED" ;
#     defparam EFBInst_0.SPI_INTR_RXOVR = "DISABLED" ;
#     defparam EFBInst_0.SPI_INTR_TXOVR = "DISABLED" ;
#     defparam EFBInst_0.SPI_INTR_RXRDY = "DISABLED" ;
#     defparam EFBInst_0.SPI_INTR_TXRDY = "DISABLED" ;
#     defparam EFBInst_0.SPI_SLAVE_HANDSHAKE = "DISABLED" ;
#     defparam EFBInst_0.SPI_PHASE_ADJ = "DISABLED" ;
#     defparam EFBInst_0.SPI_CLK_INV = "DISABLED" ;
#     defparam EFBInst_0.SPI_LSB_FIRST = "DISABLED" ;
#     defparam EFBInst_0.SPI_CLK_DIVIDER = 1 ;
#     defparam EFBInst_0.SPI_MODE = "SLAVE" ;
#     defparam EFBInst_0.EFB_SPI = "ENABLED" ;

class TimerCounter:
    pass
#     input wire tc_clki;
#     input wire tc_rstn;
#     input wire tc_ic;
#     output wire tc_int;
#     output wire tc_oc;
#     defparam EFBInst_0.TC_ICAPTURE = "DISABLED" ;
#     defparam EFBInst_0.TC_OVERFLOW = "DISABLED" ;
#     defparam EFBInst_0.TC_ICR_INT = "OFF" ;
#     defparam EFBInst_0.TC_OCR_INT = "OFF" ;
#     defparam EFBInst_0.TC_OV_INT = "OFF" ;
#     defparam EFBInst_0.TC_TOP_SEL = "ON" ;
#     defparam EFBInst_0.TC_RESETN = "ENABLED" ;
#     defparam EFBInst_0.TC_OC_MODE = "TOGGLE" ;
#     defparam EFBInst_0.TC_OCR_SET = 32767 ;
#     defparam EFBInst_0.TC_TOP_SET = 65535 ;
#     defparam EFBInst_0.GSR = "ENABLED" ;
#     defparam EFBInst_0.TC_CCLK_SEL = 1 ;
#     defparam EFBInst_0.TC_MODE = "CTCM" ;
#     defparam EFBInst_0.TC_SCLK_SEL = "PCLOCK" ;
#     defparam EFBInst_0.EFB_TC_PORTMODE = "WB" ;
#     defparam EFBInst_0.EFB_TC = "ENABLED" ;

class FlashMemory:
    pass

#     defparam EFBInst_0.UFM_INIT_FILE_FORMAT = "HEX" ;
#     defparam EFBInst_0.UFM_INIT_FILE_NAME = "NONE" ;
#     defparam EFBInst_0.UFM_INIT_ALL_ZEROS = "ENABLED" ;
#     defparam EFBInst_0.UFM_INIT_START_PAGE = 2045 ;
#     defparam EFBInst_0.UFM_INIT_PAGES = 1 ;
#     defparam EFBInst_0.DEV_DENSITY = "6900L" ;
#     defparam EFBInst_0.EFB_UFM = "ENABLED" ;
#     input wire ufm_sn;
#     output wire wbc_ufm_irq;

class EmbeddedFunctionBlock(Elaboratable):
    """This block of the FPGA includes a number of peripherals connected via an 8-bit Wishbone bus."""
    def __init__(self, address_window=None, clock=None, scl=None, sda=None):
        if isinstance(address_window, wishbone.Interface):
            args = []
            print("bus!")
            #     input wire wb_clk_i;
            #     input wire wb_rst_i;
            #     input wire wb_cyc_i;
            #     input wire wb_stb_i;
            #     input wire wb_we_i;
            #     input wire [7:0] wb_adr_i;
            #     input wire [7:0] wb_dat_i;
            #     output wire [7:0] wb_dat_o;
            #     output wire wb_ack_o;
            # super().__init__("EFB", *args)

        # Internal power signals to tie to.
        self._high = Signal()
        self._low = Signal()

        self.i2c1_scl = scl
        self.i2c1_sda = sda

        self._kwargs = {}

        if address_window is None:
            self._clock = clock

            # We aren't handed a wishbone bus so tie everything off.
            for i in range(8):
                self._kwargs["i_WBDATI%d" % i] = self._low
            for i in range(8):
                self._kwargs["i_WBADRI%d" % i] = self._low
            self._kwargs["i_WBSTBI"] = self._low
            self._kwargs["i_WBWEI"] = self._low
            self._kwargs["i_WBRSTI"] = self._low
            self._kwargs["i_WBCYCI"] = self._low
            self._kwargs["i_UFMSN"] = self._high
            self._freq = "3.02"
            self.primary_i2c = InterIntegratedCircuit(self.i2c1_scl, self.i2c1_sda)
            return

        self.pll0 = PhaseLockLoop(address_window[0x00:0x20])
        self.pll1 = PhaseLockLoop(address_window[0x20:0x40])
        self.primary_i2c = I2C(address_window[0x40:0x4a])
        self.secondary_i2c = I2C(address_window[0x4a:0x54])
        self.spi = SPI(address_window[0x54:0x5e])
        self.timer_counter = TimerCounter(address_window[0x5e:0x70])
        self.flash_memory = FlashMemory(address_window[0x70:0x76])
        self.interrupt_source = InterruptSource(address_window[0x76:0x78])

    def elaborate(self, platform):
        m = Module()
        m.submodules.high = ir.Instance("VHI", o_Z=self._high)
        m.submodules.low = ir.Instance("VLO", o_Z=self._low)
        i2c1_kwargs = {}
        for k in self.primary_i2c.kwargs:
            i2c1_kwargs[k.format(1)] = self.primary_i2c.kwargs[k]
        m.submodules.efb = ir.Instance("EFB",
                                       i_WBCLKI=self._clock,
                                       p_EFB_WB_CLK_FREQ=self._freq,
                                       p_EFB_I2C1="ENABLED",
                                       p_GSR="ENABLED",
                                       p_UFM_INIT_FILE_FORMAT = "HEX",
                                       p_UFM_INIT_FILE_NAME = "NONE",
                                       p_UFM_INIT_ALL_ZEROS = "ENABLED",
                                       p_UFM_INIT_START_PAGE = 2038,
                                       p_UFM_INIT_PAGES = 8,
                                       p_DEV_DENSITY = "7000L",
                                       p_EFB_UFM = "ENABLED",
                                       p_I2C1_WAKEUP="DISABLED",
                                       p_I2C1_GEN_CALL="DISABLED",
                                       p_I2C1_CLK_DIVIDER=8,
                                       p_I2C1_BUS_PERF="100kHz",
                                       p_I2C1_SLAVE_ADDR="0b1000001",
                                       p_I2C1_ADDRESSING="7BIT",
                                       **i2c1_kwargs,
                                       **self._kwargs)
        print("EFB instance!")
        return m

#     wire scuba_vlo;

#     VLO scuba_vlo_inst (.Z(scuba_vlo));

#     defparam EFBInst_0.EFB_WB_CLK_FREQ = "50.0" ;
#     EFB EFBInst_0 (.WBCLKI(wb_clk_i), .WBRSTI(wb_rst_i), .WBCYCI(wb_cyc_i), 
#         .WBSTBI(wb_stb_i), .WBWEI(wb_we_i), .WBADRI7(wb_adr_i[7]), .WBADRI6(wb_adr_i[6]), 
#         .WBADRI5(wb_adr_i[5]), .WBADRI4(wb_adr_i[4]), .WBADRI3(wb_adr_i[3]), 
#         .WBADRI2(wb_adr_i[2]), .WBADRI1(wb_adr_i[1]), .WBADRI0(wb_adr_i[0]), 
#         .WBDATI7(wb_dat_i[7]), .WBDATI6(wb_dat_i[6]), .WBDATI5(wb_dat_i[5]), 
#         .WBDATI4(wb_dat_i[4]), .WBDATI3(wb_dat_i[3]), .WBDATI2(wb_dat_i[2]), 
#         .WBDATI1(wb_dat_i[1]), .WBDATI0(wb_dat_i[0]), .PLL0DATI7(pll0_bus_i[8]), 
#         .PLL0DATI6(pll0_bus_i[7]), .PLL0DATI5(pll0_bus_i[6]), .PLL0DATI4(pll0_bus_i[5]), 
#         .PLL0DATI3(pll0_bus_i[4]), .PLL0DATI2(pll0_bus_i[3]), .PLL0DATI1(pll0_bus_i[2]), 
#         .PLL0DATI0(pll0_bus_i[1]), .PLL0ACKI(pll0_bus_i[0]), .PLL1DATI7(scuba_vlo), 
#         .PLL1DATI6(scuba_vlo), .PLL1DATI5(scuba_vlo), .PLL1DATI4(scuba_vlo), 
#         .PLL1DATI3(scuba_vlo), .PLL1DATI2(scuba_vlo), .PLL1DATI1(scuba_vlo), 
#         .PLL1DATI0(scuba_vlo), .PLL1ACKI(scuba_vlo), .I2C1SCLI(i2c1_scli), 
#         .I2C1SDAI(i2c1_sdai), .I2C2SCLI(i2c2_scli), .I2C2SDAI(i2c2_sdai), 
#         .SPISCKI(spi_clk_i), .SPIMISOI(spi_miso_i), .SPIMOSII(spi_mosi_i), 
#         .SPISCSN(spi_scsn), .TCCLKI(tc_clki), .TCRSTN(tc_rstn), .TCIC(tc_ic), 
#         .UFMSN(ufm_sn), .WBDATO7(wb_dat_o[7]), .WBDATO6(wb_dat_o[6]), .WBDATO5(wb_dat_o[5]), 
#         .WBDATO4(wb_dat_o[4]), .WBDATO3(wb_dat_o[3]), .WBDATO2(wb_dat_o[2]), 
#         .WBDATO1(wb_dat_o[1]), .WBDATO0(wb_dat_o[0]), .WBACKO(wb_ack_o), 
#         .PLLCLKO(pll0_bus_o[16]), .PLLRSTO(pll0_bus_o[15]), .PLL0STBO(pll0_bus_o[14]), 
#         .PLL1STBO(), .PLLWEO(pll0_bus_o[13]), .PLLADRO4(pll0_bus_o[12]), 
#         .PLLADRO3(pll0_bus_o[11]), .PLLADRO2(pll0_bus_o[10]), .PLLADRO1(pll0_bus_o[9]), 
#         .PLLADRO0(pll0_bus_o[8]), .PLLDATO7(pll0_bus_o[7]), .PLLDATO6(pll0_bus_o[6]), 
#         .PLLDATO5(pll0_bus_o[5]), .PLLDATO4(pll0_bus_o[4]), .PLLDATO3(pll0_bus_o[3]), 
#         .PLLDATO2(pll0_bus_o[2]), .PLLDATO1(pll0_bus_o[1]), .PLLDATO0(pll0_bus_o[0]), 
#         .I2C1SCLO(i2c1_sclo), .I2C1SCLOEN(i2c1_scloen), .I2C1SDAO(i2c1_sdao), 
#         .I2C1SDAOEN(i2c1_sdaoen), .I2C2SCLO(i2c2_sclo), .I2C2SCLOEN(i2c2_scloen), 
#         .I2C2SDAO(i2c2_sdao), .I2C2SDAOEN(i2c2_sdaoen), .I2C1IRQO(i2c1_irqo), 
#         .I2C2IRQO(i2c2_irqo), .SPISCKO(spi_clk_o), .SPISCKEN(spi_clk_oe), 
#         .SPIMISOO(spi_miso_o), .SPIMISOEN(spi_miso_oe), .SPIMOSIO(spi_mosi_o), 
#         .SPIMOSIEN(spi_mosi_oe), .SPIMCSN7(), .SPIMCSN6(), .SPIMCSN5(), 
#         .SPIMCSN4(), .SPIMCSN3(), .SPIMCSN2(), .SPIMCSN1(), .SPIMCSN0(), 
#         .SPICSNEN(), .SPIIRQO(), .TCINT(tc_int), .TCOC(tc_oc), .WBCUFMIRQ(wbc_ufm_irq), 
#         .CFGWAKE(), .CFGSTDBY());



#     // exemplar begin
#     // exemplar end

# endmodule
