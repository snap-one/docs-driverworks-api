
## What’s New in 3.3.0


**C4SSH Interface**

The DriverWorks API has been expanded with the addition of the new C4SSH API. This API enables Lua drivers to establish an SSH client connection to a remote device and execute a series of commands. A driver creates an instance of a C4SSH object by calling the[ C4:CreateSSHClient][1] function.



**File Interface**

As part of Control4’s plan to tighten driver security, the io.popen() call has bee removed. In doing this, driver developers need to use C4:File commands to accomplish what they previously did with io.popen (). The following APIs have been added or modified in support of this effort:

A new API: [FileCreateDir][2] has been added. This function has been added to create a new file directory. 

The [FileDelete][3] function has been modified in conjunction with O.S. release 3.3.0.  

A new API: [FileMove][4] has been added. This function moves files within certain restrictions.  

The [FileSetDir][5] has been modified In conjunction with O.S. release 3.3.0. This function is being restricted to allowed locations whereas previously it had full root access.

Additionally, a new API: [UnZip][6] has been added. This API enables Lua drivers to extract one, or more, files from a .zip archive.



**Helper Interface**

A new API: [GetCodeItems][7] has been added. This function returns Code Items for a specified device and event.

A new API: [GetAllCodeItems][8] has been added. This function returns all Code Items within the project.

A new API: [GetBootID][9] has been added. This function returns a string that contains an ID which is unique for the current kernel instance.  When the controller is re-booted, the ID will change.

A new API: [UUID][10] has been added. This function generates a UUID (Universally Unique IDentifier). This function has also been added to tighten driver security and support the removal of the the io.popen() call.

A new API: CreateTLSServer has been added. This function enables a Lua driver to create a new secure SSL/TLS server that listens for incoming connections on a specified port.

[1]:	https://snap-one.github.io/docs-driverworks-api/#createsshclient
[2]:	https://snap-one.github.io/docs-driverworks-api/#filecreatedir
[3]:	https://snap-one.github.io/docs-driverworks-api/#filedelete
[4]:	https://snap-one.github.io/docs-driverworks-api/#filemove
[5]:	https://snap-one.github.io/docs-driverworks-api/#filesetdir
[6]:	https://snap-one.github.io/docs-driverworks-api/#unzip
[7]:	https://snap-one.github.io/docs-driverworks-api/#getcodeitems
[8]:	https://snap-one.github.io/docs-driverworks-api/#getallcodeitems
[9]:	https://snap-one.github.io/docs-driverworks-api/#getbootid
[10]:	https://snap-one.github.io/docs-driverworks-api/#uuid