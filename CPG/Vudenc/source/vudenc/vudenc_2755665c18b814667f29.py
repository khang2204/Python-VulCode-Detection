from m5.params import *
from m5.proxy import *
from m5.util.fdthelper import *
from m5.SimObject import SimObject
from m5.objects.Device import PioDevice
from m5.objects.Platform import Platform
type = 'BaseGic'
abstract = True
cxx_header = 'dev/arm/base_gic.hh'
platform = Param.Platform(Parent.any, 'Platform this device is part of.')
gicd_iidr = Param.UInt32(0, 'Distributor Implementer Identification Register')
gicd_pidr = Param.UInt32(0, 'Peripheral Identification Register')
gicc_iidr = Param.UInt32(0, 'CPU Interface Identification Register')
gicv_iidr = Param.UInt32(0, 'VM CPU Interface Identification Register')
type = 'ArmInterruptPin'
cxx_header = 'dev/arm/base_gic.hh'
cxx_class = 'ArmInterruptPinGen'
abstract = True
platform = Param.Platform(Parent.any, 'Platform with interrupt controller')
num = Param.UInt32('Interrupt number in GIC')
type = 'ArmSPI'
cxx_header = 'dev/arm/base_gic.hh'
cxx_class = 'ArmSPIGen'
type = 'ArmPPI'
cxx_header = 'dev/arm/base_gic.hh'
cxx_class = 'ArmPPIGen'
type = 'GicV2'
cxx_header = 'dev/arm/gic_v2.hh'
dist_addr = Param.Addr('Address for distributor')
cpu_addr = Param.Addr('Address for cpu')
cpu_size = Param.Addr(8192, 'Size of cpu register bank')
dist_pio_delay = Param.Latency('10ns', 'Delay for PIO r/w to distributor')
cpu_pio_delay = Param.Latency('10ns', 'Delay for PIO r/w to cpu interface')
int_latency = Param.Latency('10ns', 'Delay for interrupt to get to CPU')
it_lines = Param.UInt32(128, 'Number of interrupt lines supported (max = 1020)'
    )
gem5_extensions = Param.Bool(False, 'Enable gem5 extensions')
"""
    As defined in:
    "ARM Generic Interrupt Controller Architecture" version 2.0
    "CoreLink GIC-400 Generic Interrupt Controller" revision r0p1
    """
gicd_pidr = 2864272
gicd_iidr = 33559611
gicc_iidr = 33690683
gicv_iidr = gicc_iidr
type = 'Gicv2mFrame'
cxx_header = 'dev/arm/gic_v2m.hh'
spi_base = Param.UInt32(0, 'Frame SPI base number')
spi_len = Param.UInt32(0, 'Frame SPI total number')
addr = Param.Addr('Address for frame PIO')
type = 'Gicv2m'
cxx_header = 'dev/arm/gic_v2m.hh'
pio_delay = Param.Latency('10ns', 'Delay for PIO r/w')
gic = Param.BaseGic(Parent.any, 'Gic on which to trigger interrupts')
frames = VectorParam.Gicv2mFrame([], 'Power of two number of frames')
type = 'VGic'
cxx_header = 'dev/arm/vgic.hh'
gic = Param.BaseGic(Parent.any, 'Gic to use for interrupting')
platform = Param.Platform(Parent.any, 'Platform this device is part of.')
vcpu_addr = Param.Addr(0, 'Address for vcpu interfaces')
hv_addr = Param.Addr(0, 'Address for hv control')
pio_delay = Param.Latency('10ns', 'Delay for PIO r/w')
maint_int = Param.UInt32('HV maintenance interrupt number')
gicv_iidr = Param.UInt32(Self.gic.gicc_iidr,
    'VM CPU Interface Identification Register')
def generateDeviceTree(self, state):...
gic = self.gic.unproxy(self)
node = FdtNode('interrupt-controller')
node.appendCompatible(['gem5,gic', 'arm,cortex-a15-gic', 'arm,cortex-a9-gic'])
node.append(FdtPropertyWords('#interrupt-cells', [3]))
node.append(FdtPropertyWords('#address-cells', [0]))
node.append(FdtProperty('interrupt-controller'))
regs = state.addrCells(gic.dist_addr) + state.sizeCells(4096
    ) + state.addrCells(gic.cpu_addr) + state.sizeCells(4096
    ) + state.addrCells(self.hv_addr) + state.sizeCells(8192
    ) + state.addrCells(self.vcpu_addr) + state.sizeCells(8192)
node.append(FdtPropertyWords('reg', regs))
node.append(FdtPropertyWords('interrupts', [1, int(self.maint_int) - 16, 3844])
    )
node.appendPhandle(gic)
yield node
type = 'Gicv3'
cxx_header = 'dev/arm/gic_v3.hh'
dist_addr = Param.Addr('Address for distributor')
dist_pio_delay = Param.Latency('10ns', 'Delay for PIO r/w to distributor')
redist_addr = Param.Addr('Address for redistributors')
redist_pio_delay = Param.Latency('10ns', 'Delay for PIO r/w to redistributors')
it_lines = Param.UInt32(1020,
    'Number of interrupt lines supported (max = 1020)')
maint_int = Param.ArmInterruptPin(
    'HV maintenance interrupt.ARM strongly recommends that maintenance interrupts are configured to use INTID 25 (PPI Interrupt).'
    )
cpu_max = Param.Unsigned(256,
    'Maximum number of PE. This is affecting the maximum number of redistributors'
    )
gicv4 = Param.Bool(True, 'GICv4 extension available')
