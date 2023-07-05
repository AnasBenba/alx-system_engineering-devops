# Networking basics #1

## Localhost and 127.0.0.1

The term "localhost" refers to the current machine or computer itself. It typically resolves to the IP address "127.0.0.1", which is the loopback address. When you access "localhost" or "127.0.0.1", you are connecting to the local network interface of your machine.

## 0.0.0.0

The IP address "0.0.0.0" has different meanings depending on the context. In the case of network configuration, it can serve as a default gateway or indicate that a service is listening on all available network interfaces. It represents all available IP addresses on the current network interface or acts as a "wildcard" or "any" address.

## /etc/hosts

The "/etc/hosts" file is a plain text file used by the operating system to map hostnames to IP addresses. It allows you to define custom mappings of hostnames to IP addresses, bypassing the need for DNS resolution. This file is often used for local customizations and can be edited to associate specific hostnames with desired IP addresses.

## Displaying Active Network Interfaces

To view the active network interfaces on your machine, you can use the ifconfig or ip command. These commands provide detailed information about each interface, including IP addresses, MAC addresses, and other relevant details.

## Using ifconfig

The ifconfig command is used to display and configure network interfaces. To view the active network interfaces, follow these steps:

1. Open a terminal or command prompt.
2. Enter the following command:

```
ifconfig
```

3. Press Enter.
4. The output will display the active network interfaces, along with their IP addresses, MAC addresses, and additional information.

## Telnet

Telnet is a network protocol used to establish remote terminal connections. It allows you to connect to remote systems and interact with them through a command-line interface. The `telnet` command is used to initiate a telnet session by specifying the target host and port.

## Netcat (nc)

Netcat, or `nc`, is a versatile networking utility used for reading from and writing to network connections. It can function as a basic TCP/UDP port scanner, create network connections, and transfer data between systems. The `nc` command can be used to establish connections, listen on ports, and perform various network-related tasks.

## Cut

The `cut` command is used to extract specific sections or fields from lines of text. It is often used for manipulating and filtering text-based data. By specifying a delimiter, `cut` can extract specific columns or fields from files or command output, making it a handy tool for data processing.
