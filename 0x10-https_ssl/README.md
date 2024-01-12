# 0x10. HTTPS SSL

## HTTPS and SSL: Main Roles
### HTTPS (Hypertext Transfer Protocol Secure)
HTTPS is a secure version of HTTP, the protocol used for transferring data between a user's web browser and the website they are visiting. The "S" in HTTPS stands for "Secure," indicating that the communication between the user's browser and the website is encrypted and secure.

## SSL (Secure Sockets Layer)
SSL is the predecessor to the Transport Layer Security (TLS) protocol, but the terms are often used interchangeably. SSL/TLS protocols provide a secure communication channel over the internet, ensuring the confidentiality and integrity of data exchanged between the user and the website.

The two main roles of HTTPS and SSL are:

1. **Encryption**: The primary role of SSL/TLS is to encrypt the data transmitted between the user's browser and the web server. Encryption ensures that even if a malicious actor intercepts the communication, they would not be able to understand the content without the proper decryption key.

2. **Authentication**: SSL/TLS protocols also provide a means of authenticating the identity of the web server. This helps users trust that they are connecting to the legitimate website and not a malicious impersonation. Authentication is achieved through the use of digital certificates.

## Purpose of Encrypting Traffic
The purpose of encrypting traffic, achieved through the use of SSL/TLS, is to enhance the security and privacy of information transmitted over the internet. By encrypting data, sensitive information such as login credentials, personal details, and financial transactions are protected from unauthorized access and eavesdropping.

Key benefits of encrypting traffic include:

- Confidentiality: Encryption ensures that only authorized parties can access and understand the information being transmitted.

- Integrity: It prevents tampering or alteration of data during transmission, ensuring that the received data is the same as what was sent.

- Authentication: SSL/TLS helps verify the identity of the server, assuring users that they are connecting to the intended website and not a malicious entity.

## SSL Termination
SSL termination refers to the process of decrypting the encrypted traffic at the point of entry, typically at a load balancer or a reverse proxy, before forwarding it to the web server. This allows the web server to process the unencrypted data, improving efficiency and reducing the computational load on the server.

SSL termination is commonly used in scenarios where the decryption of traffic is offloaded from the web server to a dedicated device, enhancing overall system performance and scalability.

By understanding these concepts, you can appreciate the crucial roles of HTTPS and SSL in securing online communications and protecting sensitive data from potential threats.