# Processes and Signals

## Introduction

In a Unix-like operating system, a process is an instance of a running program. It consists of the program code, along with its associated data, stack, and heap. Each process is assigned a unique identifier called the process ID (PID).

Processes communicate with each other and the operating system through signals. Signals are software interrupts that are used to notify processes of various events or to request a specific action. Signals can be sent by the operating system, other processes, or by the process itself.

This README provides an overview of processes and signals in Unix-like systems, along with some common operations and concepts related to them.

## Process States

A process can be in one of the following states:

- Running: The process is currently being executed by the CPU.
- Waiting: The process is waiting for a specific event to occur or for a resource to become available.
- Stopped: The process has been stopped, usually by receiving a signal. It can be resumed later.
- Zombie: The process has completed execution, but its entry still exists in the process table until its parent process acknowledges its termination.
- Terminated: The process has finished execution and exited.

## Process Management

Unix-like operating systems provide several commands and functions to manage processes. Here are some commonly used ones:

- `ps`: The `ps` command displays information about currently running processes.
- `top`: The `top` command provides real-time information about processes, CPU usage, and memory usage.
- `kill`: The `kill` command is used to send a signal to a process. By default, it sends the `SIGTERM` signal, which is used to request the termination of a process.
- `killall`: The `killall` command sends a signal to all processes with a given name.
- `fork()`: The `fork()` system call is used to create a new process by duplicating the existing process. The child process gets a new PID, and both the parent and child processes continue execution from the point of the `fork()` call.
- `exec()`: The `exec()` system call is used to replace the current process with a new process. It loads a new program into the current process's memory space and starts its execution.
- `wait()`: The `wait()` system call is used by a parent process to wait for the termination of its child process.
- `exit()`: The `exit()` function is called by a process to terminate its own execution.

## Signals

Signals are represented by unique integer values and are identified by their names starting with `SIG`. Here are some commonly used signals:

- `SIGINT` (2): Sent to interrupt a process by pressing `Ctrl+C` in the terminal.
- `SIGKILL` (9): Sent to force a process to terminate immediately.
- `SIGTERM` (15): Sent to request a process to terminate gracefully.
- `SIGSTOP` (19): Sent to stop a process. It can be resumed later using `SIGCONT`.
- `SIGCONT` (18): Sent to resume a stopped process.
- `SIGHUP` (1): Sent to indicate that a controlling terminal has been disconnected.
- `SIGUSR1` (10) and `SIGUSR2` (12): User-defined signals that can be used for specific purposes.
Signals can be sent to processes using the `kill` command or programmatically using the `kill()` system call in C/C++.

## Signal Handling

A process can define its own behavior when it receives a signal by handling the signal. Signal handling involves associating a specific action with a signal using the `signal()` or `sigaction()` system calls. The actions can be one of the following:

- `SIG_DFL` (default action): The default action associated with the signal.
- `SIG_IGN` (ignore signal): The signal is ignored, and no action is taken.
A custom signal handler function: A user-defined function that gets executed when the signal is received.
The custom signal handler function can perform various actions based on the received signal, such as cleaning up resources, saving data, or terminating the process.

## Conclusion

Processes and signals play a crucial role in Unix-like operating systems for managing program execution, inter-process communication, and handling events. Understanding processes and signals is essential for developing robust and responsive software in these environments. This README provides a basic overview of processes, signals, and their management, but there are many more advanced concepts and techniques to explore in this area.
