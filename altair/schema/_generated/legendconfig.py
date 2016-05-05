# This file auto-generated by altair.schema.parser.write_files().
# do not modify directly.

import traitlets as T
from ..baseobject import BaseObject


class LegendConfig(BaseObject):
    orient = T.Unicode(default_value=None, allow_none=True, help="""The orientation of the legend.""")
    properties = T.Any(default_value=None, allow_none=True, help="""Optional mark property definitions for custom legend styling.""")
    shortTimeLabels = T.Bool(default_value=None, allow_none=True, help="""Whether month names and weekday names should be abbreviated.""")

