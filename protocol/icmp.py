from protocol.protocol import *

class ICMP(PROTOCOL):
    def build(self, itype = 8, icode = 0, content = b''):
        self.ethernet_frame = \
            self.dst_mac + \
            self.src_mac + \
            b'\x08\x00'

        self.ip_frame = \
            b'\x45' + \
            b'\x00' + \
            b'\x00\x9c' + \
            b'\x00\x00' + \
            b'\x00\x00' + \
            b'\x2b' + \
            b'\x01' + \
            b'\x22\x03' + \
            self.src_ip + \
            self.dst_ip

        self.packet_data = \
            self.packet_header(b_length = 42, c_length = len(content)) + \
            self.ethernet_frame + \
            self.ip_frame + \
            bytes([itype]) + \
            bytes([icode]) + \
            b'\x00\x00' + \
            b'\x00\x00' + \
            b'\x00\x00' + \
            content
        
        return self.packet_data
