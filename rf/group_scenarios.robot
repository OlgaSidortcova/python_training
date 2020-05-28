*** Settings ***
Library  ../rf/AddressBook.py
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new group
    ${old_list}=  Get Group List
    ${group}=  New Group  name1  header1  footer1
    Create Group  ${group}
    ${new_list}=  Get Group List
    Append To List  ${old_list}  ${group}
    Group List Should Be Equal   ${old_list}   ${new_list}

Delete group
    ${old_list}=  Get Group List
    ${len}=  Get Length   ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${group}=  Get From List  ${old_list}  ${index}
    Delete Group  ${group}
    ${new_list}=  Get Group List
    Remove Values From List  ${old_list}  ${group}
    Group List Should Be Equal   ${old_list}   ${new_list}