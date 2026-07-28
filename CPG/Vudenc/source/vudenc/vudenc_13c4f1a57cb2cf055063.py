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
