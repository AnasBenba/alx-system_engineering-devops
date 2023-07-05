# Networking basics #0

## OSI Model

The OSI (Open Systems Interconnection) model is a conceptual framework that standardizes the functions of a communication system into seven distinct layers. Each layer has specific responsibilities and interacts with adjacent layers to facilitate communication between networked devices. The layers, from bottom to top, are as follows:

1. Physical Layer
2. Data Link Layer
3. Network Layer
4. Transport Layer
5. Session Layer
6. Presentation Layer
7. Application Layer

The OSI model provides a reference for network architects and developers to design and implement network protocols and technologies.

## LAN (Local Area Network)

A LAN is a computer network that connects devices within a limited geographical area, such as a home, office building, or campus. LANs are typically privately owned and allow for high-speed data transfer among connected devices. They are commonly used for sharing resources, such as files, printers, and internet connections, within a localized environment.

## WAN (Wide Area Network)

A WAN is a computer network that spans a large geographical area, connecting multiple LANs or other networks together. Unlike LANs, WANs cover vast areas and often utilize telecommunication services, such as leased lines or public networks, to establish connectivity. WANs enable long-distance communication and facilitate data exchange between geographically dispersed locations.

## Internet

The Internet is a global network of interconnected computers and networks that use the standard Internet Protocol Suite (TCP/IP). It is a vast collection of networks, including LANs, WANs, and other interconnected systems worldwide. The Internet enables the exchange of information, communication, and access to a wide range of services, such as websites, email, file sharing, and multimedia streaming. It has revolutionized the way we connect, communicate, and access information globally.

## TCP (Transmission Control Protocol) / UDP (User Datagram Protocol)

TCP and UDP are two primary transport layer protocols in the TCP/IP protocol suite used by the Internet.

TCP is a reliable, connection-oriented protocol that provides error detection, flow control, and ensures the ordered delivery of data packets. It establishes a connection between two devices, breaks data into smaller segments, numbers and sequences them, and reassembles them at the destination. TCP guarantees data integrity, making it suitable for applications where data accuracy is crucial, such as web browsing, email, and file transfer.

UDP is a lightweight, connectionless protocol that offers fast, low-overhead communication. Unlike TCP, UDP does not establish a connection or guarantee data delivery. It simply sends data packets, called datagrams, to the destination without worrying about reliability or ordering. UDP is commonly used for real-time applications, such as video streaming, online gaming, and VoIP (Voice over IP), where speed and minimal latency are more important than reliability.
