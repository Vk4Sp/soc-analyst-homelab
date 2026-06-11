# Networking Fundamentals - Day 1

## Concepts Learned

### IP Address

An IP address identifies a device on a network.

Examples:

* Private IP: 10.0.0.5
* Public IP: 140.x.x.x

### Public vs Private IP

Private IP addresses are used inside local networks and are not directly reachable from the Internet.

Public IP addresses are reachable from the Internet.

### Port

A port identifies a service running on a machine.

Examples:

* SSH : Port 22
* DNS : Port 53
* HTTP : Port 80
* HTTPS : Port 443

### Client and Server

Client:
Initiates a connection.

Server:
Waits for incoming connections.

Example:

* SSH Client = Laptop
* SSH Server = Oracle VM

### TCP Handshake

1. SYN
2. SYN-ACK
3. ACK

After the handshake, communication begins.

### DNS

DNS translates a domain name into an IP address.

Example:

google.com
↓
DNS lookup
↓
IP address
↓
TCP connection

## Commands Used

ip addr

ss -t

ss -u

ss -l

ss -tuln

## Oracle VM Observations

Private IP:
10.0.0.5

Listening Services:

* SSH (Port 22)
* DNS (Port 53 Localhost)
* RPC (Port 111)

## Next Topics

* MAC Address
* ARP
* Routing
* UDP
* Wireshark
