import asyncio
from datetime import datetime


class UdpProtocol(asyncio.DatagramProtocol):
    def datagram_received(self, data, addr):
        msg = data.decode()
        print(f"{addr[0]} - {datetime.utcnow().isoformat()}Z: {msg}")


class TcpProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.client = transport.get_extra_info("peername")

    def data_received(self, data):
        msg = data.decode()
        print(f"{self.client[0]} - {datetime.utcnow().isoformat()}Z: {msg}")


async def main():
    loop = asyncio.get_running_loop()

    transport_udp, _ = await loop.create_datagram_endpoint(
        lambda: UdpProtocol(), local_addr=("0.0.0.0", 514)
    )
    server = await loop.create_server(lambda: TcpProtocol(), "0.0.0.0", 601)

    try:
        await server.serve_forever()
    finally:
        transport_udp.close()
        server.close()


if __name__ == "__main__":
    try:
        print("Listening on UDP port 514 and TCP port 601")
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
