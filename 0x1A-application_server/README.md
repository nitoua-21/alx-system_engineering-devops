![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240907%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240907T135454Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0d114121bf9b83e4212c14ffbe086e24d9c7ab3ca94a40a5885bfac439074a1e)

Background Context
------------------

[![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/2ea1058f813d42c61f48.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240907%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240907T135454Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=53eb847b4bd649db3ffc349da4448393a860e8db31d75a4df5f2756e1cb1933c)](https://youtu.be/pSrKT7m4Ego)

Your web infrastructure is already serving web pages via `Nginx` that you installed in your [first web stack project](/rltoken/95oRNZ-zRGwLxtWECJqsWA "first web stack project"). While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your `Nginx` and make is serve your Airbnb clone project.

Resources
---------

**Read or watch**:

*   [Application server vs web server](/rltoken/meOqLRoAcbQENYWfzui7OQ "Application server vs web server")
*   [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](/rltoken/kpG6RwmwRJHzRmGUM_ERcA "How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04") (As mentioned in the video, do **not** install Gunicorn using `virtualenv`, just install everything globally)
*   [Running Gunicorn](/rltoken/2LF1j7xKJGYaUtD1HKgUeQ "Running Gunicorn")
*   [Be careful with the way Flask manages slash](/rltoken/zTCSTQxrH2za4hxbkt8K3g "Be careful with the way Flask manages slash") in [route](/rltoken/n5A0nmah-Si78zbNvdb4GA "route") - `strict_slashes`
*   [Upstart documentation](/rltoken/cldrneY3Qr7LlDysygzRHw "Upstart documentation")

Requirements
------------

### General

*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Everything Python-related must be done using `python3`
*   All config files must have comments

### Bash Scripts

*   All your files will be interpreted on Ubuntu 16.04 LTS
*   All your files should end with a new line
*   All your Bash script files must be executable
*   Your Bash script must pass `Shellcheck` (version `0.3.7-5~ubuntu16.04.1` via `apt-get`) without any error
*   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
*   The second line of all your Bash scripts should be a comment explaining what is the script doing
