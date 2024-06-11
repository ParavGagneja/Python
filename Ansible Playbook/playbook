Assume you have just installed the latest version of CentOS 7.x on a VM with GNOME Desktop. You need to configure it so that you can use it for doing the Labs for OPS445.
Study the documentation and examples of following ansible modules:
copy
file
hostname
template
user
yum
Create an ansible playbook named "config_ops445.yml" using the appropriate modules to perform the following configuration tasks on your assigned VM:

update Apache (httpd) installed in the Investigation 2 - Part 2
install extra packages repository for enterprise Linux (EPEL) if it is not already installed
remove 'tree' package
set the hostname to your Seneca username (Seneca ID)
create a new user with your Seneca_ID with sudo access
configure the new user account you created above so that you can ssh to it without password
setup a directory structure using a loop for completing and organizing labs as shown below:
      /home/[seneca_id]/ops445/lab1
      /home/[seneca_id]/ops445/lab2
      /home/[seneca_id]/ops445/lab3
      /home/[seneca_id]/ops445/lab4
      /home/[seneca_id]/ops445/lab5
      /home/[seneca_id]/ops445/lab6
      /home/[seneca_id]/ops445/lab7
      /home/[seneca_id]/ops445/lab8
      /home/[seneca_id]/ops445/lab9
when it's ready, run your playbook
in order to test it, log into the VM with the newly created user (your Seneca_ID), install the 'tree' package with sudo, and check the directory structure with the 'tree' command
if everything is correct, capture its output for a successful run of your playbook to a file named "lab9_[seneca_id].txt"
