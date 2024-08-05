# Known Issues

## 1. Searching Tags with Whitespace
- when searching for tags that appear in piping plans, the text extracted 
  contains additional white space that causes the tag to not be found.

  E.g., the following tags are not found in PIDs or mechanical-process
  piping plans:

  - HV-CA01-083
  - HV-CA01-084
  - HV-CA01-123
  - HV-CA01-125
  - POU-CA01-005
  - POU-CA01-016
  - POU-CA01-021
  - POU-CA01-022

  But these tags are found when searched with extra whitespace:
  - HV -CA01 -083
  - HV -CA01 -084
  - HV -CA01 -123
  - HV -CA01 -125
  - POU -CA01 -005
  - POU -CA01 -016
  - POU -CA01 -021
  - POU -CA01 -022

  There could be several other tags on PIDs and piping plans that may not have
  initially been found due to extra whitespace.

  Need to modify search algorithm to be able to find these tags that may be 
  improperly formatted. 