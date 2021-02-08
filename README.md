# JUSThink Dialogue and Actions Data and Code (Temporary Repository)

This is a temporary repository that contains:

1. **data**: JUSThink Dialogue and Actions Corpus v1 (event logs, test responses, and transcripts) ([data description](#data_description))
2. **code**: to process the data, and produce the figures and results in [[1]](#references) ([code description](#code_description))

The JUSThink activity and its study is described in [[2]](#references), and then findings concerning the link between children's learning, performance in the activity, and perception of self, the other and the robot, is reported in [[3]](#references).
(... Jauwairia's ICMI work, even maybe the upcoming new work?)

After completing the TODOs, the plan is to dissolve/remove this repository and:

1. Publish standalone, anonymised, clean on Zenodo (as a whole "JUSThink(-19?) Dialogue and Actions Corpus", or in two parts?)
2. Publish documented, clean code on GitHub, and DOI'e through Zenodo. Everything interlinked with each other.

## Table of Contents
1. [Installation](#installation)
2. [Data Description](#data_description)
    1. [Log Format](#log_format)
    2. [Test Responses Format](#test_format)
    3. [Transcript Format](#transcript_format)
3. [Code Description](#code_description)
3.  [Research Questions and Hypotheses in [1]](#rqs_hs)
4. [References](#references)


## 1. Installation <a name="installation"></a>
TODO: command to install Python dependencies for the code. Add a requirements.txt

```
git clone --recurse-submodules git@github.com:utku-norman/justhink-dialogue-and-actions-corpus.git
```

## 2. Data Description <a name="data_description"></a>

JUSThink Dialogue and Actions Corpus in three parts (maybe in two groups? transcripts could be published separately):

1. [logs](data/logs): one tab-separated csv log file per team for 39 teams
2. [test responses](data/test_responses): one csv pre-test file and one csv post-test file containing the responses for each item of each participant in each team for 39 teams, and the key
3. [transcripts](data/transcripts): one csv transcript file per team for 10 teams

In addition, metadata: details on the graph/network they have worked on.
(maybe add a full visualiser code as well? Will need a bit of work)


### 2.1. Logs Format  <a name="log_format"></a>
one tab-separated csv log file per team for 39 teams

### 2.2. Test Responses Format  <a name="test_format"></a>
one csv pre-test file and one csv post-test file containing the responses for each item of each participant in each 

### 2.3. Transcripts Format  <a name="transcript_format"></a>
one csv transcript file per team for 10 teams


## 3. Tools/Code Description <a name="code_description"></a>

The processing code of JUSThink Dialogue and Actions Corpus v1, consists of 7 Jupyter notebooks written in Python 3 and and two other tools used by the notebooks ([dialign](https://github.com/GuillaumeDD/dialign) and [cliffsDelta](https://github.com/neilernst/cliffsDelta)).


### 3.1. Jupyter Notebooks that Reproduce Results in [[1]](#references)

1. ✅  [Extract task performance (and other features) from logs](tools/1_extract_performance_and_other_features_from_logs.ipynb): Extract and export various task features at varying granularities (i.e. task, attempt, turn levels).
Only one feature (of performance), (minimum) error, is used next (hence a bit overkill: but is nice-to-share/fine/better-for-the-future?).
2. ✅ [Extract learning gain from test responses](tools/2_extract_learning_gain_from_test_responses.ipynb)
3. ✅ [Select and visualise a subset of teams for transcription](tools/3_visualise_transcribed_teams.ipynb)
4. ⬜️ [Extract routines from transcripts](tools/4_extract_routines_from_transcripts.ipynb) (uses [dialign](https://github.com/GuillaumeDD/dialign))
5. ⬜️ [Extract local contexts from transcripts](tools/5_extract_local_contexts_from_transcripts.ipynb)
6. ⬜️ [Combine transcripts with logs](tools/6_combine_transcripts_with_logs.ipynb)
7. ⬜️ [Recognise instructions and process follow-up actions](tools/7_recognise_instructions_process_follow-ups.ipynb)
8. ⬜️ [Test the hypotheses](tools/8_test_the_hypotheses.ipynb) in [[1]](#references) (uses [cliffsDelta](https://github.com/neilernst/cliffsDelta))

### 3.2. Utilised External Tools/Packages

1. Tool to extract routines [dialign](https://github.com/GuillaumeDD/dialign), specifically [Release 1.0](https://github.com/GuillaumeDD/dialign/releases/tag/v1.0) from [dialign-1.0.zip](https://github.com/GuillaumeDD/dialign/releases/download/v1.0/dialign-1.0.zip)
2. Tool to compute an estimator of effect size, Cliff's Delta: [cliffsDelta](https://github.com/neilernst/cliffsDelta)

## 4. Research Questions and Hypotheses in [[1]](#references) <a name="rqs_hs"></a>

* RQ1 How do the interlocutors use task specific referents? Does this link to task success?
    * H1.1: Globally, task specific referents become routine earlier for more successful teams.
    * H1.2: When task specific referents become routine, they are more likely to be surrounded by hesitation phenomena for more successful teams.
    * H1.3: Locally, routines of task specific referents are repeated less for more successful teams.

* RQ2 How do the interlocutors follow up the use of task specific referents with actions? Does this link to task success?
    * H2.1: Instructions are more likely to be followed by the corresponding actions earlier in the dialogue for more successful teams.
    * H2.2: When instructions are followed by the corresponding actions (or another action), they are more likely to be surrounded by information management phenomena for more successful teams.


## References <a name="references"></a>

[1] U. Norman\*, T. Dinkar\*, B. Bruno, P. Dillenbourg, and C. Clavel, “How Do Children Use Referring Expressions to Succeed in a Collaborative Learning Activity? Studying Alignment in Spontaneous Speech via Automatic Methods,” submitting, 2021.

[2] J. Nasir, U. Norman, B. Bruno, and P. Dillenbourg, “You Tell, I Do, and We Swap until we Connect All the Gold Mines!,” ERCIM News, vol. 2020, no. 120, 2020, [Online]. Available: [https://ercim-news.ercim.eu/en120/special/you-tell-i-do-and-we-swap-until-we-connect-all-the-gold-mines](https://ercim-news.ercim.eu/en120/special/you-tell-i-do-and-we-swap-until-we-connect-all-the-gold-mines).

[3] J. Nasir\*, U. Norman\*, W. Johal, J. K. Olsen, S. Shahmoradi, and P. Dillenbourg, “Robot Analytics: What Do Human-Robot Interaction Traces Tell Us About Learning?,” in 2019 28th IEEE International Conference on Robot and Human Interactive Communication (RO-MAN), Oct. 2019, pp. 1–7, doi: [10.1109/RO-MAN46459.2019.8956465](https://doi.org/10.1109/RO-MAN46459.2019.8956465).











