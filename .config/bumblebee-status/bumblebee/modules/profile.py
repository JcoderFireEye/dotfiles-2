# pylint: disable=C0111,R0903

"""Profile module
"""

import bumblebee.engine

ALIASES = [ "profile" ]

class Module(bumblebee.engine.Module):
    def __init__(self, engine, config):
        super(Module, self).__init__(engine, config,
            bumblebee.output.Widget(full_text=" BANDITHIJO")
        )

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
