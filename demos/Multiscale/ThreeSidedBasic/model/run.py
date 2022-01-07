import pandas as pd
from .parts.utils import * 
from model.config import exp
from cadCAD.engine import ExecutionMode, ExecutionContext,Executor

def run():
    '''
    Definition:
    Run simulation
    '''
    exec_mode = ExecutionMode()
    local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)

    simulation = Executor(exec_context=local_mode_ctx, configs=exp.configs)
    raw_system_events, tensor_field, sessions = simulation.execute()
    # Result System Events DataFrame
    df = pd.DataFrame(raw_system_events)
    return df


