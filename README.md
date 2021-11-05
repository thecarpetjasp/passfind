# passfind
A python program capable of accessing passwords associated with emails through leaked databases.
![banner](https://user-images.githubusercontent.com/71789855/140584633-77fd9f5f-164d-497a-b7be-d461d2325956.png)

#

A python program capable of accessing passwords associated with emails through leaked databases. Input any email address into passfind to find leaked passwords associated with the account.
*All credit for accessing these databases goes to:* [breachdirectory.org](https://breachdirectory.org)




*Why would I want this program?*

Passfind is a great way to experience all the perks that [breachdirectory.org] has to offer. Searches made on [breachdirectory.org] are limited to semi-clear text passwords. Thankfully a hash is provided, which wlll allow you to crack and access the full clear text password for yourself. However, depending on the length of the password, what number of characters are already revealed to you and having to crack each one individually, this can be quite time consuming. 

Passfind utilies breachdirectory's API key which will give you **all** full clear text passwords, hashes and source of the leak in a matter of seconds. Just simply enter in an email address and get your results.

Benefits:
  * Full clear text passwords
  * Source information
  * FREE API access

*Each API is limited to 50 searches per month. You can upgrade your API anytime by visiting* [Breachdirectory API Upgrade](https://rapidapi.com/rohan-patra/api/breachdirectory/pricing)


#


**INSTALL AND LAUNCH**

**Step (1):**
`git clone https://github.com/thecarpetjasp/passfind`



**Step (2):**
`cd passfind`


**Step (3): (OPTIONAL)**
`python3 install.py`
*This step will add the program to '/usr/bin/' so that you can run the program anywhere from your terminal.*


**Step (4):**
`python3 passfind.py`
or if you followed step (3):
`passfind`


#


**SETUP**

Before you can begin using PassFind - you will need BreachDirectory's FREE API key.

Head on over to [https://rapidapi.com/rohan-patra/api/breachdirectory](https://rapidapi.com/rohan-patra/api/breachdirectory) or visit [breachdirectory.org](https://breachdirectory.org) and go to API. From there, create your free account.

Once your account is set up, head back to [https://rapidapi.com/rohan-patra/api/breachdirectory](https://rapidapi.com/rohan-patra/api/breachdirectory) and click on **subscribe**. Once you've subscribed, your API key should now be valid. You API key can be found under **GET Index** labelled *X-RapidAPI-Key*. You can copy your API on the right hand side of the page under **Code Snippet** where once again it is labelled *X-RapidAPI-Key*.



Now all thats left to do is to apply your API to the program. You can do so with `nano passfind.py` / `nano passfind` and entering your API key into the variable below the note #ENTER YOUR API KEY BELOW.

*Remember, if you followed step (3) to 'INSTALL AND LAUNCH', then passfind.py will be stored at '/usr/bin/' - Full directory: '/usr/bin/passfind'.*
