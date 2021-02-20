import json

import pathlib as pl
import pandas as pd
import networkx as nx
from networkx.readwrite import json_graph


def get_team_no_from_log_filename(filename):
    '''extract team no from a log filename of format *_<team_no>.*'''
    return int(str(pl.Path(filename).stem).split('_')[-1])


def get_team_no_from_transcript_filename(filename):
    '''extract team no from a transcript filename of format *_<team_no>.*'''
    return int(str(pl.Path(filename).stem).split('_')[-1])


def get_team_no_from_corpus_filename(filename):
    '''extract team no from a corpus filename of format *_<team_no>.*'''
    return int(str(pl.Path(filename).stem).split('_')[-1])


def read_tables(input_dir, form='transcript', verbose=True):
    '''read transcript, log or corpus tables at a directory'''
    if form == 'transcript':
        func = get_team_no_from_log_filename
    elif form == 'log':
        func = get_team_no_from_transcript_filename
    elif form == 'corpus':
        func = get_team_no_from_corpus_filename
    else:
        raise ValueError
    if verbose:
        print('Reading {} files from {}.'.format(form, input_dir))

    # Make a list of the available files.
    filelist = sorted([f for f in input_dir.glob('*.csv')])
    if verbose:
        print('{} {} files found.'.format(form, len(filelist)))

    # Organize the file list as a dictionary keyed by team number.
    files = {func(f): f for f in filelist}
    if verbose:
        for team_no, file in files.items():
            print('File {} belongs to team {:2d}'.format(file.stem, team_no))

    # Read the files.
    dfs = dict()
    for team_no, f in files.items():
        # Read the file into a table.
        df = pd.read_csv(f, sep='\t')
        dfs[team_no] = df
    if verbose:
        for team_no, df in dfs.items():
            if form == 'log':
                print('{} of {:2d} contains {:4d} events'.format(
                    form.title(), team_no, len(df)))
            elif form == 'transcript':
                print('Transcript of {:2d} has {:4d} utterances'.format(
                    team_no, len(df)))

    return dfs


def read_network(graph_file):
    # Load from file, formatted as a node-link JSON.
    # c.f. https://networkx.org/documentation/stable/reference/readwrite/json_graph.html
    # in particular https://networkx.org/documentation/stable/reference/readwrite/generated/networkx.readwrite.json_graph.node_link_graph.html
    try:
        with pl.Path(graph_file).open() as f:
            data = json.load(f)
        graph = json_graph.node_link_graph(data)

        for u, v, d in graph.edges(data=True):
            u_node = graph.nodes[u]
            v_node = graph.nodes[v]

        return graph
    except IOError as e:
        # The file was missing.
        load_text = "File {} not found".format(graph_file)
        return nx.Graph()
