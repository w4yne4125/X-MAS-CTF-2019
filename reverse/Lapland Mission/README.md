# Lapland Mission

> Author: howard41436 | 楊皓丞 | B06902097, devin6011 | 林首志 | B06902049

### Description

I have been trying to win at this game for a while now, but whatever I do there's always a robot that shoots me dead :(

Can you help me win please?

source: [X-MAS Lapland Mission.zip](https://drive.google.com/open?id=1pSe5wVzYU7kC69v7oFGoPT13Sm5W2PBh)

### Solution

This is a game written in Unity, we have to kill all robots to win, but the robots shoot us dead about 0.1 seconds after it see us.

After some searching, we found out that every game class is stored in `Data/Managed/Assembly-CSharp.dll`, and we can modify and recompile it using dnSpy. At first, I changed the robots' reaction time to a very large number, but it is too time-consuming to shoot all of them dead. So I let the game manager render the winning screen at the start of the game, and easily get the flag when I reopened the game.