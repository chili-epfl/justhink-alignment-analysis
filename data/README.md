# JUSThink Dialogue and Actions Corpus

The information contained in this dataset (JUSThink Dialogue and Actions Corpus v1) include event logs, test responses, and transcripts of children engaged in the JUSThink activity in teams of two.

The information was collected in two international schools in Switzerland, in November 2019.

The JUSThink activity and its study is described in [[2]](#references), and then findings concerning the link between children's learning, performance in the activity, and perception of self, the other and the robot, is reported in [[3]](#references). See the [project website](https://www.epfl.ch/labs/chili/index-html/research/animatas/justhink/) for more details.

## Table of Contents
1. [Content](#code_description)
2. [Acknowledgements](#acknowledgements)
3. [References](#references)

## 1. Content

JUSThink Dialogue and Actions Corpus in consisted of three parts:

1. [logs](logs): one tab-separated csv log file per team for 39 teams (see [logs content](#log_content))
2. [test responses](test_responses): one csv pre-test file and one csv post-test file for 39 teams, and the key (see [tests content](#test_content))
3. [transcripts](transcripts): one csv transcript file per team for 10 teams (see [transcripts content](#transcript_content))

In addition, there is [metadata](metadata) contains the details on the network that the children have worked on.


### 1.1. Logs  <a name="log_content"></a>

This part of the dataset contains log data for 39 teams, from the JUSThink-19 study [1, 2]. 
It consists of 39 files, with one tab-separated csv log file per team for 39 teams.
In particular, the content is:
<!-- #### Content -->
* name: The English name of the Pokemon
* japanese_name: The Original Japanese name of the Pokemon
* pokedex_number: The entry number of the Pokemon in the National Pokedex
* against_?: Eighteen features that denote the amount of damage taken against an attack of a particular type
hp: The Base HP of the Pokemon

### 1.2. Test Responses  <a name="test_content"></a>
containing the responses for each item of each participant in each team
This part of the dataset contains the test responses for 39 teams, as they participate in the JUSThink activity [1, 2]. 
It consists of 2 files: one comma-separated CSV file for the pre-test responses, and one comma-separated CSV file for the post-test responses for each test item (among 10 items) for each participant for 39 teams.
In particular, the content is:
* TODO

### 1.3. Transcripts  <a name="transcript_content"></a>
one csv transcript file per team for 10 teams

This part of the dataset contains the dialogue transcripts for 10 teams (among the 39 teams) from the JUSThink-19 study [1, 2, 3]. 
It consists of 2 files: one comma-separated CSV file for the pre-test responses, and one comma-separated CSV file for the post-test responses for each test item (among 10 items) for each participant for 39 teams.
In particular, the content is:
* TODO



## Acknowledgements
 This project has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 765955. Namely, the [ANIMATAS Project](https://www.animatas.eu/).


## References <a name="references"></a>

[1] U. Norman\*, T. Dinkar\*, B. Bruno, P. Dillenbourg, and C. Clavel, “How Do Children Use Referring Expressions to Succeed in a Collaborative Learning Activity? Studying Alignment in Spontaneous Speech via Automatic Methods,” submitting, 2021.

[2] J. Nasir, U. Norman, B. Bruno, and P. Dillenbourg, “You Tell, I Do, and We Swap until we Connect All the Gold Mines!,” ERCIM News, vol. 2020, no. 120, 2020, [Online]. Available: [https://ercim-news.ercim.eu/en120/special/you-tell-i-do-and-we-swap-until-we-connect-all-the-gold-mines](https://ercim-news.ercim.eu/en120/special/you-tell-i-do-and-we-swap-until-we-connect-all-the-gold-mines).

[3] J. Nasir\*, U. Norman\*, B. Bruno, and P. Dillenbourg, “When Positive Perception of the Robot Has No Effect on Learning,” in 2020 29th IEEE International Conference on Robot and Human Interactive Communication (RO-MAN), Aug. 2020, pp. 313–320, doi: [10.1109/RO-MAN47096.2020.9223343](https://doi.org/10.1109/RO-MAN47096.2020.9223343).





