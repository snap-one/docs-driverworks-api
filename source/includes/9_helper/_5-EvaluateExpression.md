## EvaluateExpression

EvaluateConditional evaluates the expression and returns a Boolean result. This API has 3 parameters, a logic operator and two operands.  ‘value1’ is the left operand and ‘value2’ is the right operand. 

###### Available from 2.10.0


### Signature

`C4:EvaluateExpression(logic, value1, value2)`


| Parameter | Description |
| --- | --- |
| logic | Operator used in the conditionals. The following strings are accepted:
| | EQUAL |
| | NOT\_EQUAL |
| | LESS\_THAN | | LESS\_THAN\_OR\_EQUAL |
| | GREATER\_THAN |
| | GREATER\_THAN\_OR\_EQUAL |
| value 1 | Left operand of the expression |
| value 2 | Right operand of the expression |


### Returns

`True or False`


### Example

`C4:EvaluateExpression("GREATER_THAN_OR_EQUAL", 50, 0)`

In the example above, the expression could be written as “result = (50 \>= 0)” and would evaluate to result being equal to “true”.