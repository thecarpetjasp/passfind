# PASSFIND
![banner](https://user-images.githubusercontent.com/71789855/140584633-77fd9f5f-164d-497a-b7be-d461d2325956.png)

A python program capable of accessing passwords associated with emails through leaked databases.


#

A python program capable of accessing passwords associated with emails through leaked databases. Input any email address into passfind to find leaked passwords associated with the account.
*All credit for accessing these databases goes to:* [breachdirectory.org](https://breachdirectory.org)




*Why would I want this program?*

Passfind is a great way to experience all the perks that [breachdirectory.org] has to offer. Searches made on [breachdirectory.org] are limited to censored passwords. A hash is provided, which wlll allow you to crack and access the full clear text password for yourself. However, depending on the length of the password, what number of characters are already revealed to you and having to crack each one individually, this can be quite time consuming. 

Passfind utilises breachdirectory's API key which will give you **all** full clear text passwords, hashes and source of the leak in a matter of seconds. Just simply enter in an email address and get your results.

Benefits:
  * Full clear text passwords
  * Source information
  * FREE API access

*Each FREE API is limited to 50 searches per month. You can upgrade your API anytime by visiting* [Breachdirectory API Upgrade](https://rapidapi.com/rohan-patra/api/breachdirectory/pricing)

#



![found_passwords](https://user-images.githubusercontent.com/71789855/141419652-6a8236a9-1f12-4d26-8a7b-3097d6cec5af.jpg)


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

*(NOTICE!) A recent update to BreachDirectory has effected the use of their API keys. Until this is resolved, please continue to use the PASSCRACK feature for this program instead.* 

*(UPDATE!) A new update has been added to PassFind. You can now resume searching as usual. However, due to the changes that were made on BreachDirectory, each password that is cracked for WILL be counted as a single search. So, for 5 passwords cracked on a single email, will now be counted towards as 5 searches of your monthly searches. I wouldn't want to recommend finding a way to avoid paying for an API key... But, if these changes affect how much you get to use your free account, I would suggest creating multiple free accounts...*

Before you can begin using PassFind - you will need BreachDirectory's FREE API key.

Head on over to [https://rapidapi.com/rohan-patra/api/breachdirectory](https://rapidapi.com/rohan-patra/api/breachdirectory) or visit [breachdirectory.org](https://breachdirectory.org) and click API. From there, create your free account.

Once your account is set up, head back to [https://rapidapi.com/rohan-patra/api/breachdirectory](https://rapidapi.com/rohan-patra/api/breachdirectory) and click on [**Subscribe to test**], then choose free BASIC plan. Once you've subscribed, your API key should now be valid. Your API key can be found under **GET Index** labelled *X-RapidAPI-Key*. You can copy your API on the right hand side of the page under **Code Snippet** where once again it is labelled *X-RapidAPI-Key*.



Now all thats left to do is to apply your API to the program. You can do so with `nano passfind.py` / `nano passfind` and entering your API key into the variable below the comment 'ENTER YOUR API KEY BELOW'.

*Remember, if you followed step (3) to 'INSTALL AND LAUNCH', then passfind.py will be stored at '/usr/bin/' - Full directory: '/usr/bin/passfind'.*



#



**(NEW UPDATE) *PASSCRACK INTRODUCTION***

PASSFIND is now introducing it's new feature; PASSCRACK!

PASSCRACK does not depend on any API key whatsoever. So if you find yourself out of all 50 queries for the month, PASSCRACK will immediately take action.

Yes, this means PASSCRACK is unlimited! There is a small price to pay however. Each password must be cracked individually, there is no way to access clear text passwords all at once. Each password can take anywhere from 1 minute to several hours to crack. No source information is available for any cracked password.

To get started, head on over to [breachdirectory.org](https://breachdirectory.org) and input the target email to receive your censored passwords and their encrypted SHA-1 hashes. That's all PASSCRACK needs! Just input the censored password you wish to crack, followed by it's SHA-1 hash and let PASSCRACK do it's job.

I highly recommend using [weleakinfo.to](https://weleakinfo.to) if censored characters exceed more than 4 characters long. Unless you have the computing power and the storage capacity to execute such a big task, then PASSCRACK will give you the choice to do so. [Weleakinfo.to](https://weleakinfo.to) display the same censored passwords in exact same order, except they always and only censor the last 4 characters. This will cut out a huge amount of time and computing power, with cracking speeds always being more or less under 1 minute long. Attempting to create such large dictionaries where censored passwords contain more than 4 censored characters will result in longer waiting times and more storage capacity. For this reason, it is always recommended using [weleakinfo.to](https://weleakinfo.to) if censored passwords contain more than 4 censored characters. 


Please **always** use the hash provided to you by [breachdirectory.org](https://breachdirectory.org).

#

![passcrack_intro](https://user-images.githubusercontent.com/71789855/141419655-1397bff1-2f94-4aac-974a-e3bf790bb1e9.png)

#
![cracked_result](https://user-images.githubusercontent.com/71789855/141419650-939bb79a-b5c0-4afc-a2d7-fc1fe81becde.jpg)

#
*PASSCRACK is currently exclusive to Linux users only. A Windows update will be coming shortly!*
