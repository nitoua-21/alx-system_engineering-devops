### ALX Software Engineering - Tasks for Project 0x00. Shell, basics

`0-current_working_directory` : prints the absolute path name of the current working directory.

`1-listit` : displays the contents list of your current directory.

`2-bring_me_home` : changes the working directory to the user’s home directory

`3-listfiles`: displays current directory contents in a long format

`4-listmorefiles`: displays current directory contents, including hidden files (starting with .).

`5-listfilesdigitonly`: displays current directory contents in Long format with user and group IDs displayed numerically and hidden files (starting with .)

`6-firstdirectory`: creates a directory named my_first_directory in the /tmp/ directory.

`7-movethatfile`: moves the file betty from /tmp/ to /tmp/my_first_directory.

`8-firstdelete`: deletes the file betty from /tmp/my_first_directory

`9-firstdirdeletion`: deletes the directory my_first_directory that is in the /tmp directory.

`10-back`: changes the working directory to the previous one.

`11-lists`: lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.

`12-file_type`: prints the type of the file named iamafile, located in /tmp

`13-symbolic_link`: creates a symbolic link to /bin/ls, named __ls__.  in the current working directory

`14-copy_html`: copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

`100-lets_move`: moves all files beginning with an uppercase letter to the directory /tmp/u

`101-clean_emacs`: deletes all files in the current working directory that end with the character ~

`102-tree`: creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.

`103-commas`: lists all the files and directories of the current directory, separated by commas (,).

`school.mgc`: a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.
> The `school/mgc` file is generated in 2 steps:
> Step 1: create a `school` file with the synthax bellow
> `0 string SCHOOL School data file
> !:mime School`
> Step 2: Compile the file to generate a magaic file
> `file -C -m school`
> A `school.mgc` file will be generated.

### Ressources
- [What Is “The Shell”?](http://linuxcommand.org/lc3_lts0010.php)
- [Navigation](http://linuxcommand.org/lc3_lts0020.php)
- [Looking Around](http://linuxcommand.org/lc3_lts0030.php)
- [A Guided Tour](http://linuxcommand.org/lc3_lts0040.php)
- [Manipulating Files](http://linuxcommand.org/lc3_lts0050.php)
- [Working With Commands](http://linuxcommand.org/lc3_lts0060.php)
- [Reading Man pages](http://linuxcommand.org/lc3_man_pages/man1.html)
- [Keyboard shortcuts for Bash](https://www.howtogeek.com/181/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/)
- [LTS](https://wiki.ubuntu.com/LTS)
- [Shebang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29)
