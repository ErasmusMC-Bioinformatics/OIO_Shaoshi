import pandas as pd
import numpy as np
from numpy.random import uniform
from TMM import *
import scanpy as sc
import os

random_selection_proportion = 0.1 # proportion of randomly selection from atlas

# Loading Atlas
adata = sc.read_h5ad('GSE115469.h5ad')
liver_cell_atlas = adata.to_df().T

metadata = adata.obs
metadata = metadata.filter(['CellType_sub'])
metadata.columns = ['CellType']

def cell_expr_generator(selected_cell,cell_atlas_matrix,cell_type_annotation):    
    selected_cell = selected_cell
    cell_atlas_matrix = cell_atlas_matrix
    cell_type_annotation = cell_type_annotation
    cell_id_list = list(cell_type_annotation[cell_type_annotation['CellType'] == selected_cell].index.values)
    other_id_list = list(cell_type_annotation[cell_type_annotation['CellType'] != selected_cell].index.values)
    random_selection_number = int(len(cell_id_list) * random_selection_proportion)
    if random_selection_number < 50:
        random_selection_number = 50
    else:
        pass
    random_selection = np.random.choice(cell_id_list,random_selection_number)
    selected_cell_reference = cell_atlas_matrix.filter(random_selection).mean(axis=1)
    other_selection = np.random.choice(other_id_list,1000)
    other_cell_reference = cell_atlas_matrix.filter(other_selection).mean(axis=1)
    scaling = np.random.uniform(0,1)
    proportion = [scaling,1-scaling]
    sim_expr = selected_cell_reference * proportion[0] * 100 + other_cell_reference * proportion[1] * 100
    return sim_expr, proportion

def train_simulation(selected_cell,cell_atlas_matrix,cell_type_annotation,simulation_number):
    selected_cell = selected_cell
    cell_atlas_matrix = cell_atlas_matrix
    cell_type_annotation = cell_type_annotation
    simulation_number = simulation_number
    sim_expr = {}
    proportion = []
    sim_list = []
    for i in range(simulation_number):
        sim_id = 'Train-%s'%(i + 1)
        sim_list.append(sim_id)
        pseudo_bulk = cell_expr_generator(selected_cell,cell_atlas_matrix,cell_type_annotation)
        sim_expr[sim_id] = pseudo_bulk[0]
        proportion.append(pseudo_bulk[1])
    sim_expr = pd.DataFrame.from_dict(data = sim_expr)
    sim_expr = cpm(sim_expr)
    proportion = np.array(proportion)
    proportion = pd.DataFrame(data = proportion, columns = [selected_cell,'Other'])
    proportion.index = sim_list
    return sim_expr,proportion

def test_simulation(selected_cell,cell_atlas_matrix,cell_type_annotation,simulation_number):
    selected_cell = selected_cell
    cell_atlas_matrix = cell_atlas_matrix
    cell_type_annotation = cell_type_annotation
    simulation_number = simulation_number
    sim_expr = {}
    proportion = []
    sim_list = []
    for i in range(simulation_number):
        sim_id = 'Test-%s'%(i + 1)
        sim_list.append(sim_id)
        pseudo_bulk = cell_expr_generator(selected_cell,cell_atlas_matrix,cell_type_annotation)
        sim_expr[sim_id] = pseudo_bulk[0]
        proportion.append(pseudo_bulk[1])
    sim_expr = pd.DataFrame.from_dict(data = sim_expr)
    sim_expr = cpm(sim_expr)
    proportion = np.array(proportion)
    proportion = pd.DataFrame(data = proportion, columns = [selected_cell,'Other'])
    proportion.index = sim_list
    return sim_expr,proportion

all_cell_types = list(set(metadata['CellType']))

try:
    os.mkdir('Pseudobulk')
except:
    pass
    
for selected_cell in all_cell_types:
    test = test_simulation(selected_cell,liver_cell_atlas,metadata,500)
    test_expr = test[0]
    test_proportion = test[1]
    test_expr.to_csv('Pseudobulk/%s.TestExpression.txt'%selected_cell,sep='\t')
    test_proportion.to_csv('Pseudobulk/%s.TestTarget.txt'%selected_cell,sep='\t')


