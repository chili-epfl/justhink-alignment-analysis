import pathlib as pl
import pandas as pd

def get_team_no_from_log_filename(filename):
    '''extract team no from a log filename of format *_<team_no>.*'''
    return int(str(pl.Path(filename).stem).split('_')[-1])


def get_team_no_from_transcript_filename(filename):
    '''extract team no from a transcript filename of format *_<team_no>.*'''
    return int(str(pl.Path(filename).stem).split('_')[-1])


def load_logs(logs_dir, verbose=True):
    # Make a list of the available log files.
    log_filelist = sorted([f for f in logs_dir.glob('*.csv')])
    if verbose:
        print('{} log files found.'.format(len(log_filelist)))

    # Organize the log file list as a dictionary keyed by team number.
    log_files = {
        get_team_no_from_log_filename(f): f
        for f in log_filelist
    }
    if verbose:
        for team_no, file in log_files.items():
            print('File {} belongs to team {:2d}'.format(file.stem, team_no))

    # Read the log files.
    log_dfs = dict()
    for team_no, f in log_files.items():
        # Read the file into a table.
        df = pd.read_csv(f, sep='\t')
        log_dfs[team_no] = df
    if verbose:
        for team_no, df in log_dfs.items():
            print('Log of {:2d} contains {:4d} events'.format(team_no, len(df)))

    return log_dfs


def load_transcripts(transcripts_dir, verbose=True):
    # Make a list of the available transcript files.
    transcript_filelist = sorted([f for f in transcripts_dir.glob('*.csv')])
    if verbose:
        print('{} transcript files found.'.format(len(transcript_filelist)))

    # Organize the transcript file list as a dictionary keyed by team number.
    transcript_files = {
        get_team_no_from_transcript_filename(f): f
        for f in transcript_filelist
    }
    if verbose:
        for team_no, file in transcript_files.items():
            print('File {} belongs to team {:2d}'.format(file.stem, team_no))

    # Read the transcript files.
    transcript_dfs = {task_index: pd.read_csv(
        f, sep='\t') for task_index, f in transcript_files.items()}
    if verbose:
        for team_no, df in transcript_dfs.items():
            print('Transcript of {:2d} has {:4d} utterances'.format(
                team_no, len(df)))

    return transcript_dfs
