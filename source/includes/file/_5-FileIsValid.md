## FileIsValid

Used to see if a file is still valid to be written or read from. This is useful to check before or after reading to see if an end of file condition has been reached. This function returns a bool of the file status. This API can be invoked during OnDriverInit.

###### Available from 1.6.0.



### Signature

`C4:FileIsValid`



### Example

`isOkay = C4:FileIsValid(fh)`	