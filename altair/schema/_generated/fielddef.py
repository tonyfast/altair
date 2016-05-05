# This file auto-generated by altair.schema.parser.write_files().
# do not modify directly.

import traitlets as T
from ..baseobject import BaseObject
from .timeunit import TimeUnit
from .type import Type
from .binproperties import BinProperties
from .aggregateop import AggregateOp


class FieldDef(BaseObject):
    timeUnit = T.Instance(TimeUnit, default_value=None, allow_none=True)
    displayName = T.Unicode(default_value=None, allow_none=True)
    type = T.Instance(Type, default_value=None, allow_none=True)
    bin = T.Union([T.Bool(default_value=None, allow_none=True), T.Instance(BinProperties, default_value=None, allow_none=True)])
    aggregate = T.Instance(AggregateOp, default_value=None, allow_none=True)
    field = T.Unicode(default_value=None, allow_none=True)
    value = T.Union([T.CFloat(default_value=None, allow_none=True), T.Unicode(default_value=None, allow_none=True), T.Bool(default_value=None, allow_none=True)])

