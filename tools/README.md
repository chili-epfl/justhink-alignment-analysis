# JUSThink Dialogue and Actions Corpus - Alignment Analysis Tools
This repostiory contains tools to process the data, and produce the figures and results in [[1]](#references) ([code description](#code_description))

The purpose is to publish documented, clean code on GitHub, and DOI'e through Zenodo. Everything interlinked with each other.

## Table of Contents
1. [Installation](#installation)
3. [Content](#code_description)
3. [Research Questions and Hypotheses in [1]](#rqs_hs)
4. [Acknowledgements](#acknowledgements)
4. [References](#references)


## 1. Installation <a name="installation"></a>
Run the following command to obtain the source code:
```
git clone --recurse-submodules git@github.com:utku-norman/justhink-dialogue-and-actions-corpus.git
```
TODO: command to install Python dependencies for the code. Add a requirements.txt; or a disclaimer on the dependencies (per notebook, that are imported in the very first cell)


## 2. Content <a name="content"></a>

The processing code of JUSThink Dialogue and Actions Corpus v1, consists of 7 Jupyter notebooks written in Python 3 and and two other tools used by the notebooks ([dialign](https://github.com/GuillaumeDD/dialign) and [cliffsDelta](https://github.com/neilernst/cliffsDelta)).


### 2.1. Jupyter Notebooks that Reproduce Results in [[1]](#references)

1. ✅ [Extract task performance (and other features) from logs](tools/1_extract_performance_and_other_features_from_logs.ipynb): Extract and export various task features at varying granularities (i.e. task, attempt, turn levels).
Only one feature (of performance), (minimum) error, is used next (hence a bit overkill: but is nice-to-share/fine/better-for-the-future?).
2. ✅ [Extract learning gain from test responses](tools/2_extract_learning_gain_from_test_responses.ipynb)
3. ✅ [Select and visualise a subset of teams for transcription](tools/3_visualise_transcribed_teams.ipynb)
4. ✅ [Extract routines from transcripts](tools/4_extract_routines_from_transcripts.ipynb) (uses [dialign](https://github.com/GuillaumeDD/dialign) to extract routines)
5. ⬜️ [Combine transcripts with logs](tools/5_combine_transcripts_with_logs.ipynb)
6. ⬜️ [Recognise instructions and detect follow-up actions](tools/6_recognise_instructions_detect_follow-up_actions.ipynb)
7. ⬜️ [Test the hypotheses](tools/7_test_the_hypotheses.ipynb) in [[1]](#references) (uses [cliffsDelta](https://github.com/neilernst/cliffsDelta) to estimate effect size)

### 2.2. Utilised External Tools/Packages

1. Tool to extract routines [dialign](https://github.com/GuillaumeDD/dialign), specifically [Release 1.0](https://github.com/GuillaumeDD/dialign/releases/tag/v1.0) from [dialign-1.0.zip](https://github.com/GuillaumeDD/dialign/releases/download/v1.0/dialign-1.0.zip)
2. Tool to compute an estimator of effect size, Cliff's Delta: [cliffsDelta](https://github.com/neilernst/cliffsDelta)

## 3. Research Questions and Hypotheses addressed in in [[1]](#references) <a name="rqs_hs"></a>

* RQ1 How do the interlocutors use task specific referents? Does this link to task success?
    * H1.1: Task specific referents become routine earlier for more successful teams.
    * H1.2: When (a) task specific referents become routine and (b) their routines are primed, they are more likely to be surrounded by hesitation phenomena for more successful teams.

* RQ2 How do the interlocutors follow up the use of task specific referents with actions? Does this link to task success?
    * H2.1: Instructions are more likely to be followed by the corresponding actions earlier in the dialogue for more successful teams.
    * H2.2: When instructions are followed by the corresponding actions (or another action), they are more likely to be surrounded by information management phenomena for more successful teams.


## Acknowledgements <a name="acknowledgements"></a>
 This project has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 765955. Namely, the [ANIMATAS Project](https://www.animatas.eu/).


## References <a name="references"></a>

[1] U. Norman\*, T. Dinkar\*, B. Bruno, P. Dillenbourg, and C. Clavel, “How Do Children Use Referring Expressions to Succeed in a Collaborative Learning Activity? Studying Alignment in Spontaneous Speech via Automatic Methods,” submitting, 2021.

[2] J. Nasir, U. Norman, B. Bruno, and P. Dillenbourg, “You Tell, I Do, and We Swap until we Connect All the Gold Mines!,” ERCIM News, vol. 2020, no. 120, 2020, [Online]. Available: [https://ercim-news.ercim.eu/en120/special/you-tell-i-do-and-we-swap-until-we-connect-all-the-gold-mines](https://ercim-news.ercim.eu/en120/special/you-tell-i-do-and-we-swap-until-we-connect-all-the-gold-mines).

[3] J. Nasir\*, U. Norman\*, B. Bruno, and P. Dillenbourg, “When Positive Perception of the Robot Has No Effect on Learning,” in 2020 29th IEEE International Conference on Robot and Human Interactive Communication (RO-MAN), Aug. 2020, pp. 313–320, doi: [10.1109/RO-MAN47096.2020.9223343](https://doi.org/10.1109/RO-MAN47096.2020.9223343).





