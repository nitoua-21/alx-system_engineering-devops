
### 0x0B. SSH

Background Context
------------------

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/244/zPVRKhPsUP5lK.gif)

Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using `ssh`. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of [a previous project](/rltoken/UQIQV4HJGvBv0qrHhlDFaQ "a previous project") shared in your [intranet profile](/rltoken/8ZlNV0J-sa-dijhmhJolOg "intranet profile").

You can access your server information in the [my servers](/rltoken/e2_s_pXwBVuYbhrvoesfrg "my servers") section of the intranet, each line with contains the IP and username you should use to connect via `ssh`.

**Note:** Your server is configured with an Ubuntu 20.04 LTS environment.

Resources
---------

**Read or watch**:

*   [What is a (physical) server - text](/rltoken/dkgW9lKiBRiUZHfq0MDJuw "What is a (physical) server - text")
*   [What is a (physical) server - video](/rltoken/AxFcTdcXUCsrVp01X_EbFA "What is a (physical) server - video")
*   [SSH essentials](/rltoken/ux0eM1QU9reNyG45b0erAQ "SSH essentials")
*   [SSH Config File](/rltoken/Rc9FpSy4ZaQWPlcWLinbNw "SSH Config File")
*   [Public Key Authentication for SSH](/rltoken/tOcxk5mtkedBM0WxyDZxTw "Public Key Authentication for SSH")
*   [How Secure Shell Works](/rltoken/j0atjRrVfZ6F810qmPfAzA "How Secure Shell Works")
*   [SSH Crash Course](/rltoken/FKqd8CjxExmpWGu6xGavKw "SSH Crash Course") (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)

**For reference:**

*   [Understanding the SSH Encryption and Connection Process](/rltoken/JB-Vi4dR3q6nF4MBhsn8kQ "Understanding the SSH Encryption and Connection Process")
*   [Secure Shell Wiki](/rltoken/SpiYWE79Yfr_vWDg42dzCw "Secure Shell Wiki")
*   [IETF RFC 4251 (Description of the SSH Protocol)](/rltoken/f2O0OQq9tch2MYeNAzkg5w "IETF RFC 4251 (Description of the SSH Protocol)")
*   [Internet Engineering Task Force](/rltoken/gd1W1UvB0KeJVWwM8BLvhA "Internet Engineering Task Force")
*   [Request for Comments](/rltoken/jb-IrnQnUh-PsEDlbAU0Kw "Request for Comments")

**man or help**:

*   `ssh`
*   `ssh-keygen`
*   `env`

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/0Wgw_i87NIVCfUcRzdZgkg "explain to anyone"), **without the help of Google**:

### General

*   What is a server
*   Where servers usually live
*   What is SSH
*   How to create an SSH RSA key pair
*   How to connect to a remote host using an SSH RSA key pair
*   The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`

### Copyright - Plagiarism

*   You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
*   You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
*   You are not allowed to publish any content of this project.
*   Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
------------

### General

*   Allowed editors: `vi`, `vim`, `emacs`
*   All your files will be interpreted on Ubuntu 20.04 LTS
*   All your files should end with a new line
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   All your Bash script files must be executable
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
*   The second line of all your Bash scripts should be a comment explaining what is the script doing