#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import can
import isotp
from can.interfaces.pcan import *

# create a bus instance
# many other interfaces are supported as well (see below)
with can.Bus(interface='pcan') as bus:
    # send a message
    bus.set_filters([{"can_id": 0x7B9, "can_mask": 0x7FF, "extended": False}])
    # message = can.Message(arbitration_id=0x214, is_extended_id=False,
    #                     data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    # bus.send(message, timeout=0.2)
    addr = isotp.Address(isotp.AddressingMode.Normal_11bits, rxid=0x7B9, txid=0x7B1)
    stack = isotp.CanStack(bus, address=addr)
    stack.send(b'\u0010\u0003')
    # iterate over received messages
    for msg in bus:
        print("{:X}: {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X}".format(msg.arbitration_id, msg.data[0], msg.data[1], msg.data[2], msg.data[3], msg.data[4], msg.data[5], msg.data[6], msg.data[7]))

    # or use an asynchronous notifier
    # notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])


