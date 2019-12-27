# X-MAS Helper

> Author: howard41436 | 楊皓丞 | B06902097, disam | 王松億 | B06705049

### Description

As organizers of X-MAS CTF, we are using bots to ensure that the competition keeps running smoothly. We have made this Discord bot: X-MAS Helper#2918 to help us check the flags for various challenges by using the !flag command. This command is safe to use because the bot actively checks if the requesting user has the Organizer role assigned, so regular participants can't access the flags.

We're so sure that the code is secure, that we're willing to share the part that checks the role:

Code:

```python
if (message.content == "!flag"):
	ok = False
for role in message.author.roles:
	if (role.name == "Organizer"):
		ok = True
	if (ok):
		printer = "The flag is: **{}**".format(FLAG)
	else:
		printer = "Unauthorized."
```

### Solution

The key point of this challenge is that discord bots can be added to different servers, and the bot's id is public in the X-MAS CTF's discord server. Therefore, the X-MAS Helper should check what server is it in in addition to the message author's role, but it didn't. So I just need to open my own server, set myself as Organizer role, invite X-MAS Helper bot into my server, than type `!flag`, then the bot will give me the flag.