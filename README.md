# Computing for Life Sciences Final Project
Created December 2024 by Abigail Greenway

## Project / Assignment Goals
### Program Purpose
I want this program to help me quickly understand my cohort's behavior data from SPSS. This will help me assign experimental groups, which is a process we need done frequently and quickly.

We need our groups to have similar behavior histories (lever presses, infusions) to be able to say our manipulation actually caused the difference between them. We save data in SPSS to run statistics and move it to Prism for graphing.

**Graphs are the easiest way to find specific individuals that are making a group uneven (and importantly, visual data are what my PI wants to see). BUT: Prism has an entirely different data layout from SPSS, which is tedious to manage.**

If I can have a program just read my SPSS data, graph it, and annotate it, I wouldn't need Prism for graphs that I need frequently and quickly.

*I originally discussed a program that processes raw output files from our operant chambers. It turns out 1) these files need to be exported, and 2) the lab already has an excel file that can bin the exported data. Instead, the project I've described above isn't currently automated, and I think it will help me if not the whole lab.* 

### Things I want this code to do:

**Use concepts introduced in the class:**
1. Organize the program into folders
2. Section the code into modules for ease of use and debugging
3. Batch process files, don't read / process individually
4. Optimize, lint, notate (comment), and document (readme) the program

**Process my data:**
1. Read in my .csvs from SPSS correctly, not as strings
2. Recognize groups and sort subjects into them
3. Calculate some basic information and statistics about the groups
4. Output this information to the "data" folder
5. Plot behavior data over time for the groups
6. Output this information to the "plots" folder

*Wishlist of bonus features:*
1. Recognize outlier subjects and recommend them for removal from the group.
2. Graphs that are really nice to look at.
3. Extremely simple execution (click the python file and it's done) so that my noncoding colleagues can use this.

## Data Layout
This program will run on an SPSS file template that organizes data based on the stage of behavior that the animals are in. You can see the appendix for a more detailed explanation of the project and timeline.
|Column Name| Data Meaning |
| --------- |:------------:|
|ID         | Rat ID, values are DT01 - DT23|
|Sex        |0 = Male, 1 = Female|
|Group      |0 = No react (control), 1 = React (experimental)| 
|Weight     |Rat's weight on certain days throughout the paradigm| 
|SA.Act.XX  |# of active (correct) lever presses on the XX day of SA|
|SA.Inact.XX|# of inactive (incorrect) lever presses on the XX day of SA|
|SA.Inf.XX  |# of infusions on the XX day of SA|
|EXT.Act    |# of active (correct) lever presses on the XX day of EXT|
|EXT.Inact  |# of inactive (incorrect) lever presses on the XX day of EXT|

There are BLANK columns that hold a value of # for visual organization between behavior stages in SPSS, which is like if Excel were purposefully ugly and uncustomizeable.

There are also REACT columns which are always 0 (no lever available), and pEXT / TEST columns which are unused for this pilot cohort.

## Appendix: Behavioral Model of Relapse
We run a context-induced reinstatement model of cocaine relapse in order to study memory reconsolidation. This means we're interested in the facts that:
1. One discrete context (flooring, smell, sound, and light) can indicate that drugs are available, and
2. Exposure to the cocaine-associated context represents the activation of neuronal circuits that hold or  modify the memory, which makes neuronal plasticity much more likely (Hebb says you first have to "fire" in order to "wire"). This makes the drug memory temporarily susceptible to manipulation.

These concepts have been used therapeutically to reduce the strength of associations in negative valence diseases, like PTSD and phobias (exposure therapy). We are trying to use it to find out what brain regions and neuronal mechanisms are required for a positive valence disease - drug abuse.

### Behavioral Schedule
1. **SA: Self-Administration Days 1-10:** Rats learn to respond (lever presses) for cocaine (infusions) in one context
2. **EXT: Extinction Days 1-7:** Rats extinguish responding in another context; responding generally high on the first day ("where's my cocaine?!") and trends to 0 by day 7
3. **REACT: Reactivation Day 1:** Rats are returned to the cocaine context (no cocaine access, just exposure to the context). There should be no data for these days, as the levers are not available.

This is where my pilot cohort ends, as we were only interested in viral tracers and neuron activity during REACT and didn't do a manipulation. The SPSS file is set up like a full project, with EXT and TEST columns, but they are unused.