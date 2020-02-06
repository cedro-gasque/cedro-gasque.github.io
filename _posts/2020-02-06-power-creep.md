---
layout: post
title: "Power Creep"
subtitle: How creatures have improved over time
tags: [mtg, python, data-science]
image: /img/gray-ogre.PNG
---

There is always this pervasive idea of "power creep" in games like Magic: the Gathering.

The idea that the power level of game elements increase over time as the creators have to
create new elements that can outcompete old game elements in order to sell their newer product.

![Power Creep versus R&D at Wizards of the Coast headquarters.](https://img.scryfall.com/cards/art_crop/front/7/8/789965c4-f3c8-4ef3-8854-9b4016356d20.jpg){: .center-block :}

_Power creep: the [Kudzu](https://scryfall.com/card/ced/205/kudzu) of game design._ {style=text-align:center}

After doing this analysis, I learned that the increase in creature power level was intentional,
as spells were notoriously more powerful than creatures, and the coolest creatures were often the worst.
You can read [this wonderful blog post from 2013](https://magic.wizards.com/en/articles/archive/latest-developments/where-wild-things-are-2013-11-15)
about the idea of creature power level. 

But the information is still interesting to look at (especially when you see where it spikes and drops).

# Driving Question:

## Can you visualize the idea of "power creep" in Magic: the Gathering?

I imported my data from a wonderful source called [Magic: The Gathering Developers](https://magicthegathering.io/), using their Python SDK.