# SupaSorter

I am building Supa Sorter as my first real live project, really so I can practice; getting something actually built, startting to use GitHub, iterating the project to improve it, hopefully you will take a look at it and help me improve it too!

1. I wanted to learn how to build sorting algorithms as a way of practicing my developing coding skills.
2. I was interested to understand how effective different sorts are on differing environments.
3. I was keen to build an app that really does something so I can then refactor and improve iterably.
4. Ideally I will get a version of this so anyone can run it and upload data so I can explore the speed of different set ups, perhaps create a web service to let people run the tests and compare their system speeds against others.

Current Features

- Generates a random data set, length determined by the user.
- Runs 10 different sorts, using the Python sort method as the baseline, it really is incredibly fast!
- Shows how long each sort takes.
- Compares all the resulting sorted lists to make sure they match the baseline.
- There are now two options:
- 1. Runs all the sorts once, for a user defined sample size and then outputs a bar chart of the results
- 2. Runs all the sorts multiple times for increasing sample sizes and outputs a plot of the results to see how well (or otherwise) different sorts scale

Future Features

- Save the data to JSON or Excel
- User the the filename of the file to record hardware/OS te searches were done on
- Upload to a data repository
- Compare your speed results to others with similar/different systems
- Refactor code!
- Investigate different timing mechanism, current one works but is a little clunky and there is lots of repeated ciode.
