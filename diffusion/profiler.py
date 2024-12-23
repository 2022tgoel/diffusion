from composer.profiler import Profiler, cyclic_schedule
from composer.profiler import JSONTraceHandler

composer_trace_dir = '~/profiler/composer_traces'
torch_trace_dir = '~/profiler/torch_traces'

def profiler():
    return Profiler(
        trace_handlers=[JSONTraceHandler(folder=composer_trace_dir, overwrite=True)],
        sys_prof_disk=True,
        sys_prof_net=True,
        schedule=cyclic_schedule(
            wait=1,
            warmup=1,
            active=4,
            repeat=2,
        ),
        torch_prof_folder=torch_trace_dir,
        torch_prof_overwrite=True,
        torch_prof_memory_filename=None,
    )