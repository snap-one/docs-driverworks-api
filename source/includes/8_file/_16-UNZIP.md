## UnZip
Function for extracting files from a .zip archive. This API enables Lua drivers to extract one, or more, files from a .zip archive. See [https://en.wikipedia.org/wiki/ZIP\_(file\_format)][1]
 

_This API was introduced in O.S. Release 3.3.0._


### Signature

`C4:UnZip()`


| Parameters | Description |
| --- | --- |
| string | zipfile: A string containing the file path to the ZIP archive to be extracted. |
| string | filespec: A string containing a file specification that identifies the file, or files, to be extracted. For example, the file specification "*" matches all files in the archive. The file specification "*.lua" indicates that only Lua files are extracted. |
| string | destination: A string containing the path (directory) into which the archive is extracted. Directories within the archive are created relative to the specified destination. |


| Returns | Description |
| --- | --- |
| boolean | status: Boolean indicating whether all files were successfully extracted. true: All files were successfully extracted and no errors occurred. false: One, or more, errors occurred during extraction. |
| array | fileset: An array containing a list of files that were successfully extracted. The path for each file is relative to the archive. |
| table | errors: A two-dimensional table containing a list of files that failed to be extracted. Each file is associated with a string describing the error that occurred. |


### Examples

The examples to the right illustrate the usage of the C4:Unzip function. Note that each sample utilizes a generic Lua function called printTable that dumps the contents of a specified table. This is done to illustrate how to interpret the return values of the function. There are numerous examples of printTable online.




```xml
Example 1

result, fileset, errors = C4:Unzip("/opt/control4/var/drivers/c4z/TuneIn.c4z", "*", "/opt/control4/var/drivers/c4z/TuneIn")
print(result)
printTable(fileset)
printTable(errors)

Executing this sample produces the following output.

true
table: 0xa42c380 {
[1] => "driver.xml"
[2] => "driver.lua"
.
.
.
[287] => "www/icons/device/experience_80.png"
[288] => "www/icons/device/experience_90.png"
}
table: 0xa186b60 {
}

The output can be interpreted as follows:
The result is true, indicating that all files were extracted successfully.
The fileset array contains 288 files (truncated for display purposes) that were extracted successfully. Note that the path to each file is relative to the archive.
The errors table is empty because no errors occurred.
```


Example 2
```xml
result, fileset, errors = C4:Unzip("/opt/control4/var/drivers/c4z/TuneIn.c4z", "*.lua", "/opt/control4/var/drivers/c4z/TuneIn")
print(result)
printTable(fileset)
printTable(errors)

Executing this sample produces the following output.

true
table: 0xb68c5e0 {
[1] => "driver.lua"
}
table: 0xb5cc640 {
}

The output can be interpreted as follows.
The result is true, indicating that all files were extracted successfully.
The fileset array contains a single entry because only one file matched the file specification: "*.lua".
The errors table is empty because no errors occurred.
```


```xml
Example 3

result, fileset, errors = C4:Unzip("/opt/control4/var/drivers/c4z/TuneIn.c4z", "*.gif", "/opt/control4/var/drivers/c4z/TuneIn")
print(result)
printTable(fileset)
printTable(errors)

Executing this sample produces the following output.
```

```xml
false
table: 0xb5cc600 {
}
table: 0xb68ab00 {
[www/composer/ico_16_tunein.gif] => "Could not open file "/opt/control4/var/drivers/c4z/TuneIn/www/composer/ico_16_tunein.gif": Not a directory"
[www/composer/ico_32_tunein.gif] => "Could not open file "/opt/control4/var/drivers/c4z/TuneIn/www/composer/ico_32_tunein.gif": Not a directory"
}
```

```xml
The output can be interpreted as follows.
The result is false, indicating that one, ore more, errors occurred during extraction.
The fileset array is empty because no files were extracted.
The errors table contains two entries, one for each file matching the file specification: "*.gif". Each file is associated with a string describing the error that occurred.
```


```xml
Example 4
```

```xml
result, fileset, errors = C4:Unzip("/opt/control4/var/drivers/c4z/Bogus.c4z", "*", "/opt/control4/var/drivers/c4z/Bogus")
print(result)
printTable(fileset)
printTable(errors)

Executing this sample produces the following output.

false
table: 0xb1285e0 {
}
table: 0xb652200 {
[/opt/control4/var/drivers/c4z/Bogus.c4z] => "The specified zip file does not exist"
}

The output can be interpreted as follows:
• The result is false, indicating that one, ore more, errors occurred during extraction.
• The fileset array is empty because no files were extracted.
• The errors table contains a single entry containing the zip file itself. The associated error message indicates that the specified file does not exist.
```

[1]:	See%20https://en.wikipedia.org/wiki/ZIP_(file_format)