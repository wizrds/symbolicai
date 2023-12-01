from ...base import Engine


class OutputEngine(Engine):
    def __init__(self):
        super().__init__()

    def id(self) -> str:
        return 'output'

    def forward(self, argument):
        expr, processed, args, kwargs  = argument.prop.prepared_input
        res = None
        if expr:
            if processed:
                res = expr(processed)
            else:
                res = expr(*args, **kwargs)

        metadata = {}

        return [kwargs], metadata

    def prepare(self, argument):
        argument.prop.prepared_input = argument.prop.expr, argument.prop.processed_input, argument.prop.args, argument.prop.kwargs
