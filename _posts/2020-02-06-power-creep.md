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

<p align="center"><i>Power creep: the <a href="https://scryfall.com/card/ced/205/kudzu">Kudzu</a> of game design.</i></p>

After doing this analysis, I learned that the increase in creature power level was intentional,
as spells were notoriously more powerful than creatures, and the coolest creatures were often the worst.
You can read [this wonderful blog post from 2013](https://magic.wizards.com/en/articles/archive/latest-developments/where-wild-things-are-2013-11-15)
about the idea of creature power level. 

But the information is still interesting to look at (especially with drastic shifts in power level between sets).

## Driving Question: Can you visualize the idea of "power creep" in Magic: the Gathering?

The first step was determining how I would measure power level objectively. The most obvious data I had access to was each creature's cost, power and toughness.

I imported my data from a wonderful source called [Magic: The Gathering Developers](https://magicthegathering.io/), using their Python SDK.

![Power]

First step was cleaning my data. I didn't care about the text, rulings, or translations,
so I ended up dropping a lot of the columns.
I was also only going to analyze creatures, so I dropped everything that was not a creature.
Finally, I left out a long list of sets that were all reprints or
non-competitive sets without enough unique cards to represent useful sample sizes.

I ended up with a still pretty large dataset even after so many exclusions, with over 10000 unique cards.

The next step was actually creating the data point I would be comparing.
This wasn't very difficult, as I just used the ratio between
the total power and toughness and the converted mana cost of each card.