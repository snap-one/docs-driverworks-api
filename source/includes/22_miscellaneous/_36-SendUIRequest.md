## SendUIRequest

Function that sends a request to another driver. It uses the proxy or protocol ID value of the driver as a means to target the driver where the request will be sent. The driver receiving the SendUIRequest must have an a UIRequest function configured which will contain the return values requested by the SendUIRequest call.

###### Available from 2.9.0


### Signature

`C4:SendUIRequest (int,string, tParams)`


| Parameter | Description |
| --- | --- |
| int | Proxy or protocol ID value of the driver receiving the SendUIRequest |
| str | Request to send in string format |
| table | Table containing values sent with the request. If no values are needed an empty table must be sent. |


### Returns

Data is returned to the driver sending the SendUIRequest in XML format.


### Examples

`C4:SendUIRequest(231, "GET_MY_DRIVER_DATA", tParams)`

The above example is used below in a driver initiating the SendUIRequest. In this example, the API contains a value of 231. This is the proxy ID value of the driver where the request is being sent. This is followed by a request called  `GET_MY_DRIVER_DATA`. This is an expected request by the driver receiving the SendUIRequest. A table of parameters follows the command.  

	function TestUIRequest()
		local tParams = {}
		tParams["PARAM_X"] = 1024
		tParams["PARAM_Y"] = 768
		C4:SendUIRequest(231, "GET_MY_DRIVER_DATA", tParams)
	end

To the right is an example of the required UIRequest found in the driver receiving the SendUIRequest. In this example, when the request is received it takes the values in the tParams table and, if they are not a specified value of 640 or 480, multiplies them by 10. It then formats the values into XML and returns them through retValue to the driver that initiated the SendUIRequest.

	function UIRequest(sRequest, tParams)
	    tParams = tParams or {}
	    local param_x = tonumber(tParams["PARAM_X"]) or 640
	    local param_y = tonumber(tParams["PARAM_Y"]) or 480
	               
	         local value_x = param_x * 10
	         local value_y = param_y * 10
	               
	         local retValue = "<driver_data>"
	         retValue = retValue .. "<value_x>" .. value_x .. "</value_x>"
	         retValue = retValue .. "<value_y>" .. value_y .. "</value_y>"
	         retValue = retValue .. "</driver_data>"
	               
	    return retValue
	end

The XML below is the returned value.

	--Returned Value
	
	<driver_data>
	    <value_x>10240</value_x>
	    <value_y>7680</value_y>
	</driver_data>
